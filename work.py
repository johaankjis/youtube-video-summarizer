from pytube import YouTube
from pydub import AudioSegment
import os
from google.cloud import speech
from google.cloud.speech import enums, types
import openai


def download_youtube_video(url):
    yt = YouTube(url)
    video = yt.streams.filters(only_audio=True).first()
    out_file = video.download(output_path=".")
    return out_file


def extract_audio(file_path):
    audio = AudioSegment.from_file(file_path)
    audio.export("audio.wav", format="wav")
    return "audio.wav"


def transcribe_audio(audio_path):
    client = speech.SpeechClient()
    with open(audio_path, 'rb') as audio_file:
        content = audio_file.read()

    audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code='en_US'
    )

    response = client.recognize(config=config, audio=audio)

    transcript = ""
    for result in response.results:
        transcript += result.alternatives[0].transcript + " "

    return transcript.strip()


def summarize_text(text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Summarize the following text:\n\n{text}",
        max_tokens=150
    )
    summary = response['choices'][0]['text'].strip()
    return summary


def main():
    openai.api_key = 'Insert your api key here for chatgpt'
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = \
        "path_to_your_service_account_key"

    url = input("Please enter the Youtube video URL: ")
    video_path = download_youtube_video(url)
    audio_path = extract_audio(video_path)
    transcript = transcribe_audio(audio_path)
    summary = summarize_text(transcript)

    print("\nTranscript:\n", transcript)
    print("\nSummary:\n", summary)


if __name__ == "__main__":
    main()
