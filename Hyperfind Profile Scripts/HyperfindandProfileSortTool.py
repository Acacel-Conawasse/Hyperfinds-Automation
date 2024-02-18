import csv

# Define the input and output file names
input_file_name = 'HyperfindandProfileList.txt'
output_file_name = 'sortedprofile.txt'

# Initialize a dictionary to store the profile to hyperfinds mapping
profile_hyperfinds = {}

# Read the input file
with open(input_file_name, 'r') as infile:
    # Assuming the file is tab-delimited
    reader = csv.reader(infile, delimiter='\t')
    next(reader)  # Skip the header line
    for row in reader:
        # Each row should have two columns: hyperfind and profile
        hyperfind, profile = row
        if profile not in profile_hyperfinds:
            profile_hyperfinds[profile] = []
        profile_hyperfinds[profile].append(hyperfind)

# Sort the profiles and their hyperfinds
sorted_profiles = sorted(profile_hyperfinds.items())

# Write the sorted profiles and hyperfinds to the output file
with open(output_file_name, 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    for profile, hyperfinds in sorted_profiles:
        # Join the hyperfinds with '#' and write to file
        writer.writerow([profile, '#'.join(sorted(hyperfinds))])

print(f"Data has been processed and output to {output_file_name}")
