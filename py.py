#https://docs.python.org/3.8/tutorial/index.html      - documentation
#python gets executed in the order in which its written
#variables and data types
char_name = "John"
char_age = 70 #or 70.5674 etc int, float
isMale = False #boolean
print("my name is " + char_name)
print( "my age is " + str(char_age)) #conversion of data types

#strings
print("Giraffe\n Academy") #next line
print("Giraffe\" Academy") # \ is an escape sequence, any character after that will be rendered literally i.e here it wont be detected as quotation of print
phrase = "Giraffe Academy" #storing in variable
print(phrase)
print(phrase + " is cool") #concatenation
print(phrase.lower()) #applying functions to the string
print(phrase.upper().isupper()) #applying multiple functions
print(len(phrase))
print(phrase[3])#0 indexing extracting character
print(phrase.index("a")) #gives index of first a
print(phrase.index("Acad")) #gives index of start of substring entered
print(phrase.replace("Giraffe","Elephant"))
print(phrase[2:6])#displays substring from 2 to 6 not including 6

#numbers
n = -5
print(abs(n)) #absolute 
print(pow(3,2)) #power
print(max(4,6)) #maximum or min
# import math for more like ceil, floor, sqrt

#input
var = input("enter name: ") #input is always taken as string value
age = input("enter age :")
print("hello " + var + " you are " + age)
#two ways of converting string to int(or float)
num1 = int(input("num1:"))
num2 = input("num2:")
print(num1 + int(num2))

#lists: a data structure,creating a list and putting a bunch of related values and use it throughout the program
#friends = ["kevin", 2, False] #can use diff data type
friend = ["kevin", "karen", "Jim"]  #can access by index
print(friend[-2])#can access with negatives too, this will give karen
friends = ["kevin", "karen", "Jim","lolo","hehe"]
print(friends[1:])#displays everything from index 1 onwards
print(friends[1:3])#diplays all elements from 1 to 3 not including 3

#list functions
lucky_nos = [4,8,15,16,23,42]
friends = ["kevin", "karen", "Jim","lolo","hehe"]
friends.extend(lucky_nos) #to append one list to another
friends.append("creel") #to add item to the end of list
friends.insert(1,"kellu")#to insert kellu at index position 1 and other elements get pushed to the right
friends.remove("Jim") #to remove an element
friends.clear() #to get rid of all elements of the list
friends = ["kevin", "karen", "Jim","lolo","hehe"]
friends.pop() #to remove last element
friends = ["kevin", "karen", "Jim","lolo","hehe"]
print(friends.index("lolo")) #a way to find if element is in the list
friends = ["kevin", "karen", "Jim","lolo","hehe","Jim"]
print(friends.count("Jim")) #to count no of occurences of jim
friends.sort() #to sort
lucky_nos.sort()
lucky_nos.reverse() #to reverse the order of list
friends2 = friends.copy #to copy all attributes of friends 

#tuples: type of data structure - they are immutable i.e they cannot be modified at all
coordinate = (4,5) #this is a tuple
print(coordinate[0]) 
coordinates = [(4,5), (6,7), (80, 34)] #list of tuples 

#functions and return stmt
def sayhi(name):
	print("hello user")
	return 1
age = sayhi("mike")
print(age)

#ifstmt
is_male = True
is_tall = False
if is_male or is_tall: #or => ||
	print("you're a tall or a male person")
elif is_male and is_tall: #and => &&
	print("you're a tall male")
elif is_male and not(is_tall): #not is for negation
	print("bleh")
else:
	print("you iz nothing son")
#in python: or, and , not
# >= <= != etc are valid too and can be used for strings too

#dictionaries:  stores info as key-valuepairs; keys should be unique; keys can be numbers too
months = {
	"Jan":"January",
	"Feb":"February",
	"Mar":"March"
}
#ways to access-
print(months["Mar"])
print(months.get("Dec","not found")) #second value is some kind of default message which is displayed if key entered cant be found 

#whileloops
i = 1
while i <= 10:
	print(i)
	i+=1
#forloop
for letter in "Giraffe Academy":
	print(letter)
friends = ["kevin", "karen", "Jim","lolo","hehe"]
for friend in friends:
	print(friend)
for index in range(10):
	print(index)#prints 0-9	
for index in range(3,10):
	print(index)#prints 3-9
for index in range(len(friends)):
	print(friends[index])

#exponentfunction: to raise a no. to a certain no.
print(2**3)#2^3

#2D Lists and nested loops
number_grid = [
	[1,2,3],
	[5,6,7],
	[9,4,8],
	[0]
]
print(number_grid[0][2])#accessing list elements
#to parse through the grid
for row in number_grid :
	for col in row :
		print(col)
#if letter in "AEIOUaeiou" => looking for vowel 
#try&except
try:
	no = int(input("enter no"))
	print(no)
except:
	print("wasnt a no ")
try:
	value = 10/0
	number = int(input("enter no."))
	print(number)
except ZeroDivisionError as err: #name of one possible error; #to print the real error
	print(err)
except ValueError:
	print("invalid input")

#files:to read file from outside of our python file

