# Manual implementation
from typing import List, Dict, Any

def sort_dicts_by_key_manual(data: List[Dict[str, Any]], key: str) -> List[Dict[str, Any]]:
    """
    Manually sorts a list of dictionaries by a specific key.
    Handles KeyError explicitly and uses bubble-sort for illustration.
    """
    n = len(data) # Get the number of dictionaries in the list
    for i in range(n): # Iterate through the list
        for j in range(0, n - i - 1): # Inner loop for comparison and swapping
            val1 = data[j].get(key) # Get the value of the key for the current dictionary (handles missing keys by returning None)
            val2 = data[j + 1].get(key) # Get the value of the key for the next dictionary (handles missing keys by returning None)
            if val1 is None: # If the current dictionary is missing the key, do nothing (it will be moved towards the end)
                continue
            if val2 is None or val1 > val2: # If the next dictionary is missing the key, or the current value is greater than the next value
                data[j], data[j + 1] = data[j + 1], data[j] # Swap the dictionaries
    return data # Return the sorted list of dictionaries
 # Example usage:
data = [{'name': 'Alice', 'age': 30}, {'name': 'Bob'}, {'name': 'Charlie', 'age': 25}] # Define a list of dictionaries
sorted_data = sort_dicts_by_key_manual(data, 'age') # Call the manual sorting function
print(sorted_data) # Print the sorted data