from memory_profiler import profile
import h5py
from pathlib import Path


# memory checker
@profile
def create_and_store_intervals(
    input_file_path: Path, output_file_path: Path, min_val: float, max_val: float
):
    """
    Processes an HDF5 file, filtering and storing data based on given value range.

    Parameters:
    input_file_path (Path): Path to the input HDF5 file containing the 'random_numbers' dataset.
    output_file_path (Path): Path where the output HDF5 file will be created and saved.
    min_val (float): The minimum value of the range used for filtering the dataset.
    max_val (float): The maximum value of the range used for filtering the dataset.

    The function does not return any value.

    Raises:
    IOError: If there is an issue with opening or reading the input file or writing to the output file.
    KeyError: If the 'random_numbers' dataset is not found in the input file.
    """
    try:
        with h5py.File(input_file_path, "r") as infile:
            try:
                dataset = infile["random_numbers"]
            except KeyError:
                raise KeyError(
                    f"Dataset 'random_numbers' not found in {input_file_path}"
                )

            with h5py.File(output_file_path, "w") as outfile:
                out_dataset = outfile.create_dataset(
                    "data", (0,), maxshape=(None,), dtype=dataset.dtype
                )
                out_index = 0

                for value in dataset:
                    if min_val <= value <= max_val:
                        out_dataset.resize(out_index + 1, axis=0)
                        out_dataset[out_index] = value
                        out_index += 1
    except IOError as e:
        raise IOError(f"An I/O error occurred: {e}")


if __name__ == "__main__":
    create_and_store_intervals("random_numbers.hdf5", "interval.hdf5", 0.2, 0.3)