#read files
employee_file = open("employees.txt","r")#to open file; filename should have full path if not in same directory; second parameter is mode. "r" for reading(to read from the file and do stuff with the existing content), "w" for writing(can modify and write), "a" for appending(to add to end of file), "r+" for reading and writing
print(employee_file.readable())#if file is readable or not (ie if in read mode it will return True)
print(employee_file.read())#to read entire file ie outputs all contents
print(employee_file.readline())#to read one line from the file
print(employee_file.readline())#reads next line and prints out ; outputs with one line space
print(employee_file.readlines())#reads file and prints contents as a list
print(employee_file.readlines()[1])#outputs element at index 1 of the list created
for employee in employee_file.readlines():
	print(employee) #outputs each element of the list created out of the file
employee_file.close()#to close file
#writing and appending to files
employee_file = open("employees.txt","a")
employee_file.write("\nmoti")#be careful, if run twice it will append again and not in new line! so add \n
employee_file.close()#to close file
employee_file = open("employees.txt","w")
employee_file.write("hehe") #will overwrite on entire file! so file will end up having only this name as content
employee_file.close()
employee_file = open("employees1.txt","w")#here new file is created in the same directory and stuff is written to that
employee_file.write("hello new")
employee_file.close()
employee_file = open("employees.html","w")#html file will be created in the same directory
employee_file.write("<p>yo bois</p>") 
employee_file.close()
'''
module: python file that can be included in our python file
just import filepath(only filename if in same directory)
search python modules for an entire useful list
Lib stores external modules
built in modules are built into the python language so cant directly access them, will have to download
pip: is a package manager 
'''
#classes and objects
#we can essentially create data types using classes 
#for eg in a file named Student.py:
class Student: #to create a template kind of thing for student
	#define attributes about Student
#note that classes are private entities and to access stuff within them you need public entities. init here is a method and that lets us access all members inside init
'''
A method in python is somewhat similar to a function, except it is associated with object/classes. Methods in python are very similar to functions except for two major differences.

1.The method is implicitly used for an object for which it is called.

2.The method is accessible to data that is contained within the class.	
A method in object-oriented programming (OOP) is a procedure associated with a message and an object.
Python decided to do methods in a way that makes the instance to which the method belongs be passed automatically, but not received automatically: the first parameter of methods is the instance the method is called on.
Here comes the use of self. self basically refers to whichever instance(object) is being upon at that time .
''' 
	def __init__(self, name, major, gpa, is_on_probation): #initialize function; we can basically map out what attributes the student should have
	 			  
		self.name = name #here, the name of the object that is passed gets stored under name attribute. 
		self.major = major
		self.gpa = gpa
		self.is_on_probation = False
#in another python file we can use this class-
from Student #name of file
import Student #name of class
st1 = Student("Jim", "Business",3.1,False)
st2 = Student("pam", "Art",2.5,True)
#here, objects are created and their property values are passed to the respective attribute 
print(st1.major) #to access the values
print(st2.gpa)

#class functions
	#in addition to the init func above we can add this
	def on_honor_roll(self):
		if self.gpa >= 3.5:
			return True
		else:
			return False
print(st1.on_honor_roll())

#inheritance: inheriting one class into another
#class1
class Chef:
	def make_chicken(self):
		print("chef makes a chicken")
	def make_veges(self):
		print("chef makes veges")
#class 2, going to use(inherit) funcs of class 1  in 2
from Chef import Chef
class ChineseChef(Chef): #now we can use all functionalities of Chef in ChineseChef

	def make_machurian(self):
		print("chef makes machurian")
	def make_schezwan(self):
		print("chef makes schezwan")
#note: if class 1 and 2 both have same function, the one in which stuff is inherited overrides the one that is inherited. ie function in class 2 will override function in class 1
'''
super(): The super() function is used to give access to methods and properties of a parent or sibling class.

The super() function returns an object that represents the parent class.
**it prevent your extension of the class from conflicting with the inheritance class during inheritance**
[Super is used to] return a proxy object that delegates method calls to a parent or sibling class of type. This is useful for accessing inherited methods that have been overridden in a class. 
'''
class Parent:
  def __init__(self, txt):
    self.message = txt

  def printmessage(self):
    print(self.message)

class Child(Parent):
  def __init__(self, txt):
    super().__init__(txt)

x = Child("Hello, and welcome!")

x.printmessage()

#python interpreter: type python/python3 in terminal to open it
dr chuck course extra:
files - startswith() #starting of line under for line in filename
         rstrip() #removes blank lines line.rstrip() 
          split() #to split line or string into words and store
lists - split()
dictionaries - get(dicname,defaultvalue) #to display default value when dicname key doesnt exist
			   for word in words: #here words is a list of words suppose and dic is dictionary
			       dic[word] = dic.get(word,0)+1 #here if word is there its value increments and if not then it is created and value set to 1, this is a good way to count instances and store at the same time
tuples - if (a,b,c) > (b,d,c):
               print True #ans false cuz tuple compares first element if equal then second and so on. same with numbers. this is use in dictionaries because they cant have repetitive key names so making every key value pair a tuple and then sorting it will sort acc to tuple name (makes it more like a real dictionary)
       list of tuples can also be sorted(list)
       
***list comprehension(imp)- c = {'a':1,'b':42,'c':10}
							print(sorted([(v,k) for k,v in c.items()]))
							output: [(1,'a'),(10,'c'),(42,'b')]        





	



