import random

class Player:
    def __init__(self, name, lives):
        self.name = name
        self.lives = lives
        self.choice = ''
    def getPlayerChoice(self):
        if self.name == "Computer":
            computer_options = ["rock", "paper", "scissors"]
            choice = random.choice(computer_options)
            self.choice = choice
            return choice
        else:
            choice = input("Rock, Paper, or Scissors?  ").lower()
            self.choice = choice
            return choice
    def removeLifePoint(self):
        self.lives = self.lives - 1
        return self.lives

def startGame(): 
    userProfile = Player("AlexSnows", 3)
    computerProfile = Player("Computer", 3)
    startNextRound(userProfile, computerProfile)

def startNextRound(userProfile, computerProfile) :
    userChoice = userProfile.getPlayerChoice()
    computerChoice = computerProfile.getPlayerChoice()
    print("Computer:", computerChoice, "User:", userChoice)

    if userChoice == "rock" and computerChoice == "scissors":
        
        computerProfile.removeLifePoint()
        checkNumberOfLives(userProfile, computerProfile)

    elif userChoice == "scissors" and computerChoice == "paper": 
        
        computerProfile.removeLifePoint()
        checkNumberOfLives(userProfile, computerProfile)

    elif userChoice == "paper" and computerChoice == 'rock':
        computerProfile.removeLifePoint()
        checkNumberOfLives(userProfile, computerProfile)
    
    elif userChoice == computerChoice: 
        startNextRound(userProfile, computerProfile)
    else: 
        userProfile.removeLifePoint()
        checkNumberOfLives(userProfile, computerProfile)

def checkNumberOfLives(userProfile, computerProfile) :

    print("COMPUTER lIVES LEFT:", computerProfile.lives, "USER LIVES LEFT:", userProfile.lives)

    if computerProfile.lives <= 0:
        playAgain()
        print("You have won the match!!")
    
    elif userProfile.lives <= 0:
        print("Sorry you have lost the match")
        playAgain()
    
    else:
        startNextRound(userProfile, computerProfile)
        return "We Keep Going!!!!!"
    
def playAgain(): 
    
    keepPlaying = input("Would You like to play again: (y/n) ")
    
    if keepPlaying == "y":
        startGame()
    else: 
        return 

startGame()
