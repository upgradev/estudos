import ex83login


def main():

    first = input('enter your first name: ')
    last = input('enter your last name: ')
    idnumber = input('enter yout student Id number: ')

    print('Your system login name is:')
    print(ex83login.get_login_name(first, last, idnumber))


if __name__ == '__main__':
    main()
