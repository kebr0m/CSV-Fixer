''' Short Program t that would search for empty columns in data-sets we would receive and conditionally add the content of the line associated with the empty column to
 the line above. The reason being is that the data-sets we would receive were in PDF format and had indentation within address columns.The conversion to CSV would cause error in
our data format, as it would interpret indentations as new lines. '''

import csv
import pprint

def CreateDictionaryFromCsv(inputFile):
    data = {}

    with open(inputFile, 'r') as f:
        # Create a csv reader object that uses the opened file.
        csv_reader = csv.reader(f)

        # Retrieve the header of the csv file. This is also used as the items that are present. 
        csvHeader = next(csv_reader)

        # Loop through the rest of the csv file. 
        Id = ""
        for line in csv_reader:
            # Check if the Id is not empty, if it is not empty set the Id variable so that it can be used for later rows which have no Id. 
            if (line[0].strip() != ""):
                Id = line[0]
                # If the item doesn't exist in the dictionary, asign the dictionary with data to it. 
                if (not data.get(line[0], None)):
                    data[Id] = [line[i].replace('\n', ' ') for i in range(1, len(csvHeader))]
            # Id is empty, add contents of the cells to the previous Id. 
            else:
                data[Id] = [data[Id][i - 1] +  ' ' + line[i]  if line[i].strip() != "" else data[Id][i - 1] for i in range(1, len(csvHeader))]

    return data


data = CreateDictionaryFromCsv(r"Name of the file with the updated data that you want to create")
pprint.pprint(data)

with open(r'Name of the file that includes your data', 'w', newline='') as o:
    csv_writer = csv.writer(o, )
    for key in data.keys():
        row = [key]
        row.extend(data[key])
        csv_writer.writerow(row)