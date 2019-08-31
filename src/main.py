import re
from os import listdir
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
from scipy.stats import circstd

# declare main data directories
measured_directory = 'data/measured/'
truth_directory = 'data/truth/'

# load all files in data directory (measured is enough for our algorithm)
files = listdir(measured_directory)

for file in files:

    # file number to fetch the correct corresponding file
    file_number = (re.findall('\d+', file))

    # Load measure components
    file_name = measured_directory + file
    I_stream, Q_stream, sensor_phase_bias = np.load(
        file_name, allow_pickle=True, encoding='bytes')

    # load ground truth phase
    file_name = truth_directory + \
        'data_phase_ground_truth_' + file_number[0] + '.npy'
    phase_groundtruth = np.load(file_name)

    # The original basic datapath applied to data
    measured_phase = -np.arctan2(Q_stream, I_stream)  # compute phase
    filtered_phase = []

    # Filter noise in phase images
    for image in measured_phase:
        filtered_phase.append(ndimage.gaussian_filter(image, 4))
    filtered_phase = np.asarray(filtered_phase)

    # Compute noise and error
    phase_error = np.mean(filtered_phase - phase_groundtruth, axis=0)
    phase_noise = circstd(filtered_phase, axis=0)

    # Report phase error and noise
    fig = plt.figure()
    plt.imshow(phase_error)
    plt.title("phase error")
    plt.colorbar()
    fig.savefig("results/error/phase_error_report_" + file_number[0])

    fig = plt.figure()
    plt.imshow(phase_noise)
    plt.colorbar()
    plt.title("phase noise")
    fig.savefig("results/noise/phase_noise_report_" + file_number[0])


class classname(object):
    pass
