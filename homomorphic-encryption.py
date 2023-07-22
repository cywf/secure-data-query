# Homomorphic Encryption: Homomorphic encryption allows computations to be performed on encrypted data without decrypting it. The encrypted data remains confidential, and the results of the computations are also encrypted. This way, the data owner can perform computations on encrypted data without revealing the plaintext to third parties.

from phe import paillier

# Generate public and private keys
public_key, private_key = paillier.generate_paillier_keypair()

# Original data
data = 5

# Encrypt the data
encrypted_data = public_key.encrypt(data)

# Perform computation on encrypted data
encrypted_result = encrypted_data + 7

# Decrypt the result
result = private_key.decrypt(encrypted_result)

print(result)  # Output: 12
