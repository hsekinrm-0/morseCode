# Coding Challenge 2
# Name:Nikesh Shrestha
# Student No: 2059738

# A Morse code encoder/decoder

import os
import sys
MORSE_CODE = {
    "A": "-...", "B": ".-", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..",
    "J": ".---",

    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...",
    "T": "-",

    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..", ".": ".-.-.-", "0": "-----",
    "1": ".----",

    "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    "(": "-.--.",

    ")": "-.--.-", "&": ".-...", ":": "---...", ";": "-.-.-.", "=": "-...-", "#": ".-.-.", "-": "-....-", "_": "..--.-",

    '"': ".-..-.", "$": "...-..-", "@": ".--.-.", "?": "..--..", "!": "-.-.--"
}

LETTERS = list(MORSE_CODE.keys())#using list for key value from morse code dict
MORSE_VALUES = list(MORSE_CODE.values())# Using list for taking value from Morse code dict


def get_input():
    while True: # Using while loop to ask user until they give a valid responde  
        mode = input('Would you like to encode (e) or decode (d): ')# Asking user to input e or d for encode or decode 
        if mode == 'e': # Using if statement if user input for encode 
            choice = input('Would you like to read from a file (f) or the console (c)? ')
            if choice == 'c': # using nested if statement 
                message = input('What message would you like to encode: ')
                print(encode(message))
                choice = input('Would you like to encode/decode another message (y/n)? ')#Asking user to encode\decode again then using if/else statement whether they want to end the program or still keep going.
                if choice == 'y':
                    continue
                elif choice == 'n':
                    sys.exit('\nThank you for using the program, Goodbye!')#Using .exit to end the program
                else: # If the user input error value this code run 
                    print('Invalid choice! Please try again\n')

            elif choice == 'f':
                filename = input('Enter filename: ')
                if file_exists(filename):
                    content = read_lines(mode, filename)# Open the file for reading ... While read_lines() will read content from the file 
                    print(content)
                else:
                    print("File does not exist, Try Again!\n")


            else:
                print("Invalid choice! Please Try Again\n") 

        elif mode == 'd': # Using if statement if user input for decode 
            choice = input('Would you like to read from a file (f) or the console (c)? ')
            if choice == 'c':
                message = input('What message would you like to decode: ')
                print(decode(message))
                choice = input('Would you like to encode/decode another message (y/n)? ')# Using same code for both encode and decode  
                if choice == 'y':
                    continue
                elif choice == 'n':
                    sys.exit('\nThank you for using the program, goodbye!') #Using .exit to end the program
                else:
                    print("Invalid choice! Gave a valid response\n")

            elif choice == 'f':
                filename = input('Enter filename: ')
                if file_exists(filename):
                    text = read_lines(mode, filename)# Open the file for reading ... While read_lines() will read content from the file         
                    print(text)
                else:
                    print("File does not exist, Please Try Again!\n")

            else:
                print("Invalid choice! Please Try Again\n")

        else:
            print('Invalid mode! Please Try Again\n')
            continue


def encode(message): #Building user-defined function for encode 
    cipher = ''
    message = message.upper()#Using .uppper method to convert message into capital form 
    message = list(message)
    for i in message:
        if i != ' ':
            cipher = cipher + MORSE_CODE.get(i, i) + ' '
        else:
            cipher += ' '
    return cipher


def decode(message):
    decipher = ''
    message = message.split()#The split() method splits a string into a list

    for i in message:
        decipher += LETTERS[MORSE_VALUES.index(i)]
    return decipher


def file_exists(filename):
    return os.path.exists(filename)

def read_lines(mode, filename):
    with open(filename, 'r') as file:
        text= file.read()
    if mode == 'e':
        return encode(text)
    elif mode == 'd':
        return decode(text)
    else:
        return "Invalid mode!, Try again"
    
def print_intro():
    print("\nWelcome to Wolmorse")
    print("This program encodes and decodes Morse code.\n")
    message = get_input()

def main():
    print_intro()
    # Program execution begins here
if __name__ == '__main__':
    main()
