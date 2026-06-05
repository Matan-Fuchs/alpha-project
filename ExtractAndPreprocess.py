from moabb.datasets import BNCI2014_001
from moabb.paradigms import MotorImagery

dataset = BNCI2014_001()    # download the data
dataset.subject_list = [1]  # only for the first subject

paradigm = MotorImagery(    # preprocessing settings
    n_classes = 2,          # binary filter: to only right hand vs left hand
    fmin = 8.0, fmax = 32.0, # bandpass: only take signals whose frequency is in the relevant domain
    tmin = 0.5, tmax = 2.5) # epoch: divide into time windows
X, y, metadata = paradigm.get_data(dataset = dataset, subjects = [1]) # apply preprocessing
print(f"data shape: {X.shape}") # print processed data
