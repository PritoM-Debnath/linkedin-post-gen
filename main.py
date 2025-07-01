import streamlit as st
from few_shot import FewShotPosts
from post_generation import generate_post


def main():
    st.title("LinkedIn Post Generator")
    col1, col2, col3 = st.columns(3)
    fs = FewShotPosts()
    length_option = ["Short", "Medium", "Long"]
    language_option = ["English", "Bangla"]

    with col1:
        selected_tag = st.selectbox("Topic", options = fs.get_tags())
    with col2:
        selected_length = st.selectbox("Length", options = length_option)
    with col3:
        selected_language = st.selectbox("Language", options = language_option)

    if st.button("Generate"):
        post = generate_post(selected_tag, selected_length, selected_language)
        st.write(post)

if __name__ == "__main__":
    main()