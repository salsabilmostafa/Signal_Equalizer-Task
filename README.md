# Signal_Equalizer-Task

## Overview
This is a python desktop application for signal processing with four different modes: Uniform Range, Musical Instruments, Animal Sounds, and ECG Signals. This application allows users to load signals, visualize them dynamically, analyze their frequencies in the Fourier domain, and manipulate the signal using sliders for frequency components.
## Features
- **Equalizing Modes**
  - Four Modes:
    1. Uniform Range: Manipulate signals in a uniform frequency range with 10 sliders.
    2. Musical Instruments: Analyze and modify musical instrument signals with 4 sliders.
    3. Animal Sounds: Adjust frequency components of animal sounds using 4 sliders.
    4. ECG Signals: Process ECG signals with 4 sliders for arrhythmia components.

- **Signal Visualization**
  - Dynamically plot the input signal.
  - Display Fourier domain representation of the signal.
  - Visualize the output signal after inverse Fourier transformation.
  - Visualize the detailed spectograms of the input and output signals.

- **Frequency Manipulation**
  - Use sliders to remove or amplify specific frequency components.
  - Choose from various smoothing windows: Hanning, Hamming, Rectangular, or Gaussian.


## Demo


https://github.com/salsabilmostafa/Signal_Equilizer-Task/assets/115428975/ed5f09c8-b9dc-4480-ae6a-c5c6ece9cc27


## Usage
1. Clone the repository.
    ```bash
    git clone https://github.com/salsabilmostafa/Signal_Equalizer-Task.git
    ```
2. Run the application.
    ```bash
    python main.py
    ```
3. Launch the application.
4. Choose the desired mode from the menu.
5. Load a signal file (you can use attached files).
6. Explore and manipulate the signal using sliders.
7. Choose a smoothing window for frequency modification.
8. Visualize the signal, Fourier domain, and modified signal.

## Dependencies
Ensure you have the following dependencies installed before running the application:
- Python 3.7 or above
- PyQt5
- pyqtgraph
- datetime
- pandas
- numpy
- wfdb
- matplotlib
- sys
- scipy
- os

## Contributions
Contributions are welcome! If you find any bugs or have suggestions for improvements, feel free to open an issue or submit a pull request.
