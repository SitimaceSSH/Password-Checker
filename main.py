import os
import requests
import getpass
from hibp import get_hash, count_leaks
from generator import generator
from colors import RED, GREEN, CYAN, YELLOW, RESET, BOLD


BANNER = r'''
__________                                               .___   _________ .__            __                 
\______   \_____    ______ ________  _  _____________  __| _/   \_   ___ \|  |__   ____ |  | __ ___________ 
 |     ___/\__  \  /  ___//  ___/\ \/ \/ /  _ \_  __ \/ __ |    /    \  \/|  |  \_/ __ \|  |/ // __ \_  __ \
 |    |     / __ \_\___ \ \___ \  \     (  <_> )  | \/ /_/ |    \     \___|   Y  \  ___/|    <\  ___/|  | \/
 |____|    (____  /____  >____  >  \/\_/ \____/|__|  \____ |     \______  /___|  /\___  >__|_ \\___  >__|   
                \/     \/     \/                          \/            \/     \/     \/     \/    \/      
'''


def header():
    os.system('cls||clear')
    print(f'{CYAN}{BANNER}{RESET}')
    print(f'Developer: {GREEN}Sitimace{RESET}                                                 Version: {YELLOW}1.0{RESET}\n')


def menu():
    print(f'                {BOLD}[1]{RESET}: Check Your Password')
    print(f'                {BOLD}[2]{RESET}: Generate Safe Password (No Leaked Password)')
    print(f'                {BOLD}[3]{RESET}: Exit\n')


def main():
    while True:
        header()
        menu()
        user = getpass.getuser()
          
        user_input = input(f"{user}@password-checker: ")
        try:
            if user_input == '1':
                password = getpass.getpass('Password (hidden): ')
                full_hash = get_hash(password)
                prefix = full_hash[:5]
                suffix = full_hash[5:]
                leaks = count_leaks(prefix, suffix)
                if leaks > 0:
                    print(f'{RED}[ALERT]: Password found: {leaks} times!{RESET}')
                    input('Press Enter to continue...')
                else:
                    print(f"{GREEN}[SUCCESS]: You are safe, the password was not found!{RESET}")
                    input('Press Enter to continue...')
            elif user_input == '2':
                generator()
                input('Press Enter to continue...')
            elif user_input == '3':
                print('Bye!')
                break
            else:
                print(f'{RED}[ERROR]: Invalid choice.{RESET}')
                input('Press Enter to continue...')
        except requests.RequestException:
            print(f'{RED}[ERROR]: Could not reach the Have I Been Pwned API. '
                  f'Check your internet connection and try again.{RESET}')
            input('Press Enter to continue...')
        except RuntimeError as e:
            print(f'{RED}[ERROR]: {e}{RESET}')
            input('Press Enter to continue...')
                



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('\nBye!')
