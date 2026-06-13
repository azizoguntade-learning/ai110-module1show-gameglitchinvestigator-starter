# test_game_logic.py
import pytest
from logic_utils import check_guess

def test_check_guess_hint_directions():
    """
    Tests that the check_guess function returns the correct outcome 
    and logically sound hint directions (fixing the backwards hint bug).
    """
    secret_number = 50

    # Test 1: Guess is too high (Bug was: told user to go "HIGHER!")
    outcome_high, message_high = check_guess(guess=80, secret=secret_number)
    assert outcome_high == "Too High"
    assert "LOWER" in message_high, f"Expected hint to say LOWER, but got: {message_high}"

    # Test 2: Guess is too low (Bug was: told user to go "LOWER!")
    outcome_low, message_low = check_guess(guess=20, secret=secret_number)
    assert outcome_low == "Too Low"
    assert "HIGHER" in message_low, f"Expected hint to say HIGHER, but got: {message_low}"

    # Test 3: Guess is exactly correct
    outcome_win, message_win = check_guess(guess=50, secret=secret_number)
    assert outcome_win == "Win"
    assert "Correct" in message_win