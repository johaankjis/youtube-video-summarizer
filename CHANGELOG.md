# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial project documentation
- README.md with comprehensive setup and usage instructions
- LICENSE file (MIT License)
- CONTRIBUTING.md with contribution guidelines
- CODE_OF_CONDUCT.md for community standards
- SECURITY.md for security policy
- GitHub issue templates for bug reports and feature requests
- GitHub pull request template
- requirements.txt for dependency management

## [1.0.0] - Initial Release

### Added
- YouTube video download functionality using pytube
- Audio extraction from video files using pydub
- Audio transcription using Google Cloud Speech-to-Text API
- Text summarization using OpenAI GPT models
- Command-line interface for user interaction

### Known Issues
- Typo in `work.py` line 9: `Youtube` should be `YouTube`
- Typo in `work.py` line 33: `langauge_code` should be `language_code`
- Typo in `work.py` line 50: `summmary` should be `summary`
- Missing parameter in `work.py` line 58: `url` not passed to `download_youtube_video()`
- Duplicate function definition: `extract_audio` defined twice

[Unreleased]: https://github.com/johaankjis/youtube-video-summarizer/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/johaankjis/youtube-video-summarizer/releases/tag/v1.0.0
