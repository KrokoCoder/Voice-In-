import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

# Initialize the customtkinter application
app = ctk.CTk()
app.geometry("400x200")
app.title("Audio Recorder")

# Define the recording parameters
freq = 44100  # Sampling frequency
duration = 5  # Duration in seconds for the recording

def start_recording():
    # Record audio
    recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
    sd.wait()  # Wait until the recording is finished
    
    # Save the recording temporarily
    write("recording.wav", freq, recording)
    wv.write("recording.wav", recording, freq, sampwidth=2)
    
    # Open file dialog to save the recording
    file_path = filedialog.asksaveasfilename(defaultextension=".wav", filetypes=[("WAV files", "*.wav")])
    if file_path:
        wv.write(file_path, recording, freq, sampwidth=2)
        print("Recording saved at:", file_path)

# Create and place the record button
record_button = ctk.CTkButton(app, text="Start Recording", command=start_recording)
record_button.pack(pady=20)

# Run the application
app.mainloop()
