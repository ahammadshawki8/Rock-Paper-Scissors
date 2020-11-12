import random
import time

def start():
    print("!!! WELCOME TO THE RPS GAME !!!")
    time.sleep(1.5)
    input("press enter to continue\n")
    print()

    print("Hello! Do you remember me? I am Comp. I have played head-tail with you earlier")
    valid=False
    permit=input("Would you want to play Rock-Paper-Scissor with me? (yes/no)\n")
    while not valid:
        if permit == "yes":
            print("Great!\n")
            rps()
            valid=True
        elif permit =="no":
            print()
            print("Okay, then I will play with Shawki.")
            time.sleep(2)
            valid=True
        else:
            print("Enter a valid decision.")
            valid=False
            permit=input()

    if valid:
        time.sleep(2)
        print("\n")
        print("Thank you for playing this game.")
        time.sleep(0.5)
        print("creator: Ahammad Shawki")
        time.sleep(5)

def rps():
    username=input("Please enter your username: ")
    rps_box=["r","p","s"]
    round_to_play=int(input("How many rounds you want to play?\n"))
    print("Okay then who will first heat the",round_to_play,"score will be the winner :)")
    print('\n')
    print("you have to type r for Rock, p for Paper and S for scissor.")
    print("you can always see the current score by typing score.")

    comp_total=0
    user_total=0
    while comp_total != round_to_play and user_total != round_to_play:
        user_turn=input(username+"'s turn --> ")
        
        if user_turn=="score":
            print("comps score :",comp_total,"\t",username+"'s score :",user_total,"\t","target :",round_to_play)
            print()
        else:
            comp_turn=random.choice(rps_box)
            print("Comps turn -->",comp_turn)
            
            if (comp_turn=="r" and user_turn=="s") or (comp_turn=="p" and user_turn=="r") or (comp_turn=="s" and user_turn=="p"):
                comp_total+=1
                print("comp wins this round")
                if comp_total+1 == round_to_play:
                    print()
                    print("Warning: LAST POINT.....")

            elif comp_turn==user_turn:
                print("no one wins")
                
            elif (comp_turn=="s" and user_turn=="r") or (comp_turn=="r" and user_turn=="p") or (comp_turn=="p" and user_turn=="s"):
                user_total+=1
                print(username,"wins this round")
                if user_total+1 == round_to_play:
                    print()
                    print("Warning: LAST POINT.....")
            else:
                print("Enter a valid shot")
            print()
            

    if comp_total>user_total:
        print("comp wins this game!")
    else:
        print(username," wins the game!")


if __name__ == "__main__":
    start()
