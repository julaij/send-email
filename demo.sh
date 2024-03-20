#!/bin/bash

# Create a directory
mkdir my_directory

# Navigate into the directory
cd my_directory || exit

# Create a new file
touch my_file.txt

# Add some content to the file
echo "This is a sample text file created using Bash script." > my_file.txt

# Display a message
echo "File 'my_file.txt' has been created inside the directory 'my_directory'."
