# test/test_game_logic.py
import pytest
from logic_utils import check_guess, parse_guess

class TestGameLogic:
    """Test suite for the core game engine functions."""

    def test_check_guess_hint_directions(self):
        """
        Tests that check_guess returns the correct outcome 
        and logically sound hint directions.
        """
        secret_number = 50

        # Test 1: Guess is too high
        outcome_high, message_high = check_guess(guess=80, secret=secret_number)
        assert outcome_high == "Too High"
        assert "LOWER" in message_high

        # Test 2: Guess is too low
        outcome_low, message_low = check_guess(guess=20, secret=secret_number)
        assert outcome_low == "Too Low"
        assert "HIGHER" in message_low

        # Test 3: Guess is exactly correct
        outcome_win, message_win = check_guess(guess=50, secret=secret_number)
        assert outcome_win == "Win"
        assert "Correct" in message_win

    def test_parse_guess_valid_input(self):
        """
        Tests that parse_guess correctly identifies proper integers 
        and rejects invalid inputs like floats or text.
        """
        # Valid integer
        ok, val, err = parse_guess("42")
        assert ok is True
        assert val == 42
        assert err is None

        # Invalid float (Testing the bug we fixed)
        ok, val, err = parse_guess("5.5")
        assert ok is False
        assert val is None
        assert "valid whole number" in err