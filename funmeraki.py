def my_function(option):
  print("who is the founder of face book? " + option[0])

my_function("mark gukerberg","bill gates","steve jobs",'larry page')




def my_function(a):
    i=0
    while i<len(a):
        i=i+1
    print("who is the founder of facebook",a[0])
my_function(["mark gukerberg","bill gates","steve jobs","larry page"])


2
def my_function(a):
    i=0
    max=0
    while i<len(a):
        b=a[i]
        if max<b:
            max=b
        i=i+1
    print(max)
my_function([3, 5, 7, 34, 2, 89, 2, 5])



def my_function(a):
    i=0
    sum=0
    while i<len(a):
        sum=sum+a[i]
        i=i+1
    print(sum)

my_function([3,5,34,2,89,2,5])


def my_function(a):
    a.sort()
    print(a)

my_function([6, 8, 4, 3, 9, 56, 0, 34, 7, 15])



def my_function(a):
    a.reverse()
    print(a)

my_function(["Z", "A", "A", "B", "E", "M", "A", "R", "D"])

def my_function(a):
    i=0
    min=a[i]
    while i<len(a):
        if min>a[i]:
            min=a[i]
        i=i+1
    print(min)

my_function([8, 6, 4, 8, 4, 50, 2, 7])

def sum():
    print(12+13)
sum()

def welcome():
   print("Welcome to function")
welcome()


def isEven():
    if(12%2==0):
       print("Even Number")
    else:
       print("Old Number")

isEven()
def list (a):
    i=0
    count=0
    while i<len(a):
        j=0
        count=0
        while j<len(a[i]):
            if  a[i][j]==a[i][j]:
                count=count+1
            j=j+1
        i=i+1
    print(count)

list=(['abc', 'xyz', 'aba', '1221'])

                

def say_hello_language(name, language):
    if language == "hindi":
      print("Namaste ", name)
      print("Aap kaise ho?")
    elif language == "punjabi":
      print("Sat sri akaal ", name)
      print("Tuhada ki haal hai?")
    else:
      print("Hello ", name)
      print("How are you?")
say_hello_language("Rishabh", "punjabi")
say_hello_language("Armaan", "english")
say_hello_language("Abhishek", "french")
say_hello_language("Kavay", "hindi")


def say_hello_people(name_x, name_y, name_z, name_a):
    print("Namaste ", name_x) # In hindi
    print("Alah hafiz ", name_y) # In urdu 
    print("Bonjour ", name_z) # In french 
    print("Hello ", name_a) # In english 
say_hello_people("Imitiyaz", "Rishabh", "Rahul", "Vidya")
say_hello_people("Steve", "Saswata", "Shakrundin", "Rajeev")


def attendence (name,status="absent"):
    print(name,"is",status)

attendence("meghna,","prsent")
attendence("mouni")
attendence("sashi","present")
attendence("somesh")

def greet(*names):
   for name in names:
      print("Welcome", name)


greet("Rinki", "Vishal", "Kartik", "Bijender")



def info (name,age=4):
    print(name,"is",age,"year old")

info("somesh")
info("mouni","15",)


def studentdetails(name,currenttopic,mentername):
    print(name,"your",currenttopic,"is claer with the help of ",mentername)

studentdetails("meghana","function","salony chowda")


def function_print_lines(name,foundationname):
    print("my name is ",name)
    print("i am the co_founder of the ",foundationname)

function_print_lines("rishab","Navgurukul")

def greter_than_20(a,b):
    print(a,"is greater than 20")

greter_than_20("30")
greter_than_20("30","40")

def add_numbers(num1,num2):
    num1=56
    num2=12
    print((num1+num2))

add_numbers("num1","num2")

def check_numbers(a,b):
   a=2
   b=7
   if a%2==0 and b%2==0:
       print("both are even")
   else:
       print("both are not even numbers")
    

check_numbers("a","b")

def check_numbers(a,b):
    a=[2, 6, 18, 10, 3, 75]
    b=[2, 6, 18, 10, 3, 75]
    i=0
    while i<len(a):
        if a[i]%2==0 and b[i]%2==0:
            print("both are even")
        else:
            print("not both are  even")
        i=i+1

check_numbers("a","b")

