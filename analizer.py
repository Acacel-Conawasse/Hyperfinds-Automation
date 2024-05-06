def copy_matching_lines(analyze_file, retry_file, output_file):
    # Load descriptions from analyze.txt
    with open(analyze_file, 'r') as file:
        analyze_descriptions = {line.strip() for line in file.readlines()}

    # Open the output file
    with open(output_file, 'w') as output:
        # Process retry.txt
        with open(retry_file, 'r') as retry:
            for line in retry:
                # Extract the entire description (up to the first comma)
                description = line.split(',', 1)[0].strip()
                # Check if the description starts with any name from analyze.txt
                if any(description.startswith(name) for name in analyze_descriptions):
                    output.write(line)

# Specify the file names
analyze_file = 'analyze.txt'
retry_file = 'retry.txt'
output_file = 'retry2.txt'

# Call the function
copy_matching_lines(analyze_file, retry_file, output_file)
