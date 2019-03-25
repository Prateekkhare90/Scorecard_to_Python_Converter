
# coding: utf-8

# In[ ]:

import sys
from IPython import get_ipython

def Scorecard_to_python(p):
    from IPython.core.interactiveshell import InteractiveShell
    InteractiveShell.ast_node_interactivity = "all"

    def skip_first_line(seq, n):
        for i,item in enumerate(seq):
            if i >= n:
                yield item

    import csv

    f = open(p)
    csv_f = csv.reader(f)

    Add_line = []
    for row in skip_first_line(csv_f, 2):
    #    print(row)
        row1 = ','.join(row)
        Add_line.append(row1)

    # print(Add_line)

#     for p in Add_line:
#         print(p)

    def getmystring(s):
        list1=s.split("<")
        list3=s.split("=")
        if len(list1) == 3:
            list2=[l for l in list1]
            res=list2[1].split("=")[1]
        elif len(list1) == 2:
            list2=[l for l in list1]
            res=list2[0]
        elif len(list3) == 2:
            list4=[l for l in list3]
            res=list4[0]
        return res

    results1 = []
    def SAS_Scrd_to_Py():
        for i in Add_line:
            list1 = i.split(',')
            list2 = list1[3:]
#             print(list2)
            for j in list2:
                if list2.count(' _MISSING_') == 0:
                    results1.append('elif '+list2[0]+' :'+"DF['Score']="+list2[-1])
                elif list2.count(' _MISSING_') == 1:
                    results1.append('elif '+list2[0]+' :'+"DF['Score']="+list2[-1])
                    results1.append('elif '+"DF['"+getmystring(str(list2[0])).strip()+"']"+'=='+"'NaN'"+' :'+"DF['Score']="+list2[2])
        return results1
    SAS_Scrd_to_Py()
    print(results1)
    
    Var_list = []
    def Variable_list():
        for i in Add_line:
            list1 = i.split(',')
            list2 = list1[1]
            Var_list.append(list2)
        return Var_list

    Var_list_NOdups = []
    for d in Variable_list():
            if d not in Var_list_NOdups:
                Var_list_NOdups.append(d)
                
    print(Var_list_NOdups)
    global varnum
    varnum = len(Var_list_NOdups)

    results2 = []
    for i in results1:
           if i not in results2:
            results2.append(i)
#     print(results2)

    results3 = []
    def SAS_Scrd_to_Py_Mid():
        for i in results2:
            list3 = i.split(' ')
#             print(list3)
            if len(list3) == 5 and list3[2] == "<":
                list3[1]=list3[1].replace("(", "")
                results3.append(['if '+"DF['"+list3[1]+"']"+list3[2]+list3[3]+list3[4]])
            elif len(list3) == 5 and list3[2] == "<=":
                results3.append([list3[0]+' '+"DF['"+list3[3]+"']"+'>='+list3[1]+list3[4]])
            elif len(list3) == 7:
                results3.append([list3[0]+' '+list3[1]+list3[2]+"DF['"+list3[3]+"']"+list3[4]+list3[5]+list3[6]])
            elif len(list3) != 5 and len(list3) != 7:
                results3.append(list3) 
        return results3
    SAS_Scrd_to_Py_Mid()
#     print(results3)   
    
    result3_1 =[]
    def SAS_Scrd_to_Py_Mid1():
        for i in results3:
            row = ', '.join(i)
            row1=row.replace(",", "")
            row2 = row1.split(',')
            result3_1.append(row2)
        return result3_1
    SAS_Scrd_to_Py_Mid1()
    
    result4=[]
    for item in result3_1:
        temp=[]
        for item1 in item:
            strg = item1
            for x in Var_list_NOdups:
                if x in strg:
                    newscore = "Score" +"_"+x
                    d=strg.replace("Score", newscore)
                    temp.append(d)
            result4.append(temp)
#     print(result4)
    
    result5 = []
    for item in result4:
        row = ', '.join(item)
        row1=row.replace(",", "")
        result5.append(row1)    
#     print(result5)
    
#     for p in result5:
# #         print(p)
        
    Line_indent1 = "    "    
    Line_indent = "\n        "
    Mergewords2 = []
    for p in result5:
        q=p.find(":")
        r = Line_indent1+p[0:q+1]+Line_indent+p[q+1:]
        Mergewords2.append(r)
    Mergewords2.insert(0, "def myfunc(DF):")
    Mergewords2.insert(len(Mergewords2), "    return DF" )
    print(Mergewords2)
    
    log = open("Py_elif1.py", "w")
    for g in Mergewords2:
        print(g, file = log) 

def Scorecard_to_python2(q):
    import pandas as pd
    from IPython.display import display
    import numpy as np 
    from Py_elif48 import myfunc
        
    DF=pd.read_csv(q)
 
    def SAStoPy_exe(DF):
        DF=myfunc(DF)
        return DF

    DF2 = DF.apply (lambda row: SAStoPy_exe(row),axis=1)
    display(DF2)

    DF2['Score_total'] = DF2[DF2.columns[-varnum:]].sum(axis=1)
    display(DF2)
    DF2.to_csv('Out_DF1.csv')


filename1 = ""
filename2 = ""

if len(sys.argv)==3:
    filename1 = str(sys.argv[1])
    filename2 = str(sys.argv[2])
    Scorecard_to_python(filename1)
    Scorecard_to_python2(filename2)
else:
    print("2 file must be provided")


# In[4]:

# !jupyter nbconvert --to script First_Second_7_19_500_CallingMyfunc_dyn_col.ipynb


# In[3]:

# !python First_Second_7_19_500_CallingMyfunc_dyn_col.py SASEM_Output.csv Test_data.csv

