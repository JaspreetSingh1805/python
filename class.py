def process_order(order_type, *args, **kwargs):
    print(f"Order type: {order_type}")
    
    print("Items ordered:")
    for item in args:
        print(f"- {item}")
    
    print("\nAdditional details:")
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")
    
    print("\nOrder processed successfully!")

# Corrected function calls
process_order("food", "Burger", "Pizza", "Fries", "Soda", customer="John Doe", table=5)
process_order("electronics", "Keyboard", "Mouse", "Laptop", delivery_date="2024-08-15")
