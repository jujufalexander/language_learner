from googletrans import Translator
import re

# Dictionary mapping language names to language codes
language_codes = {
    "english": "en",
    "french": "fr",
    "german": "de",
    "spanish": "es",
    "italian": "it",
    "dutch": "nl",
}

def add_spaces_after_punctuation(text):
    # Add spaces after periods, question marks, exclamation points, and semicolons
    return re.sub(r'(?<=[.!?;])', ' ', text)

def get_valid_target_language():
    while True:
        target_language = input("Enter the target language (e.g., 'Italian, Dutch, Spanish'): ").strip().lower()

        if target_language in language_codes:
            return target_language
        else:
            print("Invalid destination language. Please enter a valid language or language code.")

def main():
    translator = Translator()

    while True:
        print("Let's translate!")
        
        user_input = input("Enter text to translate (or 'exit' to quit): ").strip()

        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        # Add spaces after punctuation marks
        user_input = add_spaces_after_punctuation(user_input)

        target_language = get_valid_target_language()

        # Translate the target language to the corresponding language code
        target_language_code = language_codes[target_language]

        # Perform the translation
        translated_text = translator.translate(user_input, dest=target_language_code)

        # Output the translation with spaces
        translated_output = add_spaces_after_punctuation(translated_text.text)
        
        print(f"Translation to {target_language}: {translated_output}")
        print() 

if __name__ == "__main__":
    main()
