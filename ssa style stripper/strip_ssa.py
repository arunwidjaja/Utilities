import os


def convert_to_utf8(filename):
    # Read the file using a permissive encoding (ISO-8859-1 or latin-1)
    with open(filename, 'r', encoding='ISO-8859-1') as file:
        content = file.read()

    # Write the content back as UTF-8
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)


def filter_ssa_files(keywords, save_folder):
    # Set the working directory to the directory of this script
    script_dir = os.path.dirname(os.path.realpath(__file__))
    os.chdir(script_dir)

    # Ensure the 'edited' directory exists
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    print(f"Removing lines NOT containing:\n{'\n'.join(keywords)}")
    # Loop through all files in the current directory
    for filename in os.listdir(script_dir):
        # Only process files with .ssa extension
        if filename.endswith('.ass') or filename.endswith('.ssa'):
            input_file = filename
            output_file = os.path.join('edited', filename)
            print(f"Processing file: {filename}")
            # Step 1: Convert the file to UTF-8
            convert_to_utf8(input_file)
            # Step 2: Open the UTF-8 encoded file for filtering
            with open(input_file, 'r', encoding='utf-8') as infile:
                lines = infile.readlines()
            # Step 3: Filter lines that contain the specified keyword
            filtered_lines = [line for line in lines if any(
                keyword in line for keyword in keywords)]
            # Step 4: Write the filtered lines to the output file (also in UTF-8)
            with open(output_file, 'w', encoding='utf-8') as outfile:
                outfile.writelines(filtered_lines)
    print(f"Processing complete. New files saved in the {save_folder} folder.")


def main():
    # The string to search for
    keywords = ['GJM_Main_1080p', 'GJM_Overlap_1080p']
    save_folder = 'edited'
    filter_ssa_files(keywords, save_folder)


if __name__ == "__main__":
    main()
