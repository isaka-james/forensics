from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import hashlib

# Hash the image
def hash_image(image_path):
    with open(image_path, 'rb') as f:
        image_data = f.read()
    return hashlib.sha256(image_data).hexdigest()

# Sign the hash using the private key
def sign_image(image_path, private_key_path):
    hash_value = hash_image(image_path)

    with open(private_key_path, 'rb') as f:
        private_key = RSA.import_key(f.read())
    hash_obj = SHA256.new(hash_value.encode())
    signature = pkcs1_15.new(private_key).sign(hash_obj)

    with open("signature.bin", "wb") as sig_file:
        sig_file.write(signature)
    print("Image signed and signature saved as signature.bin")

# Main function
if __name__ == "__main__":
    # Replace with the path to your image
    IMAGE_PATH = "udom.jpg"


    # Step 2: Sign the image
    sign_image(IMAGE_PATH, "private.pem")

