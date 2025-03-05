import json

def write_output(data, output_file):
    """
    Writes transformed data to a JSON file.
    :param data: List of dictionaries (JSON objects)
    :param output_file: Path to the output file
    """
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)