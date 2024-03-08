# Open "Wave2DataConditions1.txt" for reading
with open('C:/Users/omalomo3/Desktop/Hyperfinds Automation/Data Cleaner/inputfeed.txt', 'r') as input_file:
    # Open "Hyperfinds.txt" for writing. Add 'newline=""' to prevent writing extra newlines in Windows.
    with open('C:/Users/omalomo3/Desktop/Hyperfinds Automation/Data Cleaner/W2Hyperfinds.txt', 'w', newline="") as output_file:
        # Write the header to "Hyperfinds.txt"
        output_file.write("Hyperfind Name,Description,Cost Center,Org Unit,Employment Status,Schedule Group\n")
        
        for line in input_file:
            # Split the line into columns
            columns = line.strip().split(',')
            
            # Initialize placeholders for each column in "Hyperfinds.txt"
            hyperfind_name = columns[0]  # The first column is always the Hyperfind Name
            description = ""  # Assume Description is not provided
            cost_center = ""
            org_unit = ""
            employment_status = ""
            schedule_group = ""
            
            # Process other columns based on provided criteria
            for col in columns[1:]:
                # Check for Org Unit (8 digits) or list of Org Units
                if col.isdigit() and len(col) == 8:
                    org_unit = col
                elif all(part.isdigit() and len(part) == 8 for part in col.split('#')):
                    org_unit = col

                # Check for Cost Center (10 digits) or list of Cost Centers
                if col.isdigit() and len(col) == 10:
                    cost_center = col
                elif all(part.isdigit() and len(part) == 10 for part in col.split('#')):
                    cost_center = col

                # Check for Employment Status
                if "EmploymentStatus" in col:
                    employment_status = "Y"

                # Check for Schedule Group (column before "GroupSchedule")
                if "GroupSchedule" in columns:
                    schedule_group_index = columns.index("GroupSchedule") - 1
                    if schedule_group_index >= 0:
                        schedule_group = columns[schedule_group_index]

            # Write the processed line to "Hyperfinds.txt"
            output_line = f"{hyperfind_name},{description},{cost_center},{org_unit},{employment_status},{schedule_group}\n"
            output_file.write(output_line)

print("Processing complete. Data written to Hyperfinds.txt.")
