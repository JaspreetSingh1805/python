# x = [1,2,3,4,5,1,2,3,4,5]
# c = list(set(x))
# print(c)

# second method

# x = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# c = set(x)
# print(c)


# name = "john"
# format_string = f"Hello, {name}!"
# print(format_string)

# try:
#     result =  10/0
# except ZeroDivisionError:
#     print("Error! Division by 0 is not allowed")

# def hello(a,b):
#     return a*b
# c = hello(4,3)
# print(c)

# x = [n**2 for n in range(1,11)]
# print(x)
# dict =  {
#     "name" : "john",
#     "age" : 23
# }
# dict["city"] = "new york"
# print(dict)

def process_order(order_type, *args, **kwargs):
    """
    Processes an order by printing the order type, items, and additional details.
    
    Parameters:
    - order_type (str): The type of the order (e.g., "food", "electronics").
    - *args: Variable length argument list to represent ordered items.
    - **kwargs: Arbitrary keyword arguments to represent additional details.
    """
    
    print(f"Order Type: {order_type}")
    
    print("Items Ordered:")
    for item in args:
        print(f"- {item}")
    
    print("\nAdditional Details:")
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")
    
    print("\nOrder processed successfully!\n")


process_order("food", "Burger", "Fries", "Soda", customer="John Doe", table=5)

process_order("electronics", "Laptop", "Mouse", delivery_date="2024-08-15", warranty="2 years")