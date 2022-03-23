# KuramotoParameters

Python code for calculating the two Kuramoto parameters (magnitude and phase) for measuring synchrony in oscillators.

# How to use

```python
import numpy as np
from kuramoto import get_kuramoto_params

example_array = np.array([10, 15, 18, 13, 8])

mag, phase = get_kuramoto_params(example_array)

print(mag, phase)

0.6195402848152863 4.5174977155034854

```

Below is a figure from our paper where we apply this method to investigate circadian rhythm synchrony over time in plants (https://www.biorxiv.org/content/10.1101/2022.01.11.475783v1)

![ezcv logo](https://raw.githubusercontent.com/AHallLab/KuramotoParameters/master/example_data/Synchrony.png)
