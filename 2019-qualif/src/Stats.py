from collections import *
import operator

class Stat():

    def __init__(self, array, depth = 1, removeItemIndepth1 = {},
     removeItemIndepth2 = {},removeItemIndepth3 = {}):
        self.input_array = array
        if(depth > 3 or depth < 1):
            raise ValueError("Incorrect depth value")
        self.depth = depth
        self.removeItemInDeeth1 = removeItemIndepth1
        self.removeItemInDeeth2 = removeItemIndepth2
        self.removeItemInDeeth3 = removeItemIndepth3




    def countOccurences(self):

        self.occurences = {}

        SIZE_1 = len(self.input_array)
        for x in range(0,SIZE_1):
            if(x not in self.removeItemInDeeth1):
                if(self.depth > 1):
                    SIZE_2 = len(self.input_array[x])
                    for y in range(0,SIZE_2):
                        if(y not in self.removeItemInDeeth2):

                            if(self.depth > 2):
                                SIZE_3 = len(self.input_array[x][y][z])
                                for z in range(0,SIZE_3):
                                    if(z not in self.removeItemInDeeth3):
                                        # --------Depth = 3---------
                                        if(self.input_array[x][y][z] in self.occurences):
                                            self.occurences[self.input_array[x][y]][z] = self.occurences[self.input_array[x][y][z]] + 1

                                        else:
                                            self.occurences[self.input_array[x][y][z]] = 1
                            
                             #-------Depth = 2---------
                            else:
                                if(self.input_array[x][y] in self.occurences):
                                    self.occurences[self.input_array[x][y]] = self.occurences[self.input_array[x][y]] + 1

                                else:
                                    self.occurences[self.input_array[x][y]] = 1
                #---------Depth = 3----------
                else:
                    if(self.input_array[x] in self.occurences):
                        self.occurences[self.input_array[x]] = self.occurences[self.input_array[x] + 1]

                    else:
                        self.occurences[self.input_array[x]] = 1

        return self

    def orderOccurences(self):

        self.ordered = OrderedDict(sorted(self.occurences.items(), reverse = True, key=lambda t: t[1]))
        return self












    
    