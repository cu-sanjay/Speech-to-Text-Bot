# Telegram Speech-to-Text Bot

This Telegram bot is designed to generate text from speech. Users can send voice messages to the bot, and it will convert the audio into text, providing users with a written transcription of the spoken content. The bot leverages the power of speech recognition services to achieve this functionality.
The main motive behind creating this bot is to enhance accessibility and improve communication for users who prefer reading text over listening to audio messages. By providing an automated way to transcribe voice messages into text, this bot aims to make communication more inclusive and convenient for all users.

## Features

1. **Speech-to-Text Conversion**: Users can send voice messages to the bot, and it will use a Speech-to-Text service to convert the audio into text.

2. **Real-time Transcription**: The bot generates text from the voice message in real-time and responds with the transcribed text shortly after the message is received.

3. **Multi-language Support**: The Speech-to-Text service used by the bot supports multiple languages, enabling users to transcribe voice messages in various languages.

4. **Accurate Transcription**: The bot aims to provide accurate and reliable transcriptions, but the accuracy may vary based on the quality of the audio and the performance of the underlying Speech-to-Text service.

## Getting Started

To set up and run the Telegram Speech-to-Text Bot:

1. Clone this repository to your local machine.

2. Ensure you have Python installed, and it is recommended to use a virtual environment for dependencies.

3. Install the required packages using the provided `requirements.txt` file:
   ```python
   pip install -r requirements.txt
   ```

4. Obtain your Telegram bot token by creating a new bot with the [BotFather](https://t.me/BotFather) on Telegram.

5. Sign up for a Speech-to-Text service and obtain the necessary credentials (API key, etc.).

6. Open the `config.py` file and replace `'YOUR_TELEGRAM_BOT_TOKEN'` with your actual bot token. Also, add the Speech-to-Text service credentials to the configuration.

7. Run the bot using the following command:
      ```python
      python bot.py
      ```

## Usage

Once the bot is up and running, users can interact with it in the following way:

1. Send a voice message to the bot.

2. The bot will process the voice message using the configured Speech-to-Text service and respond with the transcribed text.

## Bot Commands and Their Working

The Telegram Speech-to-Text Bot supports the following commands and functionalities:

1. `/start`: The `/start` command initiates the bot and displays a welcome message to the user.

2. `/help`: The `/help` command provides a brief explanation of how to use the bot and lists available commands.

3. `/link <URL>`: The `/link` command allows users to download a file from a given link. Replace `<URL>` with a valid URL. The bot will download the file and send it as a document to the chat.

4. `/makefile`: The `/makefile` command enables "File Make Mode." In this mode, users can create a text file by sending a series of text messages. The first line of the text will be taken as the file name, and the subsequent text will be saved as the file content. Once the file is created, the bot will send it as a document to the chat.

5. `/cancel`: The `/cancel` command cancels the "File Make Mode" if it is enabled, allowing the user to abort the file creation process.
   
   ![image](https://github.com/cu-sanjay/Speech-to-Text-Bot/assets/96792511/807dc91d-0662-4573-b879-be53fe2abe92)


6. Sending a Voice Message: Users can simply send a voice message to the bot, and it will convert the audio into text using the configured Speech-to-Text service. The bot will then respond with the transcribed text.


## Contribution

If you find any issues or have ideas for improvements, please feel free to contribute! Submit a pull request or open an issue in this repository. Your contributions are valuable and can help improve the bot's functionality.

## License

This project is licensed under the GNU General Public License v2.1 (GPL-2.1). You can use, modify, and distribute the code following the terms of the license.

## Disclaimer

This bot is an independent project and has no official affiliation with Telegram or any Speech-to-Text service providers. The accuracy of the transcriptions may vary based on the Speech-to-Text service used and the quality of the audio. Use the bot responsibly and be mindful of data privacy and legal considerations when processing voice messages. The developers are not responsible for any misuse or damages caused by the use of this bot.

---

Thank you for using the Telegram Speech-to-Text Bot! If you have any questions or need assistance, feel free to contact me. I hope this bot enhances your communication experience on Telegram! 🤖🎙️
