# YouTube Video Summarizer

This project is a Python application that converts a YouTube video into text and generates a summary using OpenAI's GPT-3/GPT-4 model. The application performs the following steps:

1. *Download YouTube Video*: Prompts the user for a YouTube video URL and downloads the video using the pytube library.
2. *Extract Audio*: Extracts the audio from the downloaded video and converts it into a WAV file using the pydub library.
3. *Transcribe Audio to Text*: Uses Google Cloud Speech-to-Text API to transcribe the audio into text.
4. *Generate Summary*: Utilizes OpenAI's GPT model to generate a concise summary of the transcribed text.

## Requirements

- Python 3.x
- pytube
- pydub
- google-cloud-speech
- openai

## Setup

1. *Install Required Libraries*:
    bash
    pip install pytube pydub google-cloud-speech openai
    

2. *Google Cloud Setup*:
    - Create a project on Google Cloud Platform.
    - Enable the Speech-to-Text API.
    - Create a service account and download the JSON key file.
    - Set the GOOGLE_APPLICATION_CREDENTIALS environment variable to the path of the JSON key file.

3. *OpenAI Setup*:
    - Obtain an API key from OpenAI.
