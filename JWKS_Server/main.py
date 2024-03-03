import rsa
import JWKS_Server
import rsa_keys

key1 = rsa.generate_rsa_keypair()
key2 = rsa.generate_rsa_keypair()

keypairs = {
  'key1': key1, 
  'key2': key2
}

JWKS_Server.app.keypairs = keypairs

if __name__ == '__main__':
    JWKS_Server.app.run(port=8080)
