import random 
import string 

def generate_password(min_length, numbers=True, special_chars=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    
    characters = letters 
    if numbers:
        characters += digits
    if special_chars:
        characters += special

    pwd = ""
    meets_criteria = False 
    has_number = False 
    has_special = False 

    while not meets_criteria or len(pwd) < min_length:
        random_char = random.choice(characters)
        pwd += random_char

        if random_char in digits:
            has_number = True
        elif random_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_chars:
               meets_criteria = meets_criteria and has_special

    return pwd

min_length = int(input("Enter minimum password length: "))
has_numbers = input("Include numbers? (y/n): ").lower() == "y"
has_specials = input("Include special characters? (y/n): ").lower() == "y"
pwd = generate_password(min_length, has_numbers, has_specials)  
print("Generated Password:", pwd)               

        


