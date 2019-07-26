#! /usr/bin/python3
import sys, random , os
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from os.path import exists


'''
this script will take a file path on input argument and create new crypted file 
with a given password aswell
./crypting.py -[OPTION] [FILE]
Options : 
    -E --> Encrypting
    -D --> Decrypting

'''
#This will be the function that encrypt the file
def encryptor(key_ , in_file_):

    chunk_SIZE_ = 64*1024  

    #the name of the output file (with a .sid extention coz that's my name)
    out_file_ = in_file_ + '.sid' 
    
    #Getting a random initialisation vector
    init_vector = get_random_bytes(16)  
    #creating a new encrypt AES object
    encryptor_ = AES.new(key_ , AES.MODE_CBC, init_vector) 
    
    with open(in_file_, 'rb') as input_: 
        with open(out_file_, 'wb') as output_:

            #writing the initialisation vector on the first 16 bytes of the file 
            #coz we'll need it to decrypt it
            output_.write(init_vector) 

            while True:
                chunk_ = input_.read(chunk_SIZE_)

                #break if there's no chunk to be writen
                if len(chunk_) == 0: 
                    break 
                elif len(chunk_) % 16 != 0:
                    #Adding some blank spaces coz the string lenght should be a multiple of 16
                    chunk_ += b" "*(16 - (len(chunk_)%16))

                #writing the encrypted copy of the chunk and we're done
                output_.write(encryptor_.encrypt(chunk_))

     #Asking the user if he want to delete the original file
     delete_original(in_file_)


def decryptor(key_ , encrypted_file):
    chunk_SIZE = 64*1024

    #restoring the originale name of the file ( deleting my name from the file lol !!)
    decrypted_file = encrypted_file[:-4]

    with open(encrypted_file, 'rb') as input_ :

        #reading the initialisation vector from the first 16 bytes of the encrypted file, coz we always store it there
        init_vector = input_.read(16)

        #creating a new AES decrypt object, blabla
        decryptor_ = AES.new(key_ , AES.MODE_CBC , init_vector) 
        with open(decrypted_file, 'wb') as output_ :
            while True :
                
                #reading the chunks from the file
                chunk_  = input_.read(chunk_SIZE)  
                
                #break if there's no information left on the file
                if len(chunk_) == 0:
                    break 

                #in the decrypting process we haven't to verify the case where the chunk size isn't a multiple of 16,
                #the encrypted file comes always with a size multiple to 16
                output_.write(decryptor_.decrypt(chunk_))

    #Asking the user if he want to delete the encrypted file ( the XXXX.sid thing )
    delete_original(encrypted_file)

#this function take your password in inpute and returns a hashed key ( 16 bytes )
def get_key_ (password_):
    hasher_ = SHA256.new(password_.encode('utf-8'))
    return hasher_.digest()

def delete_original(file_):
    while True :
        choice_ = input(f'Do you want to delete {file_} ? (Y/n)')
        if choice_.upper() == 'Y' :
            os.remove(file_)
            break
        elif choice_.upper() == 'N' :
            break


def main():
    #print(len(sys.argv))

    #Making sur that the user gives us enough parameters
    if len(sys.argv) != 3 :
        print ('''ERROR 1 : Invalide arguments !
        ./encrypt.py -[OPTION] [FILE]
        Options : 
            -E --> Encrypt
            -D --> Decrypt''')
        sys.exit()
    file_ = sys.argv[2]
    option_ = sys.argv[1]
    
    #Verfying if the option_ is valid -- the only two valid options are -D (for decrypt) and -E (for encrypt)
    if option_ != '-D' and option_ != '-E' :
        print ('''ERROR 2 : Invalide arguments !
        ./encrypt.py -[mode] [filepath]
        mode : 
            -E --> Encrypt
            -D --> Decrypt''')
        sys.exit()

    #Verifying that the file exists
    #If file_ don't exists the user is asked to provide a valide path
    elif not exists(file_):
        print (f'{file_} don\'t exists, try again with a valide path')
        sys.exit()

    #Calling the right function to do the job
    #decryptor_() to decrypt -- encryptor_() to encrypt
    if option_ == '-D':
        password_ = input('Enter your password (the wrrong file will give an inreadable file) : ')
        key_ = get_key_(password_)
        decryptor(key_ , file_)

    elif option_ == '-E':
        password_ = input('Enter your password : ')
        key_ = get_key_(password_)
        encryptor(key_ , file_)

    else:
        sys.exit()

#ENd of the main function


if __name__ == '__main__':
    main()
#I think it's working pretty well
#if u find any bugs or mistakes please contact me on my email : eio.hmdn@gmail.com
#I'm still an amateur like u see
#and sorry for the bad english, and the odd comments
#peace
