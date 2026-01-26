class ChaiUtils:
    
    # @staticmethod means this method does NOT need self or cls
    # It behaves like a normal function but is kept inside the class
    @staticmethod
    def clean_ingredients(text):
        # Split the string by commas
        # Remove extra spaces from each item
        return [item.strip() for item in text.split(",")]

# Raw string containing ingredients with extra spaces
raw = " water, milk, ginger, honey "

# Calling static method using class name
cleaned = ChaiUtils.clean_ingredients(raw)

# Printing cleaned list
print(cleaned)
