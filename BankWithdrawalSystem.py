
balance = 100000  # initial balance

try:
    amount = float(input("Enter amount to withdraw: ₦"))

    if amount > balance:
        raise ValueError("Insufficient funds! Withdrawal exceeds balance.")

    balance = balance - amount

except ValueError as e:
    print("Transaction Failed:", e)

else:
    print(f"Withdrawal successful!")
    print(f"Amount withdrawn: ₦{amount}")
    print(f"Remaining balance: ₦{balance}")

finally:
    print("Transaction logged. Thank you for using our bank service.")
