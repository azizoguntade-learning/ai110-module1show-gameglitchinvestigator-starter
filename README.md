# 👾 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

---

## 📝 Document Your Experience

**Game Purpose:** An interactive, web-based number guessing game built using Streamlit that is intentionally riddled with state management and logic bugs. It serves as a debugging exercise to understand session state, UI decoupling, and input validation.

**Bugs Discovered:**
* **The Gaslighting Hints:** The game's greater-than/less-than logic was flipped, telling the user to go "Higher" when they guessed above the secret number.
* **The Sabotage Trap:** A hidden bug converted the integer secret to a string on even-numbered attempts, breaking the math and hiding behind a bare `try/except TypeError` block.
* **Math Initialization Error:** The attempts counter started at 1 instead of 0, meaning a player with an 8-attempt limit only saw 7 attempts available at the start.
* **Infinite Game Over:** Clicking "New Game" generated a new number but failed to reset the player's `status`, `score`, or `history`, resulting in an instant "Game Over" message.
* **The Enter Key Glitch:** Pressing the Enter key in the text box reloaded the page without actually submitting the guess or updating the game state.

**Fixes Applied:**
* **Engine Decoupling:** Extracted `parse_guess`, `check_guess`, and `update_score` into a standalone `logic_utils.py` file to separate the game rules from the UI.
* **Logic Repairs:** Fixed the backwards hint bug by correcting the comparison operators and completely removed the deliberate string-conversion trap.
* **State Resets:** Updated the "New Game" button block to properly reset `st.session_state.attempts` to 0, clear the history array, reset the score, and revert the status to "playing".
* **UI Form Wrapper:** Grouped the text input and submit button inside an `st.form(clear_on_submit=True)`, which enabled native "Enter" key submissions and automatically cleared the input box after every guess.
* **Duplicate Protection:** Added validation logic that checks the history array and prevents players from losing an attempt if they submit a previously guessed number.

## 📸 Demo Walkthrough

Below is a sample run of the game played on **Normal** difficulty (Range: 1 to 100, 8 allowed attempts), assuming the secret number is 62.

1. **Game Initialization:** The game boots up cleanly. The attempt counter shows 8 attempts remaining, and the score is 0.
2. **First Guess:** The user types `50` and presses Enter. 
   * The game returns the hint: "📈 Go HIGHER!" 
   * The score deducts 5 points (Score: -5). 
   * Attempts drop to 7.
3. **Second Guess:** The user types `75` and submits.
   * The game returns the hint: "📉 Go LOWER!"
   * The score deducts another 5 points (Score: -10).
   * Attempts drop to 6.
4. **Invalid Input Try:** The user accidentally types `75` again.
   * The game catches the duplicate and warns: "You already guessed 75! Try a different number."
   * The attempt is not counted, and the score remains -10.
5. **Winning Guess:** The user types `62`.
   * The game returns: "🎉 Correct!" and triggers the balloon animation.
   * The scoring engine calculates the win bonus and updates the final score to 50.
   * The status updates to "won", prompting the user to start a new game to play again.

## 🧪 Test Results

```text
========================= test session starts =========================
platform darwin -- Python 3.12.4, pytest-7.4.4, pluggy-1.0.0
rootdir: /Users/game-glitch-investigator
collected 3 items                                                              

tests/test_game_logic.py ...                                     [100%]

========================== 3 passed in 0.08s ==========================