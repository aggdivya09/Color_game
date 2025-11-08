import random
import time

COLORS = {
    "Red": "\033[31m",
    "Blue": "\033[34m",
    "Green": "\033[32m",
    "Pink": "\033[35m",
    "Black": "\033[30m",
    "Yellow": "\033[33m",
    "Orange": "\033[38;5;208m",  
    "White": "\033[37m",
    "Purple": "\033[95m",
    "Brown": "\033[38;5;94m", 
    "Cyan": "\033[36m",         
    "Magenta": "\033[35m",     
    "LightGreen": "\033[92m", 
}

RESET = "\033[0m"

c=list(COLORS.keys())

score = 0
timeleft = 20
score_file="SCORE.txt"

def next_colour():
    global score
    global timeleft
    random.shuffle(c)
    text_color = c[0]
    word_color = c[1]

    print("\nType the COLOR of the word, not the word itself!")
    print(COLORS[word_color] + text_color + RESET)
    ans = input("Your answer: ").strip().lower()

    if ans == word_color.lower():
        score += 1
        timeleft=timeleft+2
        print("\033[32mCorrect!\033[0m")
    else:
        timeleft=timeleft-5
        print(f"\033[31mWrong!\033[0m It was {word_color}")

    # Prevent timeleft from going negative
    if timeleft < 0:
        timeleft = 0

    print(f"⏳ Time left: {timeleft} seconds")  # show updated time
    time.sleep(0.5)

def main():
    global timeleft, score
    print("🎨 COLOR GAME (Multi-User)")
    print("---------------------------------")
    print("Type the COLOR of the word shown, not the word itself!")
    input("Press Enter to start...")

    name=input("Enter your name: ").strip()

    print("Game Started!   ")

    while timeleft > 0:
        next_colour()
    print("\n-----------------------------------")
    print(f"⏰ Time’s up! Your final score is: {score}")
    print("-------------------------------------")

    with open(score_file,"a")as f:
        f.write(f"{name} - {score}\n")

    see_scores = input("\nDo you want to see previous players' scores? (yes/no): ").strip().lower()

    if see_scores == "yes":
        with open(score_file, "a+") as f:
            f.seek(0)
            lines = f.readlines()
            if lines:
                print("\n🏆 Previous Players' Scores:")
                for line in lines:
                    print(line.strip())
            else:
                print("\nNo previous scores yet!")
    else:
        print("\nThanks for playing! 👋")
        
main()

