import string
import secrets
from hibp import get_hash, count_leaks
from colors import RED, GREEN, YELLOW, RESET

def generator():
    characters_l = string.ascii_letters 
    characters_d = string.digits
    characters_s = string.punctuation

    def check_length():
        while True:
            try:
                length = int(input('length (e.g 12): '))
                if length > 4:
                    return length
                print(f'{RED}[ERROR]: Length must be greater than 4.{RESET}')
            except ValueError:
                print(f'{RED}[ERROR]: Only numbers (e.g 12){RESET}')


    def check_digits():
        digits = input('Digits(e.g 1,2,3) (y/n): ')
        while digits.lower() not in ('y', 'n'):
            digits = input('Digits(e.g 1,2,3) (y/n): ')
        return digits.lower() == 'y'
        



    def check_special():
        special_characters = input('Special Characters(e.g !,#,@) (y/n): ')
        while special_characters.lower() not in ('y', 'n'):
            special_characters= input('Special Characters(e.g !,#,@) (y/n): ')
        return special_characters.lower() == 'y'


    length = check_length()
    digits = check_digits()
    special_characters = check_special()

    def generate_password(length, digits, special_characters):
        safe = False
        while not safe:
            passwd = ''
            for i in range(length):
                if digits == True and special_characters == True:
                    passwd = passwd + secrets.choice(characters_l + characters_d + characters_s)
                elif digits == True and special_characters == False:
                    passwd = passwd + secrets.choice(characters_l + characters_d)
                elif digits == False and special_characters == True:
                    passwd = passwd + secrets.choice(characters_l + characters_s)
                else:
                    passwd = passwd + secrets.choice(characters_l)
            full_hash = get_hash(passwd)
            prefix = full_hash[:5]
            suffix = full_hash[5:]
            leaks = count_leaks(prefix, suffix)
            if leaks > 0:
                print(f'{YELLOW}[WARNING]: Generated password was found in data leaks. Generating a new one...{RESET}')
                safe = False
            else:
                safe = True
        print(f'{GREEN}[SUCCESS]: Password generated: {passwd}{RESET}')

    
    generate_password(length, digits, special_characters)
