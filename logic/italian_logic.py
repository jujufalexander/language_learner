import random
from data.italian_data import italian_vocab_unit_1, italian_vocab_unit_2, italian_convo_unit_1, italian_convo_unit_2
import re

# Function to normalize a string for comparison
def normalize_string(s):
    return re.sub(r'[^a-zA-Z0-9]', '', s.lower())

def italian_vocab_review(unit_choice):
    while True:
        print("Let's review Italian vocabulary!")

        if unit_choice == "1":
            words = list(italian_vocab_unit_1.keys())
            vocabulary = italian_vocab_unit_1 
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

            if normalize_string(user_translation) in [normalize_string(correct) for correct in correct_translations]:
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


def italian_convo_review(unit_choice):
    while True:
        print("Let's review Italian conversations!")

        correct_count = 0
        incorrect_translations = {}

        if unit_choice == "1":
            unanswered_questions = list(italian_convo_unit_1.keys())
            vocabulary = italian_convo_unit_1
        elif unit_choice == "2":
            unanswered_questions = list(italian_convo_unit_2.keys())
            vocabulary = italian_convo_unit_2
        else:
            print("Invalid unit selection.")
            return

        while unanswered_questions:
            convo_topic = random.choice(unanswered_questions)
            unanswered_questions.remove(convo_topic)

            user_translation = input(f"What does '{convo_topic}' mean in English? ").strip()

            if user_translation.lower() == 'exit':
                exit_choice = input("Are you sure you'd like to end the exercise early? (y/n): ").strip().lower()
                if exit_choice == 'y':
                    break
                else:
                    continue

            # Normalize the user's input for comparison
            user_normalized = normalize_string(user_translation)

            # Normalize each correct translation for comparison
            correct_translations = vocabulary[convo_topic].split(", ")
            correct_normalized = [normalize_string(correct) for correct in correct_translations]

            if user_normalized in correct_normalized:
                print("Correct!\n")
                correct_count += 1
            else:
                print(f"Sorry, the correct answer is: '{', '.join(correct_translations)}'\n")
                incorrect_translations[convo_topic] = correct_translations

        total_questions = len(vocabulary)
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
        else:
            unit_choice = input("Select a unit (1 or 2): ").strip()

# Rest of your code...
