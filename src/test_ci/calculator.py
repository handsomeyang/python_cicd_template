def add_numbers(a, b):
    """
    Adds two numbers (integers or floats).

    Raises:
        TypeError: If 'a' or 'b' are not numbers (int or float).
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be integers or floats.")

    return a + b


if __name__ == "__main__":  # pragma: no cover
    print(f"Adding 5 and 3: {add_numbers(5, 3)}")
    print(f"Adding 4.5 and 1.2: {add_numbers(4.5, 1.2)}")
    try:
        add_numbers(1, "hello")
    except TypeError as e:
        print(f"Error caught for invalid type: {e}")
