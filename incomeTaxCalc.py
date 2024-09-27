"""
Title: Income Tax Calculator 
Author: Hunter Dettmer

Pseudo-code: 

1. Input the gross income and number of dependents
2. Compute the taxable income using the formula:

Taxable income = gross income - 10000 - (3000 * number of dependents)

3. Compute the income tax using the formula:
Tax = taxable * 0.20
4. Print the total tax
"""

"""
Better Pseudo-code:

Compute a person's income tax.
    1. Significant constants:      # constant is a non-changing variable
        tax_rate
        standard_deduction
        deduction_per_dependent
    2. The inputs are:
        gross income
        number of dependents
    3. Computations:
        taxable income = the standard deduction - a deduction for each dependent
        income tax = is a fixed percentage of the taxable income
    4. The outputs are: 
        Your income tax
"""

# Initialize the constants
TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.00 # FLOAT - an numerical value with a decimal
DEPENDENT_DEDUCTION = 3000.00

# Request the inputs from user
grossIncome = float(input("Enter the gross income: "))
numDependents = int(input("Enter the number of dependents: "))

# Compute the income tax
taxableIncome = grossIncome - STANDARD_DEDUCTION - DEPENDENT_DEDUCTION * numDependents
incomeTax = taxableIncome * TAX_RATE

# Display the income tax
print("Your Income Tax, based on your taxable income of", taxableIncome, "is", incomeTax, ".")