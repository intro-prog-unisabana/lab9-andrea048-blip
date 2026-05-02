from utils import person_data, balance_summary
from bank_account import BankAccount

def main():
    people = []

    while True:
        print("Choose an option:")
        print("1. Add a new person")
        print("2. Add an account to a person")
        print("3. Show all balances")
        print("4. Quit")

        option = input()

        if option == "1":
            person = person_data()
            people.append(person)

        
        elif option == "2":
            name = input("Enter the person's name:\n")

            found = False
            for person in people:
                if person.name == name:
                    account_number = int(input("Enter a 4-digit account number:\n"))
                    balance = float(input("Enter the initial balance:\n"))

                    account = BankAccount(account_number, balance)
                    person.add_account(account)

                    found = True
                    break

            if not found:
                print("Person not found.")

        
        elif option == "3":
            if len(people) == 0:
                print("No data to show.")
            else:
                balance_summary(people)

        
        elif option == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1-4.")

if __name__ == "__main__":
    main()
