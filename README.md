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

## Usage

1. **Configure API Keys**:
    - Open `work.py` and replace `'Insert your api key here for chatgpt'` with your actual OpenAI API key.
    - Update the path `"path_to_your_service_account_key"` with the actual path to your Google Cloud service account JSON key file.

2. **Run the Application**:
    ```bash
    python work.py
    ```

3. **Enter YouTube URL**:
    - When prompted, enter the YouTube video URL you want to summarize.
    - The application will download the video, extract audio, transcribe it, and generate a summary.

## Example

```bash
$ python work.py
Please enter the Youtube video URL: https://www.youtube.com/watch?v=example

Transcript:
 [Transcribed text will appear here...]

Summary:
 [AI-generated summary will appear here...]
```

## Features

- ✅ Download audio from YouTube videos
- ✅ Extract audio in WAV format
- ✅ Transcribe audio to text using Google Cloud Speech-to-Text
- ✅ Generate concise summaries using OpenAI GPT models
- ✅ Command-line interface for easy interaction

## Known Issues

The current code has a few bugs that need to be addressed:
- Line 9: `Youtube` should be `YouTube` (case-sensitive)
- Line 33: `langauge_code` should be `language_code` (typo)
- Line 50: `summmary` should be `summary` (typo)
- Line 58: `download_youtube_video()` is missing the `url` parameter
- Function `extract_audio` is defined twice (lines 14-17 and 19-22)

## Troubleshooting

### Authentication Errors
- Ensure `GOOGLE_APPLICATION_CREDENTIALS` environment variable is set correctly
- Verify your OpenAI API key is valid and has sufficient credits

### Audio Processing Issues
- Make sure ffmpeg is installed for audio format conversion:
    ```bash
    # Ubuntu/Debian
    sudo apt-get install ffmpeg
    
    # macOS
    brew install ffmpeg
    
    # Windows
    # Download from https://ffmpeg.org/download.html
    ```

### Import Errors
- Ensure all dependencies are installed:
    ```bash
    pip install pytube pydub google-cloud-speech openai
    ```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

See [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [pytube](https://github.com/pytube/pytube) - For YouTube video downloading
- [pydub](https://github.com/jiaaro/pydub) - For audio processing
- [Google Cloud Speech-to-Text](https://cloud.google.com/speech-to-text) - For audio transcription
- [OpenAI](https://openai.com/) - For text summarization

## Support

If you encounter any issues or have questions, please file an issue on the GitHub repository.
