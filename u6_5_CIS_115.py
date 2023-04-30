# Mark Bulmer - CIS 115 
# Programming Exercise 6-5

def main():
    # Declare variables
    line = ''
    total = 0.0
    number = 0.0

    # Open numbers.txt file for reading
    # Make sure the numbers.txt file is in the EXACT same
    # folder as your Python program!!!
    infile = open('numbers.txt', 'r')

    for line in infile:
        number = float(line)
        
        total += number

    # Close file
    infile.close()

    # Display the total of the numbers in the file
    print('Total: ', total)

# Call the main function.
main()
