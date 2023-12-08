import random
import h5py
from pathlib import Path


import random
import h5py
from pathlib import Path
from typing import NoReturn


def gen_and_store_random_numbers(
    seed: int, length: int, file_path: Path, chunk_size: int
) -> NoReturn:
    """
    Generates a sequence of random numbers and stores them in an HDF5 file.

    Parameters:
    seed (int): Seed for the random number generator to ensure reproducibility.
    length (int): The total number of random numbers to generate.
    file_path (Path): Path to the output HDF5 file where the random numbers will be stored.
    chunk_size (int): Size of chunks used to store the numbers in the dataset.

    Raises:
    ValueError: If 'length' or 'chunk_size' is non-positive.
    IOError: If there is an issue with writing to the HDF5 file.
    """

    if length <= 0 or chunk_size <= 0:
        raise ValueError("Both 'length' and 'chunk_size' must be positive integers.")

    random.seed(seed)

    try:
        with h5py.File(file_path, "w") as hdf:
            dset = hdf.create_dataset("random_numbers", (length,), dtype="float64")

            for i in range(0, length, chunk_size):
                numbers = [random.random() for _ in range(min(chunk_size, length - i))]
                dset[i : i + len(numbers)] = numbers
    except IOError as e:
        raise IOError(f"An error occurred while writing to the HDF5 file: {e}")


if __name__ == "__main__":
    gen_and_store_random_numbers(42, 100000, "random_numbers.hdf5")
