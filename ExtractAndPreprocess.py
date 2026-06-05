from moabb.datasets import BNCI2014001
dataset = BNCI2014001()
dataset.subject_list = [1]
from moabb.paradigms import MotorImagery
paradigm = MotorImagery(
    n_classes = 2,
    fmin = 8.0, fmax = 32.0,
    tmin = 0.5, tmax = 2.5)
X, y, metadata = paradigm.get_data(dataset = dataset, subjects = [1])
print(f"data shape: {X.shape}")