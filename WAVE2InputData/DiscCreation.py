def process_file(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    updated_lines = []
    for line in lines:
        cols = line.strip().split('\t')
        description = cols[0] + ' - '
        for col in [2, 3, 5]:
            if cols[col] != 'Null':
                description += cols[col] + ' '
        updated_line = ','.join([cols[0], description.strip(), cols[4]]) + '\n'
        updated_lines.append(updated_line)

    with open(output_file, 'w') as file:
        file.write("Hyperfind Name,Description,Cost Center,Org Unit,Employment Status,Schedule Group\n")
        for line in updated_lines:
            file.write(line)
def main():
    input_file = 'C:/Users/omalomo3/Desktop/Hyperfinds Automation/WAVE2InputData/HFQueriesNoDisc.txt'  # Change this to your file path
    output_file = 'C:/Users/omalomo3/Desktop/Hyperfinds Automation/WAVE2InputData/FinalW2Creation.txt'  # Change this to your output file path
    process_file(input_file, output_file)
    print(f"Output written to {output_file}")

if __name__ == "__main__":
    main()
