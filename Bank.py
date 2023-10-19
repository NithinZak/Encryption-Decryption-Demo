import mysql.connector
import base64
from cryptography.fernet import Fernet

def Encryption(passkey,data):
    key = base64.urlsafe_b64encode(passkey.zfill(32).encode())
    encoded_data = data.to_bytes(14, byteorder='big', signed=False)
    obj = Fernet(key)
    encrypted_data = obj.encrypt(encoded_data)
    return encrypted_data

def Decryption(passkey,data):
    try:
        key = base64.urlsafe_b64encode(passkey.zfill(32).encode())
        obj = Fernet(key)
        decrypted_data = obj.decrypt(data)
        decoded_data = int.from_bytes(decrypted_data, byteorder='big', signed=False)
        return decoded_data
    except:
        if Exception:
            pass
def Encrypted_view(namepass):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='avoshiaavozaker123#',
        port=3306,
        database='bank')
    user = connection.cursor()
    user.execute('select Name from user_credentials where Name_password like %s', ((namepass,)))
    data = user.fetchall()
    for i in data:
        for j in i:
            username = j
            print(f'Name :{username}')

    user.execute('select Email from user_credentials where Name_password like %s', ((namepass,)))
    data = user.fetchall()
    for i in data:
        for j in i :
            email = j
            print(f'Email :{email}')

    user.execute('select Phone from user_credentials where Name_password like %s', ((namepass,)))
    data = user.fetchall()
    for i in data:
        for j in i:
            phone = j
            print(f'Phone number :{phone}')
    user.execute('select Account from user_credentials where Name_password like %s', ((namepass,)))
    data = user.fetchall()
    for i in data:
        for j in i:
            account = j
            print(f'Account number :{account}')


    user.execute('select Balance from user_credentials where Name_password like %s', ((namepass,)))
    data = user.fetchall()
    for i in data:
        for j in i:
            balance = j
            print(f'Balance :{balance}')

    user.close()
    connection.close()
    return

def Decrypted_view(namepass,passkey):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='avoshiaavozaker123#',
        port=3306,
        database='bank')
    user = connection.cursor()
    user.execute('select Name from user_credentials where Name_password like %s', ((namepass,)))
    data = user.fetchall()
    for i in data:
        for j in i:
            username = j
            print(f'Name :{username}')

    user.execute('select Email from user_credentials where Name_password like %s', ((namepass,)))
    data = user.fetchall()
    for i in data:
        for j in i :
            email = j
            print(f'Email :{email}')

    user.execute('select Phone from user_credentials where Name_password like %s', ((namepass,)))
    data = user.fetchall()
    for i in data:
        for j in i:
            phone = j
            print(f'Phone number :{phone}')
    user.execute('select Account from user_credentials where Name_password like %s', ((namepass,)))
    data = user.fetchall()
    for i in data:
        for j in i:
            account = j
            decrypted_account = Decryption(passkey,account)
            print(f'Account number :{decrypted_account}')

    user.execute('select Balance from user_credentials where Name_password like %s', ((namepass,)))
    data = user.fetchall()
    for i in data:
        for j in i:
            balance = j
            # print(balance)
            decrypted_balance = Decryption(passkey,balance)
            print(f'Balance :{decrypted_balance}')

    user.close()
    connection.close()
    return

# def Balance_update(namepass,passkey):
#
#     connection = mysql.connector.connect(
#         host='localhost',
#         user='root',
#         password='avoshiaavozaker123#',
#         port=3306,
#         database='bank')
#     user = connection.cursor()
#     balance = int(input('Enter your bank balance: '))
#     encrypted_balance = Encryption(passkey,balance)
#     user.execute("update user_credentials set Balance = %s where Name_password like %s ",(encrypted_balance,namepass))
#     connection.commit()
#     connection.close()
#     print(f'Balance updated successfully...')

