from Image import Image

class DataImage:



    def __init__(self):
       self.images = []


    def readData(self,filename,x,y):
        self.file = open(filename, "r")
        self.line_index = x
        lines = list(self.file)

        while self.line_index < y:
            line = lines[self.line_index]
            # La premiere ligne donne le nombre d'images
            if (self.line_index == 0):
                number = line.split("\n")[0]
                self.inputImageNumber = int(number)
            else:
                im = Image()
                im.name = self.line_index - 1
                im =self.extractImageInfos(line, im)
                self.images.append(im)

            self.line_index += 1

    def writeScore(self,filename, start=False, imageNumber=0):
        if(start):
            f2 = open(filename, "w")
            f2.write(str(imageNumber))
        else:
            f2 = open(filename, "a")

        for i in range(0, len(self.images)):
            f2.write(str(self.images[i].name) + "\n")
        f2.close()

    def extractImageInfos(self,line, im):

        line = line.replace("\n", "")

        # ici on recupere toute les tags de la ligne
        word_index = 1
        tmp_tags_list = []
        for word in line.split(" "):

            if (word_index == 1):
                im.type = word

            elif (word_index == 2):
                im.numberTags = word

            elif (word_index > 2):
                tmp_tags_list.append(word)
            word_index += 1

        im.tags = list(tmp_tags_list)
        # on ajoute le nom de l'image
        im.name = self.line_index - 1
        return im

    def getImage(self,i):
        return self.images[i]

    def pushImage(self,im):
        self.images.append(im)

    def popImage(self,i):
        res = self.images[i]
        self.images.remove(res)
        return res

    def move(self,old_pos, new_pos):
        images.insert(new_pos, images.pop(old_pos))

    def getLastImage(self):
        return self.images[len(self.images) - 1]

 

