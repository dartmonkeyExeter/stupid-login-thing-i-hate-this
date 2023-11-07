import time

logins = {
    'fartface3000': 'poopybuttfart23',
    'thesussyimpostor': 'vent123'
}

new_dict = {}

def account_management(username):
    while True:
        account_choice = input(f'hello {username}, what would you like to do?\n'
                               f'(s)ign out, (d)elete your account, or (c)hange your password: ').lower().strip()
        if account_choice == "s":
            print("signed out!")
            break
        elif account_choice == "d":
            deletion = input("are you sure? re-enter your password to continue deletion: ")
            if deletion == logins[username]:
                print("deleting account...")
                time.sleep(0.5)
                logins.pop(username)
                print("account deleted!")
                break
            elif deletion == "n":
                continue
            else:
                print("invalid input")
        elif account_choice == "c":
            new_password = input("please enter new password: ")
            logins[username] = new_password


def choice():
    login_or_register = input('would you like to login (l) or register (r)?\n').lower().strip()
    if login_or_register == 'l':
        username = input('what is your username\n').lower().strip()
        if username not in logins:
            print('not found')
        else:
            password = input('password\n').lower().strip()
            if password == logins[username]:
                account_management(username)
            else:
                print('not correct')
    elif login_or_register == 'r':
        new_username = input('what would you like to be your username?\n').strip()
        new_password = input('what would you like to be your password?\n').strip()
        logins.update({new_username: new_password})
    else:
        print('invalid input')


def iteration_speed():
    for i in range(1000000000):
        new_dict.update({f"{i}": f"{i - (i*2)}"})

    start_time = time.perf_counter()
    for i in new_dict:
        print(i)
    end_time = time.perf_counter()
    time_one = start_time - end_time

    start_time = time.perf_counter()
    for i in new_dict:
        print(new_dict[i])
    end_time = time.perf_counter()
    time_two = start_time - end_time

    start_time = time.perf_counter()
    for i in new_dict.values():
        print(i)
    end_time = time.perf_counter()
    time_three = start_time - end_time

    start_time = time.perf_counter()
    for i, j in new_dict.items():
        print(i, j)
    end_time = time.perf_counter()
    time_four = start_time - end_time

    print(f'times\n1: {time_one}\n2: {time_two}\n3: {time_three}\n4: {time_four}')

iteration_speed()


# while True:
#    choice()
