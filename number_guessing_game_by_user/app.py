import streamlit as st
import random

st.title("Number Guessing Game")

# Generate a random number between 1 and 100
if 'number' not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0

# Create input field for user's guess
guess = st.number_input("Guess a number between 1 and 100:", min_value=1, max_value=100, step=1)

# Create a button to submit guess
if st.button("Submit Guess"):
    st.session_state.attempts += 1
    
    if guess == st.session_state.number:
        st.success(f"🎉 Congratulations! You guessed the correct number in {st.session_state.attempts} attempts!")
        if st.button("Play Again"):
            st.session_state.number = random.randint(1, 100)
            st.session_state.attempts = 0
            st.experimental_rerun()
    elif guess < st.session_state.number:
        st.warning("Too low! Try a higher number.")
    else:
        st.warning("Too high! Try a lower number.")

# Add game instructions
st.sidebar.markdown("""
## How to Play
1. Enter a number between 1 and 100
2. Click 'Submit Guess'
3. Follow the hints to guess the correct number
4. Try to guess in as few attempts as possible!
""")

# Display number of attempts
st.sidebar.write(f"Number of attempts: {st.session_state.attempts}")
