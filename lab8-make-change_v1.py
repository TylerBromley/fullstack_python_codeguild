# lab8-make-change_v1.py

# get the amount, convert to float
total_pennies = float(input("Please enter the total pennies: "))

# floor division to make change
total_quarters = total_pennies // 25
total_pennies = total_pennies - total_quarters * 25
total_dimes = total_pennies // 10
total_pennies = total_pennies - total_dimes * 10
total_nickels = total_pennies // 5
total_pennies = total_pennies - total_nickels * 5

# convert back to integers
total_quarters = int(total_quarters)
total_dimes = int(total_dimes)
total_nickels = int(total_nickels)
total_pennies = int(total_pennies)

# print out the totals
print(f"You have {total_quarters} quarters, {total_dimes} dimes," +
       f" {total_nickels} nickels and {total_pennies} pennies." )