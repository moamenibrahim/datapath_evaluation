import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
from scipy.stats import circstd


class DataPathEvaluate(object):

    def __init__(self, measured_directory, truth_directory):
        self.measured_directory = measured_directory
        self.truth_directory = truth_directory

    def load_components(self, file, file_number):
        # Load measure components
        file_name = self.measured_directory + file
        I_stream, Q_stream, sensor_phase_bias = np.load(
            file_name, allow_pickle=True, encoding='bytes')

        # load ground truth phase
        file_name = self.truth_directory + \
            'data_phase_ground_truth_' + file_number[0] + '.npy'
        phase_groundtruth = np.load(file_name)
        return I_stream, Q_stream, sensor_phase_bias, phase_groundtruth

    def compute_values(self, I_stream, Q_stream, phase_groundtruth):
        '''
        Compute phase error and noise
        '''
        # The original basic datapath applied to data
        measured_phase = -np.arctan2(Q_stream, I_stream)  # compute phase

        # Filter noise in phase images
        filtered_phase = []
        for image in measured_phase:
            filtered_phase.append(ndimage.gaussian_filter(image, 4))
        filtered_phase = np.asarray(filtered_phase)

        # Compute noise and error
        phase_error = np.mean(filtered_phase - phase_groundtruth, axis=0)
        phase_noise = circstd(filtered_phase, axis=0)
        return phase_error, phase_noise

    def report_results(self, phase_error, phase_noise, file_number):
        '''
        Report phase error and noise
        '''
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
