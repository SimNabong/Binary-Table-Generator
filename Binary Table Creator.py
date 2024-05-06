def generate_binary_table():
    num_variables = int(input("How many variables for the table? "))
    
    # Calculate the maximum number based on the number of variables
    max_num = 2 ** num_variables
    
    # Iterate from 0 to the maximum number and convert each number to binary
    for i in range(max_num):
        binary_num = bin(i)[2:].zfill(num_variables)
        print(" ".join(binary_num))

# Call the function to generate the binary table
generate_binary_table()