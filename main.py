from logic.italian_logic import italian_vocab_review, italian_duo_review, italian_convo_review
from logic.spanish_logic import spanish_vocab_review, spanish_convo_review
from logic.dutch_logic import dutch_vocab_review, dutch_convo_review

def main():
    first_run = True  # Flag to check if it's the first run
    while True:
        if first_run:
            print("Hello! What language would you like to learn today?")
            first_run = False

        print("1. Italian")
        print("2. Spanish")
        print("3. Dutch")
        print("4. Exit")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            learn_italian()
        elif choice == "2":
            learn_spanish()
        elif choice == "3":
            learn_dutch()
        elif choice == "4":
            confirm_exit = input("Are you sure you want to end the session? (y/n): ")
            if confirm_exit.lower() == 'y':
                print("See you next time! Have a great day!")
                break
            else:
                print("Session continues. What language would you like to learn today?")
        else:
            print("Invalid choice. Please select a valid option.")

def learn_italian():
    while True:
        print("Let's practice Italian.")
        print("1. Vocab Review")
        print("2. Convo Review")
        print("3. Duo Review")
        print("4. Back to Main Menu") 
        choice = input("Enter your choice: ")

        if choice == "1":
            unit_choice = input("Select a unit (1 or 2): ")
            if unit_choice in ["1", "2"]:
                italian_vocab_review(unit_choice)
            else:
                print("Invalid unit selection.")
        elif choice == "2":
            italian_convo_review()
        elif choice == "3":
            italian_duo_review()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please select a valid option.")

def learn_spanish():
    while True:
        print("Let's practice Spanish.")
        print("1. Vocab Review")
        print("2. Convo Review")  
        print("3. Back to Main Menu")  
        choice = input("Enter your choice: ")

        if choice == "1":
            unit_choice = input("Select a unit (1 or 2): ")
            if unit_choice == "1" or unit_choice == "2":
                spanish_vocab_review(unit_choice)
            else:
                print("Invalid unit selection.")
        elif choice == "2":
            spanish_convo_review()
        elif choice == "3": 
            break
        else:
            print("Invalid choice. Please select a valid option.")

def learn_dutch():
    while True:
        print("Let's practice Dutch.")
        print("1. Vocab Review")
        print("2. Convo Review")
        print("3. Back to Main Menu")  
        choice = input("Enter your choice: ")

        if choice == "1":
            unit_choice = input("Select a unit (1 or 2): ")
            if unit_choice == "1" or unit_choice == "2":
                dutch_vocab_review(unit_choice)
            else:
                print("Invalid unit selection.")
        elif choice == "2":
            dutch_convo_review()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
