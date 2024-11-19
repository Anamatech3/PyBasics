#Question One
def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount if the discount is 20% or higher.
    
    Parameters:
    price (float): The original price of the item.
    discount_percent (float): The discount percentage to apply.
    
    Returns:
    float: The final price after applying the discount, or the original price if the discount is less than 20%.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Example
original_price = 100.0
discount = 35.0
final_price = calculate_discount(original_price, discount)
print(f"The final price is: ${final_price:.2f}")

#QUESTION TWO(2)
# Prompt the user for input
try:
    original_price = float(input("Enter the original price of the item: $"))
    discount_percent = float(input("Enter the discount percentage: "))
    
    # Calculate the final price
    final_price = calculate_discount(original_price, discount_percent)
    
    # Print the result
    if discount_percent >= 20:
        print(f"The final price after applying the discount is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: ${original_price:.2f}")
except ValueError:
    print("Invalid input! Please enter numeric values for the price and discount.")