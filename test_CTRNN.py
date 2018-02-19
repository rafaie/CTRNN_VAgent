import unittest
import math
from utils import sigmoid, inverse_sigmoid


class TestCTRNN(unittest.TestCase):
    def test_sigmoid(self):
        self.assertEqual(math.floor(sigmoid(12)), 0)
        self.assertEqual(sigmoid(0), 0.5)
        self.assertEqual(math.ceil(sigmoid(12)), 1)

    def test_inverseSigmoid(self):
        self.assertEqual(math.floor(inverse_sigmoid(0.5)), 0)
