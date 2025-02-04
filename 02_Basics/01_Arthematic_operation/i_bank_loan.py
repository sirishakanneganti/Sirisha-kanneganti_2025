
#!/usr/bin/python3
"""
Purpose: Bank Loan

    Simple Interest : A = P (1 + rt)

                        A	=	final amount
                        P	=	initial principal balance
                        r	=	annual interest rate
                        t	=	time (in years)

Ref :https://www.calculatorsoup.com/calculators/financial/simple-interest-plus-principal-calculator.php

Get all values in runtime
"""

# Assignment
# 1. Compound Interest Calculation
#     ref: https://www.calculatorsoup.com/calculators/financial/compound-interest-calculator.php

#!/usr/bin/python3
import time

"""
Purpose: Saving Bank

    Initial Balance 0

Algorithm
----------
Step 1: Create a variable 'balance' with initial value 0
Step 2: Initial Deposit of min balance 1500
Step 3: Salary credited of 3300
Step 4: Online Purchase of 33.33
Step 5: House Rent paid of 1500
Step 6: Display Balance with Timestamp
"""

# Step 1: Initialize balance to 0
balance = 0

# Function to display balance with timestamp
def display_balance(balance):
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")  # Get current time
    print(f"{current_time} - Current Balance: {balance:.2f}")

# Step 2: Initial Deposit
balance += 1500
display_balance(balance)

# Step 3: Salary credited
balance += 3300
display_balance(balance)

# Step 4: Online Purchase
balance -= 33.33
display_balance(balance)

# Step 5: House Rent paid
balance -= 1500
display_balance(balance)

# Final balance
display_balance(balance)
