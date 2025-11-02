# Copilot suggested code
def sort_dicts_by_key(data: list[dict], key: str) -> list[dict]:
    """
    Sorts a list of dictionaries by a given key.
    Missing keys are treated as None and placed at the end.
    """
    # Place items with missing key at the end by sorting on a tuple:
    # (missing_flag, value) so (False, 25) < (True, None).
    # The lambda function defines the key for sorting.
    # x.get(key) is None checks if the key is missing (returns True) or present (returns False).
    # x.get(key) retrieves the value associated with the key.
    # Sorting is done based on the tuple (presence of key, value).
    # Dictionaries with the key (False) come before those without the key (True).
    # For dictionaries with the key, they are sorted by their value.
    return sorted(data, key=lambda x: (x.get(key) is None, x.get(key)))


if __name__ == "__main__":
    # Example usage:
    # Define a list of dictionaries with varying keys for demonstration.
    data = [{'name': 'Alice', 'age': 30}, {'name': 'Bob'}, {'name': 'Charlie', 'age': 25}]
    # Call the sort_dicts_by_key function to sort the data by 'age'.
    sorted_data = sort_dicts_by_key(data, 'age')
    # Print the sorted data to the console.
    print(sorted_data)