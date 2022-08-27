def sum(a):
#     i=0
#     sum=0
#     while i<len(a):
#         sum=sum+a[i]
#         i=i+1
#     print(sum)

# sum((8, 2, 3, 0, 7))

# def reverse(a):
#     for i in a:
#         b=str(a[i])

# reverse("1234abcd")

# def uniq(a):
#     i=0
#     b=[]
#     while i<len(a):
#         if a[i] not in b:
#             b.append(a[i])
#         i=i+1
#     print(b)

# uniq([1,2,3,3,3,3,4,5])

# # from selectors import EpollSelector


# if bmi <= 18.5 return "Underweight"

# if bmi <= 25.0 return "Normal"

# if bmi <= 30.0 return "Overweight"


# def value(underweight,normal,overhight,obese):
#     i=0
#     if  i<=18.5:
#         print("Underweight")
#     elif i<=25.0:
#         print("normal") 
#     elif i<=30.0:
#         print("overhight")
#     else:
#         print("obese")
    
# value("18.5","25.0","30.0","31.0")


# def my_function(a):
#     # a=int(input("enter a number"))
#     if a%2==0:
#         print("even number")
#     else:
#         print("odd number")
  
# my_function(2)

# def my_function(a):
#     i=0
#     if a%2==0 and a%a==0:
#         print("not prime")
#     else:
#         print("prime number")
#     i=i+1

# my_function(4)


# def  multiply(a):
#     i=1
#     while i<=10:
#         print(a,"*",i,"=",i*a)
#         i=i+1
# multiply(12)

# def even(a):
#     i=0
#     b=[]
#     while i<len(a):
#         if a[i]%2==0:
#             b.append(a[i])
#         i=i+1
#     # print(b)
#     return(b)
    
# print(even([1,2,3,4,5,6]))

# def square(a,b):
#     i=0
#     c=[]
#     d=[]
#     while i<len(a):
#         s=a[i]**2
#         t=b[i]**2
#         c.append(s)
#         print(c)
#         d.append(t)
#         print(d)
#         i=i+1
# square([1,2,3,4,5],[26,27,28,29,30])

# def sum(a,b):
#     a=4
#     b=5
#     print(a+b)
# sum("a","b")

# def age(a):
#     i=0
#     while i<len(a):
#         if a[i]<10:
#            print("eligible to school")
#         elif a[i]<18:
#            print("eligible to vote")
#         elif a[i]<20:
#            print("eligible to drive")
#         else:
#            print("eligible to marry")
#         i=i+1
     
# age([10,18,20])


# num = 1
# def func():
#     num = 3
#     print(num)

# func()
# print(num)

# num = 1
# def func():
#     global num
#     num = num + 3
#     print(num)

# func()
# print(num)


# from itertools import count
# from string import ascii_uppercase


# def positive(a):
#     i=0
#     count=0
#     d=0
#     while i<len(a):
#         if a[i]>0:
#             count=count+1
#         else:
#             d=d+1
#         i=i+1
#     print("positive numbers",count)
#     print("negitive numbers",d)

# positive([2, -7, 5, -64, -14])


# def number():
#     a=int(input("enter a number"))
#     if a%3==0:
#         print("FIZZ")
#         if a%5==0:
#            print("BUZZ")
#            if a%3==0 and a%5==0:
#               print("FIZZ BUZZ")
#     else:
#         print(a)
# number()


# def fun():
#     a="The quick Brow Fox"
#     i=0
#     count=0
#     count1=0
#     while i<len(a):
#         if ascii_uppercase in a:
#             count=count+1
#             print(count)
#         else:
#             count1=count1+1
#             print(count1)
#         i=i+1
#     # print(count)
#     # print(count1)
# fun()

# def fun():
#     a="The quick Brow Fox"
#     count1=0
#     count2=0
#     for i in a:
#         if i>="A" and i<="Z":
#            count1=count1+1
#         elif i>="a" and i<"z":
#            count2=count2+1
#     print("capital letters",count1)
#     print("small letters",count2)
# fun()

# def match_words(words):
#   ctr = 0

#   for word in words:
#     if len(word) > 1 and word[0] == word[-1]:
#       ctr += 1
#   return ctr

# print(match_words(['abc', 'xyz', 'aba', '1221']))


# def revers_string(a):
#     b=""
#     i=len(a)
#     while i>0:
#         c=a[i-1]
#         b=b+c
#         i=i+1
#     return b
# print(revers_string("1234abcd"))

# # def show_numbers():
#     limit=int(input("enter a  number"))
#     i=0
#     while i<len(limit):
#         if 


# x=5
# def fun():
#     y=3
#     x=y+4
#     print(x)
# y=x+3
# print(y)
# fun()


# def  multiply(a):
#     i=1
#     while i<=10:
#         print(i,"*",a,"=",i*a)
#         i=i+1
# multiply(5)
# def my_fun():
#     a=[1,9,9,1]
#     i=0
#     while i<len(a):
#         print(a[i]**2,end="")
#         i=i+1
    
# my_fun()

# def my_fun(a):
#     i=0
#     c=[]
#     max=0
#     ind=0
#     while i<len(a):
#         b=len(a[i])
#         if max<(b):
#             max=b
#             ind=a[i]
#         i=i+1
#     print(ind,max)
# my_fun([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])


# a=[3,4,9,2,7,6,4,4,3,0]
# i=0
# b=[]
# c=[]
# while i<len(a):
#     if a[i] in a[i]:  
#         print(a[i])
#     # else:
#     #   c.append(a[i])
#     i=i+1



# def Remove(duplicate):
#     final_list = []
#     for num in duplicate:
#         if num not in final_list:
#             final_list.append(num)
#     return final_list
     
# # Driver Code
# duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
# print





# i=1
# count=1
# while count<5:
#     print(count)
#     count+=1


# n=int(input())
# if n%2==0:
#     print("even")
# else:
#     print("odd")


# counter=1
# while counter<=100:
#      if counter%2==0:
#       print("counter")
#       i=i+1

# def string_reverse(str):

#     rstr = ''
#     i = len(str)
#     while i > 0:
#         rstr += str[ i - 1 ]
#         i= i - 1
#     return rstr
# print(string_reverse('1234abcd'))
