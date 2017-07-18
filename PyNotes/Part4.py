#Ministry of Silly Codes July 2017
#Part4

#Files and Strings

#Opening and closing files

#myfile = open("filename", "r") r = read, w = write, a = append  Writing/appending creates file 
#if it doesn't exist.  Write overwrites the file if it exists.  To close call the 
#close function on the variable name

#Get info from mydata.txt and save to results.txt
infile = open("mydata.txt", "r")
outfile = open("results.txt", "w")

#same as
with open("mydata.txt", "r") as infile:
    with open("results.txt", "w") as outfile:
        #Do stuff
infile.close()
outfile.close()

#Writing (Strings only. One at a time. No automatic /n)
myfile = open("filename", "w")
myfile.write("This line is written to the file.") #"This" + str(1) +"line is written."
myfile.close()

#Reading (line at a time)
myfile = open("filename", "r")
lineFromFile = myfile.readline()
secondLine = myfile.readline()
myfile.close()

#Reading(whole files)
myfile = open("filename", "r")
for lineFromFile in myfile:
    #do stuff
myfile.close()

#Also (file as one string)
myfile = open("filename", "r")
fileToString = myfile.read()
myfile.close()

#All these functions can be ran on binary files with open("filename", "rb") "wb", or "ab"

#Split
a, b, c = lineFromFile.split("delimiter")
phone = "888-222-5555"
area, pref, suff = phone.split("-")
print("("+area+")"+pref+"-"+suff)
#>>>(888)222-5555