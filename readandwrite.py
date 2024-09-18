#open file to read

# employee_file =  open("file_name.txt", "r") #to read the file

# print(employee_file.readable()) # tells whether the is readable or not return true/false
# print(employee_file.read()) # displayes content in file
# print(employee_file.readlines()) # reads line by line and puts them in an array
# print(employee_file.readlines()[1]) # to read line by line access the index

# for emoloyee in employee_file.readlines():
#     print(emoloyee)
# employee_file.close() #to close the file



#appending in file
# employee_file =  open("file_name.txt", "a") #append 
# print(employee_file.write("yaayy"))

# print(employee_file.write("\nokayy"))

# employee_file.close()


#writing  in file
employee_file =  open("file_name.txt", "w") #writing means overriding in the file
print(employee_file.write("yaayy"))
# employee_file =  open("file_name.txt1", "w") #new file
employee_file =  open("index.html", "w")
employee_file.write("<p>This is HTML</p>")
employee_file.close()