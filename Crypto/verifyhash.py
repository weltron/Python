from cryptography.hazmat.primitives import hashes

# Read the hash values from the file
with open('hashes.txt', 'r') as f:
    lines = f.readlines()

# Verify the hash values for each file
for line in lines:
    parts = line.strip().split(', ')
    filename = parts[0]
    sha256_hash = parts[1]
    sha3_224_hash = parts[2]
    md5_hash = parts[3]
    
    
    # Calculate the hash values for the file
    with open(filename, 'rb') as f:
        block_size = 1024
    
        sha256 = hashes.Hash(hashes.SHA256())
        sha3_224 = hashes.Hash(hashes.SHA3_224())
        md5 = hashes.Hash(hashes.MD5())

        chunk = 0
        while chunk != b'':
            block = f.read(block_size)
            if not block:
                break
            
            sha256.update(block)   
            sha3_224.update(block)      
            md5.update(block)
            
        digest256 = sha256.finalize().hex()
        digest3_224 = sha3_224.finalize().hex()
        digestmd5 = md5.finalize().hex()
            
        
        # Verify the hash values
        sha256_verified = digest256 == sha256_hash
        sha3_224_verified = digest3_224 == sha3_224_hash
        md5_verified = digestmd5 == md5_hash
        
        # Print the results
        print(f'{filename}:')
        print(f'SHA256: {sha256_hash}, {digest256}, {sha256_verified}')
        print(f'SHA3-224: {sha3_224_hash}, {digest3_224}, {sha3_224_verified}')
        print(f'MD5 :{md5_hash}, {digestmd5}, {md5_verified}')
        print()
