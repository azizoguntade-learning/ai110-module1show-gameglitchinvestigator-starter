# 💭 Reflection: Game Glitch Investigator

## 1. What was broken when you started?

When I initially ran the application, the interface loaded with significant display lag, especially around the user input field. I immediately identified several critical state management bugs, including an attempts counter that started at five instead of six and failed to decrement after a guess. Additionally, the core game engine was structurally flawed: it allowed out-of-bounds guesses like 120 without throwing errors and provided completely backwards hints, such as telling me to go "higher" when I was already at the maximum limit.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
Enter 120    Deny input       Accepted guess    None / Silent failure
Enter 100    Hint -> "Lower"  Hint -> "Higher"        None 
Click New Game  Reset all     No Reset          Localhost reload required

---

## 2. How did you use AI as a teammate?

I used Gemini as a collaborative coding partner to brainstorm solutions, separate my game engine logic, and troubleshoot UI synchronization issues. A correct and highly useful suggestion was to wrap my text input and submit button inside an `st.form`, which perfectly resolved the bug where pressing the "Enter" key failed to register a guess. However, early on I received a misleading suggestion to manage the game state using a standard `while` loop; I quickly verified this was incorrect because it caused the app to freeze, as Streamlit requires a top-down rerun model rather than persistent background loops.

---

## 3. Debugging and testing your fixes

I decided a bug was genuinely fixed only when I could perform the exact sequence of steps that caused the original failure and observe the expected, correct behavior instead. To validate the engine, I ran a `pytest` suite against the `check_guess` function, which proved my code successfully fixed the "backwards hint" bug by asserting that guesses higher than the secret strictly returned a "LOWER" hint. The AI helped me design these tests by structuring them into a formal `TestGameLogic` class and identifying the specific boundary conditions—like exact matches and out-of-bounds inputs—that needed to be locked down.

---

## 4. What did you learn about Streamlit and state?

I would explain Streamlit to a friend as an artist who completely redraws a painting from top to bottom every single time you click a button or interact with the page. Because the script runs from scratch so frequently, it inherently forgets what was on the screen just a second ago. "Session state" acts like a permanent sticky note in the artist's pocket, allowing the application to remember critical details—like the player's running score, history, or remaining attempts—across all of those endless redraws.

---

## 5. Looking ahead: your developer habits

In future projects, I plan to consistently reuse the strategy of completely separating my core business logic from the UI code, as it made isolating bugs and writing `pytest` cases significantly easier. Next time I work with an AI assistant, I will provide smaller, targeted snippets of code alongside explicit, multi-step instructions rather than asking it to debug an entire application at once. Ultimately, this project reinforced that AI-generated code serves as an excellent rough draft, but it requires rigorous human review and testing because it frequently hallucinates the nuanced logic required for stateful web applications.