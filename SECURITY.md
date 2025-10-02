# Security Policy

## Supported Versions

We release patches for security vulnerabilities. Currently supported versions:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |

## Reporting a Vulnerability

If you discover a security vulnerability within YouTube Video Summarizer, please send an email to the repository maintainers via GitHub. All security vulnerabilities will be promptly addressed.

Please include the following information in your report:

- Type of vulnerability
- Full paths of source file(s) related to the vulnerability
- Location of the affected source code (tag/branch/commit or direct URL)
- Step-by-step instructions to reproduce the issue
- Proof-of-concept or exploit code (if possible)
- Impact of the vulnerability, including how an attacker might exploit it

### What to Expect

- **Acknowledgment**: We will acknowledge your email within 48 hours
- **Updates**: We will keep you informed about the progress toward a fix
- **Disclosure**: We will coordinate with you on the disclosure timeline
- **Credit**: We will give you credit for the discovery (unless you prefer to remain anonymous)

## Security Best Practices

When using this application:

1. **API Keys**: Never commit API keys or credentials to the repository
   - Use environment variables for sensitive data
   - Add `.env` files to `.gitignore`
   - Rotate API keys regularly

2. **Google Cloud Credentials**: 
   - Store service account JSON files securely
   - Never commit credential files to version control
   - Use appropriate IAM roles with minimal required permissions

3. **OpenAI API Key**:
   - Keep your API key confidential
   - Monitor usage to detect unauthorized access
   - Use rate limiting if available

4. **Dependencies**: 
   - Regularly update dependencies to patch known vulnerabilities
   - Use `pip-audit` or similar tools to scan for vulnerable packages

5. **Input Validation**:
   - Be cautious with user-provided YouTube URLs
   - Validate and sanitize all inputs

## Known Security Considerations

- This application downloads content from YouTube, which may be subject to copyright
- Audio files are processed locally, ensure you have sufficient disk space
- API keys are stored in plain text in the code (should be moved to environment variables)
- No input validation is performed on YouTube URLs

## Disclosure Policy

When we receive a security bug report, we will:

1. Confirm the problem and determine affected versions
2. Audit code to find similar problems
3. Prepare fixes for all supported versions
4. Release new security fix versions as soon as possible

Thank you for helping keep YouTube Video Summarizer and its users safe!
