# Language Learning Toolkit

Welcome to the Language Learning Toolkit! This Python program is designed to help you practice and learn multiple languages. You can review vocabulary, engage in conversations, and even translate text between languages. It provides support for Italian, Spanish, and Dutch languages.

## Development Status

- **Italian Language**: The Italian language support is fully functional.
- **Dutch and Spanish Languages**: Dutch and Spanish language support is still under development, and as a result, some features are limited.

## Project Structure

The directory structure reflects the following:

│ main.py
│ README.md
│
├───data
│ │ dutch_data.py
│ │ italian_data.py
│ │ spanish_data.py
│ │
│ └───__pycache__
│ dutch_data.cpython-311.pyc
│ italian_data.cpython-311.pyc
│ spanish_data.cpython-311.pyc
│
├───logic
│ │ dutch_logic.py
│ │ italian_logic.py
│ │ spanish_logic.py
│ │
│ └───__pycache__
│ dutch_logic.cpython-311.pyc
│ italian_logic.cpython-311.pyc
│ spanish_logic.cpython-311.pyc
│
├───translate
│ │ translate.py
│ │
│ └───__pycache__
│ translate.cpython-311.pyc


## How to Use

To run the program, execute `main.py`. It provides the following features:

- Choose a language (Italian, Spanish, or Dutch) to learn.
- For each language, you can:
  - Review vocabulary.
  - Engage in conversations.
  - Use Duo Review for more interactive learning.
  - Translate text to your target language using the translation module.

Here's a brief overview of the main functionalities:

- `main.py`: The main entry point of the program.
- `logic`: Contains logic for language learning and review.
- `data`: Contains language-specific data and resources.
- `translate`: A module for text translation between languages.

## Translation Module

The translation module (`translate/translate.py`) allows you to translate text between languages. It supports English, French, German, Spanish, Italian, and Dutch.

To use the translation module, follow these steps:

1. Enter the text you want to translate.
2. Choose the target language (e.g., 'Italian,' 'Dutch,' 'Spanish').
3. The program will translate the text and provide the result.

## Known Issues

Please note that a few data files within the italian_data.py contain error comments that reflect issues with the program interpreting the correct answer. These issues will be addressed in future updates.

## Contributing

Feel free to contribute to this project! If you have ideas for improvements or want to add support for more languages, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---

Enjoy learning and practicing languages with the Language Learning Toolkit!

