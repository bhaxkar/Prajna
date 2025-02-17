# Prajna (प्रज्ञा)
Prajna, the Discord bot powered by Google's Gemini AI that maintains conversation context and provides intelligent responses.

## Features

- Seamless Discord integration using discord.py
- Powered by Google's gemini-2.0-flash model
- Maintains conversation history and context
- Responds to mentions in Discord channels
- UTF-8 support for multilingual conversations

## Technical description

- **Discord Integration**: Built using the `discord.py` library for handling Discord events and messages
- **GEN AI Integration**: Leverages Google's `gemini-2.0-flash` model via the Google Generative AI API
- **Environment Configuration**: Uses dotenv for secure configuration management

## Setup and Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install discord.py python-dotenv google-generativeai 
```
3. Configure environment variables in .env:
- TOKEN: Your Discord bot token
- GOOGLE_API_KEY: Your Google API key for Gemini AI
4. Run the bot:
```bash
python main.py
```
## Usage
- Invite the bot to your Discord server
- Mention the bot (@Prajna) in any channel
- The bot will respond to your message using the Gemini AI model
- Empty mentions will be responded with a greeting message

## Contact 
👾 Bhaskar Jha (✉️ [@bhaxkar](mailto:bhaskarjha.info@gmail.com)  )
