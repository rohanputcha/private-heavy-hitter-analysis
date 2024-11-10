import numpy as np

SAMPLES=10000
MEAN=0
STD_DEV=10

def generate_gaussian_samples(file_name, num_samples, mean=0, std_dev=1):
    samples = np.random.normal(loc=mean, scale=std_dev, size=num_samples)
    int_samples = samples.round().astype(int)

    with open(file_name, 'w') as f:
        for sample in int_samples:
            f.write(f"{sample}\n")

    print(f"Generated {num_samples} samples with mean={mean}, std_dev={std_dev} and saved to {file_name}")



generate_gaussian_samples("../data/gaussian_samples.txt", num_samples=SAMPLES, mean=MEAN, std_dev=STD_DEV)