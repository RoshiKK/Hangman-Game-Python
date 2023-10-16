#Import the libraries
import random
import time

# It Open word.txt File and split each word into intergers
with open('words.txt','r') as file:
    word1=file.read()
    word_list=word1.split()

print('*** Welcome to Hangman Game ****')
print()

name=input('What is your Name : ')
print('Welcome to Hangman Game',name+'!......')
time.sleep(2) #It produce delay in program for 2 second
print('Hope you Enjoy............')
time.sleep(2)
print()
 
# Create a function to play the game
def play_game():    
    word = random.choice(word_list) #Select a random word from the list
    word_letters = set(word) #it store multiple words into single variable
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    used_letters = set()
    tries = 6
    word_guessed = set()
    special_character=('!,@,#,$,%,^,&,*,(,)')
    total_letters=int(len(word))        
    score=0   
    print('I am thinking of a word that is',total_letters,'letters long.')

    while len(word_letters) != 0 and tries > 0:
        print("You have {} tries left".format(tries)) #It reduces the tries on wrong guess and format method insert them inside the string 'tries'
        unused = alphabet - used_letters
        print("Unused letters:", ' '.join(unused)) #it prints the unused letters, and join method join them in single string
        print('-------------------------------------------------')

        guess = input("Please enter a letter : ").lower() #It take unput from user, if user enter capital letter it automatically conver into lower letter
        if len(guess)>1:
            print('Enter Only one alphabet')            
        elif guess in special_character:
            print('You are Entering Special Character, Please Enter One Alphabet')                       
        else:
            print()
        if guess in alphabet:
            used_letters.add(guess) #it adding the variable 'guess' to a set called used_letters
            if guess in word_letters:
                word_guessed.add(guess) #It adding the variable 'guess' into another set called word_guessed
                word_letters.discard(guess) #It removes the variable 'guess' from the set called word_guessed
            else:
                tries -= 1
        elif guess == word:
            word_guessed.update(word_letters) #Update method add multiple elements to set, Here it is adding all the letters of word_letters to the set word_guessed
            word_letters.clear() #It will empty the set word_letters
        else:           
            print()

        print("Used letters:", ' '.join(used_letters)) #It print Unused letters and join method join all unused words into single string
        print("Current word:", ' '.join(letter if letter in word_guessed else '_' for letter in word)) #It prints current word, if word is guessed correctly the _ will replace with word and vise versa

    if tries == 0:
        print("You lose. The word was {}.".format(word)) #It print your lose and the correct word and insert them inside the string 'word'
        print('Your Score for this game is',score)
    else:
        print("Congratulations! You won! The word was {}.".format(word)) 
        score+=10
        print('Your Score for this game is',score)          

#Create a function to play as admin
def admin(username,password):
    if username == 'admin' and password == 'admin':
        while True:
            print('1)Add word\n2)Reset leadersboard\n3)Press 3 to exit')
            choice = input('How do you wanna proceed ? ')
            if choice == '1':
                word= input('Enter new word : ')
                word= word.lower() # if word is entered in capital letters it will automatically convert into small letter
                f = open('words.txt','a')
                f.write(' '+str(word))
                f.close()
            elif choice == '2':
                f = open('scores.txt','w')
                f.write(' ')
                f.close
            elif choice == '3':
                exit()
            else:
                print('Enter a valid input')
    else:
        print('Incorrect Login')

#Create a Function for Main Interface
def main():
    while True:
        print("1)Play the game\n2)Login as admin\n3)Press 3 to exit")
        print()
        choice = input("How do you wanna proceed? ")
        if choice == "1":
            play_game() #Directs The user to function play game
        elif choice == "2":
            username = input('Enter your username : ')
            password = input('Enter your password : ')
            admin(username,password) #Directs to the Function admin to check credentials   
        elif choice == "3": #Exits the code
            break
        else:
            print("Invalid choice. Please enter a valid option.")

#it runs the main fuction
main()