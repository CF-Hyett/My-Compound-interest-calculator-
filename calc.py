# Program to calculate compound interest with monthly contributions at the end of each month
# Formula used:
# Compound interest for principal: A = P(1 + r/n)^(nt)
# Future value of a series: PMT × (((1 + r/n)^(nt) - 1) / (r/n))

# Get data from the user
principal_input = input("Enter the initial amount (principal): ")
annual_rate_input = input("Enter the annual interest rate (as a percentage): ")
compounds_per_year_input = input("Enter the number of times the interest is compounded per year: ")
years_input = input("Enter the investment period in years: ")
monthly_contribution_input = input("Enter the monthly contribution amount: ")

# Convert input data to integers
principal = int(principal_input)
annual_rate = float(annual_rate_input) / 100
compounds_per_year = int(compounds_per_year_input)
years = int(years_input)
monthly_contribution = int(monthly_contribution_input)

# Calculate compound interest plus the principal
preliminary_number = (1 + (annual_rate / compounds_per_year))
raised_to_power = (compounds_per_year * years)
compound_interest_plus_principal = principal * (preliminary_number ** raised_to_power)
print(f"The compound interest plus the principal is: {compound_interest_plus_principal:.2f}")

# Calculate the future value with deposits
one_plus = (1 + (annual_rate / compounds_per_year))
raised_to_power_2 = (compounds_per_year * years)
rate_divided_by_compounds = annual_rate / compounds_per_year
half_done = (((one_plus ** raised_to_power_2) - 1) / rate_divided_by_compounds)
future_value_with_deposits = monthly_contribution * half_done
print(f"Future value with deposits: {future_value_with_deposits:.2f}")

# Calculate the total amount
total_amount = compound_interest_plus_principal + future_value_with_deposits
print(f"Total Amount: {total_amount:.2f}")