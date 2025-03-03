import streamlit as st
import random

# Set Streamlit page config
st.set_page_config(page_title="Number Guessing Game", page_icon="🎯", layout="centered")

# Initialize session state variables
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "max_attempts" not in st.session_state:
    st.session_state.max_attempts = 7
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "message" not in st.session_state:
    st.session_state.message = ""

# Title and Instructions
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🎯 Number Guessing Game</h1>", unsafe_allow_html=True)
st.markdown("""
    <p style='text-align: center; font-size: 18px; color: #333;'>
    Guess a number between **1 and 100**. You have **7 attempts**. Let's see if you can guess it! 🚀
    </p>
""", unsafe_allow_html=True)

# Display previous message
if st.session_state.message:
    st.warning(st.session_state.message)

# User Input
if not st.session_state.game_over:
    guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1, key="guess", format="%d")

    # Button to check guess
    if st.button("Submit Guess"):
        st.session_state.attempts += 1
        if guess < st.session_state.secret_number:
            st.session_state.message = f"🔼 Too low! You have {st.session_state.max_attempts - st.session_state.attempts} attempts left."
        elif guess > st.session_state.secret_number:
            st.session_state.message = f"🔽 Too high! You have {st.session_state.max_attempts - st.session_state.attempts} attempts left."
        else:
            st.success(f"🎉 Congratulations! You guessed the correct number **{st.session_state.secret_number}** in {st.session_state.attempts} attempts!")
            st.session_state.game_over = True

        # If max attempts reached
        if st.session_state.attempts >= st.session_state.max_attempts and guess != st.session_state.secret_number:
            st.session_state.message = f"😢 Game Over! The correct number was **{st.session_state.secret_number}**."
            st.session_state.game_over = True

# Restart Button
if st.session_state.game_over:
    if st.button("🔄 Play Again"):
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.session_state.message = ""
