import time #import the time library

def countdown(t): #create a function called countdown with a parameter t in seconds
    while t: 
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs) #format the timer into mins and secs
        print (timer, end="\r") 
        time.sleep(1) #after 1 second the timer will stop/sleep
        t -= 1

    print('Timer completed!') #print this message after the time is complete

t = input('Enter the time in seconds: ') #ask the user to type the amount of seconds

countdown(int(t)) #passing t as an integer to avoid error