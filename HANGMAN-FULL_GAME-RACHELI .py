def hangman():
    """The hangman game process according to the rules of the game
    :return: None
    :rtype: NoneType
    """
    MAX_TRIES = 6
    old_letters_guessed = []
    num_of_tries = 0
    opening_screen()
    file_path = input("Enter a file path: ")
    index = int(input("Enter the index of the chosen word: "))
    secret_word = choose_word(file_path, index)
    #End of loop - when the player loose or win:
    while num_of_tries < MAX_TRIES and not check_win(secret_word, old_letters_guessed): 
        #Start of the game:
        if old_letters_guessed == []:
            print("let's start!")
            print_hangman(num_of_tries)
            print('_ '*len(secret_word))
        letter_guessed = input("Guess a letter: ")
        #The loop ends when the player presses a valid character:
        while try_update_letter_guessed(letter_guessed, old_letters_guessed) == False:
            letter_guessed = input("Guess a letter: ")
        if letter_guessed not in secret_word:
            num_of_tries += 1
            print(":(")
            print_hangman(num_of_tries)
            print(show_hidden_word(secret_word, old_letters_guessed))
        else:
            print(show_hidden_word(secret_word, old_letters_guessed))

    #Cheking why the loop ends - lose or win.
    if num_of_tries == MAX_TRIES:
        print("LOSE")
    else:
        print("WIN")

            
HANGMAN_PHOTOS = {
    0: "    x-------x",
    1: """    x-------x
    |
    |
    |
    |
    |""",
    2: """    x-------x
    |       |
    |       0
    |
    |
    |""",
    3: """    x-------x
    |       |
    |       0
    |       |
    |
    |""",
    4: """    x-------x
    |       |
    |       0
    |      /|\\
    |
    |""",
    5: """    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
    """,
    6: """    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |""",}            
NOT_UPDATED_STR = "X\n{0}"


def opening_screen():
    HANGMAN_ASCII_ART = '''Welcome to the game Hangman\n 
  _    _                                        
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                      __/ |                      
                     |___/'''
    MAX_TRIES = '\n6'
    print(HANGMAN_ASCII_ART, MAX_TRIES)

def check_win(secret_word, old_letters_guessed):
    """Chekes if the player already guessed the whole word correctly
    :param secret_word: the word that the player needs to guess
    :param old_letters_guessed: the letters that were guessted (user's input)
    :type secret_word: string
    :type old_letters_guessed: list
    :return: True if the secret word was guessed, otherwise False
    :rtype: boolean
    """
    for char in secret_word:
        if char not in old_letters_guessed:
            return False
    return True

def choose_word(file_path, index):
    """Picks one word from a list of words, read from a file, according to a given index in the list
    :param file_path: the path of the file that the word is chosen from hin
    :param index: the index of the word to choose (starting from 1)
    :type file_path: string
    :type index: int
    :return: the chosen word according to 'index'
    :rtype: string
    """
    with open(file_path, 'r') as words:
        word_list = words.read().split(' ')
    i = (index - 1) % len(word_list)
    return word_list[i]

def check_valid_input(letter_guessed, old_letters_guessed):
    """Checks the validation of user’s input, e.g one English letter, not entered
    before
    :param letter_guessed: user’s input
    :param old_letters_guessed: previous inputs
    :type letter_guessed: string
    :type old_letters_guessed: list
    :return: True if input is valid, False if not.
    :rtype: boolean
	"""
    return len(letter_guessed) == 1 and letter_guessed.isalpha() \
           and not letter_guessed.lower() in old_letters_guessed

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """Checks validation of user’s input (as in previous task).
    if so, adds it to "old_letters_guessed" and returns True. Otherwise returns
    False.
    :param letter_guessed: user’s input
    :param old_letters_guessed: previous (valid) inputs
    :type letter_guessed: string
    :type old_letters_guessed: list
    :return: True if input is valid, False if not.
    :rtype: boolean
	"""
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed.lower())
        return True
    else:
        print_list_not_updated(old_letters_guessed)
        return False

def print_list_not_updated(my_list):
    """Prints not-ypdated string.
    :param my_list (not updates)
    :type my_list: list
    """
    print(NOT_UPDATED_STR.format(" -> ".join(sorted(my_list))))

def show_hidden_word(secret_word, old_letters_guessed):
    """Displays guessed letters in the secret word, and '_' for letters that were
    not guessed yet
    :param secret_word: the word that the player needs to guess
    :param old_letters_guessed: the letters that were guessted (user's input)
    :type secret_word: string
    :type old_letters_guessed: list
    :return: the word that needs to be guessed with letters in the right places and '_' in the right places
    :rtype: string
    """
    return_str = ""
    for char in secret_word:
        if char in old_letters_guessed: 
           return_str += char + " "
        else:
           return_str += "_ "
    return return_str[:-1]
def print_hangman(num_of_tries):
    """Returns the right photo of the hangman according the number of the wrong tries
    :param num_of_tries: the number of the wrong tries that the user tried
    :param HANGMAN_PHOTOS: the 7 positions of the hangman
    :type num_of_tries: int
    :type HANGMAN_PHOTOS: dict
    :return: the photo of the hangman according to the 'num_if_tries'
    :rtype: string
    """
    print(HANGMAN_PHOTOS[num_of_tries])

def main():
    hangman()

if __name__ == "__main__":
  main()

