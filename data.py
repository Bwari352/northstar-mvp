ORDERS_DB = {
    "ORD1001": {
        "status": "Shipped",
        "carrier": "FedEx",
        "tracking_number": "FX-987654321",
        "estimated_delivery": "2026-08-15",
        "items": ["Running Shoes - Size 10"]
    },
    "ORD1002": {
        "status": "Processing",
        "carrier": "Pending",
        "tracking_number": "N/A",
        "estimated_delivery": "2026-08-18",
        "items": ["Denim Jacket - M"]
    },
    "ORD1003": {
        "status": "Delivered",
        "carrier": "UPS",
        "tracking_number": "1Z9999999999",
        "estimated_delivery": "2026-08-01",
        "items": ["Wireless Headphones"]
    }
}

# Mock Inventory Database
INVENTORY_DB = {
    "running shoes": {"size 9": 5, "size 10": 0, "size 11": 3},
    "denim jacket": {"S": 2, "M": 4, "L": 0},
    "wireless headphones": {"Standard": 12}
}

# General Return Policy Information
RETURN_POLICY_INFO = (
    "Northstar Retail Return Policy:\n"
    "• Returns are accepted within 30 days of delivery.\n"
    "• Items must be unused and in original packaging.\n"
    "• To initiate a return, enter your Order ID and select 'Process Return'."
)