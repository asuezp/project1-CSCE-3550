import rsa
import datetime
import random
import string

def generate_rsa_keypair(bits=2048):
    private_key, public_key = rsa.newkeys(bits)
    
    # Generate a random key ID
    key_id = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    
    # Set the expiry timestamp to 1 year from now
    expiry = datetime.datetime.now() + datetime.timedelta(days=365)
    
    return {
        'private_key': private_key, 
        'public_key': public_key,
        'key_id': key_id,
        'expires': expiry
    }

keypair = generate_rsa_keypair()
print(keypair)
