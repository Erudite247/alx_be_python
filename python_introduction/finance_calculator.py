#!/bash/bin
# finance_calculator.py
# Prompt the user to enter their monthly income
monthly_income = float(input("Enter your monthly income: "))
# Prompt the user to enter their monthly expenses
monthly_expenses = float(input("Enter your monthly expenses: "))
# Calculate the monthly savings
monthly_savings = monthly_income - monthly_expenses
project_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print("Your monthly savings are " + "$" + str( monthly_savings))
print("Project savings after one year, with interest, is:"   +  " $"+ str( project_savings))
