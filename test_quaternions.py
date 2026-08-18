import unittest
import math
from quaternions import Quaternions


class TestQuaternions(unittest.TestCase):
    def setUp(self):
        self.q1 = Quaternions(1, 2, 3, 4)
        self.q2 = Quaternions(5, 6, 7, 8)
        self.zero = Quaternions(0, 0, 0, 0)
        self.real = Quaternions(5, 0, 0, 0)

        # The basis vectors
        self.i = Quaternions(0, 1, 0, 0)
        self.j = Quaternions(0, 0, 1, 0)
        self.k = Quaternions(0, 0, 0, 1)

    def test_init_and_attributes(self):
        self.assertEqual(self.q1.a0, 1)
        self.assertEqual(self.q1.a1, 2)
        self.assertEqual(self.q1.a2, 3)
        self.assertEqual(self.q1.a3, 4)

    def test_str_rep(self):
        self.assertEqual(str(self.q1), "1 +2i +3j +4k")

    def test_equality(self):
        self.assertEqual(self.q1, Quaternions(1, 2, 3, 4))
        self.assertNotEqual(self.q1, self.q2)
        self.assertNotEqual(self.q1, (1, 2, 3, 4))

    def test_addition(self):
        sum = self.q1 + self.q2
        self.assertEqual(sum, Quaternions(6, 8, 10, 12))

    def test_subtraction(self):
        diff = self.q1 - self.q2
        # (1-5, 2-6, 3-7, 4-8) = (-4, -4, -4, -4)
        self.assertEqual(diff, Quaternions(-4, -4, -4, -4))

    def test_multiplication(self):
        # i*i = j*j = k*k = -1
        real_minus_one = Quaternions(-1, 0, 0, 0)
        self.assertEqual(self.i * self.i, real_minus_one)
        self.assertEqual(self.j * self.j, real_minus_one)
        self.assertEqual(self.k * self.k, real_minus_one)

        # i*j = k
        self.assertEqual(self.i * self.j, self.k)
        # j*i = -k
        self.assertEqual(self.j * self.i, Quaternions(0, 0, 0, -1))
        # j*k = i
        self.assertEqual(self.j * self.k, self.i)
        # k*j = -i
        self.assertEqual(self.k * self.j, Quaternions(0, -1, 0, 0))

    def test_magnitude(self):
        self.assertAlmostEqual(abs(self.q1), math.sqrt(30))
        self.assertEqual(abs(self.real), 5)
        self.assertEqual(abs(self.zero), 0)

    def test_conjugate(self):
        self.assertEqual(self.q1.conjugate(), Quaternions(1, -2, -3, -4))
        self.assertEqual(self.real.conjugate(), self.real)

    def test_inverse(self):
        inv_q1 = self.q1.inverse()
        self.assertAlmostEqual(inv_q1.a0, 1 / 30)
        self.assertAlmostEqual(inv_q1.a1, -2 / 30)
        self.assertAlmostEqual(inv_q1.a2, -3 / 30)
        self.assertAlmostEqual(inv_q1.a3, -4 / 30)

    def test_inverse_zero(self):
        with self.assertRaises(ValueError):
            self.zero.inverse()

    def test_division(self):
        result_div_real = self.q1 * self.real.inverse()
        self.assertAlmostEqual(result_div_real, Quaternions(0.2, 0.4, 0.6, 0.8))

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            self.q1 * self.zero.inverse()


if __name__ == '__main__':
    unittest.main()
