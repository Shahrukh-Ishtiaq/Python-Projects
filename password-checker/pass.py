import streamlit as st
import re

def check_password(password):
    rules = {
        "Length (min 8 characters)": len(password) >= 8,
        "Uppercase letter (A-Z)": bool(re.search(r"[A-Z]", password)),
        "Lowercase letter (a-z)": bool(re.search(r"[a-z]", password)),
        "Number (0-9)": bool(re.search(r"\d", password)),
        "Special character (@, $, !, %, etc.)": bool(re.search(r"[@$!%*?&#]", password))
    }
    
    score = 0
    suggestions = []
    
    for rule, passed in rules.items():
        if passed:
            score += 1
        else:
            suggestions.append(f"- {rule}")
    
    if score <= 2:
        strength, color = "Weak", "red"
    elif score == 3 or score == 4:
        strength, color = "Medium", "orange"
    else:
        strength, color = "Strong", "green"
    
    return strength, color, suggestions

st.title("🔐 Password Strength Checker")
password = st.text_input("Enter your password:", type="password")

if password:
    strength, color, suggestions = check_password(password)
    st.markdown(f"### Strength: <span style='color:{color}; font-weight:bold;'>{strength}</span>", unsafe_allow_html=True)
    
    if suggestions:
        st.markdown("### Suggestions to Improve Your Password:")
        st.markdown("\n".join(suggestions))
    else:
        st.markdown("✅ Your password meets all the criteria!")