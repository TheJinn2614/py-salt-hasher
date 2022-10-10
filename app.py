import hashlib
import sys
import pyfiglet
import string
import random
import os
# ASCII art

ascii_art = pyfiglet.figlet_format("Salt & Hash Inc", font = "slant")
print(ascii_art)

# Program starts here

# START MAIN PART
# Usage message
print("\nUsage: python app.py")

# Initial message
print("\nThis program will require a username and a password (both as input) and store in the database,\nhowever not before salting and hashing the password!")

# Getting the username and saving it to a variable
user = input("\nPlease enter your username: ")

# Echo back the username
print(f"\nThe username you entered is: {user}")

# Get the user's answer by using input() and save to a variable
user_answer = input("Is this username accurate?\n\nPlease answer with \"yes\" or \"no\": ")
user_answer = user_answer.lower()

# User validation check
if user_answer != "yes":
	print("Please re-enter your username!")
	exit()

# Declare the 2 password variables and make sure the pw-input func has 2 params for them 
password = ""
password_re_enter = ""

# Define a function where I ask the user to input their password
def password_input():
	password = input("\nPlease enter your password: ")
	password_re_enter = input("Please re-enter your password for security reasons: ")
	return (password, password_re_enter)

# Act on the double entry check
password, password_re_enter = password_input()
while (password != password_re_enter):
	print("\nThe passwords do NOT match!")
	print("\nPlease re-enter the passwords!")
	password, password_re_enter = password_input()

# Salt part

# import salt dictionary with 1000 random english words
with open("salts.txt", "r") as f:
	salt_dic = f.read()

# Turn salt_dic into an array
salt_dic = salt_dic.split()

# Select a random word from the dictionary
salt = random.choice(salt_dic)
salt = "".join(salt)
# printing the salt here would actually print it

# Concatenate the salt and hash and make sure to append it rather than prepend it.
salted_pass = "".join([password, salt])

# printing the password or salted password here would actually print them

salted_pass = salted_pass.encode()

# Define a function with an input parameter of pw for password with the intention of hashing the password with SHA256 and returning the value
def hashing_pass(pw):
	hashed = hashlib.sha256(pw).hexdigest()
	return hashed

hashed_password = hashing_pass(salted_pass)

# Time to insert our salted and hashed passwords as well as the usernames to our mysql db

