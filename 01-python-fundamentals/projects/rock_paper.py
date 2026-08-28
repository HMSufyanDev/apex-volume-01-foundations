import random

choices = {
    "r": 0,  # Rock
    "p": -1, # Paper
    "s": 1   # Scissor
}

names = {
    0: "Rock",
    -1: "Paper",
    1: "Scissor"
}

# Initialize scores 
user_score = 0
computer_score = 0
draws = 0

print("=== Welcome to Rock, Paper, Scissors! ===")

# Main game loop
while True:
    print(f"\nScoreboard -> You: {user_score} | Computer: {computer_score} | Draws: {draws}")
    choose = input("Enter choice (R for Rock, P for Paper, S for Scissor, or Q to Quit): ").lower()

    # Exit condition
    if choose == 'q':
        print("\nThanks for playing!")
        break

    # Input validation
    if choose not in choices:
        print("Invalid choice! Please enter R, P, S, or Q.")
        continue

    user = choices[choose]
    computer = random.choice([0, -1, 1])

    print(f"You chose: {names[user]} | Computer chose: {names[computer]}")

    # Game logic & updating scores
    if user == computer:
        print("It's a draw!")
        draws += 1
    elif (user - computer) in (-1, 2):
        print("You Win this round!")
        user_score += 1
    else:
        print("Computer Wins this round!")
        computer_score += 1

# Final summary when quitting
print("\n" + "="*30)
print("FINAL RESULT")
print(f"You: {user_score} | Computer: {computer_score} | Draws: {draws}")

if user_score > computer_score:
    print("Overall Winner: YOU!")
elif computer_score > user_score:
    print("Overall Winner: COMPUTER!")
else:
    print("Overall Result: IT'S A TIE!")
print("="*30)