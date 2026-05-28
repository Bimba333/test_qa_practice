def get_order_status(order):
    if "status" in order: 
        return order["status"].lower()
    return "unknown"