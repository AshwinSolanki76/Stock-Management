import pandas as pd

StockFilePath="Data/stock.csv"
AllItemsPath="Data/AllItems.csv"
SortedStock="Data/SortedStock.csv"

StockData=pd.read_csv(StockFilePath)
AllItemsData=pd.read_csv(AllItemsPath)

def AddStock(name,price,No_of_units):
    global StockData
    i=len(StockData)
    newData=pd.DataFrame({"Name":name,"Price":price,"Number of units":No_of_units},index=[i])
    StockData=pd.concat([StockData,newData])
    StockData.to_csv(StockFilePath,index=False)

def ReduceStockItemBy(name,ReduceBy=1):
    newStockData=StockData.set_index(StockData["Name"])
    t=newStockData.loc[name]["Number of units"]==0
    if not StockData['Name'].isin([name]).any():
        print("No Item found to reduce!!!")
    elif t:
        print("Already number of "+name+" is zero")
    else:
        StockData.loc[StockData[StockData["Name"]==name].index,"Number of units"]-=ReduceBy
        StockData.to_csv(StockFilePath,index=False)
        print("Reduced "+name+" By",ReduceBy)

def GetStockItemTotalNumber(name):
    return int(StockData[StockData["Name"]==name]["Number of units"].sum())

def GetPriceByName(name):
    return int(AllItemsData[AllItemsData["name"]==name]["price"])

def OrganizeStock():
    dd={}
    dp={}

    for name,price,unit in zip(StockData["Name"],StockData["Price"],StockData["Number of units"]):
        if name in dd:
            dd[name]+=unit
        else:
            dd[name]=unit
            dp[name]=price
    
    SortedDataFrame=pd.DataFrame({"Name":list(dd.keys()),"Price":list(dp.values()),"Unit":list(dd.values())})
    SortedDataFrame.to_csv(SortedStock,index=False)
def OrganizeSortedStock():
    CustomerOrder=pd.read_csv("Data/customerOrder.csv")
    dd={}
    dp={}
    for name,unit in zip(CustomerOrder["name"],CustomerOrder["unit"]):
        if name in dd:
            dd[name]+=unit
        else:
            dd[name]=unit
            dp[name]=GetPriceByName(name)
    k=[int(un)*int(pr) for un,pr in zip(dd.values(),dp.values())]
    df=pd.DataFrame({"Name":list(dd.keys()),"Unit":list(dd.values()),"Unit Price":list(dp.values()),"Totle Price":[int(un)*int(pr) for un,pr in zip(dd.values(),dp.values())]})
    df=df.append({"Name":"------","Unit":"-------","Unit Price":"-------","Totle Price":"---------"},ignore_index=True)
    df=df.append({"Name":"Total","Unit":sum(list(dd.values())),"Unit Price":"-------","Totle Price":sum(k)},ignore_index=True)
    # df=df.append({"Name":"Total","Unit":"-------","Unit Price":"-------","Total Price":2},ignore_index=True)
    return str(df)
