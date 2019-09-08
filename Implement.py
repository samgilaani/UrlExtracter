from URL_EXTRACTER import *

i_file_name = input("Enter the html file name (ex. main.htm) : ")
o_file_name = input("Enter the result file name (ex. result.txt): ")
text = read_file(i_file_name)
list_of_urls = url_finder(text)

if line_printer(list_of_urls,o_file_name) :
    print("success !")
else :
    print("sth went wrong !")
