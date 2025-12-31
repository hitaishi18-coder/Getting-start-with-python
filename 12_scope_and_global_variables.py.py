# COLLECTIONS --------  >> LIST , TUPLE , SET , DICTIONARY

# ------ LISTS --------

# used to store collections of data 
# allow duplicate 

thislist = ["apple","banana","cherry"]
print(thislist)

thislist = ["apple","banana","cherry","apple","cherry"]
print(thislist)

print(len(thislist))


list1 = ["apple","banana","cherry"]
list2 = [1,5,7,9]
list3 = [True, False, False]


list1 = ["abc", 34 , True , 40, "male"]
print(type(list1))

# list constructor 
thislist = list(("apple", "banana","cherry"))
print(thislist)

print(thislist[1])

# negative indexing means -1 refers last index 

thislist = ["apple","banana","cherry"]
print(thislist[-1])

# ranges 

thislist = ["apple","banana","cherry","orange","kiwi","melon","mango"]
print(thislist[2:5])

thislist = ["apple","banana","cherry","orange","kiwi","melon","mango"]
print(thislist[:4])

print(thislist[2:])

print(thislist[-4:-1])


thislist = ["apple","banana","cherry"]
if "apple" in thislist:
    print("yes, apple is in the fruit list")


# change the item value 
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#change the range of item value 

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)


# insert item 

thislist = ["apple","banana","cherry"]
thislist.insert(2,"watermelon")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# append item 
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# extend 
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# add any iterable 
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# remove item 
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

# remove specified index 
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


# loop lists 
thislist = ["apple","banana","cherry"]
for x in thislist:
    print(x)


thislist = ["apple","banana","cherry"]
for i in range(len(thislist)):
    print(thislist[i])

print("--------")    

# using while loop

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#list comprehemsion 

fruits = ["apple","banana","cherry","kiwi","mango"]
newlist = []

for x in fruits:
    if "a" in x :
        newlist.append(x)

print(newlist)        


newlist = [x for x in fruits if "a" in x ]
print(newlist)

newlist = [x for x in fruits if x != "apple"]
print(newlist)

# no if statement 
newlist = [x for x in fruits]


newlist = [x for x in range(10)]
print(newlist)

newlist = [x for x in range(10) if x < 5 ]
print(newlist)


newlist = [x.upper() for x in fruits]
print(newlist)

# you can set outcome to whatever you like 
newlist = ['hello' for x in fruits]
print(newlist)

# replace element 
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

# sorting 
thislist = ["orange","mango","kiwi","pineapple","banana"]
thislist.sort()
print(thislist)


thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# sort descending 
thislist = ["orange","mango","kiwi","pineapple","banana"]
thislist.sort(reverse = True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse= True)
print(thislist)

# customise sort function 

def myfunc(n):
    return abs(n - 50)
thislist = [100, 50, 65, 82, 32]
thislist.sort(key = myfunc)
print(thislist)

# case sensitive sort 
thislist = ["banana","orange","kiwi","cherry"]
thislist.sort()
print(thislist)


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# reverse order : reverse the order of the list 
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# copy list 
thislist = ["apple","banana","cherry"]
mylist = thislist.copy()
print(mylist)
print("-----")

# use list() method 
thislist = ["apple","banana","cherry"]
mylist = list(thislist)
print(mylist)
print("-----")


#slice 
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(thislist)

# join lists 
list1 = ["a","b","c"]
list2 = [1,2,3]

list3 = list1 + list2
print(list3)

list1 = ["a","b","c"]
list2 = [1,2,3]
for x in list2:
    list1.append(x)

print(list1)    

list1 = ["a","b","c"]
list2 = [1,2,3]

list1.extend(list2)
print(list1)