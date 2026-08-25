def is_valid_input(data):
    if data is None:
        return False
    if not isinstance(data, (str, int, float)):
        return False
    if isinstance(data, str):
        stripped = data.strip()
        if len(stripped) == 0:
            return False
        # Allow letters, numbers and spaces only
        for char in stripped:
            if not (char.isalnum() or char.isspace()):
                return False
    if isinstance(data, (int, float)):
        if not (0 <= data <= 1000):
            return False
    return True

def process_data(item):
    if isinstance(item, str):
        return item.strip().title()
    return item * 2

def main():
    # Sample data simulating inputs for the automation tool
    inputs = [5, "hello world", -1, "test", 1500, "invalid@char", 42, "", None, "Valid123", 100]
    results = []
    # Main processing loop with input validation
    for idx, item in enumerate(inputs):
        print(f"Processing item {idx + 1}: {item}")
        if not is_valid_input(item):
            print("  -> Skipped: invalid input")
            continue
        processed = process_data(item)
        results.append(processed)
        print(f"  -> Result: {processed}")
    print("\nAll results:", results)
    return results

if __name__ == "__main__":
    main()