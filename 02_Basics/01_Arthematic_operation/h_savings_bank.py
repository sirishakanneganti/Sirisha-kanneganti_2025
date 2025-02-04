
#!/usr/bin/python3
"""
Purpose: Saving Bank

    Initial Balance 0

Algorithm
----------
Step 1: Create an variable 'balance' with initial value 0
Step 2: Initial Despoit of min balance 1500
Step 3: Salary credited of 3300
Step 4: Online Purchase of 33.33
Step 5: House Rent paid of 1500
Step 6: Display Balance
"""

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

