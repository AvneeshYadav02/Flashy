# Flashy: A Language Learning Flashcard App

Flashy is a desktop flashcard application designed to help you learn new vocabulary. It uses a set of words from a CSV file and a timer to prompt you to learn words. After a few seconds, the card flips over to reveal the translation. You can mark words as "known" to remove them from the study list, helping you focus on the words you still need to learn.

Features

    Interactive Flashcards: Displays a flashcard with a French word on the front. After a few seconds, the card automatically flips to show the English translation.

    Progress Tracking: Tracks the words you've learned. When you click the "right" button, the word is removed from the study list.

    Dynamic Word List: The application loads a new word list when you start it and saves the remaining words to a file so you can pick up where you left off.

    User-Friendly Interface: The application is built with tkinter and uses images to create a simple, engaging interface.

How to Install and Run

To run this application, you need to have Python installed on your system.

    Clone the Repository (or download the files).

    Navigate to the Project Directory in your terminal.

    Run the main script:
    Bash

    python main.py

How to Use

    When you start the app, a French word will appear on the flashcard.

    Wait for the timer to finish. The card will flip to show the English translation.

    If you know the word, click the "RIGHT" button. The word will be removed from your study list, and a new card will appear.

    If you don't know the word, click the "WRONG" button. The word will remain in your study list to be shown again later.

Customization

You can easily adapt this application to learn any language.

    Create a CSV file: Create a new .csv file with two columns, one for the new language and one for English. For example, if you want to learn Spanish, your file could be named spanish_words.csv and have "Spanish" and "English" as column headers.

    Update the Code: In main.py, change the name of the CSV file the program reads from and the column names to match your new file.
