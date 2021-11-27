#william shaw srn

#from random import randint

num = 0
ans = 0
playerans = 0
choice = ""
num1 = 0
num2 = 0
score = 0
#def generatenum():
 #   num = random.randint(1,9)
 #   return num

def start_game():
    while True:
        num1 = 2#generatenum()
        num2 = 3#generatenum()
        choice = input('Would you like to try addition, subtraction, or multiplication?\nOr would you like to exit?\n')

        if choice == "multiplication":
            ans = num1*num2
            print("what is the product of", num1, "and", num2)
            playerans = input
            if playerans == ans:
                print("correct")
                score += 1
            else:
                print("incorrect")

        elif choice == "addition":
            ans = num1+num2
            playerans = input("what is the sum of " + str(num1) + "and " + str(num2) + "\n")
            if playerans == ans:
                print("correct")
                score += 1
            else:
                print("incorrect")

        elif choice == "subtraction":
            ans = num1-num2
            print("what remains of", num1, "if we take away", num2)
            playerans = input
            if playerans == ans:
                print("correct")
                score += 1
            else:
                print("incorrect")

        elif choice =="end":
            break

        else:
            print("please enter valid choice")
start_game()
        

