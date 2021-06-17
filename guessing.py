low = 0
high = 100
guess = (high+low)/2.0
answer=''

print('Please think of a number between 0 and 100!')

while answer!='c':
    print('Is your secret number '+str(int(guess))+'?')
    answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if answer == 'l':
        low = guess
    elif answer == 'h':
        high = guess
    elif answer == 'c':
        print('Game over. Your secret number was: ',end=str(guess))          
    else: 
        print("Don't recognize that input")               
    guess = int((high+low)/2.0)
