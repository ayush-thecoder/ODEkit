import unittest
import numpy as np
from easyode import EasyODE

class TestEasyODE(unittest.TestCase):
    def test_simple_harmonic_oscillator(self):
        def sho(t, y):
            x, v = y
            return [v, -x]

        solver = EasyODE(
            sho,
            (0, 2 * np.pi),
            [1, 0],
            t_eval=np.linspace(0, 2 * np.pi, 1000)
        )
        result = solver.solve()

        self.assertIsNotNone(result)
        max_displacement = np.max(np.abs(result.y[0]))
        self.assertAlmostEqual(max_displacement, 1, delta=0.05)
        self.assertEqual(len(result.t), 1000)
        self.assertEqual(result.y.shape[1], 1000)
        self.assertTrue(result.success)

    def test_invalid_solve(self):
        def bad_func(t, y):
            return "not valid"

        solver = EasyODE(bad_func, (0, 1), [0])
        with self.assertRaises(RuntimeError):
            solver.solve()

if __name__ == '__main__':
    unittest.main()
