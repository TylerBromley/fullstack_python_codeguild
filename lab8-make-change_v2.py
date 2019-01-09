# lab8-make-change_v2.py

# get the amount, convert to float, multiply by 100
total_amount = float(input("Please enter the amount to change: "))
total_amount = round(total_amount * 100)

# floor division to make change
total_quarters = total_amount // 25
total_amount = total_amount - total_quarters * 25
total_dimes = total_amount // 10
total_amount = total_amount - total_dimes * 10
total_nickels = total_amount // 5
total_pennies = total_amount - total_nickels * 5


# print out the totals
print(f"You have {total_quarters} quarters, {total_dimes} dimes," +
       f" {total_nickels} nickels and {total_pennies} pennies." )