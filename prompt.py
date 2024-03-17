## loading all the environment variables
from dotenv import load_dotenv
load_dotenv() 

# Import Important libraries
import streamlit as st
import google.generativeai as genai
import os

# Configure Google API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Set up the Model
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
},
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

# Load Gemini Pro model
model = genai.GenerativeModel(model_name="gemini-pro", generation_config=generation_config, safety_settings=safety_settings)


# Navbar
st.set_page_config(
    page_title="Prompt Generator",
    page_icon="👨‍🎓",
    layout="centered",
    initial_sidebar_state="collapsed",
)



# title of our app
#st.title('✍️ AI Prompt Engineer')

# Add the Title
st.markdown(
    "<h1 style='text-align: center; color: black;'>"
    "✨ AI Prompt Engineer"
    "</h1>",
    unsafe_allow_html=True
)


# create a subheader
#st.subheader("You can generate any type of Prompt for your blog or any other purpose. 🤖")

# create a subheader
st.markdown('''
<style>
h3 {
    font-family: 'Open Sans', sans-serif;
    font-size: 16px;
    line-height: 24px;
    margin-top: 0;
    margin-bottom: 24px;
}
</style>
<h3 style="text-align: center; color: black;">🔥 Make Your Creativity Shine with AI Prompt Engineer! 🔥<br />Generate prompts for blogs, social media, content marketing, and more!</h3>
''', unsafe_allow_html=True)

# sidebar for the user input

with st.sidebar:
    st.title("Input Settings")
    st.subheader("Enter Details for the Section")
    
    # Topic
    topic = st.text_input("Topic: What is the topic of the prompt? Eg: python, machine learning,..")
    
    # Goal
    task = st.text_area(" Task: What do you want to achieve with the prompt? Eg: writing a blog, analyzing a text,..")
    
    # Add the Voice Tones
    voice_tones = st.sidebar.selectbox("Choose Voice Tones:", ["Formal","Friendly", "Bold", "Adventurous", "Witty", "Professional", "Casual", "Informative", "Creative", "Trendy", "Caring", "Cheerful", "Excited", "Funny", "Sad", "Serious", "Tense", "Vulnerable", "Angry", "Surprised", "Worried", "Assertive", "Confident", "Cooperative", "Encouraging" ])
    
    # Add the Writing Styles
    writing_styles = st.sidebar.selectbox("Choose Writing Styles:", ["Academic", "Conversational", "Creative", "Critical", "Descriptive", "Instructive", "Technical", "Analytical","Business", "Causal", "Emotional", "Expository", "Formal", "Informal", "Legal", "Medical", "Poetic", "Persuasive"])
    
    # Audience
    audience = st.selectbox("Audience: [Who is the target audience?]", ["Teenager", "Adult", "20-years-old", "30-years-old",  "40-years-old", "50-years-old", "Senior", "Everyone", "Uninformed Audience", "Neutral Audience", "Business Audience", "Researcher", "Expert Audience", "My Boss", "My Student", "My Teacher", "My Family", "My Friends", "My Colleagues"] )
    
    # Word Counter
    word_count = st.number_input("Word Count", min_value=10, max_value=3000, step=100)
    
    # Character Counter
    character_count = st.number_input("Character Count", min_value=10, max_value=3000, step=100)
    
    # Prompt Context
    prompt_context = st.text_area("Prompt Context: Provide a brief context or situation where the prompt will be used (optional)")
    
    # Example prompt
    example_prompt = st.text_area("Example prompt: Provide an example of a prompt that you would like your generated prompts to be similar to (optional)")
    
    

    # Prompt
    prompt_parts = [
            f"""
            Act as a Prompt Engineer, To create an AI prompt, start by defining your goal and gathering data. Next, write a clear, concise prompt that will guide the AI you' re using to generate the output you desire. Generate an effective AI prompt is a critical to obtaining the expected results out of language models like ChatGPT, GPT-3, Gemini etc.  Finally, test and iterate on your prompt until you achieve the desired results. With a little bit of southern patience and some New Yorker creativity, you'll have an amazing AI prompt that can help you automate tasks and enhance your workflows!
            Follow these guidelines:

            Clarity: Ensure that the prompt is clear, concise, and direct. This increases the likelihood that the AI will understand what you are asking and generate an appropriate response.
            Context: The more specific and contextual your prompt, the better the large language model can generate relevant responses. If you're looking for a specific type of response, include that information in your prompt.
            Completeness: Provide as much relevant information as possible to help guide the AI. If there are crucial details about the scenario or question that the AI wouldn't know, make sure to include them.
            Instruction: If you want a particular style or format for the response, specify this in the prompt. For instance, if you want a response in the form of a poem, bullet points, or formal language, indicate this.
            Open-ended vs. Closed-ended: If you're looking for creative or expansive responses, use open-ended questions. For more specific, concise answers, use closed-ended questions.
            
            Goal: {task} {topic} {voice_tones} {audience} {writing_styles} of {word_count} words and {character_count} characters optional.
            Prompt Context: Provide a brief context or situation where the prompt will be used {prompt_context}  
            Example prompt: Provide an example of a prompt that you would like your generated prompts to be similar to {example_prompt}
            
            Based on the context and example prompt, write an effective AI prompt that will guide the AI you're using to generate the output you desire.
            
            
            """
            ]

    # Submit Button
    submit_button = st.button("Generate")

    # Clear All Button
    clear_button = st.button("Clear All")

if submit_button:
    # Display the spinner
        # Generate the response
        response = model.generate_content(prompt_parts)

        # Display the blog output
        st.write(response.text)
        
        
        
# Adding the HTML footer
# Profile footer HTML for sidebar


# Render profile footer in sidebar at the "bottom"
# Set a background image
def set_background_image():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://images.pexels.com/photos/4097159/pexels-photo-4097159.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1);
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

set_background_image()

# Set a background image for the sidebar
sidebar_background_image = '''
<style>
[data-testid="stSidebar"] {
    background-image: url("https://www.pexels.com/photo/abstract-background-with-green-smear-of-paint-6423446/");
    background-size: cover;
}
</style>
'''

st.sidebar.markdown(sidebar_background_image, unsafe_allow_html=True)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Custom CSS to inject into the Streamlit app
footer_css = """
<style>
.footer {
    position: fixed;
    right: 0;
    bottom: 0;
    width: auto;
    background-color: transparent;
    color: black;
    text-align: right;
    padding-right: 10px;
}
</style>
"""


# HTML for the footer - replace your credit information here
footer_html = f"""
<div class="footer">
    <p>Developed by: Farhan Akbar</p>
    <a href="https://www.linkedin.com/in/farhan-akbar-ai/"><img src="https://img.shields.io/badge/LinkedIn-Profile-blue?style=for-the-badge&logo=linkedin" alt="LinkedIn"/></a>
    <a href="mailto:rasolehri@gmail.com"><img src="https://img.shields.io/badge/Email-Contact%20Me-red?style=for-the-badge&logo=email" alt="Email"/></a>
    <a href="https://github.com/"><img src="https://img.shields.io/badge/GitHub-Profile-blue?style=for-the-badge&logo=github" alt="GitHub"/></a>
</div>
"""

# Combine CSS and HTML for the footer
st.markdown(footer_css, unsafe_allow_html=True)
st.markdown(footer_html, unsafe_allow_html=True)


