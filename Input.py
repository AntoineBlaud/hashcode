import os
import sys
import copy

class Input():


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




    '''
    Depreciate, it's not unique
    '''
    def hashArray(self,ignoreItem={}, ignoreLine={}):

        i_line = 0
        i_item = 0

        self.array_hashed = copy.deepcopy(self.array)
        for x in self.array:
            # if we don't want line
            if(i_line not in ignoreLine):
                for y in x:
                    #if we don't want item
                    if(i_item not in ignoreItem):

                        self.array_hashed[i_line][i_item] = int(hash(self.array[i_line][i_item]))
                    i_item+=1
            i_item = 0
            i_line+=1



        return self







