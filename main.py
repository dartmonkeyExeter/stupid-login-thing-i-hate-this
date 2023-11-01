login_or_register = ''
logins = {
    'fartface3000': 'poopybuttfart23',
    'thesussyimpostor': 'vent123'
}

while True:
    login_or_register = input('would you like to login (l) or register (r)?\n').lower().strip()
    if login_or_register == 'l':
        username = input('what is your username\n').lower().strip()
        if username not in logins:
            print('not found')
        else:
            password = input('password\n').lower().strip()
            if password == logins[username]:
                print(f'hello {username}')
            else:
                print('not correct')
    elif login_or_register == 'r':
        new_username = input('what would you like to be your username?\n').strip()
        new_password = input('what would you like to be your password?\n').strip()
        logins.update({new_username: new_password})
    else:
        print('invalid input')
