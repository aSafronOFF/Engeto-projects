"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Antonin Safronov
email: antonin.safronov@gmail.com
discord: TonyEntony#4102
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.''']

separator_length = 70
separator = '-' * separator_length
message = "Your text has been analyzed!"
goodbye_message = "Thank you for using our text analyzer!"

registered_users = {"bob": "123", 
                    "ann": "pass123", 
                    "mike": "password123", 
                    "liz": "pass123"}
usernames = list(registered_users.keys())

user = input("Username:\n")
password = input("Password:\n")

if user in usernames: #checks if user is saved in database
    if password == registered_users[user]:
        centered_message = f"Welcome! you can start analyzing your text {user}.".center(separator_length)
        #separator for better readibility
        print(f"{separator}\n{centered_message}\n{separator}")
    else:
        print("Incorrect password.")
        quit()
else:
    print("Username not found.")
    quit()

texts_by_number = {}
for index, value in enumerate(TEXTS): #converts list of texts to dictionary for later usage
    texts_by_number[index + 1] = value

texts_count = len(TEXTS) #counts number of provided texts in the list for later usage
selected_text = input(f"Enter a number of the text you would like to analyze (1 - {texts_count}): ")

if not selected_text.isdigit(): #checks if user inserted integer which is required
    print(f"You must insert a number. Please select (1 - {texts_count}).")
    quit()
else:
    selected_text = int(selected_text)
    print("Selected text:", selected_text)

    if selected_text not in texts_by_number: #checks if the selected number of text corresponds with the number of "uploaded" texts
        print(f"This number is not included in your list, please select (1 - {texts_count}).")
        quit()
    else:
        pass

words = texts_by_number[selected_text].split()
word_count = len(words)

centered_message = message.center(separator_length)
#separator for better readibility
print(f"{separator}\n{centered_message}\n{separator}")

print(f"There are {word_count} words in the selected text.")

numbers = []
capital_words = []
all_capital_letters_words = []
non_capital_words = []

for word in words:
    if word.isdigit():
        numbers.append(word)
    elif word.isupper():
        all_capital_letters_words.append(word)
    elif word[0].isupper():
        capital_words.append(word)
    else:
        non_capital_words.append(word)

print(f"There are {len(capital_words)} titlecase words.")
print(f"There are {len(all_capital_letters_words)} uppercase words.")
print(f"There are {len(non_capital_words)} lowercase words.")
print(f"There are {len(numbers)} numeric strings.")

numbers_sum = 0
for number in numbers:
    numbers_sum += int(number)

print(f"The sum of all the numbers is: {numbers_sum}")
print("\n")

word_lengths = {}
for word in words:
    length = len(word)
    if length in word_lengths:
        word_lengths[length] += 1
    else:
        word_lengths[length] = 1

sorted_lengths = sorted(word_lengths.items()) #creates list of tuples for the later usage in graph

print("Word lengths and their count:")
for length, count in sorted_lengths:
    print(f"Length {length} | {'*' * count} {count} words")

centered_message = goodbye_message.center(separator_length)

print(f"{separator}\n{centered_message}\n{separator}")

