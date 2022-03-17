import os #import the operating system for python to use
#creating a function that renames multiple files

#first of all create a funtion contining 'i'
def main(): #brackets are empty as it doesn't have to take any parameter and use def to create the function
    i = 0 #set i to 0, as a default all the files in the folder are 0
    path = "C:/Users/Edmun/Documents/Python Projects/Images/"   #Specify the path which is the directory in which the folder is
                                                                #and where python will look for the files. Change everything to 
                                                                #a forward slash as if it is a backslash it will create an 
                                                                #error message. Don't forget to add a backslask to the end
    for filename in os.listdir(path): #Create a for loop to loop through all the files from the specified path and storing 
                                      #as a list 
        my_dest = "img" + str(i) + ".jpg" #Create a variable called my_dest to give the final name and where the name will begin  
                                         #with image and then add a number i and finally save them as a .jpg file
        my_source =path + filename 
        my_dest =path + my_dest
        os.rename(my_source, my_dest) #the renaming function, (source, destination)
        i += 1 #looping through each iteration/file in order by 1

if __name__ == '__main__': #use the if statement to run the function
    main()        
        
                                                       
                                                        