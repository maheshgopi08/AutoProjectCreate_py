#To automate the project creation

import sys
import os
#from github import Github

#creating a folder in the respective project directories

#path= "c:/users/administrator/documents/" #Defeault directory to store the differerent projects

username = "maheshgopi08" #Insert your github username here
password = "" #Insert your github password here



def create():
    
    print((sys.argv[1:]))
    folderName = str(sys.argv[1])
    if("py" in folderName ):    #Condition for python
        path="c:/users/administrator/documents/python/"
    if("fl" in folderName ):    #Condition for flutter
        path="C:/src/projects/"
    
    

    
    os.makedirs(path + str(folderName))

    #user = Github(username, password).get_user()
    #repo = user.create_repo(folderName)
    #print("Succesfully created repository {}".format(folderName))


if __name__ == "__main__":
    create()