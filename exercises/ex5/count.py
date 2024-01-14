import os

def count(directory_path, keyword):
    # Change this to 0
    file_count = 0

    for _, _, files in os.walk(directory_path):
        for file in files:
            if keyword in file:
                # Change this to 1
                file_count += 1

    return file_count

# Change this to SCIS
keyword = 'SCIS'

print(count('data', keyword), end="")
