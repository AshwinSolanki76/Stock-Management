import pandas as pd

# names=["Vedanti","Zinal","Harsh","Janam","Ashwin"]
# password=["Pathak","Patel","Parmar","Shah","Solanki"]

UserDataFileName="Data/users.csv"
UserData=pd.read_csv(UserDataFileName)

def CheckPassword(UserName,Password):
    return UserData[UserData["Name"]==UserName].isin([Password]).any().any()

def AddUser(name,password):
    global UserData
    i=len(UserData)
    if UserData['Name'].isin([name]).any():
        print("User "+name+" already exist")
    else:
        temp=pd.DataFrame({"Name":name,"Password":password},index=[i])
        UserData= pd.concat([UserData,temp])
        UserData.to_csv(UserDataFileName,index=False)

def delUserByName(name,password):
    if not UserData['Name'].isin([name]).any():
        print("No User called "+name+" exist!!!")
    elif CheckPassword(name,password):
        UserData.drop(UserData[UserData['Name']==name].index,inplace=True)
        UserData.to_csv(UserDataFileName,index=False)
    else:
        print("Please check Your password!!!")

def ChangeUsername(OldName,password,NewName):
    if not UserData['Name'].isin([OldName]).any():
        print("No User called "+OldName+" exist!!!")
    elif UserData['Name'].isin([NewName]).any():
        print("User "+NewName+" already exist")
    elif CheckPassword(OldName,password):
        UserData.loc[UserData['Name']==OldName,"Name"]=NewName
        UserData.to_csv(UserDataFileName,index=False)
        print("UserName updated!")
    else:
        print("Please Check your Password!!!")

def ChangePassword(UserName,OldPassword,NewPassword):
    if not UserData['Name'].isin([UserName]).any():
        print("No User called "+UserName+" exist!!!")
    elif CheckPassword(UserName,OldPassword):
        UserData.loc[UserData['Password']==OldPassword,"Password"]=NewPassword
        UserData.to_csv(UserDataFileName,index=False)
        print("Password Updated!")
    else:
        print("Please Enter correct Password")

