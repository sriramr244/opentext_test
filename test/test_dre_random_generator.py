import unittest
import os
from dre_random.components.build_list import gen_and_store_random_numbers
import h5py


class TestGenerateStoreRandomNumber(unittest.TestCase):
    def test_file_creation(self):
        """Test if the HDF5 file is created."""
        test_file = "test_random_numbers.hdf5"
        gen_and_store_random_numbers(42, 100, test_file)
        self.assertTrue(os.path.exists(test_file))
        os.remove(test_file)

    def test_file_content(self):
        """Test if the file contains the correct number of elements."""
        test_file = "test_random_numbers.hdf5"
        length = 100
        gen_and_store_random_numbers(42, length, test_file)
        with h5py.File(test_file, "r") as hdf:
            dset = hdf["random_numbers"]
            self.assertEqual(len(dset), length)
        os.remove(test_file)


if __name__ == "__main__":
    unittest.main()
