from threading import Thread,RLock
from DataImage import DataImage
import random
from Evalue import Evalue


lock = RLock()

class ImageOrganizerHorizontal(Thread):

    # on trie unordonned images au fur et a mesure en utilisant un algorithme glouton
    # a chaque tour on compare les images et on les ajoute dans ordonned_images


    def __init__(self,data,name):
        Thread.__init__(self)
        self.unordonned_images = data
        self.name = name
        self.ordonned_images = DataImage()
        self.end = False
        self.score = 0


    def run(self):

        # On ajoute une image de manière aléatoire
        r = random.randint(0,len(self.unordonned_images.images))
        self.ordonned_images.pushImage(self.unordonned_images.popImage(r))

        
        # tant qu'il reste des images dans unodonned_images
        while(len(self.unordonned_images.images) > 1):
            MAX_SCORE = 0
            MAX_IMAGE_TEST = 1
            self.MAX_TEST = int(len(self.unordonned_images.images)/100)

            s = len(self.ordonned_images.images)
            if(s % 100 == 0):
                with lock:
                    print(str(s) +" traité " + self.name)

            # on compare MAX_TEST images avec la derniere de ordonned_image
            for i in range(0,self.MAX_TEST):
                j = random.randint(0,len(self.unordonned_images.images) - 2)

                im1 = self.ordonned_images.getLastImage()
                im2 = self.unordonned_images.getImage(i)

                tags1 = im1.tags
                tags2 = im2.tags

                score = Evalue.countCollapse2ImageTags(tags1,tags2)
                if(score > MAX_SCORE):
                    MAX_SCORE = score
                    MAX_IMAGE_TEST = j
            
            # j = meilleur image trouvée
            try:
                self.ordonned_images.pushImage(self.unordonned_images.popImage(j))
            except:
                print("Erreur, image inexistante dans unordonned_images")
                print(str(j) + "  " + str(len(self.unordonned_images.images)) )
        self.end = True

    def getResult(self):
        return self.ordonned_images

    def countScore(self):
        i = 0
        c = self.ordonned_images.images
        while (i < len(c)):
            tags1 = c[i].tags
            tags2 = c[i].tags

            self.score += Evalue.countCollapse2ImageTags(tags1,tags2)

            i+=1
        return self.score


            
            




        
