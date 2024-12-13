from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import hashlib
from Crypto.PublicKey import RSA

# Hash the image
def hash_image(image_path):
    with open(image_path, 'rb') as f:
        image_data = f.read()
    return hashlib.sha256(image_data).hexdigest()

# Verify the signature using the public key
def verify_image(image_path, public_key_path, signature_path):
    hash_value = hash_image(image_path)

    # Load the public key
    with open(public_key_path, 'rb') as f:
        public_key = RSA.import_key(f.read())

    # Load the signature
    with open(signature_path, 'rb') as f:
        signature = f.read()

    # Verify the signature
    hash_obj = SHA256.new(hash_value.encode())
    try:
        pkcs1_15.new(public_key).verify(hash_obj, signature)
        print("Signature is valid. The image is authentic.")
    except (ValueError, TypeError):
        print("Signature is invalid. The image may have been tampered with.")

# Main function
if __name__ == "__main__":

    # Replace with the paths to your files
    IMAGE_PATH = input("Name of Image: ")
    PUBLIC_KEY_PATH = "public.pem"
    SIGNATURE_PATH = "signature.bin"

    # Verify the image
    verify_image(IMAGE_PATH, PUBLIC_KEY_PATH, SIGNATURE_PATH)

