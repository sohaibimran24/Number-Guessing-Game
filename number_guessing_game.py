# ============================================
# Number Guessing Game
# Author: Muhammad Sohaib Imran
# FAST-NUCES, Lahore | FinTech
# ============================================

import random
import os


def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header():
    """Print game header."""
    print("\n" + "=" * 40)
    print("        🎯 NUMBER GUESSING GAME")
    print("        Muhammad Sohaib Imran")
    print("        FAST-NUCES, Lahore")
    print("=" * 40)


def choose_difficulty():
    """Let player choose difficulty level."""
    print("\n  Select Difficulty:\n")
    print("  1. 🟢 Easy   — Guess 1 to 50   (10 attempts)")
    print("  2. 🟡 Medium — Guess 1 to 100  (7 attempts)")
    print("  3. 🔴 Hard   — Guess 1 to 200  (5 attempts)")

    while True:
        choice = input("\n  Enter choice (1/2/3): ").strip()
        if choice == '1':
            return 50, 10, "Easy 🟢"
        elif choice == '2':
            return 100, 7, "Medium 🟡"
        elif choice == '3':
            return 200, 5, "Hard 🔴"
        else:
            print("  ❌ Invalid choice! Enter 1, 2, or 3.")


def get_hint(guess, target, low, high):
    """Give a smart hint to the player."""
    difference = abs(guess - target)
    percentage = (difference / target) * 100

    if guess < target:
        direction = "📈 Too LOW!"
    else:
        direction = "📉 Too HIGH!"

    if percentage <= 5:
        warmth = "🔥 VERY HOT! So close!"
    elif percentage <= 15:
        warmth = "♨️  Getting warm..."
    elif percentage <= 30:
        warmth = "🌤  Lukewarm..."
    else:
        warmth = "🧊 Very cold!"

    return f"  {direction} {warmth}"


def print_attempts_bar(attempts_left, max_attempts):
    """Display a visual attempts remaining bar."""
    filled = attempts_left
    empty = max_attempts - attempts_left
    bar = "🟩" * filled + "🟥" * empty
    print(f"\n  Attempts Left: {bar} ({attempts_left}/{max_attempts})")


def calculate_score(attempts_used, max_attempts, difficulty_range):
    """Calculate score based on performance."""
    base_score = 1000
    attempt_penalty = (attempts_used - 1) * (1000 // max_attempts)
    difficulty_bonus = difficulty_range * 2
    return max(0, base_score - attempt_penalty + difficulty_bonus)


def play_game(scores):
    """Play a single round of the number guessing game."""
    clear_screen()
    print_header()

    difficulty_range, max_attempts, difficulty_name = choose_difficulty()
    target = random.randint(1, difficulty_range)
    attempts_used = 0
    guesses = []

    print(f"\n  ✅ Difficulty: {difficulty_name}")
    print(f"  🎯 Guess a number between 1 and {difficulty_range}")
    print(f"  You have {max_attempts} attempts. Good luck!\n")

    while attempts_used < max_attempts:
        attempts_left = max_attempts - attempts_used
        print_attempts_bar(attempts_left, max_attempts)

        if guesses:
            print(f"  Previous guesses: {', '.join(map(str, guesses))}")

        try:
            guess = int(input(f"\n  🎯 Enter your guess (1-{difficulty_range}): "))
        except ValueError:
            print("  ❌ Please enter a valid number!")
            continue

        if guess < 1 or guess > difficulty_range:
            print(f"  ❌ Number must be between 1 and {difficulty_range}!")
            continue

        attempts_used += 1
        guesses.append(guess)

        if guess == target:
            score = calculate_score(attempts_used, max_attempts, difficulty_range)
            clear_screen()
            print_header()
            print(f"\n  🎉 CONGRATULATIONS! You got it!")
            print(f"  ✅ The number was: {target}")
            print(f"  🎯 Attempts used : {attempts_used}/{max_attempts}")
            print(f"  ⭐ Score         : {score} points\n")
            scores['wins'] += 1
            scores['total_score'] += score
            return True
        else:
            hint = get_hint(guess, target, 1, difficulty_range)
            print(hint)

    # Out of attempts
    clear_screen()
    print_header()
    print(f"\n  💀 GAME OVER! You ran out of attempts!")
    print(f"  ❌ The number was: {target}")
    print(f"  Your guesses: {', '.join(map(str, guesses))}\n")
    scores['losses'] += 1
    return False


def print_stats(scores):
    """Display player statistics."""
    total_games = scores['wins'] + scores['losses']
    win_rate = (scores['wins'] / total_games * 100) if total_games > 0 else 0

    print(f"\n  📊 YOUR STATS")
    print(f"  ─────────────────────────")
    print(f"  Games Played : {total_games}")
    print(f"  Wins         : {scores['wins']} 🏆")
    print(f"  Losses       : {scores['losses']} 💀")
    print(f"  Win Rate     : {win_rate:.1f}%")
    print(f"  Total Score  : {scores['total_score']} ⭐")
    print(f"  ─────────────────────────\n")


def main():
    """Main game loop."""
    clear_screen()
    print_header()
    print("\n  Welcome to the Number Guessing Game!")
    print("  Can you guess the secret number?\n")

    player_name = input("  Enter your name: ").strip() or "Player"
    print(f"\n  Welcome, {player_name}! Let's play! 🎮\n")

    scores = {
        'wins': 0,
        'losses': 0,
        'total_score': 0,
        'name': player_name
    }

    while True:
        play_game(scores)
        print_stats(scores)

        again = input("  🔄 Play again? (yes/no): ").strip().lower()
        if again not in ['yes', 'y']:
            clear_screen()
            print_header()
            print(f"\n  Thanks for playing, {player_name}!")
            print_stats(scores)

            total_games = scores['wins'] + scores['losses']
            if total_games > 0:
                if scores['wins'] > scores['losses']:
                    print(f"  🏆 Great job! You won more than you lost!\n")
                elif scores['losses'] > scores['wins']:
                    print(f"  💪 Keep practicing! You'll get better!\n")
                else:
                    print(f"  🤝 Perfectly balanced! Well played!\n")

            print("  — Muhammad Sohaib Imran | FAST-NUCES\n")
            break


if __name__ == "__main__":
    main()
