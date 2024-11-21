def remove_characters_from_file(input_file, output_file, characters_to_remove):
    """
    Removes all characters contained within a specific string from the content of a file.

    Parameters:
    - input_file (str): Path to the input file.
    - output_file (str): Path to the output file.
    - characters_to_remove (str): String containing characters to remove.
    """
    try:
        # Read the contents of the input file
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Create a translation table to remove unwanted characters
        translation_table = str.maketrans('', '', characters_to_remove)
        
        # Apply the translation to the content
        cleaned_content = content.translate(translation_table)
        
        # Write the cleaned content to the output file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(cleaned_content)
        
        print(f"Characters successfully removed. Cleaned file saved as '{output_file}'.")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # File paths
    input_file_path = "sequences_test_no_labels.txt"  # Replace with your input file path
    output_file_path = "cleaned_sequences.txt"  # Replace with your desired output file path

    # Characters to remove
    chars_to_remove = "BJOUZX"  # Example: removes all vowels

    remove_characters_from_file(input_file_path, output_file_path, chars_to_remove)
