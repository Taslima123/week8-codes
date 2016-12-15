print("Welcome to the Prudent Healthcare Hospital")
print("Lets start with users login process:-")
print("1.Registration\n2.Appointment\n3.Payment\n4.Exit")

#textfile="read.txt"  for record patient information
#textfile="paid.txt"  for record payment information
#textfile="app.txt"  for record appointment information

def login():
    email=input("Enter your username:")
    passw=input("Enter your password:")
    print("username and password matched")
    print("login successful")


def writes(patient_id, first_name, last_name, address, gender,DOB,contact):
    fw = open('read.txt', "a")
    fw.write("%1s%20s%20s%20s%20s%20s%20s\n" % (patient_id, first_name, last_name, address, gender,DOB, contact))
    fw.close()

def registration():

    post=input("only physician can login")
    print(post)
    login()
    print("You are a physian")
    users = input("now registration of patient press Enter")
    patient_id = input("Enter patient_id:")
    first_name = input("Enter your first_name:")
    last_name = input("Enter your last name:")
    address = input("Enter your address:")
    gender = input("Enter your gender: ")
    DOB=input("Enter your DOB")
    contact = input("Enter your contact number:")
    writes(patient_id, first_name, last_name, address, gender,DOB, contact)
    print("THANK YOU!!!")
    print("\nUser created!\n")
    print("information saved in text file")
    last()

def read():
    users = open("read.txt",'r')
    extract = input("Please input patient ID")
    for each_line in users:
        (patient_id, first_name, last_name, address, gender,DOB, contact) = each_line.split()

        if (patient_id == extract):
            print(patient_id, first_name, last_name, address, gender,DOB, contact)
    users.close()

def appointment2w(patientID,AppointmentID,Doctor,status):
    fw = open('app.txt', "a")
    fw.write("%1s%20s%20s%20s\n" % (patientID,AppointmentID,Doctor,status))
    fw.close()

def appointment2():
    read()
    patientID=input("re Enter your patientID")
    AppointmentID=input("Enter your AppointmentID")
    Doctor = input("Choose your doctor\n Dr.kelvin\n Dr.Scott \n Dr.Nitesh \n Dr.Richard")
    status=input("Complete or Appointment")

    appointment2w(patientID, AppointmentID,Doctor,status)
    last()


def cost(extract,name,through,recebill):
        fw = open('paid.txt', "a")
        fw.write("%1s%20s%20s%20s\n" % (extract,name,through,recebill))
        fw.close()


def credit(extract,name,through,amount):
    fw = open('paid.txt', "a")
    fw.write("%1s%20s%20s%20s\n" % (extract,name,through,amount))
    fw.close()

def cashpaid():
    read()
    extract = input("Please re-input patient ID")

    name=input("Enter your name")
    through=input("write through cash")
    recebill = input("Please enter the amount in Rs.:-")
    print(recebill)
    cost(extract,name,through,recebill)
    print("Thank you")
    last()

def creditpaid():
    read()
    extract = input("Please re-input patient ID")

    name = input("Enter your name")
    through = input("write through credit card")
    crebill = input("Please enter the credit card number")
    amount = input("please enter total amount in Rs.")
    print(crebill)
    credit(extract, name, through, amount)
    print("Thank you")
    last()

def last():
    print("1.Registration\n2.Appointment\n3.Payment\n4.Exit")

    choose = input("Enter Choice?")
    number = int(choose)

    if (number == 1):

        registration()

    elif (number == 2):
        appointment2()

    elif (number == 3):
        post = input("only accountant can login")
        print(post)
        login()

        users = input("1.By cash\n2.By Credit")
        number = int(users)
        if (number == 1):
            cashpaid()
        elif (number == 2):
            creditpaid()
        else:
            print("wrong choice")

    elif (number == 4):
        logout()
    else:
        print("wrong choice")


def logout():
    print("logout")
#main part
choose= input("Enter Choice?")
number= int(choose)

if (number==1):
    registration()

elif(number==2):
    appointment2()

elif(number==3):
    post = input("only accountant can login")
    print(post)
    login()
    print("you are login as a accountant")

    users = input("1.By cash\n2.By Credit")
    number = int(users)
    if (number == 1):
        cashpaid()
    elif (number == 2):
        creditpaid()
    else:
        print("wrong choice")

elif (number == 4):
    logout()
else:
    print("wrong choice")