def withdraw(namepass):
   try:
       passkey = input('Enter the 4 digit key :')
       while len(passkey) != 4:
           print('Wrong key...')
           main(namepass)
       amount = int(input("ENTER THE AMOUNT DO YOU WANT TO WITHDRAW : "))

       mydb = mysql.connector.connect(
           host="localhost",
           user="root",
           password="avoshiaavozaker123#",
           port=3306,
           database='bank'
       )
       mycursor = mydb.cursor()
       mycursor.execute("select Balance from user_credentials where Name_password=%s", (namepass,))
       balance = mycursor.fetchone()
       mycursor.execute("select Passkey from user_credentials where Name_password=%s", (namepass,))
       key = mycursor.fetchall()
       for i in key:
           for j in i:
               # print(i)
               if j == int(passkey):
                   for i in balance:
                       encry_balance = i
                       decrypted_balance = Decryption(passkey, encry_balance)
                       # print(decrypted_balance)
                       if decrypted_balance >= amount:
                           decrypted_balance -= amount
                           encrypted_balance = Encryption(passkey, decrypted_balance)
                           mycursor.execute("update user_credentials set Balance=%s where Name_password =%s",
                                            (encrypted_balance, namepass))
                           mydb.commit()
                           mydb.close()
                           return "DEAR USER, YOU DEBITED BY RS.", amount
                       else:
                           print('Balance not enough...')
                           main(namepass)
               else:
                   print('Wrong key...')
                   main(namepass)
   except Exception:
       print('Somthing went wrong...')
       main(namepass)


def deposit(namepass):
    try:
        passkey = (input('Enter the 4 digit key :'))
        while len(passkey) != 4:
            print('Wrong key...')
            main(namepass)
        amount = int(input("ENTER THE AMOUNT DO YOU WANT TO DEPOSIT : "))

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="avoshiaavozaker123#",
            port=3306,
            database='bank'
        )
        mycursor = mydb.cursor()
        mycursor.execute("select Balance from user_credentials where Name_password=%s", (namepass,))
        balance = mycursor.fetchone()
        mycursor.execute("select Passkey from user_credentials where Name_password=%s", (namepass,))
        key = mycursor.fetchall()
        for i in key:
            for j in i:
                # print(i)
                if j == int(passkey):
                    for i in balance:
                        encry_balance = i
                        decrypted_balance = Decryption(passkey, encry_balance)
                        # print(decrypted_balance)
                        decrypted_balance += amount
                        encrypted_balance = Encryption(passkey, decrypted_balance)
                        mycursor.execute("update user_credentials set Balance=%s where Name_password =%s",
                                         (encrypted_balance, namepass))
                        mydb.commit()
                        mydb.close()
                        return "DEAR USER, YOU CREDITED BY RS.", amount
                else:
                    print('Wrong key...')

                    main(namepass)
    except Exception:
        print('Somthing went wrong...')
        main(namepass)


def main(namepass):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="avoshiaavozaker123#",
        port=3306,
        database='bank'
    )
    mycursor = mydb.cursor()


    print('1.View\n2.Deposit\n3.Withdraw\n4.Logout')
    selector = input('Select your option :')
    if selector == '1':
        yn = input('Do you want to see the decrypted data...?(y/n) :')
        if yn.upper() == 'Y':
            passkey = (input('Enter the 4 digit key :'))
            while len(passkey) != 4:
                print('Wrong key...')
                main(namepass)
            mycursor.execute("select Passkey from user_credentials where Name_password=%s", (namepass,))
            key = mycursor.fetchall()
            for i in key:
                for j in i:
                    # print(i)
                    if j == int(passkey):
                        Decrypted_view(namepass, passkey)
                    else:
                        print('Wrong key...')

            # key = base64.urlsafe_b64encode(passkey.zfill(32).encode())

            main(namepass)
        elif yn.upper() == 'N':
            Encrypted_view(namepass)
            main(namepass)
        else:
            print('Invalid answer...')
    elif selector == '2':
        print(deposit(namepass))
        main(namepass)
    elif selector == '3':
        print(withdraw(namepass))
        main(namepass)
    elif selector == '4':
        x = input('Do you want to Logout...?(y/n) :')
        if x.upper() == 'Y':
            print('Logged out...')
            return
        elif x.upper() == 'N':
            print('Logging cancelled...')
            main(namepass)
        else:
            print('Invalid answer...')
            main(namepass)
    else:
        print('Invalid answer...')
        main(namepass)

