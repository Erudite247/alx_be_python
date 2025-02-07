# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """Perform division with error handling for zero division and non-numeric input."""
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        denom = float(denominator)

        # Perform the division
        result = num / denom
        return f"The result of the division is {result:.1f}"  # Change .2f to .1f

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
