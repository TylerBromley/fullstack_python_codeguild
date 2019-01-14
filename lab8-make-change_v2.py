# lab8-make-change_v2.py

# get the amount, convert to float, multiply by 100
amount = round(float(input("Please enter the amount to change: ")) * 100)
#total_amount = round(total_amount * 100)

# floor division to make change
quarters = amount // 25
amount %= 25
dimes = amount // 10
amount %= 10
nickels = amount // 5
amount %= 5
pennies = amount

# print out the totals
print(f"You have {quarters} quarter(s), {dimes} dime(s)," +
       f" {nickels} nickel(s) and {pennies} penny/pennies." )