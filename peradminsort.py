# Define a function to read peradminlist.txt and generate the required output
def generate_peradmin_costcenters(filename):
    peradmin_costcenters = {}  # Dictionary to store PerAdmin and associated CostCenters

    # Read the file line by line
    with open(filename, 'r') as file:
        for line in file:
            # Split each line by whitespace
            data = line.strip().split('\t')
            if len(data) == 2:  # Ensure there are two elements in the line
                peradmin, costcenter = data
                # If PerAdmin already exists in dictionary, append the CostCenter
                if peradmin in peradmin_costcenters:
                    peradmin_costcenters[peradmin].append(costcenter)
                else:  # If PerAdmin doesn't exist, create a new entry
                    peradmin_costcenters[peradmin] = [costcenter]

    # Format the dictionary into the required output format
    formatted_output = ''
    for peradmin, costcenters in sorted(peradmin_costcenters.items()):
        formatted_output += f"{peradmin},{'#'.join(costcenters)}\n"

    return formatted_output

# Main function to execute the script
def main():
    filename = 'PerAdminList.txt'  # Name of the input file
    output = generate_peradmin_costcenters(filename)
    # Write the output to Peradminsorted.txt
    with open('Peradminsorted.txt', 'w') as file:
        file.write(output)

if __name__ == "__main__":
    main()
