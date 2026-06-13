def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100

def parse_guess(raw: str):
    """
    Parse user input into an int guess.
    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if not raw:
        return False, None, "Enter a guess."

    try:
        # FIX: Collaborated with AI to remove the float() conversion trick, 
        # forcing strict int() casting to properly reject decimals.
        value = int(raw)
    except ValueError:
        return False, None, "That is not a valid whole number."

    return True, value, None

def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    # FIX: AI helped me realize the try/except TypeError block was hiding a string comparison bug. 
    # We deleted that block entirely and flipped the logic to fix the backwards hints.
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    else:
        return "Too Low", "📈 Go HIGHER!"

def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    # FIX: AI and I identified and removed an arbitrary rule that added 5 points 
    # on even-numbered attempts. Now, all incorrect guesses consistently subtract 5 points.
    if outcome in ["Too High", "Too Low"]:
        return current_score - 5

    return current_score