import streamlit as st
import random

# Store random number 
if 'random_number' not in st.session_state:
    st.session_state.random_number = random.randint(1, 100)

st.title("🎯 Number Guessing Game")
st.write("Guess a number between 1 and 100!")

# User input
user_guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

# Check button
if st.button("Check Guess"):
    if user_guess < st.session_state.random_number:
        st.warning("Too low! Try a higher number.")
    elif user_guess > st.session_state.random_number:
        st.warning("Too high! Try a lower number.")
    else:
        st.success("🎉 Congratulations! You guessed the correct number.")
        st.session_state.random_number = random.randint(1, 100) 

# Button to restart the game
if st.button("Restart Game"):
    st.session_state.random_number = random.randint(1, 100)
    st.success("Game restarted! Try guessing again.")