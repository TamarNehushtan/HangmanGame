HANGMAN_PHOTOS = {
    '0': "x-------x",
    '1':
        """x-------x
|
|
|
|
|""",
    '2': """x-------x
|       |
|       0
|
|
|""",
    '3': """x-------x
|       |
|       0
|       |
|
|""",
    '4': """x-------x
|       |
|       0
|      /|\\
|
|""",
    '5': """x-------x
|       |
|       0
|      /|\\
|      /
|""",
    '6': """x-------x
|       |
|       0
|      /|\\
|      / \\
|"""
}


MAX_TRIES = 6


def opening_screen():
    hangman_ascii_art = """
      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                         |___/"""
    print(hangman_ascii_art)
    print(MAX_TRIES)


def choose_word(file_path, index):
    with open("words.txt", "r") as words:
        words = words.read()
    list_words = words.split(" ")
    fix_list_words = []
    for word in list_words:
        if word in fix_list_words:
            continue
        else:
            fix_list_words.append(word)
    guess_word = ""
    is_guess_word = False
    while is_guess_word is False:
        if index <= len(fix_list_words):
            guess_word = fix_list_words[index - 1]
            is_guess_word = True
        else:
            index = index - len(fix_list_words)
    return guess_word


def print_hangman(num_of_tries):
    print(HANGMAN_PHOTOS[str(num_of_tries)])


def show_hidden_word(secret_word, old_letters_guessed):
    for char in secret_word:
        if char in old_letters_guessed:
            print(char, end=" ")
        else:
            print("_", end=" ")
    print("\n")


def check_win(secret_word, old_letters_guessed):
    return all(elem in old_letters_guessed for elem in secret_word)


def check_valid_input(letter_guessed, old_letters_guessed):
    """The function check the input from the user, if the string is valid and whether the user has already guessed the
    character in the past.
    :param letter_guessed: The character from the user
    :param old_letters_guessed: a list of all the letters that were guessed
    :type letter_guessed: string
    :type old_letters_guessed: list
    :return: if the input is valid. (new guessed of only one characters
    :rtype bool
    """
    if (len(letter_guessed) > 1) or (letter_guessed.isalpha() is False) or (letter_guessed.lower()
                                                                            in old_letters_guessed):
        return False
    else:
        return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if check_valid_input(letter_guessed, old_letters_guessed) is True:
        old_letters_guessed.append(letter_guessed.lower())
        return True
    elif check_valid_input(letter_guessed, old_letters_guessed) is False:
        print('X')
        print(" -> ".join(sorted(old_letters_guessed)))
        return False


def main():
    opening_screen()
    path_file_words = input("Enter file path: ")
    index = input("Enter index: ")
    print("Let's start!")
    secret_word = choose_word(path_file_words, int(index))
    num_of_tries = 0
    old_letters_guessed = []
    print_hangman(num_of_tries)
    show_hidden_word(secret_word, old_letters_guessed)
    end_game = False
    while end_game is False:
        guess_letter = input("Guess a letter: ")
        while try_update_letter_guessed(guess_letter, old_letters_guessed) is False:
            guess_letter = input("Guess a letter: ")
        if guess_letter.lower() not in secret_word:
            num_of_tries += 1
            print(":(\n" + HANGMAN_PHOTOS[str(num_of_tries)]+"\n")
        show_hidden_word(secret_word, old_letters_guessed)
        if check_win(secret_word, old_letters_guessed):
            print("WIN")
            end_game = True
        elif num_of_tries == MAX_TRIES:
            print("LOSE")
            end_game = True


if __name__ == "__main__":
    main()
