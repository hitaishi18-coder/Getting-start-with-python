class TeaLeaf:
    
    def __init__(self, age):
        # Store real age in a "protected" variable _age
        self._age = age

    # @property makes age act like an attribute
    @property
    def age(self):
        # Whenever we read leaf.age, this method runs
        # It returns stored age + 2 (extra processing)
        return self._age + 2
    
    # Setter for age
    @age.setter
    def age(self, age):
        # Validation before setting value
        if 1 <= age <= 5:
            self._age = age
        else:
            raise ValueError("Tea leaf age must be between 1 and 5 years")
        

# Creating object
leaf = TeaLeaf(2)

# Calling property -> actually runs age() method
print(leaf.age)
# Output: 4  (because 2 + 2)

# Trying to set an invalid age
leaf.age = 6   #  This will raise ValueError

print(leaf.age)  # This line never runs because of the error
