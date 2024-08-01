import os
from utils import utils
import streamlit as st
from PIL import Image
from topicsimplifier import ComplexTopicSimplifier, VisulaGeneration
from dotenv import load_dotenv; load_dotenv()


# Setup your config
utils.page_config()
utils.style_app()


# Load and display the logo
image = Image.open("./logo/lyzr-logo.png")
st.image(image, width=150)

# App title and introduction
st.title("Complex Topic Simplifier")
st.markdown("The Complex Concept Simplifier app leverages Lyzr.ai to break down intricate ideas into clear, concise explanations tailored to various audiences, complete with relatable examples and analogies.")

# Setting up the sidebar for input
st.sidebar.title("Complex Topic Simplifier")
API_KEY = st.sidebar.text_input(label="API Key",placeholder='OpenAI API Key', type="password")

st.sidebar.markdown('---')
utils.template_end()
utils.social_media()

if API_KEY != "":
    Topic = st.text_area(label='Enter your Concept/Topic', placeholder='Write your concept or topic')
    Level = st.selectbox(label="Select Target Audience", options=["","Beginner", "Intermedite"])
    if (Topic and Level) != "":
        if st.button('Submit'):
            simplifiedConcept = ComplexTopicSimplifier(apikey=API_KEY, topic=Topic, audience=Level)
            EXPLAINATION = simplifiedConcept[0]['task_output']
            # visual = VisulaGeneration(apikey=API_KEY,explanation=Topic)
            # VISUAL = visual[0]['task_output'].local_file_path
            st.markdown('---')
            st.write(EXPLAINATION)
            # st.image(VISUAL)


