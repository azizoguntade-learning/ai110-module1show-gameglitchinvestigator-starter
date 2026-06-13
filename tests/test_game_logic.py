# test/test_game_logic.py
import pytest
from logic_utils import check_guess, parse_guess, update_score

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

        # Invalid float
        ok, val, err = parse_guess("5.5")
        assert ok is False
        assert val is None
        assert "valid whole number" in err

    def test_update_score_logic(self):
        """
        Tests that scoring math correctly rewards wins and penalizes misses.
        """
        current = 50

        # Test 1: Win on attempt 0 (Formula: 100 - 10 * 1 = 90 points)
        new_score = update_score(current_score=current, outcome="Win", attempt_number=0)
        assert new_score == current + 90

        # Test 2: Win on attempt 15 (Should floor at 10 points, not go negative)
        floor_score = update_score(current_score=current, outcome="Win", attempt_number=15)
        assert floor_score == current + 10

        # Test 3: Incorrect guesses strictly deduct 5 points
        high_score = update_score(current_score=current, outcome="Too High", attempt_number=1)
        assert high_score == current - 5
        
        low_score = update_score(current_score=current, outcome="Too Low", attempt_number=2)
        assert low_score == current - 5