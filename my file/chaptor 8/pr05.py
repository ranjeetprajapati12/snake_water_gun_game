# a= "   my name is khan   "
# print (a)
# print(a.strip())

def remove_strip(string,word):
    a=string.replace(word," ")
    return a.strip()
y="ram is a good boy"
y=remove_strip(y,"ram")
print(y)


#a.lstrip()
#a.rstrip()
#a.strip()
