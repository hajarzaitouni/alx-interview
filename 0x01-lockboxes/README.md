# Lockboxes
This project is about a Python function that determines if all boxes in a given list can be opened. Each box may contain keys to other boxes, and the goal is to see if all boxes can be unlocked starting from the first box.

## Algorithm

1. Initialize a list `keys` with the first key (0) since the first box is always open.
2. Iterate through each key in `keys`:
    - For each key, retrieve the corresponding box and iterate through the keys it contains.
    - If a key found in the box is not already in `keys` and corresponds to a valid box (i.e., the key is less than the total number of boxes), add this key to `keys`.
3. After processing all accessible keys, check if the number of keys collected is equal to the number of boxes.
4. Return `True` if all boxes can be opened (i.e., all keys were collected), otherwise return `False`.

