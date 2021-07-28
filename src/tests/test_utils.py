"""Test the utility functions"""

import pathlib
import unittest

# from reu_repro_py.utils import reu_repro_py
from reu_repro_py import reu_repro_py


HERE = pathlib.Path(__file__).parent

class TestUtils(unittest.TestCase):
    """Test the utilities"""

    def test_my_func(self):
        """Test :func reu_repro_py"""

        file1 = HERE.joinpath('test1.txt')
        file2 = HERE.joinpath('test2.txt')

        res = reu_repro_py(file1, file2)
        expected = [
            ('hi', 'bye'),
            ('hello', 'goodbye'),
            ('hii', 'kbye')
        ]

        self.assertEqual(expected, res)