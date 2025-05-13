from whisper_diarization import transcribe_with_diarization

# Path to the audio file you want to test
audio_path = "alpha_meeting_input.mp3"  # Change this to the path of your audio file

# Call the transcription function
transcription = transcribe_with_diarization(audio_path)

# Print the result
for line in transcription:
    print(line)
