def order_processing(customer_name, item_ordered, quantity, shipping_address):
    # Simulate order processing
    item_price = 1200  # Example price per item
    total_cost = item_price * quantity
    
    processing_details = {
        "Customer Name": customer_name,
        "Item Ordered": item_ordered,
        "Quantity": quantity,
        "Cost per Item": item_price,
        "Total Cost": total_cost,
        "Shipping Address": shipping_address
    }

    return processing_details

# Example usage:
customer = "Mark Hamill"
item = "Lightsaber"
quantity_ordered = 17
shipping_address = "123 Main St, Luisville"

order_result = order_processing(customer, item, quantity_ordered, shipping_address)
print("Order Processing Result:", order_result)
print()
