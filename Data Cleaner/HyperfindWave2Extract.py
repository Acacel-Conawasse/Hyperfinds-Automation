# Define file paths
wave2_list_path = 'C:/Users/omalomo3/Desktop/Hyperfinds Automation/Data Cleaner/Wave2HyperfindList.txt'
raw_conditions_path = 'C:/Users/omalomo3/Desktop/Hyperfinds Automation/Data Cleaner/Raw Conditions Processed.txt'
output_path = 'C:/Users/omalomo3/Desktop/Hyperfinds Automation/Data Cleaner/WAVE2HyperfindConditions.txt'

# Step 1: Read "Wave2Hyperfind List.txt" and store SHORTNM values
with open(wave2_list_path, 'r') as file:
    # Skip the header
    next(file)
    # Read and strip newlines, then store
    shortnm_list = [line.strip() for line in file]

# Step 2: Read "Raw Conditions Processed.txt" and find matches
matches = []
with open(raw_conditions_path, 'r') as file:
    # Skip the header
    next(file)
    for line in file:
        # Check if the SHORTNM in this line matches any from the list
        for shortnm in shortnm_list:
            if line.startswith(shortnm + ','):
                matches.append(line)
                break

# Step 3: Write matched lines to "WAVE2HyperfindConditions.txt"
with open(output_path, 'w') as outfile:
    for match in matches:
        outfile.write(match)

print(f"Matched conditions written to {output_path}")
