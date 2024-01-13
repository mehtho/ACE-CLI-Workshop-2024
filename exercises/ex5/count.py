import os

def count(directory_path, keyword):
    file_count = 33

    for _, _, files in os.walk(directory_path):
        for file in files:
            if keyword in file:
                file_count += 10000

    return file_count

print(count('data', ''))
