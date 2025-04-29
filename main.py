import random

# Define snakes and ladders
snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

# Player positions
positions = { "Player 1": 0, "Player 2": 0 }

def roll_dice():
    return random.randint(1, 6)

def move_player(player, position):
    dice = roll_dice()
    print(f"{player} rolled a {dice}")
    position += dice
    if position > 100:
        position = 100
    if position in snakes:
        print(f"Oh no! {player} got bitten by a snake and falls to {snakes[position]}")
        position = snakes[position]
    elif position in ladders:
        print(f"Lucky! {player} climbed a ladder to {ladders[position]}")
        position = ladders[position]
    print(f"{player} is now on {position}")
    return position

def play_game():
    current_player = "Player 1"
    while True:
        input(f"\n{current_player}'s turn. Press Enter to roll the dice...")
        positions[current_player] = move_player(current_player, positions[current_player])
        if positions[current_player] == 100:
            print(f"\n🎉 {current_player} wins! 🎉")
            break
        current_player = "Player 2" if current_player == "Player 1" else "Player 1"

if __name__ == "__main__":
    print("🎲 Welcome to Snakes and Ladders 🎲")
    play_game()
