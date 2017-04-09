# Import csv and labelimage
import csv, labelimage, os

# Log Function
def log(file, message):
    # Print the message
    print(message)

    # Write the message to the file
    file.write(message)

# Main Function
def main():
    # Open dataset file
    dataset = open('dataindex.csv', 'rb')

    # Open log file
    logfile = open('log.log', 'a')

    # Initialize csvreader for dataset
    reader = csv.reader(dataset)

    # Read data from reader
    data = list(reader)

    # Variables for progress counter
    lines = len(data)
    i = 0

    # Analyze data in dataset
    for row in data:
        # Assign image name and state to variables
        image = row[1] + row[0]

        # Print image information
        log(logfile, '({}/{}) Processing image: {}'.format(i + 1, lines, image))

        # Increment i
        i += 1

        # Run tensorflow testing
        data = labelimage.test(image, [log, logfile])
	
    # Close files
    dataset.close()
    logfile.close()

# Execute main function if name is equal to main
if __name__ == '__main__':
    main()
