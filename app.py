import streamlit as st

def add_pauses(text):
    """
    Inserts [[addpause]] tags after commas and periods.
    """
    if not text:
        return ""
    
    # Replace commas and periods with the punctuation + tag
    # We add a space after the tag for readability
    processed_text = text.replace(",", ", [[addpause]]")
    processed_text = processed_text.replace(".", ". [[addpause]]")
    
    return processed_text

# --- App Layout ---
st.set_page_config(page_title="Audio Text Formatter", page_icon="???")

st.title("??? Text to Audio Formatter")
st.write("Paste your script below to automatically insert `[[addpause]]` tags for audio generation.")

# Input Area
raw_text = st.text_area("Input Text", height=200, placeholder="Paste your text here...")

# Processing
if raw_text:
    formatted_text = add_pauses(raw_text)
    
    st.subheader("Formatted Text")
    st.info("Copy the text below:")
    
    # Display as a code block which has a built-in 'copy' button on hover
    st.code(formatted_text, language="text")
    
    # Optional: specialized copy button if the text is very long
    st.download_button(
        label="Download as .txt",
        data=formatted_text,
        file_name="formatted_script.txt",
        mime="text/plain"
    )