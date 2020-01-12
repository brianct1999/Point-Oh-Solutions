#########################################
#                                       #
#   Simple login script to access       #
#   encrypted files within a specified  #
#   directory.                          #
#                                       #
#   Created by Brian Thomas, 1/11/2020  #
#                                       #
#########################################


import hashlib
import sys
import pdb
import io

#Fancy prompt garb I thought looked cool :)
IN = "\n:: "
OUT = "\n== "
ERR = "\n=E= " 

def start():

    #Check if users exist, if not create new user. Used the convoluted open/close statements as i got unexpected errors without doing so
    f = open("users.dat", "r")
    if(f.readline() == ""):
        file.close(f)
        f = open("users.dat", "w")
        print OUT + "No user found. Create new user? (y/n)"
        
        x = raw_input(IN)
        if(x == "y"):
            createUser()
            login()
        elif(x == "n"):
            print OUT + "Goodbye!\n"
            quit()
        else:
            print ERR + "Invalid response"
    #If previous user exists, proceed to login
    login()
        

def createUser():

        #Open files for writing, and store both user and password hashes in respective files
        userf = open("users.dat", "a")
        pswdf = open("pass.dat", "a")
        
        
        
        print OUT + "Enter username:"
        user = hashlib.sha256(raw_input(IN).strip('\n')).hexdigest() 
        userf.write(user + '\n')
        print OUT + "Create a strong password"
        pswd = hashlib.sha256(raw_input(IN).strip('\n')).hexdigest()
        pswdf.write(pswd + '\n')
        print OUT + "User created successfully\n"

def login():

    
    print OUT + "Please enter your username and password"
    
    #Line index to iterate through files, both files should have same amount of lines
    lineCount = 0
    
    with open('users.dat', 'r') as f:
        for i in f:
            lineCount += 1
    
    userf = open("users.dat", "r")
    pswdf = open("pass.dat", "r")
    user = hashlib.sha256(raw_input(IN)).hexdigest()
    pswd = hashlib.sha256(raw_input(IN)).hexdigest()
    
    #Iterate through each file using index i, comparing stored hashes against entered credentials
    #Couldnt use a for loop, index out of range error occured, used a while loop to forgoe this
    i = 0
    while(i < lineCount):
        
        #Separate Checksum string variable to prevent readline() counter from resetting in if statement
        userChksum = userf.readline().strip('\n')
        pswdChksum = pswdf.readline().strip('\n')
        if(userChksum == user and pswdChksum == pswd):
            
            #log in and proceed to main loop
            print OUT + "Logged in successfully"
            mainLoop()
        i += 1
    print ERR + "Incorrect username/password"
    start()
   
    
def mainLoop():
        pass
        sys.exit()
        #Code to be added here. 
        #program will encrypt files with encrypted username and password, 
        #used to store secure files that cannot be accessed without the AES key

    

#Entry point, used for debugging, will be deprecated upon finished product      
#start()
