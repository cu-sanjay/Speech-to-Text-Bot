import speech_recognition as sr
import config

class SpeechToText:
    def __init__(self):
        # Create a SpeechRecognition recognizer instance
        self.recognizer = sr.Recognizer()

    def recognize_speech_from_audio(self, audio_file_path, language='en-US'):
        """
        Recognizes speech from an audio file using the SpeechRecognition library.

        :param audio_file_path: Path to the audio file to be transcribed.
        :param language: Language code for the desired transcription language (default: 'en-US').
        :return: Transcribed text or None if the transcription fails.
        """
        try:
            with sr.AudioFile(audio_file_path) as source:
                self.recognizer.adjust_for_ambient_noise(source)
                audio_data = self.recognizer.record(source)
                text = self.recognizer.recognize_google(audio_data, language=language)
                return text
        except sr.UnknownValueError:
            return None
        except sr.RequestError as e:
            print(f"Speech recognition service error: {e}")
            return None

# Instantiate the SpeechToText class
speech_to_text = SpeechToText()
