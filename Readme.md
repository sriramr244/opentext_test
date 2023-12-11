# Project Overview DRE - RANDOM
This project is designed to execute two specific types of jobs, both involving the manipulation and storage of random numbers, driven by XML configurations. The implementation focuses on efficient data handling and extendibility for future enhancements.

## Functionalities
The project encapsulates two primary functionalities:

#### Random Number Generation:

- Seed-Based Creation: Generates random numbers based on a provided seed.
- Storage: Stores the generated numbers in an HDF5 file, leveraging its efficient storage capabilities.
- Chunk-Based Processing: Utilizes chunk processing to enhance performance and avoid loading the entire dataset into memory.
#### Data Processing:

- Load and Filter: Loads the random number file, creates intervals, and stores the data based on a specified minimum and maximum range.
- Scope for Improvement: There is potential to optimize time complexity in this functionality.
- Memory Profiling: Includes memory profiling to monitor memory usage during data loading.

### System Design

Package Structure:

- Components Folder: Contains scripts like build-list.py for random number generation and data processing functionalities.
Utils Folder: Houses common utility functions like reading YAML files and converting XML into a dictionary.
Configuration and Control:

- XML and XSD: Uses XML files for input job descriptions and validates them against a schema defined in an XSD file located in the data folder.
- Job Controller: A central controller processes XML jobs, ensuring they adhere to the schema before executing them.

### Testing and Automation
- Unit Testing: Implemented for random number generation functionality, with the plan to extend it to other parts of the project.
- GitHub Workflows: Utilizes continuous integration to test all pushes to the repository.

## Extensibility and Future Improvements
- Configuration Management: Future scope includes developing a configuration manager to handle config.yaml files more efficiently.
- Parallel Processing: The main function could be enhanced to handle multiple non-dependent jobs in parallel using multiprocessing.
- Metadata and Logging: Incorporating metadata in HDF5 storage and implementing job logging for better traceability and data management.
- API Extension: The system is designed to be extendable to an API-based application..
- Data Storage and Transformation: Exploring the division of HDF5 files into multiple XML files with a common job ID for efficient parallel processing and storage.
- Potential Use of MarkLogic: Utilizing MarkLogic with Xquery for efficient Extract and Transform tasks, facilitating queries based on job ID and number intervals.



### Unexplored Areas:
- OOP Principles: The project currently doesn't utilize Object-Oriented Programming, which can be explored for better structure.
- Storage Enhancements: Current storage in directories can be evolved to use NoSQL databases for parallel processing and efficient querying.
- Type hinting validation
- Containerization for consitency throughout the operating systems
- Time based scheduling: Use of cron to run this job periodically


## Getting started
- Create a virtual environment 
    `python -m venv name-for-venv`
- Activate the virtual environment
    `source path-to-venv/bin/activate`
- Install all the dependancies: 
        `pip install -r requirements.txt`
- Load XML jobs in the `data/input` folder'
- Run the main file
        `python main.py`

### To run unit tests

- `pytest test/`
