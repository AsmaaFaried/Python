



from asyncio.windows_events import NULL
import re,mysql.connector

try:
   mydb = mysql.connector.connect(
   host="localhost",
   user="root",
   password="",
   database='Python'
   )
except Exception as ex:
    print("SQL Exception : ",ex)

class Person:
    def __init__(self,full_name, money, sleep_mood, health_rate):
        self.full_name=full_name
        self.money=money
        self.sleep_mood=sleep_mood
        if health_rate >0 and health_rate < 100:
            self.health_rate=health_rate
        else:
            self.health_rate=NULL
        

    def sleep(self,hours):
        if hours == 7:
            print("Happy sleep : "+self.hours)
        if hours > 7:
            print("lazy sleep : "+self.hours)
        if hours < 7:
            print("Tired sleep : "+self.hours)
        

    def eat(self,meals):
        if meals == 3:
            print(self.meals+" meals = 100 health rate")
        if meals == 2:
            print(self.meals+" meals = 75 health rate")
        if meals == 1:
            print(self.meals+" meal = 50 health rate")


    def buy(self,items):
        if items == 1:
            self.money=self.money-10
        return Person.buy 


class Emp(Person):
    def __init__(self, full_name, money, sleep_mood, health_rate,id, email, work_mood, salary ,is_manager):
        super().__init__(full_name, money, sleep_mood, health_rate)
        self.id=id
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if re.fullmatch(regex, email):
            self.email=email
        else:
            self.email=NULL
        self.work_mood=work_mood
        if salary >= 1000:
            self.salary=salary
        else:
            self.salary=0
        self.is_manager=is_manager

    def work(self,hours):
        if hours == 8:
            print("Happy work")
        if hours > 8:
            print("lazy work")
        if hours < 8:
            print("Tired work")

    def sendEmail(self,to, subject,bodyreceiver_name):
        f=open("sendEmail.txt",'w')
        f.write("To:"+to+"\n Subject: "+subject+"\n Body: "+bodyreceiver_name)
        f.close()



cur = mydb.cursor()    
cur.execute('''CREATE TABLE Employee(
            id int primary key not null,
            full_name char(60),
            email char(60),
            money double,
            salary double,
            work_mood char(60),
            sleep_mood char(60),
            health_rate int,
            is_manager boolean
            );''')


class Office:
    def __init__(self,name,employees):
        self.name=name
        self.employees=employees

    def get_all_employees(self):
        cur.execute(''' SELECT * FROM Employee''')
        rows = cur.fetchall()
        for row in rows:
            print(row)
    def get_employee(self,Emp_Id):
        cur.execute(f'SELECT * FROM Employee WHERE id='+Emp_Id)
        print(cur.fetchone())
    def hire(self,Emp):
        print(Emp)
        query1=f'INSERT INTO Employee(id,full_name,email, money,salary, work_mood, sleep_mood, health_rate, is_manager)values({Emp["id"]}, "{Emp["full_name"]}",{Emp["email"]}, "{Emp["mony"]}",{Emp["salary"]},{Emp["work_mood"]},{Emp["sleep_mood"]},{Emp["health_rate"]},{Emp["is_manager"]})'
        cur.execute(query1)
    def fire(self,Emp_Id):
        cur.execute(f'DELETE FROM Employee WHERE id='+Emp_Id)   

#################### Menu ##################

flag =True
while(flag):
    officeObj=Office('office One',[])
    print("1-Add :\n2-Get Employee\n3-Get All Employees :\n4-Delete Employee :\n5-Quit\n")
    choice=input("Enter choice: ")
    if choice=="1":
            id=input("Enter ID : ")
            full_name=input("Enter Name : ")
            email=input("Enter Email: ")
            money=input("Enter Money : ")
            salary=input("Enter Salary : ")
            work_mood=input("Enter work_mood : ")
            sleep_mood=input("Enter sleep_mood : ")
            health_rate=input("Enter health_rate : ")
            is_manager=input("Enter number 1 if this is a manager : ")
            officeObj.hire({"id":id, "full_name":full_name,"email":email,"money":money,"salary":salary,"work_mood":work_mood,"sleep_mood":sleep_mood,"health_rate":health_rate,"is_manager":is_manager})
    elif choice=="2":
            id=input("Enter ID : ")
            officeObj.get_employee(Emp_Id)
    elif choice=="3":
            officeObj.get_all_employees()
    elif choice=="4":
            id=input("Enter Employee ID : ")
            officeObj.fire(Emp_id)
    elif choice=="5":
            exit
    else:
         print('Wrong choice number, please choose correct one')
         flag =False

mydb.commit() 
mydb.close()
