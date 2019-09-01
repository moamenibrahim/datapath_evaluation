import re
from os import listdir
from src.datapath_evaluate import DataPathEvaluate

# declare main data directories
measured_directory = 'data/measured/'
truth_directory = 'data/truth/'

# declare a child class
dataPathEvaluate = DataPathEvaluate(measured_directory, truth_directory)

# load all files in data directory (measured is enough for our algorithm)
files = listdir(measured_directory)

for file in files:

    if file.endswith('npy'):

        # file number to fetch the correct corresponding file
        file_number = (re.findall('\d+', file))
        # Load measure components
        I_stream, Q_stream, sensor_phase_bias, phase_groundtruth = dataPathEvaluate.load_components(
            file, file_number)

        # Calculate phase error and noise
        phase_error, phase_noise = dataPathEvaluate.compute_values(
            I_stream, Q_stream, phase_groundtruth)

        # Report phase error and noise
        dataPathEvaluate.report_results(phase_error, phase_noise, file_number)
