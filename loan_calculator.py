import math

print("""What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:""")
parameter = input()
if parameter != "p":
    print("Enter the loan principal:")
    loan_principal = float(input())
if parameter != "a":
    print("Enter the monthly payment:")
    monthly_payment = float(input())
if parameter != "n":
    print("Enter the number of periods:")
    number_of_periods = int(input())
print("Enter the loan interest:")
loan_interest = float(input())

nominal_interest_rate = loan_interest / (12 * 100)

# Number of monthly payments
if parameter == "n":
    n = math.log(monthly_payment / (monthly_payment - nominal_interest_rate * loan_principal), 1 + nominal_interest_rate)
    number_of_months = math.ceil(n)
    if number_of_months < 12:
        months_string = (" month " if number_of_months > 1 else " months ") + "to repay the loan!"
        print("It will take " + str(number_of_months) + months_string)
    elif number_of_months % 12 == 0:
        number_of_years = number_of_months // 12
        years_string = (" year " if number_of_years == 1 else " years ") + "to repay the loan!"
        print("It will take " + str(number_of_years) + years_string)
    else:
        number_of_years = math.floor(number_of_months / 12)
        last_year_number_of_months = number_of_months - number_of_years * 12
        months_string = (" month " if last_year_number_of_months > 1 else " months ") + "to repay the loan!"
        print("It will take " + str(number_of_years) + " years and" + str(last_year_number_of_months) + months_string)

# Annuity monthly payment amount
elif parameter == "a":
    annuity_payment = loan_principal * (nominal_interest_rate * math.pow(1 + nominal_interest_rate, number_of_periods)) / (math.pow(1 + nominal_interest_rate, number_of_periods) - 1)
    print("Your monthly payment = " + str(math.ceil(annuity_payment)) + "!")

# Loan principal
elif parameter == "p":
    loan_principal = monthly_payment / ((nominal_interest_rate * math.pow(1 + nominal_interest_rate, number_of_periods)) / (math.pow(1 + nominal_interest_rate, number_of_periods) - 1))
    print("Your loan principal = " + str(loan_principal) + "!")
