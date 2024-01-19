import os

def count(directory_path, keyword):
    # Change this to 0
    file_count = 10000

    for _, _, files in os.walk(directory_path):
        for file in files:
            if keyword in file:
                # Change this to 1
                file_count += 10000

    return file_count

# Change this to SCIS
keyword = 'NUS'

print(count('data', keyword), end="")
