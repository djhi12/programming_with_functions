from datetime import date

"""
You work for a retail store that wants to increase sales on Tuesday and Wednesday, which are the store’s slowest sales days. On Tuesday and Wednesday, if a customer’s subtotal is $50 or greater, the store will discount the customer’s subtotal by 10%.
"""

current_date = date.today()

day_of_week = current_date.weekday()

# Mapping the integer value to the corresponding day
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
specific_day = days[day_of_week]
# print(specific_day)


"""
If the subtotal is $50 or greater and today is Tuesday or Wednesday, your program must subtract 10% from the subtotal. Your program must then compute the total amount due by adding sales tax of 6% to the subtotal. Your program must print the discount amount if applicable, the sales tax amount, and the total amount due.

"""
subtotal = float(input("\nPlease enter the subtotal: "))
sales_tax = 0.06
discount = .10

# Discount based on day
if specific_day == 'Tuesday' or specific_day == 'Wednesday':
    if subtotal >= 50:
        discounted_amount = subtotal * discount
        print(f"Discount amount: {discounted_amount:.2f}")
        
        # Subtract subtotal and discounted amount
        subtracted_amount = subtotal - discounted_amount
        # print(f"{subtracted_amount}")
        
        # Multiple the subtracted amount to sales tax
        sales_tax_amount = subtracted_amount * sales_tax
        print(f"Sales tax amount: {sales_tax_amount:.2f}")
        
        # Total
        total_amount = subtracted_amount + sales_tax_amount
        print(f"Total: {total_amount:.2f}")
        
    elif subtotal < 50:
        sales_tax_amount = subtotal * sales_tax
        print(f"Sales tax amount: {sales_tax_amount:.2f}")
        
        total_amount = sales_tax_amount + subtotal
        print(f"Total: {total_amount:.2f}")
        
    else:
        print("Type the right details.")
        
# If the day is not Tuesday and Wednesday
elif specific_day != 'Tuesday' and specific_day != 'Wednesday':
    if subtotal < 50 or subtotal >= 50:
        sales_tax_amount = subtotal * sales_tax
        print(f"Sales tax amount: {sales_tax_amount:.2f}")
        
        total_amount = sales_tax_amount + subtotal
        print(f"Total: {total_amount:.2f}")
        
    else:
        print("Type the right details.")
        
else:
    print("Type the right details.")
    
        
        
    
# elif specific_day != 'Tuesday' and specific_day != 'Wednesday':
    

    

    
    
    