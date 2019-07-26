# pycrypt
this script encrypt and decrypt files using AES technology comming with the [pycrypto](https://pypi.org/project/pycrypto/) liberary in python.

# Requirements
pycrypto liberary must be installed on your machine. 
just run the following commande :

```bash
pip install pycrypto
```
Or:
```bash
pip install requirements
```

# Usage
```bash
$./crypting.py -[OPTION] [FILE]
```

# Encrypting
```bash
$./pycrypt.py -E file.xxx
Enter your password : xxxxxxx
$
```
you'll find the encrypted file (.sid file) in the same directory

# Decrypting
```bash
$./pycrypt.py -D file.xxx.sid
Enter your password (the wrrong file will give an inreadable file) : xxxxxxx
$
```
