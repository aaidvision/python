Ex.No:1 Different Number Data Types

a=3
print a
print(type(a))
b=5.6
print b
print(type(b))
c='Noornisha'
print c
print(type(c))
d=2+3j
print d
print(type(d))

Ex. No. 2 Find the NCR values of a given number using function

def nCr(n,r):
 return(fact(n)/(fact(r)*fact(n-r)))
def fact(n):
 res = 1
 for i in range (2,n+1):
 res = res*i
 return res
n=int(input("enter the number n"))
r=int(input("enter the number r"))
print "the value is = ",int (nCr(n,r))

Ex. No. 3 Print whether a num is positive/negative using if else

a=int(input("enter the number "))
if (a>0):
print("the given number is positive")
else:
print("the given number is negative") 

Ex. No.4 Find whether this given values is prime or not using if elif

num = int(input("please enter any number:"))
if (num==0 or num==1):
 print num,"number is neither prime nor composite"
elif num>1:
 for i in range(2, num):
 if(num%i)==0:
 print num, "is not a prime number"
 break
 else:
 print num, "is prime number"
else:
 print num, "please enter the positive number only"

Ex. No. 5 Compute the number of vowels, constants and words in a file.

def counting(filename):
 txt_file=open(filename,"r")
 vowvel=0
 line=0
 consonants=0
 vowvels_list=['a','e','i','o','u','A','E','I','O','U']
 for alpha in txt_file.read():
 if alpha in vowvels_list:
 vowvel+=1
 elif alpha not in vowvels_list and alpha !="\n":
 consonants+=1
 elif alpha=="\n":
 line+=1
 print"Number of vowels in=",vowvel
 print"new lines in=",line
 print"number of consonants in=",consonants
counting('a.text')


Ex.No. 6 Print all of the unique words in a file in alphabetical order

infile=open('file.txt','r')
text=infile.read()
text=text.lower()
words=text.split()
words=[word.strip('.,!;()[]')for word in words]
words=[word.replace("'s",'')for word in words]
unique=[]
for word in words:
if word not in unique:
 unique.append(word)
unique.sort()
print (unique)

Ex. No: 7 Define a module to fine odd or even number between 1 and 100

def oddeven():
 start,end=1,100
 for num in range(start,end+1):
 if(num%2)==0:
 print("{0} is even number".format(num))
 else:
 print("{0} is odd number".format(num))
oddeven()

Ex. No: 8 Create a list 

List = ['Mathematics', 'chemistry', 'physics', 'computer sciene','commerce']
List.insert(2,'english') 
print List 
List.remove('commerce')
print List
List.append('tamil')
print List
print len(List)
print List.pop(0)
print len(List)
print List

Ex. No: 9 Create a tuple

test_tup1=(1,3,5,7,8,9)
test_tup2=(4,6)
print("the original tuple1:"+str(test_tup1))
print("the original tuple2:"+str(test_tup2))
res=test_tup1+test_tup2
print("the tuple after concatenation is:"+str(res))
N=4
res=((test_tup1,)*N)
print("the tuple after repetition is:"+str(res))
print("the membership of tuple1 and tuple2 is:")
print("the number 3 in test tup1:",3 in test_tup1)
print"the number 3 in test tup2:",3 in test_tup2
print("Accessing the items from tuple1")
for item in test_tup1:
 print(item)
stop=4
indices=slice(stop)
result=test_tup1[indices]
print"sliced tuple:",result 

Ex. No: 10 Sort ascending and descending order

y={'parveen':40,'noornisha':4,'np':1,'an':3}
l=list(y.items())
l.sort()
print 'Ascending order is',l
l=list(y.items())
l.sort(reverse=True)
print 'Descending order is',l
dict=dict(l)
print "dictionary",dict

Ex. No: 11 Find the area of rectangle using class and object.

class rect():
 def __init__(self,breadth,length):
 self.breadth=breadth
 self.length=length
 def area(self):
 return self.breadth*self.length
a=int(input("Enter breadth of rectangle:"))
n=int(input("Enter length of rectangle:"))
obj=rect(a,n)
print "Area of rectangle:",obj.area()

