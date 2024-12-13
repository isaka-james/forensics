python3 python3 -m venv assigment
pip install pip install pycryptodome

openssl genrsa -out private.pem 2048
openssl rsa -in private.pem -pubout -out public.pe

python3 sign-image.py
python3 verify-image.py
