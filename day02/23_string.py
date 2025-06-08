# Ask the user for the information of three items

initial_balance = float(input("Enter initialbalance:"))
time_years = int(input("Enter time years:"))
interest_rate = float(input("Enter time rate:"))

Simple_Interest= initial_balance * (1 + interest_rate * time_years)

print(f"Initial Balance: {initial_balance:.2f}")
print(f"Initial Balance: {time_years:,}")
print(f"Initial Balance: {Simple_Interest:.2%}")


# Then print the following output
#     Initial Balance: PHP Initial Balance (two decimal places)
#     Time (in Years): Years (four decimal places)
#     Interest Rate: Interest Rate in Percentage (four decimal places)
#     ===================================================================
#     Simple Interest: initial_balance * (1 + interest_rate * time_years)

