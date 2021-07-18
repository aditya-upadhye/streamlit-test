import streamlit as st
# This is the title part
st.title("First Tutorial")
# This is the header part
st.header("The header part")
# This is the subheader part
st.subheader("The subheader part")
# The text part
st.text("This is the first line of the body")

# Let try markdown
st.markdown("## This is a Markdown")

# Lets try some colorful text

st.success("Your work is done!!!!")

st.info("Once again think about it")

st.warning("You think really work is done?")

st.error("Yes, confirm. Work is not done")

st.exception("Exception raised (The name 'hashtag' is not defined)")

# Writing a text

st.write("Text using write function")


# Importing Image
from PIL import Image
img = Image.open("Error.jpg")
st.image(img, width=300)

# Importing Video
# vid_file = open("Day 27.mp4", "rb").read()
# st.video(vid_file)

# Importing Audio
# audio_file = open("examplemusic.mp3", "rb").read()
# st.audio(audio_file, format = 'audio/mp3')

# Widget
# Checkbox 
if st.checkbox("Show/Hide"):
    st.text("Showing or Hiding widget")

# Radio Button
status = st.radio("What is your status?", ("Active", "Inactive"))
if status == "Active":
    st.success("You are Active!!!")
else:
    st.error("You are Inactive. Active Now.")

# Select Box
Occupation = st.selectbox("Your Occupation", ["Programmer", "Doctor", "Chartered Accountant", "Businessman"])
st.write(f"You selected {Occupation}")

# Multi Select 
multioption = st.multiselect("Choose multiple options : ", ["Option 1", "Option 2", "Option 3", "Option 4"])
st.write("You selected ", len(multioption), "options")

# Slider 
level = st.slider("What is your level?", 1, 5)

# Button
st.button("Simple Button")

if(st.button("About")):
    st.text("You pressed the Simple Button")

# Text Input 
firstname = st.text_input("Enter Your Firstname", "Type here.... ")
if st.button("Submit"):
    result = firstname.title()
    st.success(result)

# Text Area
message = st.text_area("Enter Your message", "Type here.... ")
if st.button("Submit message"):
    result = message.title()
    st.success(result)

# Date Input 
import datetime 
today = st.date_input("Today is ", datetime.datetime.now())

the_time = st.time_input("The time is ", datetime.time())

# Displaying JSON
st.text("Display JSON")
st.json({'name' : "Aditya", 'gender' : "Male"})

# Display Raw Code
st.text("Display Raw Code")
st.code ("import numpy as np")

# Display Raw Code 
with st.echo():
    # This will also show as a comment 
    import pandas as pd
    df = pd.DataFrame()

# Progress Bar
import time
my_bar = st.progress(0)
for p in range(10):
    my_bar.progress(p + 1)

# Spinner
with st.spinner("Waiting ..."):
    time.sleep(5)
st.success("Finished!")

st.balloons()

# Sidebars
st.sidebar.header("About")
st.sidebar.text("This is Streamlit Tutorial")

# Functions
@st.cache
def run_fxn():
    return range(100)

st.write(run_fxn())

#Plot 
st.pyplot()

# DataFrames
st.dataframe(df)

# Tables
st.table(df)