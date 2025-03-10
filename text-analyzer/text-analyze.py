import streamlit as st

def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

def text_analyzer():
    st.title("📊 Text Analyzer")
    
    # User Input
    text = st.text_area("Enter a paragraph:")
    if not text.strip():
        st.warning("Please enter a valid text.")
        return
    
    # Word & Character Count
    word_count = len(text.split())
    char_count = len(text)
    vowel_count = count_vowels(text)
    
    # Search & Replace
    search_word = st.text_input("Enter a word to search:")
    replace_word = st.text_input("Enter a word to replace with:")
    
    if search_word and replace_word:
        modified_text = text.replace(search_word, replace_word)
        st.subheader("Modified Paragraph:")
        st.write(modified_text)
    
    # Uppercase & Lowercase Conversion
    st.subheader("Text Transformations:")
    st.write("Uppercase:", text.upper())
    st.write("Lowercase:", text.lower())
    
    # Operators Usage
    avg_word_length = char_count / word_count if word_count else 0
    contains_python = "Python" in text
    
    # Results Display
    st.subheader("Text Analysis Results:")
    st.write(f"Total Words: {str(word_count)}")
    st.write(f"Total Characters (including spaces): {str(char_count)}")
    st.write(f"Total Vowels: {str(vowel_count)}")
    st.write(f"Average Word Length: {avg_word_length:.2f}")
    
    if contains_python:
        st.success("✅ The text contains the word 'Python'!")
    else:
        st.error("❌ The text does not contain the word 'Python'.")

if __name__ == "__main__":
    text_analyzer()
