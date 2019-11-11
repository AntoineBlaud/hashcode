from Node import Node
import re
import copy
class IO():

    def __init__(self, filename):
        self.filename = filename
        self.NcompiledFiles = None
        self.NtargetsFiles = None
        self.NavailableServers = None

        #Only nodes
        self.compiledFiles = {}
        # Graph représentation (node have childrens)
        self.targetsFiles = []

    
    def getData(self):
        f = open(self.filename, 'r')
        infos = f.readline().split(" ")

        self.NcompiledFiles = infos[0]
        self.NtargetsFiles = infos[1]
        # delete \n
        self.NavailableServers = infos[2][0]

        for i in range(0,int(self.NcompiledFiles)):
            #Get file infos
            line = f.readline()
            infos = line.split(" ")
            # infos[0] = name
            node = Node(infos[0])
            node.addToPack("cT",infos[1])
            node.addToPack("rT",infos[2][0])
            #Get files dependencies 
            line =f.readline()
            line = re.sub("\n","",line)
            line = line.split(" ")[1:]
            for dependencies in line:
                #Get the node
                d = self.compiledFiles[dependencies]
                node.add(dependencies,d)
            self.compiledFiles[infos[0]] = node
        
        for i in range(0,int(self.NtargetsFiles)):
            line = f.readline()
            line = re.sub("\n","",line)
            infos = line.split(" ")
            cFile = self.compiledFiles[infos[0]]
            cFile.target = True
            cFile.addToPack("deadline",int(infos[1]))
            cFile.addToPack("points",int(infos[2]))
            self.targetsFiles.append(cFile)

        return self.targetsFiles
        






        