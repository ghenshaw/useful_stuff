

def make(string,FILE_NAME):
    '''
    Creates a .typ file from a string.
    This file serves as  a typing
    lesson used by the program gtypist
    '''
    lines = string.split("\n")
    f = open(FILE_NAME,"w")
    f.write("S:\n")
    for line in lines: 
        f.write(" :"+line+"\n")

