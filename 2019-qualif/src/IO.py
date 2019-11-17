import os
import sys
import copy
import json

class IO():


    def __init__(self,filename):
        self.filename = filename;
        self.array = []

    
    def fileToArray(self, removeItem={}, ignoreLine={}):
        # Read file
        f = open(self.filename,"r")

        # Item number
        i = 0
        # Line counter for Ignore Line
        reader = 0
        for line in f:
            # Treat only intersesting Line
            if(reader  not in ignoreLine):
                #Transform line into arrray
                buffer = line.split(' ')

                #Delete useless item
                for j in removeItem:
                    buffer.pop(j)

                #insert item ID at start
                buffer.insert(0,i)
                #Remove \n 
                buffer[len(buffer)-1] = buffer[len(buffer)-1][:-1]
                # Add buffer to array
                self.array.append(buffer)
                i+=1
            

            reader+=1


        return self

    def compileOutputH(self,filesIN,fileOut):

        out = open(fileOut,'w')
        for file in filesIN:
            f = open(file,'r')
            j = json.load(f)
            d = j["array"]
            for im in d:
                out.writelines(str(im[0])+"\n")

        out.close()
        f.close()


    def compileOutputV(self,filesIN,fileOut):

        out = open(fileOut,'w')
        for file in filesIN:
            f = open(file,'r')
            j = json.load(f)
            d = j["array"]
            i = 0
            while i < len(d)-2:
                im1 = d[i];
                im2 = d[i+1];
                out.writelines(str(im1[0]) +" " + str(im2[0])+"\n")
                i = i+2

        out.close()
        f.close()

    def compileOutputHVV(self,filesIN,fileOut):

        out = open(fileOut,'w')
        for file in filesIN:
            f = open(file,'r')
            j = json.load(f)
            d = j["array"]
            i = 0
            while i < len(d)-2:
                im1 = d[i];
                im2 = d[i+1];
                im3 = d[i+2];
                out.writelines(str(im1[0])+"\n")
                out.writelines(str(im2[0])+ " " + str(im3[0])+"\n")
                i = i+3

        out.close()
        f.close()