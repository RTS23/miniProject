from tinydb import TinyDB, Query

database = TinyDB("D:/nLetsCode/NodeProject/hello/simple_login/database.json")
User = Query()

def display():
    status = input('apakah anda sudah memiliki akun? y/n press q to quit\n')

    while True:
        if status.lower() == 'y':
            login()
            break
        elif status.lower() == 'n':
            create()
            status = input('Apakah anda ingin login ? y/n/q\n')
        elif status.lower() == 'q':
            break
        else:
            print('Input Salah')
            status = input('apakah anda sudah memiliki akun? y/n\n')

def login():
    username = input('masukkan username anda: ')
    password = input('masukkan password anda: ')

    while True:
        if  database.search(User.id == username) and database.search(User.password == password):
            print('Welcome to the jungle')
            break
        else:
            print('Password atau username anda salah !')
            reInput = input('Apakah anda ingin mengisi kembali akun anda? y/n/q\n')
            if reInput.lower() == 'y':
                username = input('masukkan username anda: ')
                password = input('masukkan password anda: ')
            elif reInput.lower() == 'n':
                display()
            else:
                break

def create():
    while True:
        username = input('Masukkan username: ')
        password = input('Masukkan password: ')
        if database.search(User.id == username):
            print('Username ini telah terpakai, gunakan username lain !')
        else:
            database.insert({'id' : username, 'password' : password})
            break

    print('Akun berhasil dibuat')

display()