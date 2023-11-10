def remove_and_strip(string,value):
    string = string.replace(value,'')
    return string.strip()
var="   Fucking Nazi Bitch!    "
print(remove_and_strip(var,'Nazi'))