# ODEkit

**ODEkit** is a lightweight Python package for solving and visualizing ordinary differential equations, especially tailored for physics students and educators.

## Features
- Elegant interface with `solve_ivp` from SciPy
- Prettified visualizations using `matplotlib`
- Educational examples (like simple harmonic motion)
- Built-in testing for reliability

## Installation
```bash
pip install git+https://github.com/ayush-thecoder/ODEkit.git
```

## Quickstart Example
```python
from easyode import EasyODE
import numpy as np

def oscillator(t, y):
    x, v = y
    return [v, -x]

solver = EasyODE(oscillator, (0, 10), [1, 0], t_eval=np.linspace(0, 10, 500))
solver.solve()
solver.plot(labels=["Displacement", "Velocity"])
```

## License
This project is licensed under the MIT License.

## Author
Developed by Ayush Yadav
