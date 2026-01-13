def chai_flavor(flavor="masala"):
    """return the flavor of chai .."""
    chai = "ginger"
    return flavor

# __doc__ → Prints the docstring of the function
print(chai_flavor.__doc__)

# __name__ → Prints the function name
print(chai_flavor.__name__)

# help() shows built-in function documentation
help(len)

print("--------------------------")


def generate_bill(chai=0, samosa=0):
    """
    Calculate the total bill for chai and samosa.

    :param chai: Number of chai cups (10 rupees each)
    :param samosa: Number of samosa (15 rupees each)
    :return: (total amount, thank you message as string)
    """
    total = chai * 10 + samosa * 15
    return total, "Thank you for visiting chaicode.com"


# Calling the function
amount, message = generate_bill(chai=2, samosa=3)

print("Total Bill:", amount)
print(message)
