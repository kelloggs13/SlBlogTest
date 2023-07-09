
import streamlit as st
from googletrans import Translator # from: pip install googletrans==3.1.0a0
import pipreqs as req



def translate_text(txt_in, src="de", dest="en"):
    txt_out = Translator().translate(txt_in, src=src, dest=dest).text
    return txt_out

st.set_page_config(page_title="Stories & Tidbits related to Data Analysis, R and Python"
                   , layout="wide"
                   )

tab_about, tab_blog = st.tabs(["About Me", "Blog"])

with tab_about:
    with st.container():
        p_language_emojy = st.radio(" ", options=["🍔", "🥨", "🍕", "🍱", "✡️"], horizontal=True)
        if p_language_emojy == "🍔":
            p_language = "en"
        if p_language_emojy == "🥨":
            p_language = "de"
        if p_language_emojy == "🍕":
            p_language = "it"
        if p_language_emojy == "🍱":
            p_language = "ja"
        if p_language_emojy == "✡️":
            p_language = "he"

    with st.container():
        txt_cv_line_1 = translate_text("Good to have you here. I use this blog as a collection of small stories related to data analytics and R."
                                , src="en"
                                , dest=p_language)
        txt_cv_line_2 = translate_text("It is created using R markdown and distill, and then published via netlify"
                                , src="en"
                                , dest=p_language)
        txt_cv_line_3 = translate_text("If you have any comments or feedback you can reach me via Linkedin."
                                , src="en"
                                , dest=p_language)
        
        st.write(txt_cv_line_1)
        st.write(txt_cv_line_2)
        st.write(txt_cv_line_3)


with tab_blog:
    st.markdown("blog")




