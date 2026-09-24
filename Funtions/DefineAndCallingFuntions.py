# ============================================================
# ANATOMY OF A FUNCTION
# ============================================================

#   def keyword    function name    parameters
#       ↓               ↓              ↓
def calculate_discount(price,       percent):
    """
    Docstring: Explains what the function does.
    Always write this for functions you'll reuse.

    Args:
        price   (float): Original price in rupees
        percent (float): Discount percentage

    Returns:
        float: Final price after discount
    """
    # Function BODY — indented 4 spaces
    discount = price * percent / 100
    final    = price - discount
    return final      # ← return sends value back to caller


# CALLING the function
result = calculate_discount(1000, 20)  # 1000=price, 20=percent
print(result)    # 800.0

# Store result and use it
price1 = calculate_discount(5000, 10)
price2 = calculate_discount(2000, 25)
price3 = calculate_discount(800,  5)

print(f"Price 1: ₹{price1}")   # ₹4500.0
print(f"Price 2: ₹{price2}")   # ₹1500.0
print(f"Price 3: ₹{price3}")   # ₹760.0