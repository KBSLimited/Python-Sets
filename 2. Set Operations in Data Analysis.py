def remove_duplicates(customer_ids):
    unique_customer_ids = set(customer_ids)
    return unique_customer_ids

# Example data
customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

# Remove duplicates and display unique customer IDs
unique_customers = remove_duplicates(customer_ids)
print("Unique Customer IDs:", unique_customers)