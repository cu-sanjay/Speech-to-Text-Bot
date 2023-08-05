from pydub import AudioSegment
import os
import config

def process_voice_message(audio_file_path):
    """
    Process the voice message audio file, convert to WAV format if needed, and transcribe using the Speech-to-Text service.

    :param audio_file_path: Path to the voice message audio file.
    :return: Transcribed text or an error message if processing fails.
    """
    try:
        # Convert the audio to WAV format (if needed) for compatibility with the Speech-to-Text service
        audio = AudioSegment.from_file(audio_file_path)
        if audio.frame_rate != 16000:  # Sample rate for Google's Web Speech API
            audio = audio.set_frame_rate(16000)

        wav_audio_file = os.path.splitext(audio_file_path)[0] + ".wav"
        audio.export(wav_audio_file, format="wav")

        # Perform speech-to-text using the Speech-to-Text service
        text = config.speech_to_text.recognize_speech_from_audio(wav_audio_file, language=config.SPEECH_TO_TEXT_LANGUAGE)

        # Clean up temporary WAV file
        os.remove(wav_audio_file)

        return text
    except Exception as e:
        print(f"Audio processing error: {e}")
        return "Error: Audio processing failed."
