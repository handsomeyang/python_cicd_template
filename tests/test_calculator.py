import pytest
from python_cicd_template.calculator import add_numbers


# --- Test Case 1: Happy Path (Integers) ---
def test_add_two_integers():
    """Tests the addition of two standard positive integers."""
    result = add_numbers(5, 3)
    assert result == 8


# --- Test Case 2: Happy Path (Floats) ---
def test_add_two_floats():
    """Tests the addition of two floating-point numbers."""
    result = add_numbers(4.5, 1.2)
    # Using a tolerance check for floats is often a best practice
    assert abs(result - 5.7) < 1e-6


# --- Test Case 3: Zero and Negative Numbers ---
def test_add_zero_and_negative():
    """Tests addition involving zero and a negative number."""
    result = add_numbers(-10, 10)
    assert result == 0

    result_negative = add_numbers(-5, -3)
    assert result_negative == -8


# --- Test Case 4: Invalid Input Type (Exception Handling) ---
def test_add_invalid_type_raises_error():
    """Tests that a TypeError is raised when a non-numeric type is passed."""

    # We use pytest.raises to assert that a specific exception is raised
    with pytest.raises(TypeError) as excinfo:
        add_numbers(1, "hello")

    # Optional: Check the exception message
    assert "Both inputs must be integers or floats." in str(excinfo.value)

    # Test another invalid combination (list and int)
    with pytest.raises(TypeError):
        add_numbers([1, 2], 5)


# --- Test Case 5: Parameterized Testing (Advanced) ---
# A great way to test many simple inputs without writing repetitive functions.
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),  # Positive integers
        (-1, 5, 4),  # Negative and positive
        (0, 0, 0),  # Zeros
        (10.5, 2.5, 13.0),  # Floats
    ],
)
def test_add_numbers_parameterized(a, b, expected):
    """Tests multiple inputs using a single, parameterized test function."""
    assert add_numbers(a, b) == expected
