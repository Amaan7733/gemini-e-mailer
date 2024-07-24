import google.generativeai as genai
import os
from dotenv import load_dotenv, find_dotenv 
import streamlit as st

_ = load_dotenv(find_dotenv())
# import os

os.environ["GRPC_VERBOSITY"] = "NONE"


genai.configure(api_key=os.environ.get("GENAI_API_KEY"))



st.title("Gemini Smart e-Mailer")
reciever = st.text_input("Enter Reciever name and resignation")
topic = st.text_input("Please provide the reason to write this e-mail")

prompt = f"""You are an expert in writing a proffessional email. 
I need your help to write a presice email to '{reciever}' . 
The reason to write email is '{topic}' explain the reason in detail. Give some insight also,
 Write an proffessional email to '{reciever}' by describing the reason which is '{topic}'. 
 The email should be in 0 words minimun. You can use lite humour but it does not affect the sencerity of your email. """



gen_btn = st.button("Gen email")
if gen_btn:
    if reciever and topic:
        model = genai.GenerativeModel("gemini-1.5-flash")
        res = model.generate_content(prompt,stream=True)
        for chunk in res:
            # st.text_area("Email",chunk.text, height=500)
            print(chunk.text)
            print("_"*80)
        st.text_area("Email",res.text, height=500)
    else:
        st.text_area("Error", "Please fill the above field to generate the email.")


# print(res.text)