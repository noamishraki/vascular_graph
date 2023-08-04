# Vascular Data to NetworkX Graph Conversion

This Python-based tool allows you to convert vascular data from a specific `.mat` file in Vida format, into a NetworkX graph. The conversion to a NetworkX graph provides an easy way to analyze, visualize, and manipulate the vascular network using NetworkX's powerful features.

## Input

To use this tool, you need to provide the following inputs:

1. `file_path`: The path to the `.mat` file containing the vascular data. This file should adhere to the specific structure expected by the extractor.

2. `dataset_name`: The name of the dataset in the `.mat` file. It is used by the `VascularDataExtractor` to extract relevant vascular information.

## Requirements

Before using this tool, ensure you have the following prerequisites installed on your system:

1. Python (>=3.6)
2. NetworkX (>=2.5)
3. SciPy (>=1.6)
4. NumPy (>=1.20)


## Usage

1. Ensure you have Python (>=3.6) installed on your system.

2. Install the required dependencies: NetworkX, SciPy, and NumPy.

3. In the main.py file, update the file_path and dataset_name variables to match your specific data:
```
file_path = "path/to/your/vascular_data.mat"
dataset_name = "your_dataset_name"
```
4. Run the main.py script using Python:

The script will read the vascular data from the specified .mat file, convert it into a NetworkX graph, and save the resulting graph as a pickled file (vascular_graph_output.pkl) in the same directory
