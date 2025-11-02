# Copilot suggested code
def sort_dicts_by_key(data: list[dict], key: str) -> list[dict]:
    """
    Sorts a list of dictionaries by a given key.
    Missing keys are treated as None and placed at the end.
    """
    # Custom key function to handle None values by treating them as larger than any other value
    # Use a lambda function as the key for sorting
    # x.get(key, float('inf')) safely retrieves the value associated with the key
    # If the key is not found, it returns float('inf'), effectively placing None values at the end
    return sorted(data, key=lambda x: x.get(key, float('inf')))

# Example usage:
# Define a list of dictionaries with varying keys
data = [{'name': 'Alice', 'age': 30}, {'name': 'Bob'}, {'name': 'Charlie', 'age': 25}]
# Call the function to sort the data by the 'age' key
sorted_data = sort_dicts_by_key(data, 'age')

# Display the sorted data to verify the fix
# display() is used for rich output in environments like Colab
print(sorted_data)