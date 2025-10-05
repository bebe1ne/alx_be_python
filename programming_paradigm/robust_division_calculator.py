def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        if denom == 0:
            return "Error: Division by zero is not allowed."
        return num / denom
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except ValueError:
        return "Error: Invalid input. Please enter numeric values."
    except Exception as e:
        return f"An unexpected error occurred: {e}"
    else:
        return "Division successful."
    finally:
        print("Execution of safe_divide complete.")
    