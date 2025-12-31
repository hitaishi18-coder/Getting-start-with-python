#------ SETS IN PYTHON -------
# Sets are unordered, unindexed, and do not allow duplicate values
# immutable 

thisset = {"apple", "banana", "cherry"}

# Looping through a set
# Order is not guaranteed in sets
for x in thisset:
    print(x)


thisset = {"apple", "banana", "cherry"}
# Checking if an element exists in set
print("banana" in thisset)


thisset = {"apple", "banana", "cherry"}
# Checking if an element does NOT exist in set
print("banana" not in thisset)


thisset = {"apple", "banana", "cherry"}
# Adding a single element to the set
thisset.add("orange")
print(thisset)


thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
# Adding elements from another set
thisset.update(tropical)
print(thisset)


thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
# update() can also add elements from a list
thisset.update(mylist)
print(thisset)


thisset = {"apple", "banana", "cherry"}
# remove() removes specified element
# Raises error if element not found
thisset.remove("banana")
print(thisset)


thisset = {"apple", "banana", "cherry"}
# discard() removes element safely
# Does NOT raise error if element not found
thisset.discard("banana")
print(thisset)


thisset = {"apple", "banana", "cherry"}
# pop() removes a random element
# Because sets are unordered
x = thisset.pop()
print(x)
print(thisset)


thisset = {"apple", "banana", "cherry"}
# clear() removes all elements from set
thisset.clear()
print(thisset)


thisset = {"apple", "banana", "cherry"}
# del deletes the entire set
del thisset

# Accessing after deletion will raise NameError
# print(thisset)


thisset = ["apple", "banana", "cherry"]
# This is a LIST, not a set
# Looping through list
for x in thisset:
    print(x)

# -------- SET UNION --------
# Union means: all unique elements from both sets

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
# union() returns a NEW set containing all unique elements
print(set3)


set3 = set1 | set2
# | is another way to perform union (only works with sets)
print(set3)


set3 = set1.union(set2, {"John", "Elena"}, {"apple", "bananas", "cherry"})
# union() can take multiple sets at once
print(set3)


set3 = set1 | set2 | {"John", "Elena"} | {"apple", "bananas", "cherry"}
# Using | operator to combine multiple sets
print(set3)


x = {"a", "b", "c"}
y = (1, 2, 3)
# union() also works with other iterables like tuples

z = x.union(y)
print(z)


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set1.update(set2)
# update() adds elements of set2 into set1
# NOTE: update() modifies the original set
print(set1)



# -------- SET INTERSECTION --------
# Intersection means: common elements only

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
# Returns a new set with common elements
print(set3)


set3 = set1 & set2
# & is another way to do intersection
print(set3)


set1.intersection_update(set2)
# Keeps only common elements in set1
# Original set is modified
print(set1)


set1 = {"apple", 1, "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)
# IMPORTANT:
# True == 1 and False == 0 in Python
# So they are treated as same values in sets
print(set3)



# -------- SET DIFFERENCE --------
# Difference means: elements present in first set but NOT in second

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)
# Returns elements only in set1
print(set3)


set3 = set1 - set2
# Another way to perform difference
print(set3)


set1.difference_update(set2)
# Removes common elements from set1
# Modifies the original set
print(set1)



# -------- SYMMETRIC DIFFERENCE --------
# Symmetric difference means:
# elements that are NOT common in both sets

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)
# Returns non-common elements from both sets
print(set3)


set3 = set1 ^ set2
# ^ is another way to perform symmetric difference
print(set3)


set1.symmetric_difference_update(set2)
# Updates set1 with non-common elements
print(set1)



# -------- FROZENSET --------
# frozenset is an immutable version of set

x = frozenset({"apple", "bananan", "cherry"})
# Elements cannot be added or removed
print(x)
print(type(x))
