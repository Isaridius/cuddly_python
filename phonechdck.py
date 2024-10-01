# Database Initialization
customers = {} # Empty Dictionary to Store customer data

# Initialize our database size
customer_count = int(input("How many customers: "))

# Based on the the number of users, we will add related user data to the dictionary
for i in range(customer_count):
    customer_key = f"Customer {i}"

    current_name = input(f"User {i}'s name: ")
    phone_company = input("Input user's Phone Maker: ")

    customers[customer_key] = [current_name, phone_company]

print("Our Database:")
print(customers)
