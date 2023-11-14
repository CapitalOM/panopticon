import streamlit as st
import pandas as pd
import numpy as np
import time
import os
from dotenv import load_dotenv
from scraper.scraper import PanoptoScraper

load_dotenv()
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

def main():
    st.title('✨Panopticon 💻✨')
    st.subheader('Summarize your Panopto Lecture!')

    with st.form("lecture_form"):
        openai_api_key = st.text_input(label="Enter your OPENAI API Key (from platform.openai.com):", placeholder="sk-...", key="input_api", type="default")

        lecture_url = st.text_input(label="Enter your Panopto Lecture URL:", placeholder="https://harvard.hosted.panopto.com/...", key="input_url", type="default")

        username = st.text_input(label="Enter your HarvardKey email:", placeholder="<email>@college.harvard.edu", key="input_username", type="default")
        password = st.text_input(label="Enter your HarvardKey password:", placeholder="************", key="input_password", type="password")

        st.text("*Note that these are not stored anywhere for security purposes.*")
        submitted = st.form_submit_button("Submit")
        if submitted:
            if (lecture_url == "" or username == "" or password == ""):
                st.text("Error. Please enter all values in the form.")
                return

            credentials = { "username": username, "password": password }

            st.text("Beginning scraping lecture... (wait around 30 seconds)")
            Pscraper = PanoptoScraper(credentials=credentials, url=lecture_url)
            st.text("Check for a DUO push on your phone in ~15 seconds!")
            run_scrape_success = Pscraper.scrape_lecture()

            if (run_scrape_success):
                st.text("Finished scraping lecture!")
                st.text("Generating summary...")
                
                key = openai_api_key or OPENAI_API_KEY

                if (key == ""):
                    st.text("Error. OPENAI API Key needed. Please enter your API key.")
                    return
                
                # summary = "Testing copying ability."
                summary = Pscraper.generate_summary(key)
                st.code(summary)
                return
            else: 
                st.text("Error. Scrapping did not occur. Try again or wait later.")
                return
        
if __name__=="__main__":
    main()




# DATE_COLUMN = 'date/time'
# DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
#             'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

# @st.cache_data
# def load_data(nrows):
#     data = pd.read_csv(DATA_URL, nrows=nrows)
#     lowercase = lambda x: str(x).lower()
#     data.rename(lowercase, axis='columns', inplace=True)
#     data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
#     return data

# data_load_state = st.text('Loading data...')
# data = load_data(10000)
# data_load_state.text("Done! (using st.cache_data)")

# if st.checkbox('Show raw data'):
#     st.subheader('Raw data')
#     st.write(data)

# st.subheader('Number of pickups by hour')
# hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
# st.bar_chart(hist_values)

# # Some number in the range 0-23
# hour_to_filter = st.slider('hour', 0, 23, 17)
# filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

# st.subheader('Map of all pickups at %s:00' % hour_to_filter)
# st.map(filtered_data)