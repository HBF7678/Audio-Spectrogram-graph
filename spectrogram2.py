import sys
import numpy as np
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
import matplotlib.pyplot as plt
import librosa
import librosa.display
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Audio Spectrogram")

        # Create the main widget
        self.main_widget = QtWidgets.QWidget(self)

        # Create the QLabel for the filepath
        self.label = QtWidgets.QLabel(self)
        self.label.setText("File path:")

        # Create the QLineEdit for the filepath
        self.filepath_text = QtWidgets.QLineEdit(self)

        # Create the QPushButton to browse for the file
        self.browse_button = QtWidgets.QPushButton(self)
        self.browse_button.setText("Browse")
        self.browse_button.clicked.connect(self.browse_file)

        # Create the QPushButton to generate the spectrogram
        self.spectrogram_button = QtWidgets.QPushButton(self)
        self.spectrogram_button.setText("Generate Spectrogram")
        self.spectrogram_button.clicked.connect(self.generate_spectrogram)

        # Create the matplotlib FigureCanvas for the spectrogram
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure) 

        # Create the layout for the main widget
        layout = QtWidgets.QVBoxLayout(self.main_widget)
        layout.addWidget(self.label)
        layout.addWidget(self.filepath_text)
        layout.addWidget(self.browse_button)
        layout.addWidget(self.spectrogram_button)
        layout.addWidget(self.canvas)

        self.setCentralWidget(self.main_widget)
         def browse_file(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '/home')
        self.filepath_text.setText(fname[0])

    def generate_spectrogram(self):
        # Load the audio file
        filepath = self.filepath_text.text()
        y, sr = librosa.load(filepath)

        # Compute the spectrogram
        hop_length = 512
        n_fft = 2048
        S = librosa.stft(y, n_fft=n_fft, hop_length=hop_length)
        S_db = librosa.amplitude_to_db(np.abs(S), ref=np.max)

        # Plot the spectrogram
        ax = self.figure.add_subplot(111)
        librosa.display.specshow(S_db, sr=sr, hop_length=hop_length, x_axis='time', y_axis='log', ax=ax)
        ax.set_title('Log-frequency power spectrogram')
        ax.set_xlabel('Time')
        ax.set_ylabel('Frequency (Hz)')
        self.canvas.draw()
        if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())