import json


# Load mock databases from JSON files
with open("data/orders.json", "r", encoding="utf-8") as file:
    orders_data = json.load(file)

with open("data/inventory.json", "r", encoding="utf-8") as file:
    inventory_data = json.load(file)


# Convert orders JSON into the format used by the application
ORDERS_DB = {}

for order in orders_data:
    ORDERS_DB[order["order_id"]] = {
        "status": order["status"],
        "carrier": order["carrier"],
        "tracking_number": order["tracking_number"],
        "tracking_url": order.get("tracking_url"),
        "estimated_delivery": order["estimated_delivery"],
        "items": order["items"]
    }


# Convert inventory JSON into the format used by the application
INVENTORY_DB = {}

for product in inventory_data:
    product_name = product["product_name"].strip().lower()
    size = product["size"].strip()
    stock_count = product["stock_count"]

    if product_name not in INVENTORY_DB:
        INVENTORY_DB[product_name] = {}

    INVENTORY_DB[product_name][size] = stock_count


# General Return Policy Information
RETURN_POLICY_INFO = (
    "Northstar Retail Return Policy:\n"
    "• Returns are accepted within 3-5 after days of delivery.\n"
    "• Items must be unused and in original packaging.\n"
    "• To initiate a return, enter your Order ID and select 'Process Return'."
)
