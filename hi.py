# Define the conversion rate from EGP to USD
conversion_rate = 50  # 1 USD = 50 EGP

# Function to convert EGP to USD
def egp_to_usd(egp_amount):
    """
    Convert the given amount in EGP to USD using the predefined conversion rate.
    
    :param egp_amount: Amount in EGP to be converted
    :return: Equivalent amount in USD
    """
    return egp_amount / conversion_rate

# Take input from the user
egp_amount = float(input("Enter the amount in EGP: "))  # Prompt the user to enter an amount in EGP and convert it to a float

# Convert the amount to USD
usd_amount = egp_to_usd(egp_amount)  # Call the conversion function with the user input

# Display the result
print(f"{egp_amount} EGP is equivalent to {usd_amount:.2f} USD")  # Print the result, formatted to 2 decimal places

