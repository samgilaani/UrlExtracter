def read_file(file_name):
    file = open(file_name,"r")
    content = file.read()
    file.close()
    return content

def url_finder(text):
    list_of_urls = []
    splited_text = text.split('href="')
    del(splited_text[0])
    for i in splited_text :
        list_of_urls.append(i.split('"')[0])
    return list_of_urls

def line_printer(list_to_print,file_name):
    try :
        file = open(file_name,"w")
        for line in list_to_print :
            file.write(line+"\n")
        file.close()
        return True
    except :
        return False
    
