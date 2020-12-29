from tkinter import *
from PIL import Image,ImageTk
from UserManager import *
from StockManager import *
import time
import pandas as pd

AllItems=pd.read_csv("Data/AllItems.csv")
sortedstock=pd.read_csv("Data/SortedStock.csv")

ItemNames=AllItems["name"].values.tolist()
ItemPrice=AllItems["price"].values.tolist()
global CustomerData
CustomerData=pd.read_csv("Data/customerOrder.csv")

def CartMessage():
    global cartWindow
    global ItemName
    global ItemNumber
    global ItemNameWithNumbers
    global CustomerData

    name,number=ItemName.get().split()[0],ItemNumber.get()

    if GetStockItemTotalNumber(name)<number:
        message=Label(cartWindow,text=f"Sorry maximum number of {name} is {GetStockItemTotalNumber(name)}",fg="red",font=("times new roman",15,"bold")).place(x=100,y=300)
    elif number<=0 :
        message=Label(cartWindow,text="Sorry quantity cannot be zero                    ",fg="red",font=("times new roman",15,"bold")).place(x=100,y=300)
    else:
        # CustomerData
        message=Label(cartWindow,text="Add to Cart                                      ",fg="green",font=("times new roman",15,"bold")).place(x=100,y=300)
        temp=pd.DataFrame({"name":[name],"unit":[number]})
        CustomerData=pd.concat([CustomerData,temp])
        CustomerData.to_csv("Data/customerOrder.csv",index=False)

def CartWindow():
    global cartWindow
    global ItemName
    global ItemNumber

    # global Loginwindow
    cartWindow=Toplevel(Loginwindow)
    cartWindow.title("Cart Window")
    cartWindow.geometry("500x500+550+120")
    namewithnumber=[str(str(na)+"  ₹"+str(pr)+"  x"+str(nu)) for na,pr,nu in zip(sortedstock["Name"],sortedstock["Price"],sortedstock["Unit"])]
    ItemName=StringVar()
    ItemNumber=IntVar()
    
    ItemName.set(namewithnumber[0])
    ItemNumber.set(1)

    opt=OptionMenu(cartWindow,ItemName,*namewithnumber).place(x=50,y=50,height=50,width=175)
    ent=Entry(cartWindow,textvariable=ItemNumber,border=0,bg="white",font=("Bold",25)).place(x=250,y=50,width=100,height=50)
    btn=Button(cartWindow,command=CartMessage,text="Add to cart",bg="green",font=("Bold",13),fg="white").place(x=375,y=425,height=50,width=100)
    btnn=Button(cartWindow,command=makeRecipt,text="Get Recipt",bg="darkgreen").place(x=10,y=425,height=50,width=100)
    

def makeRecipt():
    global reciptWindow
    reciptWindow=Toplevel(cartWindow)
    reciptWindow.title("Recipt")
    message=Label(reciptWindow,text=OrganizeSortedStock()).place(x=0,y=0)

def RegisterWindow():
    global Registerwindow
    global RegisterID
    global RegisterPASSWORD

    Registerwindow=Toplevel(mainWindow)
    Registerwindow.geometry("500x500+550+120")
    Registerwindow.title("Register Window")

    RegisterID=StringVar()
    RegisterPASSWORD=StringVar()

    RegisterIdLABEL=Label(Registerwindow,text="User Name",font=("times new roman",20,"bold")).place(x=20,y=100)
    RegisterPasswordLABEL=Label(Registerwindow,text="Password",font=("times new roman",20,"bold")).place(x=20,y=200)

    RegisterIDEntry=Entry(Registerwindow,textvariable=RegisterID,width=40).place(x=200,y=100)
    RegisterPASSWORDentry=Entry(Registerwindow,textvariable=RegisterPASSWORD,width=40).place(x=200,y=200)

    RegisterBUTTON=Button(Registerwindow,command=RegisterDisplaymessage,text="Register",font=("times new roman",20,"bold"),fg="white",bg = 'green',cursor="hand2").place(x=200,y=400)


def LoginWindow():
    global Loginwindow

    Loginwindow=Toplevel(mainWindow)
    Loginwindow.geometry("500x500+550+120")
    Loginwindow.title("Login Window")

    #Labels
    LoginLABLE=Label(Loginwindow,text="User Name",font=("times new roman",20,"bold")).place(x=20,y=100)
    passwordLABBLE=Label(Loginwindow,text="Password",font=("times new roman",20,"bold")).place(x=20,y=200)

    #Variables
    global LoginID_VARIABLE
    global LoginPASSWORD_VARIABLE

    LoginID_VARIABLE=StringVar()
    LoginPASSWORD_VARIABLE=StringVar()
    #Text Fields
    LoginID=Entry(Loginwindow,textvariable=LoginID_VARIABLE,width=40).place(x=200,y=100)
    LoginPASSWORD=Entry(Loginwindow,textvariable=LoginPASSWORD_VARIABLE,width=40).place(x=200,y=200)

    #Button
    LoginButton=Button(Loginwindow,command=LogINdisplaymessage,text="Login",font=("times new roman",20,"bold"),fg="white",bg = 'green',cursor="hand2").place(x=200,y=400)

def RegisterDisplaymessage():
    global Registerwindow
    global RegisterID
    global RegisterPASSWORD

    if CheckUserName(RegisterID.get()):
        message=Label(Registerwindow,text="User already exist",fg="red",font=("times new roman",20,"bold")).place(x=150,y=300)
    elif RegisterID.get().isnumeric():
        message=Label(Registerwindow,text="Username cannot be just number",fg="red",font=("times new roman",20,"bold")).place(x=80,y=300)
    else:
        message=Label(Registerwindow,text="Registration Successfull...!!!",fg="green",font=("times new roman",20,"bold")).place(x=150,y=300)
        AddUser(RegisterID.get(),RegisterPASSWORD.get())

def LogINdisplaymessage():
    global LoginID_VARIABLE
    global LoginPASSWORD_VARIABLE
    global Loginwindow
    global Cartwindow
    # print(LoginID_VARIABLE)
    if not CheckUserName(LoginID_VARIABLE.get()):
        message=Label(Loginwindow,text="User Not Found",fg="red",font=("times new roman",20,"bold")).place(x=150,y=300)
    else:
        if not CheckPassword(LoginID_VARIABLE.get(),LoginPASSWORD_VARIABLE.get()):
            message=Label(Loginwindow,text="Incorrect Password",fg="red",font=("times new roman",20,"bold")).place(x=150,y=300)
        else :
            # message=Label(Loginwindow,text="Login Successfull",fg="green",font=("times new roman",20,"bold")).place(x=150,y=300)
            # Loginwindow.destroy()
            Loginwindow.withdraw()
            CartWindow()

def main():
    global mainWindow
    mainWindow=Tk()
    mainWindow.geometry("1920x800+0+0")
    mainWindow.title("Main Window")

    bg=ImageTk.PhotoImage(file="background.JPG")
    bgi=Label(mainWindow,image=bg).place(x=0,y=0,relwidth=1,relheight=1)

    frame1=Frame(mainWindow,bg="white").place(x=480,y=100,width=700,height=500)
    title=Label(frame1,text="Please Select any option to continue",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=600,y=110)
    LoginButton=Button(frame1,command=LoginWindow,text="Login",font=("times new roman",20,"bold"), bd = '0',cursor="hand2") .place(x=670,y=200,width=300,height=100)
    RegisterButton=Button(frame1,command=RegisterWindow,text="Register",font=("times new roman",20,"bold"), bd = '0',cursor="hand2").place(x=670,y=400,width=300,height=100)
    mainWindow.mainloop()

main()