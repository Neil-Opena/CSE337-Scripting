#Password Check
#Part 1

def validate_length(password):
    if(len(password) < 6 or len(password) > 20):
        return False
    return True

def validate_characters(password):
    has_number, has_uppercase, has_special = False, False, False
    for char in password:
        if(char.isdigit()):
            has_number = True
        elif(char.isupper()):
            has_uppercase = True
        elif(not char.isalnum()):
            has_special = True
    return (has_number and has_uppercase and has_special)

def validate_substring(password):
    dictionary = {}
    for i in range(0, len(password) - (2)):
        substring = password[i:i + 3]
        num_occurrence = dictionary.get(substring)
        if(num_occurrence == None):
            num_occurrence = 1
        else:
            num_occurrence += 1
        dictionary[substring] = num_occurrence
    for key in dictionary.keys():
        if(dictionary.get(key) != 1):
            print(dictionary)
            return False
    return True

def validate_palindrome(password):
    reverse = (password[::-1])
    return not reverse == password

def validate_unique_characters(password):
    dictionary = {}
    for char in password:
        num_occurrence = dictionary.get(char)
        if(num_occurrence) == None:
            num_occurrence = 1
        else:
            num_occurrence +=1
        dictionary[char] = num_occurrence
    return len(dictionary.keys()) > (len(password) / 2)

def validate_username_appearance(password):
    reverse = username[::-1]
    return not ((username in password) or (reverse in password))

def validate(password):
    return validate_length(password) and validate_characters(password) and validate_substring(password) and validate_palindrome(password) and validate_unique_characters(password) and validate_username_appearance(password)

username = input("Username: ")
password = input("Password: ")

print(validate(password))