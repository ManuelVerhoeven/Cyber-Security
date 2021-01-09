#!/usr/bin/python

import crypt

def testPass(hashlist):
    salt = hashlist[0:11] #seperate the salt value from hash, sha512 is 11 characters.
    #print ('[+] Salt: ' +salt) to check if the correct salt value was being seperated
    pwdList = open('200words.txt','r') #load in the wordlist im using
    for pwd in pwdList.readlines(): #going through the txt file line by line 
            pwd = pwd.strip('\n')
            hashAlgo = crypt.crypt(pwd,salt)
            #print ('[+] Encryption to match: ' +hashlist) the encryption that im trying to match again for testing purposes
            #print ('Word encrypted: ' +pwd) word from wordlist that im encrypting 
            #print ('[+] Hash value: ' +hashAlgo) the encrypted form of the word from word list that i 
            if hashAlgo == hashlist: #comparing if encrypted word from word list is the same as the one from the shadow file
                print ('[*] Password: '+pwd+ '\n')
                return
    print ('[-]Password not found.\n')
    return

def main():
    hashlist = open('shadow.txt','r') #loading in the shadow file and its hashs
    for line in hashlist.readlines(): # going through it line by line
        if ':' in line: #seperating the user from the hashed password
            user = line.split(':')[0]
            hashlist = line.split(':')[1].strip(' ')
            print ('[*]Attempting to crack password for: ' +user)
            testPass(hashlist)
            
if __name__ == '__main__':
    main()
    

 
 
