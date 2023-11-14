# Panopticon

Panopticon is a LLM-assisted Panopto lecture scraper and summarizer for Harvard students. Compile your lecture into succinct, comprehensive notes within seconds!

> This tool is designed for Harvard Students, since it scrapes the Harvard hosted Panopto server and login. However, it can be relatively easily modified for any school's Panopto server.

## Install

* Clone this repository via `git clone`

* Install the necessary dependencies via
```$ pip install -r requirements.txt```

## Usage

### Locally

* Run `streamlit run app.py` to run the app locally.

    * If you want to use your own OpenAI API key for all to access, create a `.env` file in the root directory with `OPENAI_API_KEY=<your_key>` written in it.

### Cloud Hosted

* Access the application via this [link](https://panopticon.streamlit.app/) hosted by Streamlit Cloud.
