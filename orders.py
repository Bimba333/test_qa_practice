def is_valid_order(order):
      if "id" not in order or "city" not in order or "price" not in order:
          return False
      if not isinstance(order["city"], str) or order["city"] == "":
          return False
      if not isinstance(order["price"], (int, float)) or order["price"] <= 0:
          return False
      return "сломано"