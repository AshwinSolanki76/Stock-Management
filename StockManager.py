import pandas as pd

StockFilePath="Data/stock.csv"
AllItemsPath="Data/AllItems.csv"

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
