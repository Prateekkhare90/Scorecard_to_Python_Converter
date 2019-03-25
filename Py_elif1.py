def myfunc(DF):
    if DF['MoSold']<796:
        DF['Score_MoSold']=30
    elif 796<=DF['MoSold']<1079:
        DF['Score_MoSold']=38
    elif DF['MoSold']=='NaN' :
        DF['Score_MoSold']=38
    elif 1079<=DF['MoSold']<1567:
        DF['Score_MoSold']=41
    elif 1567<=DF['MoSold']<1830:
        DF['Score_MoSold']=43
    elif DF['MoSold']>=1830:
        DF['Score_MoSold']=45
    if DF['GrLivArea']<1373:
        DF['Score_GrLivArea']=147
    elif DF['GrLivArea']=='NaN' :
        DF['Score_GrLivArea']=147
    elif 1373<=DF['GrLivArea']<1540:
        DF['Score_GrLivArea']=65
    elif 1540<=DF['GrLivArea']<1944:
        DF['Score_GrLivArea']=40
    elif 1944<=DF['GrLivArea']<2464:
        DF['Score_GrLivArea']=3
    elif DF['GrLivArea']>=2464:
        DF['Score_GrLivArea']=-29
    if DF['LotArea']<6000:
        DF['Score_LotArea']=117
    elif 6000<=DF['LotArea']<10512:
        DF['Score_LotArea']=71
    elif DF['LotArea']=='NaN' :
        DF['Score_LotArea']=71
    elif 10512<=DF['LotArea']<12198:
        DF['Score_LotArea']=49
    elif 12198<=DF['LotArea']<16900:
        DF['Score_LotArea']=18
    elif DF['LotArea']>=16900:
        DF['Score_LotArea']=-40
    if DF['WoodDeckSF']<100:
        DF['Score_WoodDeckSF']=41
    elif DF['WoodDeckSF']=='NaN' :
        DF['Score_WoodDeckSF']=41
    elif 100<=DF['WoodDeckSF']<130:
        DF['Score_WoodDeckSF']=43
    elif 130<=DF['WoodDeckSF']<256:
        DF['Score_WoodDeckSF']=41
    elif 256<=DF['WoodDeckSF']<319:
        DF['Score_WoodDeckSF']=37
    elif DF['WoodDeckSF']>=319:
        DF['Score_WoodDeckSF']=35
    return DF
