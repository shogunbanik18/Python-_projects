# import cv2
# import math
# # this is a comment 
# print("Hello World\n")
# print(math.gcd(3,6))
# # this is a comment 
# print(5+8)
# '''
#     this is a multi-line comment 
# '''
b="Harry"
c = 45.32
d=2
a= 34 

print(a) 
print(b) 
print(c) 
print(a+d)
print(a-d)
print(a*d)
print(a/d)


# Wrong syntax 
# harry project =45

#1. variable shoud start with a letter or an alphabet 
# 2.variable cannot start with a number 
#it can only contain alphanumeric charactger 
# variable names case sensitive i.e Harry and harry are different variables 
typeA =type(a)
typeB =type(b)
print(typeA)
print(typeB)
e ="31.23"
# e =int(e)
e=str(e)
# e =float(e)s
# e =3.14
print(e)
print(type(e))


name ="shogun,Sonu,sonty" 
# multiline strings use single cotes three times
# name ='''shogun
#         is a good boy '''

# slicing of strings 
# print(name[2:4])
# print(name)
# print(len(name))
# print(name.strip())

var =name.lower()
var =name.replace("o","a")
var =name.replace(","," ")
# print(var)

stri ="This is a"
name =" Shogun"
name2="Rohan"
stri2 = "This is not a"
            # use of f string 
# temp ="this is a {0} and he is a good boy named {1}".format(name,name2)
temp =f"this is a {name} and he is a good boy named {name2}"

print(temp)
print(stri+ name +  stri2)
# QUIZ :TRY THESE OPERATOR 

#1. ** exponent operator 
# 2. // floor division operator
# 3. % modulo operator 
a=8
print(a**2)
print(a//2)
print(a%2)

''' 
    PYTHON COLLECTION
    1.List
    2.Tuple
    3.set
    4.Dictionary
'''

    # '''lIST  JUST LIKE ARRAY IN OTHER PROGRAMMING LANGUAGES'''
    # ITEMS CAN BE CHANGED IN LIST 
lst = [61,2,3,4,6,41]
var= type(lst)
lst[2]=45
# var =lst[2]
# # .append is used to add element at the end of list 
# # lst.append(100)
# lst.insert(1,100)
# lst.remove(61)
# # removes the last element 
# lst.pop()

# del lst[2]
var=lst
print(var)
lst.clear()

'''TUPLE'''
# ''' ITEMS CANNOT BE CHANGED IN TUPLE '''
# VARIABLES ONCE ASSIGNED CANNOT BE CHANGED 
a = ("Harry","Shogun","Rohan")
var =a
# a[0] ="vikrant"
# since it is a tuple 
#  CANNOT DO THIS

# a= list(a)
# a[0] ="vikrant"
# var =a

print(var)
print(type(var))

# print(x)

'''SET NO REPEAT OF ELEMENTS '''
s1={23,2,2,2,2,2,2,2,2,2,2,2,2,25,2,2,2,4,4,4,4,4,4,4,4,4,4,4,4,5,5,5,5,5}
s1.add(33333)
s1.update([12,12,423,3423,634,123,432,23])
print(len(s1))
s1.discard(5)
# .pop,.clear,.del,.intersection,.union just like lists
print(s1)


'''# DICTIONARY'''
harryDict = {
    "Name" : "Harry",
    "Class": "4th",
    "Marks" : 34.34,
    "Hours in school": 6,
}

# print(harryDict)
harryDict["Marks"] = 34
print(harryDict["Marks"])
print(harryDict)
harryDict.pop("Marks")
# Functions that can be used 
# del,clear,pop,update 
print(harryDict)

# Conditionals In Python 
# age= 34 
            # user defined input 
age =input("Enter your Age\n")
age =int (age)
# print(type(age))
if (age>18) :
    print("You can drive a car")

# elif just like else if in c program 
elif(age==18):
    # a= true
    # b=false
    print("You are an Awesome Teen") 
else:
    print("You cannot drive a car")


#Loops 
#scenario : you have to print numbers between 1 to 1000
        # use of for loop 

# for i in range(0,1000):
#     print(i)


li=[1,432,"this"]
for item in li:
    print(item)

# quiz : use for loops to iterate dictionary and sets and tuple 
# while loop 
# use of break 
# continue is used for skipping a particular value 
# i=0
# while(i<100):
#     i+=1
#     if i==78:
#         continue
#     print(i+1)


# Functions
# syntax 
def greet():
    print("Good Morning Sir")
    print("Good Morning maam")
    print("Good Morning uncle")

greet()
# greet()
# greet()

def sum(a,b):
    print("Running Sum")
    c=a+b
    return a+b

d=sum(3,4)
print(d)


# Object oriented programming part 
class Employee:
    # use of constructor 
    # def__init__(self , gname, gsalary):
    # def__init__(self, gname ,gsalary)
    #     self.name = gname
    #     self.salary = gsalary

# harry =Employee("Harry", 34)
# print(harry.name)
# print(harry.salary)