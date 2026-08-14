from data import ORDERS_DB, INVENTORY_DB, RETURN_POLICY_INFO

def check_order_status(order_id: str) -> str:
    """Task NS-03: Order status lookup logic."""
    clean_id = order_id.strip().upper()
    if clean_id in ORDERS_DB:
        order = ORDERS_DB[clean_id]
        return (
            f"**Order ID:** {clean_id}\n\n"
            f"• **Status:** {order['status']}\n"
            f"• **Carrier:** {order['carrier']}\n"
            f"• **Tracking Number:** {order['tracking_number']}\n"
            f"• **Estimated Delivery:** {order['estimated_delivery']}"
        )
    return f"❌ Order ID `{clean_id}` not found. Please double-check your order number (e.g., ORD1001)."

def process_return_info(order_id: str) -> str:
    """Task NS-04: Returns and refunds deflection logic."""
    clean_id = order_id.strip().upper()
    if clean_id in ORDERS_DB:
        order = ORDERS_DB[clean_id]
        if order["status"] == "Delivered":
            return (
                f"✅ **Order {clean_id} is eligible for return!**\n\n"
                f"**Instructions:**\n"
                f"1. Pack items: `{', '.join(order['items'])}` in original packaging.\n"
                f"2. Your return label is ready to download below.\n"
                f"3. Drop off at any authorized shipping center.\n\n"
                f"*Refunds take 3-5 business days after receipt.*"
            )
        else:
            return f"⚠️ Order `{clean_id}` has not been marked as delivered yet (Current status: {order['status']}). Returns can only be processed after delivery."
    
    return f"ℹ️ **General Return Policy:**\n\n{RETURN_POLICY_INFO}"

def check_stock(product_name: str, size: str) -> str:
    """Task NS-05: Stock availability query logic."""
    prod_clean = product_name.strip().lower()
    size_clean = size.strip()
    
    if prod_clean in INVENTORY_DB:
        sizes = INVENTORY_DB[prod_clean]
        if size_clean in sizes:
            count = sizes[size_clean]
            if count > 0:
                return f"✅ **In Stock!** We currently have **{count}** unit(s) of '{product_name.title()}' in size `{size_clean}`."
            else:
                other_sizes = [s for s, c in sizes.items() if c > 0]
                alt_msg = f"Available sizes: {', '.join(other_sizes)}" if other_sizes else "Out of stock in all sizes."
                return f"❌ **Out of Stock.** Size `{size_clean}` is currently out of stock. ({alt_msg})"
        else:
            return f"⚠️ Size `{size_clean}` is not available for this item. Options: {', '.join(sizes.keys())}."
    
    return f"❌ Product '{product_name}' not found in our catalog."
