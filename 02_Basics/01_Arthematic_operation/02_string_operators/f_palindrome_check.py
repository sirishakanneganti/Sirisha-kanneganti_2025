
#!/usr/bin/python3
"""
Purpose: Demonstration of Palindrome check

    palindrome strings
        dad
        mom

Algorithms:
-----------
Step 1: Take the string in run-time and store in a variable


"""
#!/usr/bin/python3
"""
Purpose: Demonstration of Palindrome check

    palindrome strings:
        dad
        mom
        sirisha

Algorithms:
-----------
Step 1: Take the string in run-time and store it in a variable
Step 2: Reverse the string and check if it matches the original string
Step 3: Print the result based on the comparison

"""

# Step 1: Take input from user or use predefined strings
input_string = input("Enter a string to check if it's a palindrome: ")

# Example for "sirisha"
example_string = "sirisha"

# Step 2: Reverse the string and check if it matches the original string
if input_string == input_string[::-1]:
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")

# Check for the predefined string "sirisha"
if example_string == example_string[::-1]:
    print(f"'{example_string}' is a palindrome.")
else:
    print(f"'{example_string}' is not a palindrome.")


