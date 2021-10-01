import string
alphabet = string.ascii_lowercase           #"abcdefghijklmnopqrstuvwxyz"

def decrypt():
    # taking the input of the encrypted message/ciphertext from the user
    encrypted_message = input("Enter the encrypted_message/ciphertext : ").strip() 
    print()
   
    for key in range(26):  #brute forcing all the keys .. as caesar cipher contains 26 keys (0-25)
    
        decrypted_message = ""
    
        for c in encrypted_message: #decrypting the ciphertext for a specific key
    
            if c in alphabet:
                position = alphabet.find(c)  #locating the position of the ciphertext in the alphabet series
                new_position = (position - key) % 26 #using the decrypting algorithm
                new_character = alphabet[new_position]  #replacing old character with new one
                decrypted_message += new_character        #appending the decrypted_message
            else:
                decrypted_message += c
        print("Key %s : %s" %(key,decrypted_message))         #printing the decrypted_message for all the keys


decrypt() #calling the function