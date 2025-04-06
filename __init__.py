from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

class EasyODE:
    def __init__(self, deriv_func, t_span, y0, t_eval=None, method='RK45', **kwargs):
        self.deriv_func = deriv_func
        self.t_span = t_span
        self.y0 = y0
        self.t_eval = t_eval
        self.method = method
        self.kwargs = kwargs
        self.solution = None

    def solve(self):
        try:
            self.solution = solve_ivp(
                self.deriv_func,
                self.t_span,
                self.y0,
                t_eval=self.t_eval,
                method=self.method,
                **self.kwargs
            )
            if not self.solution.success:
                raise RuntimeError("ODE solver failed: " + self.solution.message)
        except Exception as e:
            raise RuntimeError(f"Failed to solve ODE: {e}")
        return self.solution

    def plot(self, labels=None, title="ODE Solution", xlabel="Time", ylabel="Values"):
        if self.solution is None:
            raise ValueError("You need to call solve() before plotting.")
        plt.figure(figsize=(10, 6))
        for i in range(len(self.solution.y)):
            plt.plot(self.solution.t, self.solution.y[i], label=labels[i] if labels else f'y{i}')
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()
