# Digital Line Coding Techniques - Implementation and Visualization

This project provides Python implementations of several common digital line coding techniques used to convert binary data into digital signals suitable for transmission. It also includes a visualization component using Matplotlib to display the resulting waveforms.


## Overview

The core logic resides in `digital_data_to_signal.py`, which defines the `dataToSignal` class. This class takes a binary string as input and offers methods to generate signal representations based on different encoding schemes.

The `gui.py` file uses the `dataToSignal` class and `matplotlib` to generate plots of these waveforms, making it easy to visualize and compare the different techniques.

The `main.py` script demonstrates how to use these classes, generating and plotting signals for a sample binary string (`101000110` by default).



## Features

* Implements the following line coding schemes:
    * **NRZ (Unipolar Non-Return-to-Zero):** Represents '1' with a positive voltage (`V`) and '0' with zero voltage.
    * **NRZ-L (Non-Return-to-Zero Level):** Represents '1' with one voltage level (e.g., `+V`) and '0' with the opposite level (e.g., `-V`).
    * **NRZ-I (Non-Return-to-Zero Inverted):** A '1' bit causes a transition (inversion) in the signal level at the beginning of the bit interval. A '0' bit causes no transition. (Optionally configurable for inversion on '0').
    * **Manchester:** Guarantees a mid-bit transition for clock recovery.
        * G.E. Thomas convention (default): '0' -> Low-to-High transition, '1' -> High-to-Low transition.
        * IEEE 802.3 convention (optional): '0' -> High-to-Low transition, '1' -> Low-to-High transition.
    * **Differential Manchester:** Combines elements of NRZ-I and Manchester. Always has a mid-bit transition. A '0' bit causes an additional transition at the beginning of the bit interval, while a '1' does not.
* Visualizes the generated signals using Matplotlib.
* Allows customization of the voltage level (`V`).

## Usage

### Installation
To use the project, you'll need Python installed along with these dependencies:
- numpy
- matplotlib

You can install them using pip:
```bash
pip install numpy matplotlib
```

### Quickstart Guide

#### Step 1: Create a Data Object
```python
# Convert binary string to signal with voltage range ±2V
data = dataToSignal('101000110', V=2)
```

#### Step 2: Plot Signals
Use the `gui` class to visualize signals:
```python
g = gui(mybin=data)

# Plot NRZ and NRZI
g.Plot_list([ ('NRZ', data.NRZ), 
              ('NRZI', data.NRZI) ])

# Plot Manchester encoding
g.plot_Manchester(ieee802dot3=False)
```
### Example Script

```python
# Convert binary string and visualize signals
data = dataToSignal('101000110', V=2)

# Print converted signals
print("NRZ Signal:", data.NRZ())
print("NRZI Signal:", data.NRZI())
print("Manchester Signal (IEEE 802.3 compliant):", data.toManchester(ieee802dot3=True))
print("Differential Manchester Signal:", data.toDifferentailManchester())

# Visualize signals
g = gui(mybin=data)
g.plot_NRZL()
g.plot_NRZI()
g.plot_Manchester()
g.plot_DifferentailManchester()
```


## Code Structure

* `digital_data_to_signal.py`: Contains the `dataToSignal` class with the logic for different line coding schemes.
* `gui.py`: Contains the `gui` class responsible for plotting the signals using Matplotlib. Includes individual plot methods (`plot_NRZ`, `plot_NRZL`, etc.)
* `main.py`: The main execution script that demonstrates the usage of the classes and generates the plots.
* `notes.md`: contains additional notes, explanations and theoretical background about the line coding techniques.
