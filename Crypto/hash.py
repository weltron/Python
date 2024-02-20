import os
import random
from cryptography.hazmat.primitives import hashes

#function to corrupt hashes
def corrupt_hashes(hashes_dict):
    # List of binary files that will be randomly used for corruption
    files = ["file1.bin", "file2.bin", "file3.bin", "file4.bin", "file5.bin", "file6.bin", "file7.bin", "file8.bin", "file9.bin", "file10.bin"]
    # Choose 4 or 5 files to corrupt hashes
    num_corrupt_files = random.randint(4, 5)
    corrupt_files = random.sample(files, num_corrupt_files)

    # Corrupt hashes for the chosen files
    for filename in corrupt_files:
        for name, _ in hash_functions:
            if filename in hashes_dict:
                if name in hashes_dict[filename]:
                    # Intentionally corrupt hash
                    hashes_dict[filename][name] = 'corrupted_' +  hashes_dict[filename][name]

    return hashes_dict

# The block size to use for reading the files
block_size = 1024

# Hash functions to use
hash_functions = [
    ("SHA256", hashes.SHA256()),
    ("SHA3_224", hashes.SHA3_224()),
    ("MD5", hashes.MD5())
]



# Dictionary to hold the hashes for each file
hashes_dict = {}

# Compute the hashes for each file and hash function
for filename in os.listdir():
    if filename.endswith(".bin"):
        with open(filename, 'rb') as f:
            for name, hash_func in hash_functions:
                # Create a new hash object
                digest = hashes.Hash(hash_func)
                chunk = 0
                # Read the file in blocks and update the hash object
                while chunk != b'':
                    block = f.read(block_size)
                    if not block:
                        break
                    digest.update(block)

                hashes_dict.setdefault(filename, {})[name] = digest.finalize().hex()

#corrupt hashes
hashes_dict = corrupt_hashes(hashes_dict)           

# Write the hashes to a text file
with open("hashes.txt", "w") as f:
    for filename, file_hashes in hashes_dict.items():
        line = f"{filename}, {file_hashes['SHA256']}, {file_hashes['SHA3_224']}, {file_hashes['MD5']}\n"
        f.write(line)

print("Hashes saved to hashes.txt")
