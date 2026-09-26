import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="EduGenie - Vetri Thiran", page_icon="🎓")
st.title("🎓 EduGenie - AI Learning Assistant")
st.subheader("Vetri-Thiran Payirchi Thittam")

api_key = st.sidebar.text_input("Gemini API Key", type="password", help="aistudio.google.com la free ah kedaikum")
if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    question = st.text_input("Un Kelvi Enna? / Your question:")
    if st.button("Ask EduGenie 🚀"):
        if question:
            with st.spinner("Yosikiren da... 🤔"):
                try:
                    response = model.generate_content(f"You are EduGenie, helpful Tamil Nadu skill training assistant. Answer in Tanglish simply: {question}")
                    st.success(response.text)
                except Exception as e:
                    st.error(f"Error da: {e}")
        else:
            st.warning("Kelvi type pannu da!")
else:
    st.info("👈 Sidebar la Gemini API Key podu da!")

st.sidebar.markdown("---")
st.sidebar.write("✅ Epic 1: Setup Done")
st.sidebar.write("✅ Epic 2: UI Done")
st.sidebar.write("✅ Epic 3: AI Logic Done")
st.sidebar.write("✅ Epic 4: Deploy Ready")
