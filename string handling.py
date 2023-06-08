import re
##String Handling

#name = ' fred ' ' blogga ' ' peter '
#testvar='test'

#print(name + 'test')

#print("The answer is ", 42, "always", sep='\b', end='')

#html="  <tr>    <td> <font colour="#69000"> <b> Username : </b> </font> </td> "

name= ' Sky Glass '

#covert to lower case
print('Sky'.lower())

#convert to upper case
print(name.upper())

#replace a string
name1=name.replace('y','e')
print(name1)

#find a string
print(name.find('s'))

#ends with
if name.endswith('y'):
    print("name ends with y")

print (name.endswith('k'))

#length of string
print(len(name))

#slicing start:end -1
print(name[2:5])

#strips empty spaces
print(name.strip())

age = 20
message= "Hello, my age is "+str (age)
print(message)

newMessage = "Hello, my age is {} "
print(newMessage.format(age))

newMessage1="Hello, my age is {1} and I work with {0} "
print(newMessage1.format(20,'sky'))

#string split
line='root::0:0:superuser:/root:/bin/sh'
elems=line.split(':')

print(elems[0])
print(elems[1])
print(elems[2])
print(elems[3])

line1='Hello World, This is sunny.'
elems1=line1.split('T')
elems1=line1.split('W')

print(elems1[0])
print(elems1[1])

##Regex
message="Sky Glass"
newMessage=re.search("^Sky.*Glass$",message)
print(newMessage)
if newMessage:
    print("text found")
else:
    print("text not found")

text="hello world 123"
if re.match(r"^hello", text):
        print("its hell in there")

if re.match(r"^[0-9 a-z]+$",text):
        print("string is all alpha")

