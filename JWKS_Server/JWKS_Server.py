import json
from flask import Flask, jsonify, request
import rsa
import jwt
import datetime


app = Flask(__name__)

# Will store RSA keypair  
keypairs = {}

def get_valid_keypair(key_id):
    if key_id in app.keypairs:
        kp = app.keypairs[key_id]
        if kp['expires'] > datetime.datetime.now():
            return kp
        
def get_expired_keypair():
    # Return an expired key
    for kp in app.keypairs.values():
        if kp['expires'] < datetime.datetime.now():
            return kp
            
@app.route('/.well-known/jwks.json')
def jwks():
    # Construct JWKS from unexpired keys
    keys = []
    
    for key_id, kp in app.keypairs.items():
        if kp['expires'] > datetime.datetime.now():  
            keys.append({
              'kid': key_id,
              'kty': 'RSA',
              'e': encode_key(kp['public_key'].e),  
              'n': encode_key(kp['public_key'].n),
            })
    
    jwks = {'keys': keys}
    return jsonify(jwks)

@app.route('/auth')
def auth():   
    key_id = request.args.get('key_id') 
    expired = request.args.get('expired','').lower() == 'true'
    
    if expired:
        kp = get_expired_keypair()
    else:
        kp = get_valid_keypair(key_id)
        
    if not kp:
        return jsonify({'error':'Invalid keypair'})
    
        
    
