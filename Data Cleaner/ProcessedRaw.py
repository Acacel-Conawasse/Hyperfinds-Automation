# Define the path to the input text file
input_file_path = 'Raw Conditions.txt'
# Define the path to the output text file
output_file_path = 'Raw Conditions Processed.txt'

# Initialize a dictionary to hold SHORTNM as keys and a list of VALUETXT as values
shortnm_dict = {}

# Read the input file
with open(input_file_path, 'r') as file:
    # Skip the header
    next(file)
    for line in file:
        # Split each line by comma
        parts = line.strip().split(',')
        if len(parts) == 2:
            shortnm, valuetxt = parts
            # Append the VALUETXT to the list of values for this SHORTNM
            if shortnm in shortnm_dict:
                shortnm_dict[shortnm].append(valuetxt)
            else:
                shortnm_dict[shortnm] = [valuetxt]

# Open the output file in write mode
with open(output_file_path, 'w') as outfile:
    # Iterate through the dictionary and concatenate VALUETXT values for each SHORTNM
    for shortnm, valuetxts in shortnm_dict.items():
        concatenated_valuetxt = '^|||^'.join(valuetxts)
        outfile.write(f"{shortnm}: {concatenated_valuetxt}\n")

print(f"Output written to {output_file_path}")
