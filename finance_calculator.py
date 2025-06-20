monthly_income = int(input ("Enter your monthly income:"))
monthly_expenses = int(input ("Enter your total monthly expenses:"))
monthly_savings =  monthly_income -  monthly_expenses
print (f"monthly saving = {monthly_savings}")
Project_Annual_Savings = monthly_savings * 12 + (monthly_savings*12*0.05)
print (f"Projected savings after one year, with interest, is: {Project_Annual_Savings}")
