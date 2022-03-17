import random #import the 'random' library

print('Welcome To Your Password Generator') #create a welcome message

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789' #create a string of random characters 
                                                                                      #to be chosen as the password inputs

number = input('Please enter the amount of passwords you would like to generate: ')
number = int(number)

length = input('Please enter the desired length of your password: ')
length = int(length)

print('\nHere are your passwords:')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)