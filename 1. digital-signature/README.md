### Signing and Verifying Images**

This project shows how to sign an image using a private key and verify it using a public key. The user will be asked to input the path of the image when running the scripts.

---

### **Setup**

**Install the required package:**
   ```bash
   pip install pycryptodome
   ```

---

### **Generate Keys**
1. **Generate a private key:**
   ```bash
   openssl genrsa -out private.pem 2048
   ```

2. **Generate a public key from the private key:**
   ```bash
   openssl rsa -in private.pem -pubout -out public.pem
   ```

---

### **Usage**

#### 1. **Sign the Image**
   Run the script to sign an image:
   ```bash
   python3 sign_image.py
   ```

   - When prompted, enter the full path to your image (e.g., `example.jpg`).
   - The script will use the private key (`private.pem`) to sign the image and create a file named `signature.bin`.

#### 2. **Verify the Image**
   Run the script to verify the image and its signature:
   ```bash
   python3 verify_image.py
   ```

   - When prompted, enter the full path to your image and the signature file (`signature.bin`).
   - The script will use the public key (`public.pem`) to verify the image.

---

### **Result**
- If the image is valid, the script will say:
  ```
  Signature is valid. The image is authentic.
  ```
- If the image or signature is tampered with, it will say:
  ```
  Signature is invalid. The image may have been tampered with.
  ```

---

### **Notes**
- Keep `private.pem` secret to ensure security.
- Share `public.pem` with others to verify the signature.
