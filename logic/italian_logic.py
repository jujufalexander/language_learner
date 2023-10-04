import random
from data.italian_data import italian_vocab, italian_vocab_unit_2, italian_duo_1, italian_convo

def italian_vocab_review(unit_choice):
    while True:
        print("Let's review Italian vocabulary!")

        if unit_choice == "1":
            words = list(italian_vocab.keys())
            vocabulary = italian_vocab 
        elif unit_choice == "2":
            words = list(italian_vocab_unit_2.keys())
            vocabulary = italian_vocab_unit_2  
        else:
            print("Invalid unit selection.")
            return

        random.shuffle(words)

        correct_count = 0  # Initialize a count for correct answers
        incorrect_translations = {}  # Initialize a dictionary to store incorrect translations

        for word in words:
            user_translation = input(f"What does '{word}' mean in English? ").strip().capitalize()

            # Option to exit the exercise early
            if user_translation.lower() == 'exit':
                exit_choice = input("Are you sure you'd like to end the exercise early? (y/n): ").strip().lower()
                if exit_choice == 'y':
                    break
                else:
                    continue

            correct_translations = vocabulary[word].split(", ")  # Split multiple translations by comma and space

            if user_translation.capitalize() in correct_translations:
                print("Correct!\n")
                correct_count += 1
            else:
                print(f"Sorry, the correct answer is: '{', '.join(correct_translations)}'\n")
                incorrect_translations[word] = correct_translations

        total_questions = len(words)
        correct_percentage = (correct_count / total_questions) * 100

        print(f"Exercise completed!\nYou got {correct_count} out of {total_questions} correct, which is {correct_percentage:.2f}%.")

        if incorrect_translations:
            print("\nIncorrect translations:")
            for word, correct_translations in incorrect_translations.items():
                print(f"'{word}' should mean: {', '.join(correct_translations)}")

        print()
        another_review = input("Do you want to review another set of vocabulary? (y/n): ").strip().lower()
        if another_review != 'y':
            break
        else:
            unit_choice = input("Select a unit (1 or 2): ").strip()


def italian_convo_review():
    while True:
        print("Let's review Italian conversations!")

        correct_count = 0  
        incorrect_translations = {}  

        unanswered_questions = list(italian_convo.keys())  

        while unanswered_questions:
            convo_topic = random.choice(unanswered_questions)  
            unanswered_questions.remove(convo_topic)  

            user_translation = input(f"What does '{convo_topic}' mean in English? ").strip().capitalize()

            if user_translation.lower() == 'exit':
                exit_choice = input("Are you sure you'd like to end the exercise early? (y/n): ").strip().lower()
                if exit_choice == 'y':
                    break
                else:
                    continue

            correct_translations = italian_convo[convo_topic].split(", ")  

            if user_translation.capitalize() in correct_translations:
                print("Correct!\n")
                correct_count += 1
            else:
                print(f"Sorry, the correct answer is: '{', '.join(correct_translations)}'\n")
                incorrect_translations[convo_topic] = correct_translations

        total_questions = len(italian_convo)
        correct_percentage = (correct_count / total_questions) * 100

        print(f"Exercise completed!\nYou got {correct_count} out of {total_questions} correct, which is {correct_percentage:.2f}%.")

        if incorrect_translations:
            print("\nIncorrect translations:")
            for convo_topic, correct_translations in incorrect_translations.items():
                print(f"'{convo_topic}' should mean: {', '.join(correct_translations)}")

        print()
        another_review = input("Do you want to review another set of conversations? (y/n): ").strip().lower()
        if another_review != 'y':
            break


def italian_duo_review():
    while True:
        print("Let's review Italian duos!")

        correct_count = 0 
        incorrect_translations = {} 

        unanswered_questions = list(italian_duo_1.keys()) 

        while unanswered_questions:
            duo_topic = random.choice(unanswered_questions) 
            unanswered_questions.remove(duo_topic) 

            user_translation = input(f"What does '{duo_topic}' mean in English? ").strip().capitalize()

            if user_translation.lower() == 'exit':
                exit_choice = input("Are you sure you'd like to end the exercise early? (y/n): ").strip().lower()
                if exit_choice == 'y':
                    break
                else:
                    continue

            correct_translations = italian_duo_1[duo_topic].split(", ") 

            if user_translation.capitalize() in correct_translations:
                print("Correct!\n")
                correct_count += 1
            else:
                print(f"Sorry, the correct answer is: '{', '.join(correct_translations)}'\n")
                incorrect_translations[duo_topic] = correct_translations

        total_questions = len(italian_duo_1)
        correct_percentage = (correct_count / total_questions) * 100

        print(f"Exercise completed!\nYou got {correct_count} out of {total_questions} correct, which is {correct_percentage:.2f}%.")

        if incorrect_translations:
            print("\nIncorrect translations:")
            for duo_topic, correct_translations in incorrect_translations.items():
                print(f"'{duo_topic}' should mean: {', '.join(correct_translations)}")

        print()
        another_review = input("Do you want to review another set of duos? (y/n): ").strip().lower()
        if another_review != 'y':
            break
