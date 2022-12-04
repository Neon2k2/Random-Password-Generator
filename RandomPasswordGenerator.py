import random
import math
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers =["1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ['!', '#', '$', '%', '&','*','+']

print("Yo lets generate you a password that cant be hacked!!")

n_letters = int(input("How many letters you want in your password\n"))
n_numbers = int(input("how many numbers you want in your password\n"))
n_symbols = int(input("how many symbols you want in your password\n"))

passwordL = []
for n in range(0, n_letters):
    passwordL.append(letters[random.randint(0, len(letters)-1)])

passwordn = []
for n in range(0, n_numbers):
    passwordn.append(numbers[random.randint(0, len(numbers)-1)])

passwords = []
for n in range(0, n_symbols):
    passwords.append(symbols[random.randint(0, len(symbols)-1)])   
password = []

for PL in passwordL:
    password.append(PL)

    passwordL.pop(passwordL.index(PL))

    if len(passwordL) == math.floor((len(passwordL))/2):
        break;


for PN in passwordn:
    password.append(PN)
    passwordn.pop(passwordn.index(PN))
    if len(passwordn) == math.floor((len(passwordn))/2):
        break;
      
        
for PS in passwords:
    password.append(PS)
    passwords.pop(passwords.index(PS))
    if len(passwords) == math.floor((len(passwords))/2):
        break;


for PN in passwordn:
    password.append(PN)               
for PS in passwords:
    password.append(PS)

for PL in passwordL:
    password.append(PL)

password = "".join(password)
print(f"your new password is {password}")   
