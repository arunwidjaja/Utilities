import os


def convert_to_utf8(filename):
    # Read the file using a permissive encoding (ISO-8859-1 or latin-1)
    with open(filename, 'r', encoding='ISO-8859-1') as file:
        content = file.read()

    # Write the content back as UTF-8
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)


def filter_ssa_files(keyword):
    # Set the working directory to the directory of this script
    script_dir = os.path.dirname(os.path.realpath(__file__))
    os.chdir(script_dir)

    # Ensure the 'edited' directory exists
    if not os.path.exists('edited'):
        os.makedirs('edited')

    # Loop through all files in the current directory
    for filename in os.listdir(script_dir):
        # Only process files with .ssa extension
        if filename.endswith('.ass') or filename.endswith('.ssa'):
            input_file = filename
            output_file = os.path.join('edited', filename)

            print(f"Converting {filename} to UTF-8.")
            # Step 1: Convert the file to UTF-8
            convert_to_utf8(input_file)

            # Step 2: Open the UTF-8 encoded file for filtering
            with open(input_file, 'r', encoding='utf-8') as infile:
                lines = infile.readlines()

            print(f"Removing lines containing {keyword} from {filename}")
            # Step 3: Filter lines that contain the specified keyword
            filtered_lines = [line for line in lines if keyword in line]

            print(f"Saving {filename}")
            # Step 4: Write the filtered lines to the output file (also in UTF-8)
            with open(output_file, 'w', encoding='utf-8') as outfile:
                outfile.writelines(filtered_lines)


def main():
    search_string = 'GJM_Main_1080p'  # The string to search for
    filter_ssa_files(search_string)


if __name__ == "__main__":
    main()
