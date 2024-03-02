TO START :

1. Open command line (cmd ).
2. Write in teminal: cd ....................UWAGA: podać path ścieżkę !!!!!!!!1
3. Then write in terminal : pip install -e .
4. Push the ENTER bottom.
5. Write in terminal: .............-  UWAGA: z setup wyjąć nazwę komendy!


_________________________________________BOT DESCRIPTION____________________________________________

The project is a console assistant bot that recognizes commands entered from the keyboard and reacts in accordance with the entered command.

The the bot starts working it loads the list of contacts from the "bot_save.bin" file.

The bot allows you to enter and save information such as: Name, Surname, phone number, e-mail address and date of birth into the contact list and notes.

The bot allows you to search, edit and delete the information you enter.

The bot shows how many days are left until the selected contact's birthday.

The bot checks whether the phone number entered by the user into the contact book składa się z tylko i wyłącznie z 9 cyft.

The bot checks whether the e-mail address entered into the contact book has the correct format.

        A valid e-mail address consists of:

        1. The first part of the email address (before the @ sign) may consist of:
        - uppercase and/or lowercase letters of the Latin alphabet [A-Za-z],
        - numbers [0-9]
        - underscore [\_]
        - dot character at least once

        2. The second part of the email address consists only of:
        - @ sign (exactly one)

        3. The third part of the email address may consist of:
        - uppercase and/or lowercase letters of the Latin alphabet [A-Za-z]
        - numbers [0-9]
        - underscore character
        - dash character

        4. The fourth part of the email address may consist of:
        - two or three lowercase letters of the Latin alphabet [a-z]
        - dot character at least once (for example: .com.pl or .pl)


The bot only accepts commends presented below:

THE BOT ACCEPTS COMMANDS:

1. 'add phone' 
2. 'change phone'
3. 'delete phone'
4. 'show contact'
5. 'add contact'
6. 'add note'
7. 'add birthday'
8. 'birthday'
9. 'show all'
10. 'find contact'
11. 'save'
12. 'exit'

The bot saves the list of contacts in the "bot_save.bin" file, which is created when it finishes working.

The bot terminates after the user enters the 'exit' command.