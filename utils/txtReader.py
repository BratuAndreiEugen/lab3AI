def textReader(path):
    with open(path) as f:
        array = []
        #matrix = []
        for line in f:  # read  lines
            edge = [int(x) for x in line.split()]


textReader("C:\Proiecte SSD\Python\lab3AI\\networks\\extraTests\\emails.txt")