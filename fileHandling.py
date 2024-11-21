# Question ONE; File Read and Write Challenge
def modify_file(input_file, output_file):
    try:
        # Read content from the input file
        with open(input_file, 'r') as infile:
            content = infile.readlines()
        
        # Modify the content
        modified_content = []
        for line in content:
            # Example transformation: Convert text to uppercase
            modified_content.append(line.upper())
        
        # Write modified content to the output file
        with open(output_file, 'w') as outfile:
            outfile.writelines(modified_content)
        
        print(f"File has been modified and saved to {output_file}.")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

#QUESTION TWO(2)
def error_handling_lab():
    try:
        # Prompt user for the filename
        filename = input("Enter the filename to read: ")

        # Try to open and read the file
        with open(filename, 'r') as file:
            print("\nFile content:\n")
            print(file.read())

    except FileNotFoundError:
        print(f"\nError: The file '{filename}' does not exist. Please check the filename and try again.")

    except PermissionError:
        print(f"\nError: You don't have permission to read the file '{filename}'.")

    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

# Call the function to test
error_handling_lab()

