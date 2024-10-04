1)data type
m = 7001
print(m,type(m))
n = 664.65
print(n,type(n))
p = 'usaif ahamed'
print(p,type(p))

2)positive
a=int(input("Enter x: "))
if (a > 0):
    print(a,"is positive")
else:
    print(a,"is negative")

3)prime or not
def prime(num):
    if num <=1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
number=int(input("enter the number:"))
if prime(number):
    print(number,"is prime")
else:
    print(number, "is not a prime number")


4)NCR
n=int(input("enter n value"))
r=int(input("enter r value"))
def fact(x):
    f=1
    for i in range(1,x+1):
        f=f*i
    return f
NCR=fact(n)/(fact(r)*fact(n-r))
print("NCR value 15:",NCR)

5)Vowel
vow=['a','e','i','o','u']
con=[]
for i in range(97,122):
    if(chr(i)not in vow):
        con.append(chr(i))
    print(con)
print(x)
print(len(x))
f=open('c.txt','r')
m=f.read()
x=m.split()
v=0
c=0
for j in m:
    if j in vow:
        v+=1
    elif j in con:
        c+=1
print('No.of vowels= ',v)
print('No.of Consonants= ',c)

6)alpha
f = open ("a.txt","r")
g = f.read()
h = g.split()
print("Given Names (INPUT)")
print(h)
n = len(h)
for i in range(0,n-1):
    for j in range(i+1,n):
        if(h[i]>h[j]):
            t=h[i]
            h[i]=h[j]
            h[j]=t
print("NAMES IN ALPHABETICAL ORDER")
print(h)

7)odd or even
def Oddeve(x):
    if (x%2==0):
        print(x,"is even")
else:
    print(x, "is odd")


import pack1
for i in range (1,10):
    pack1.Oddeve(i)



8)class and object
class Rect:
    def __init__(self, B, L):
        self.B = B
        self.L = L
    def area(self):
        return self.B * self.L
p1 = Rect(6, 5)
print("Breadth of Rectangle =", p1.B)
print("Length of Rectangle =", p1.L)
print("Area of Rectangle =", p1.area())

9)sort
fruit = {"1":"APPLE","2":"BANANA","3":"GRAPE","4":"ORANGE"}
print(fruit)
print("Student Values \n", fruit.values())
print("Student Keys \n", fruit.keys())
roll = list (fruit.values())
roll.sort(reverse=True)
print("Students value in reverse\n", roll)
name = list (fruit.values())
name.sort()
print("Student Keys Sorted\n", name)



10)tuple
v = ("ABDULLA","USAIF","SALMAAN", 47)
print("Tuple Values:")
print(v)
v = v + (17,77)
print("1.Values after Concatenation:")
print(v)
v = v * 2
print("2.Values after Repetition:")
print(v)
w = "SALMAAN"
print("3.Finding SALMAAN in Membership....")
if w in v:
    print(w, "is member of v")
else:
    print(w, "is not member of v")
print("4.Accessing the Items:")
print("Accessing 1st Item = ",v[0])
print("Accessing 4th Item = ",v[3])
print("5.Slicing the Values:")
print(v[2:4])

11)list
members=["ABDULLA", "USAIF", "NASAR", "SALMAAN"]
print("List",members)
members.insert(2, "BASHEEER")
print("OP:1.After inserting a new value in 2nd position")
print("List",members)
members.remove("USAIF")
print("OP:2. After removing an particular element")
print("List",members)
members.append("AHAMED")
print("OP:3.After adding a new element")
print("List",members)
print("OP:4. Total number of elementss in list", len(members))
members.pop()
print("OP:5.Default pop delete the last element")
print("List",members)
