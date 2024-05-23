<h1 align="center">⚔️ Pixels Fighting</h1>

## Description

"Pixels Fighting" is a Python-based visual simulation that uses the Pygame library to create a dynamic grid where each cell (box) can be either "alive" or "dead". The user can choose to input custom colors for the "alive" and "dead" states using HEX values or let the program assign random colors.

## Features

- **Custom Color Input**: Users can choose to enter custom HEX color values for the "alive" and "dead" states of the cells.
- **Random Color Assignment**: If no custom colors are provided, the program assigns random colors to the cells.
- **Dynamic Grid Simulation**: A grid of cells is displayed, with half of the cells starting as "alive" and the other half as "dead". The state of the cells updates continuously, simulating a simple form of cellular automaton.
- **Error Handling**: The program includes robust input validation, ensuring users provide correct HEX color formats and valid responses to prompts.

## Dependencies
It is required to have python or python3.x installed in your terminal in order to run the code for any information about how to install it visit this website [here](https://docs.python-guide.org/starting/install3/linux/).

### Pygame:

```sh
python3 -m pip install -U pygame --user
```

### NumPy:

```sh
pip install numpy
```

## How to Run

1. Ensure you have Python and Pygame installed.
2. Clone the repository and navigate to the project directory.
3. Run the script:

```sh
python (or python3) pixels_fighting.py
```

## Example
Here's a quick example of how the program runs:

   ```sh
🎨 Do you want to insert custom colors? (yes/no): yes
🌹 Enter the HEX value for 'alive' color (format: #HEX): #FF5733
🥀 Enter the HEX value for 'dead' color (format: #HEX): #333333
 ```

<h1 align="center">Enjoy the show!</h1>
