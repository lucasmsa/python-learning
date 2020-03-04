import csv

with open('test.csv', 'r') as csvFile:
    csvReader = csv.reader(csvFile)
    
    # Will jump the first line, that contains only the column name
    #next(csvReader)

    with open('newTest.csv', 'w') as newCsvFile:
        csvWriter = csv.writer(newCsvFile, delimiter='\t')

        for line in csvReader:
            csvWriter.writerow(line)


with open('newTest.csv', 'r') as newCsvFile:
    # Must specify new delimiter    
    csvReader = csv.reader(newCsvFile, delimiter='\t')

    for line in csvReader:
        print(line)


with open('test.csv', 'r') as csvFile:
    # Csv files can also be openned as dict
    csvReader = csv.DictReader(csvFile)

    # More organized form of treating data
    for line in csvReader:
        print(line['first_name'])


    with open('newTest.csv', 'w') as newCsvFile:
        fieldNames = ['first_name', 'last_name', 'email']

        csvWriter = csv.writer(newCsvFile, fieldNames=fieldNames, delimiter='\t')
        csvWriter.writeheader()

        for line in csvReader:
            csvWriter.writerow(line)