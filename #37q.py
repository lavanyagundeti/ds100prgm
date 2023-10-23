#37q

def calculate_compound_interest(principal, rate, time, compounding_frequency):
    
    rate = rate / 100

    
    amount = principal * (1 + rate / compounding_frequency) ** (compounding_frequency * time)
    interest = amount - principal

    return amount, interest


principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in percentage): "))
time = float(input("Enter the number of years: "))
compounding_frequency = int(input("Enter the number of times interest is compounded per year: "))


future_value, interest_earned = calculate_compound_interest(principal, rate, time, compounding_frequency)


print(f"Principal Amount: ${principal:.2f}")
print(f"Annual Interest Rate: {rate}%")
print(f"Time (in years): {time}")
print(f"Compounding Frequency: {compounding_frequency} times per year")
print(f"Future Value: ${future_value:.2f}")
print(f"Interest Earned: ${interest_earned:.2f}")
