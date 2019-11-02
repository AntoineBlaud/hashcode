import threading

class Score(threading.Thread):

    def __init__(self,filenameIN, filenameOUT):
        threading.Thread.__init__(self)
        self.filenameIN = filenameIN
        self.filenameOUT = filenameOUT


    def run (self):

        while False:
            # load file infos
            fIN = open(self.filenameIN,'r')
            fOUT = open(self.filenameOUT,'r')
            fIN_lines = fIN.readlines()
            fOUT_lines = fOUT.readlines()

            for line in fOUT_lines:
                print(line)

        #print("score OK")





        


