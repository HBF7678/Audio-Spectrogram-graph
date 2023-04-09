import tkinter as tk    
from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
from scipy import signal

class AudioSpectrogram:
    def __init__(self, root):
        self.root = root
        self.file_path = tk.StringVar()

        # Creating the GUI
        self.create_widgets()

    def create_widgets(self):
        # Creating the main frame
        frame = tk.Frame(self.root)
        frame.pack()
    
        # Creating the open file button
        open_file_button = tk.Button(frame, text="Open File", command=self.open_file)
        open_file_button.pack()

        # Creating the plot button
        plot_button = tk.Button(frame, text="Plot", command=self.plot)
        plot_button.pack()

    def open_file(self):
        # Opening the file dialog to select the audio file
        self.file_path.set(filedialog.askopenfilename())

    def plot(self):
        # Loading the audio file
        sample_rate, samples = wavfile.read(self.file_path.get())

        # Calculating the spectrogram using signal.spectrogram() function
        frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate)

        # Plotting the spectrogram using matplotlib.pyplot.pcolormesh() function
        plt.pcolormesh(times, frequencies, np.log10(spectrogram))
        plt.ylabel('Frequency [Hz]')
        plt.xlabel('Time [sec]')
        plt.show()

# Creating the main window
root = tk.Tk()
root.title("Audio Spectrogram")
root.geometry("300x100")

# Creating the AudioSpectrogram object
audio_spectrogram = AudioSpectrogram(root)

# Running the main loop
root.mainloop()