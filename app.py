import streamlit as st
from cipher import caesar_cipher

#Configuration of the page
st.set_page_config(
    page_title="Caesar Cipher",
    page_icon="🔐",
    layout="centered"
)

#sidebar controls
with st.sidebar:
    st.header("SETTINGS")
    shift = st.number_input(
        "Shift Value (1-26)",
        min_value=1,
        max_value=26,
        value=3,
        step=1,
        help="Must be between 1 and 26"
    )
    mode = st.radio("Operation", ["Encrypt", "Decrypt"])

#main interface
st.title("🔐 The Caesar Cipher Interactive Tool")
text = st.text_area("Enter Your Message:", height=150)

if st.button("Process Text"):
    if text.strip():
        with st.spinner(f"{mode}ing..."):
            result = caesar_cipher(
                text,
                shift,
                mode.lower()
            )

            st.success("DONE!")
            st.subheader("Result:")
            st.code(result)
    else:
        st.error("Please enter some text!")