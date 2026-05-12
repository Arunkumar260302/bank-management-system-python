import pymysql
class BankManagement:
    def __init__(self):
        self.con=pymysql.connect(
            host="localhost",
            user="root",
            password="Arun@2002",
            database="python02"
        )
        self.cur=self.con.cursor()
    def create_account(self):
        acc_no=int(input("Enter Account No: "))
        name=input("Enter Name: ")
        balance=int(input("Enter Balance: "))
        sql="insert into accounts values(%s,%s,%s)"
        val=(acc_no,name,balance)
        self.cur.execute(sql,val)
        self.con.commit()
        print("Account Created")
    def deposit(self):
        acc_no=int(input("Enter Account Number: "))
        amount=int(input("Enter Amount: "))
        sql="update accounts set balance=balance + %s where acc_no=%s"
        val=(amount,acc_no)
        self.cur.execute(sql,val)
        self.con.commit()
        print("Amount Deposited")
    def display(self):
        acc_no=int(input("Enter Account Number: "))
        sql="select * from accounts where acc_no=%s"
        self.cur.execute(sql,(acc_no,))
        data=self.cur.fetchone()
        print(data)
obj=BankManagement()
while True:
    print("1.Create Account")
    print("2.Deposit")
    print("3.Display")
    print("4.Exit")
    ch=int(input("Enter Choice: "))
    if ch==1:
        obj.create_account()
    if ch==2:
        obj.deposit()
    if ch==3:
        obj.display()
    if ch==4:
        break                            