def login():
    name = input("ENTER YOUR NAME: ")
    password = input("ENTER YOUR PASSWORD: ")
    namepass = (name+password)
    # passkey = input('Enter the 4 digit key :')
    # while len(passkey) != 4:
    #     passkey = input('Enter the 4 digit key :')

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="avoshiaavozaker123#",
        port=3306,
        database="bank"
    )

    cursorsign = mydb.cursor()
    # cursorsign.execute("use testdb")

    try:
        cursorsign.execute("select * from user_credentials where Name_password = %s", ((namepass,)))
        user_data = cursorsign.fetchall()
        if user_data:
            print("LOGIN SUCCESSFUL")
            main(namepass)
        else:
            print("LOGIN FAILED")
            print('1.Try again\n2.Back')
            x = input('Select from above :')
            if x == '1':
                login()
            elif x == '2':
                return
            else:
                return

    except Exception as e:
        print("An error occurred in login:", e)
    cursorsign.close()
    mydb.close()


def signup():
    name = input("ENTER YOUR NAME: ")
    password = input("ENTER YOUR PASSWORD: ")
    while len(str(password)) < 8:  # password strength verification
        print('Enter a password with minimum of 8 letters..')
        password = input("ENTER YOUR PASSWORD: ")
    namepass = name + password
    passkey = (input('Enter the 4 digit key which is not startig with zero :'))
    while len(passkey) != 4:
        print('Please enter a 4 digit number')
        passkey = (input('Enter the 4 digit key :'))
    if passkey[0] == '0':
        print('dont start with 0...')
        signup()
        # passkey = (input('Enter the 4 digit key :'))
    email = input('Enter your email: ')
    while email[-10:] != '@gmail.com':  # email format verification
        print('Wrong email format')
        email = input('Enter your email :')
    phone = int(input('Enter your phone number: '))
    while len(str(phone)) != 10:  # phone number verification
        print('Worng phone number format')
        phone = int(input('Enter your phone number :'))
    ac_num = int(input("ENTER YOUR ACCOUNT NUMBER: "))
    while len(str(ac_num)) not in range(9, 14):  # account number verification
        print('Wrong number...')
        ac_num = int(input('Enter your account number :'))
    encrypted_ac_num = Encryption(passkey, ac_num)
    balance = int(input('Enter your bank balance: '))
    encrypted_balance = Encryption(passkey, balance)
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="avoshiaavozaker123#",
        port=3306,
        database="bank"
    )

    cursorsign = mydb.cursor()
    # cursorsign.execute("use testdb")

    try:
        cursorsign.execute('select Name_password from user_credentials')
        data = cursorsign.fetchall()
        for i in data:
            if i == (namepass,):
                print('User already exists, Please login...')
                login()
                break
        print('Signed in successfully...')
        cursorsign.execute(
            "insert into user_credentials(Name_password,Name,Email,Phone, Account, Balance, Passkey) values (%s, %s, %s, %s, %s, %s, %s)",
            (namepass, name, email, phone, encrypted_ac_num, encrypted_balance, passkey))
        mydb.commit()
        main(namepass)
    except Exception as e:
        if "Duplicate entry" in str(e):
            print("User already exists, Please login...")
            login()
        else:
            print("An error occurred:", e)

    cursorsign.close()
    mydb.close()

def selector():
   try:
       choice = int(input(" 1.SIGN UP\n 2.LOGIN\n ENTER YOUR CHOICE: "))

       if choice == 1:
           signup()
       elif choice == 2:
           login()
           selector()
       else:
           print('Invalid answer....')
   except Exception:
       print('Somthing went wrong...')
       selector()
selector()

