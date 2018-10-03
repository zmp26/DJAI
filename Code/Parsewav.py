from scipy.io import wavfile
import numpy as np
import os

for filename in os.listdir('/Users/jacobbell/Desktop/DJAI/Wavs/'):
    if filename.endswith('.wav'):
        print(wavfile.read('/Users/jacobbell/Desktop/DJAI/Wavs/'+filename, False))
