import numpy as np


class Bank:
    def __init__(self, name, dateOfBirth) -> None:
        """
        Initializes the Bank class with the account holder's details.

        Args:
            name (str): The name of the account holder.
            dateOfBirth (str): The date of birth of the account holder.
        """
        self.name = name
        self.dateOfBirth = dateOfBirth
        self.accountNumber = np.random.randint(100000, 1000000)
        self.minimumAmount = 10000
        self.totalBalance = 0

    def deposit_amount(self, depositAmount: int) -> None:
        """
        Deposits a specified amount into the account.

        Args:
            depositAmount (int): The amount to deposit.
        """
        self.totalBalance += depositAmount
        print(f"{depositAmount} deposited in your account.")
        print(f"New balance: {self.totalBalance}")

    def withdraw_amount(self, withdrawAmount: int) -> None:
        """
        Withdraws a specified amount from the account.

        Args:
            withdrawAmount (int): The amount to withdraw.
        """
        if withdrawAmount > self.totalBalance:
            print("Amount exceeds current balance.")
        else:
            self.totalBalance -= withdrawAmount
            print(f"{withdrawAmount} withdrawn successfully.")
            print(f"Remaining balance: {self.totalBalance}")
            if self.totalBalance < self.minimumAmount:
                print(
                    "Warning: Your account balance is below the minimum required amount. Please deposit more funds."
                )

    def current_balance(self) -> None:
        """
        Displays the current balance of the account.
        """
        print(f"Name: {self.name}")
        print(f"Your balance: {self.totalBalance}")


def create_account() -> Bank:
    """
    Creates a new bank account by gathering user details.

    Returns:
        Bank: A new Bank object representing the created account.
    """
    print("Welcome to Python Bank\n")
    name = input("Enter your name: ")
    dateOfBirth = input("Enter your date of birth (DD/MM/YY): ")
    bank = Bank(name=name, dateOfBirth=dateOfBirth)
    print("\nYour account has been created successfully!")
    print("Below are your account details. Please verify:\n")
    print(
        f"Name: {name}\nDate of Birth: {dateOfBirth}\nAccount Number: {bank.accountNumber}"
    )
    return bank


def main():
    print("------------- *** Welcome to Python Bank *** --------------\n")
    answer = input("Would you like to create an account? (y/n): ").strip().lower()

    if answer == "y":
        bank = create_account()
        while True:
            action = input(
                "\nWhat would you like to do? \n1. Deposit amount\n2. Withdraw amount\n3. See current balance\n4. Exit\nChoose an option (1/2/3/4): "
            ).strip()

            if action == "1":
                depositAmount = int(input("Enter deposit amount: "))
                bank.deposit_amount(depositAmount=depositAmount)
            elif action == "2":
                withdrawAmount = int(input("Enter withdraw amount: "))
                bank.withdraw_amount(withdrawAmount=withdrawAmount)
            elif action == "3":
                bank.current_balance()
            elif action == "4":
                print("Thank you for using Python Bank!")
                break
            else:
                print("Please enter a valid option.")
    else:
        print("Thank you for visiting Python Bank!")


if __name__ == "__main__":
    main()
