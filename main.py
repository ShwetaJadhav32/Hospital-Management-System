# pip install pwinput   -- # Import pwinput module to mask the password with '*' during user input.

from admin import Admin

def main():
    ch = 0
    while(ch != '2'):
        print("=" * 50)
        print("CITY HOSPITAL".center(50))
        print("Hospital Management System".center(50))
        print("=" * 50)
        print('''Please select Option:
        1. Login
        2. Exit''')

        ch = input('Enter Choice:')
        if(ch == '1'):
            login()
        elif(ch == '2'):
            print("=" * 50)
            print('Exit...'.center(50))
            print('Thank you for Choosing us!'.center(50))
            print("=" * 50)
        else:
            print('Invalid Choice...')

def login():
    print('===== LOGIN PAGE =====')
                    
    uname = 'CityHospital'
    passw = '1234'
    username = input('Enter Username:')
    
    import pwinput

    password = pwinput.pwinput(prompt='Enter Password: ', mask='*')
    

    if(uname == username and passw == password):
        print('✅ Login Successful!')
        a = Admin()
    else:
        print("=" * 50)
        print("❌ Invalid Username or Password.".center(50))
        print("Please Try Again.".center(50))
        print("=" * 50)
        

if(__name__ == '__main__'):
    main()