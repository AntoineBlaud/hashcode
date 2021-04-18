import random
import time
#declare list 
imageNumber = 0
image_name = []
image_number_tags = []
image_tags = []
image_type = []
image_collaped_same_tags = []
import time

def getImages(filename):

    global imageNumber
    global image_name
    global image_number_tags
    global image_tags
    global image_type
    global image_collaped_same_tags


    f = open(filename,"r")
    line_index = 0
    for line in f:

        line = line.replace("\n", "")
        

        if(line_index==0):
            number = line.split("\n")[0]
            imageNumber = int(number)


        else:
            word_index = 1
            tmp_tags_list = []
            for word in line.split(" "):

                if(word_index == 1):
                    image_type.append(word)

                elif(word_index == 2):
                    image_number_tags.append(word)

                elif(word_index > 2):
                    tmp_tags_list.append(word)
                word_index+=1

            image_tags.append(list(tmp_tags_list))

        line_index +=1

        if(line_index>0):
            image_name.append(line_index-1)





def countCollapse2ImageTags(pos1,pos2):
    tags_1 = image_tags[pos1]
    tags_2 = image_tags[pos2]
    counter = 0
    if(len(tags_1) > len(tags_2)):
        tags_min = tags_2
        tags_test = tags_1
    else:
        tags_min = tags_1
        tags_test = tags_2

    for tag in tags_min:
        if tag in tags_test:
            counter+=1
    return counter

def countCollapseImageTags(pos1,pos2):
    # retourne la nouvelle valeur en cas de déplacement

    if(pos2>pos1+1):
        return countCollapse2ImageTags(pos1,pos2) + countCollapse2ImageTags(pos1,pos2-1)
    elif(pos2 == (pos1+1) and pos1>1):
        return countCollapse2ImageTags(pos1,pos2) + countCollapse2ImageTags(pos1,pos1-1)
    else:
        return countCollapse2ImageTags(pos1,pos2)

def countCollapseImageTagsPos(pos):
    # on retoune la valeur de la position 
    if(pos>0):
        return countCollapse2ImageTags(pos,pos + 1) + countCollapse2ImageTags(pos,pos - 1)
    else:
        return countCollapse2ImageTags(pos,pos + 1)




def move(pos1,pos2):

    image_name.insert(pos2,image_name.pop(pos1))
    image_type.insert(pos2,image_type.pop(pos1))
    image_tags.insert(pos2,image_tags.pop(pos1))


def init():
    tmp = []
    for i in range(0,imageNumber - 1):
        tmp.append(countCollapse2ImageTags(i,i+1))

    return tmp


def train(rank):
    global imageNumber
    
    sub_1 = 0
    sub_2 = imageNumber - 3
    counter = 0

    for image in range(sub_1,sub_2):
        counter+=1
        if(counter%5000==0):
            print(countScore())
            time.sleep(1)

        current_value = countCollapseImageTagsPos(image)
        i = 0
        #print("image:" + str(image) + " sur:" + str(sub_2)) 
        number_test = int(imageNumber/(5*rank))
        while (i < number_test):
            pos = random.randint(0,imageNumber-2)
            if(pos!=image):
                a = countCollapseImageTags(image,pos)
                b = countCollapseImageTagsPos(pos)
                if(a > max(current_value, b)):
                    move(image,pos)
                    print("Founded !")
                    break
            i+=1
            if(i==number_test and current_value < 1):
                image_name.pop(image)
                image_type.pop(image)
                image_tags.pop(image)
                imageNumber-=1
                #image_collaped_same_tags = init()
                print("poped")

            

            






def loopTrain(n):
    global imageNumber
    for i in range(2,n):
        print("loop:" + str(i))
        print("Image :" + str(imageNumber))
        print(countScore())
        time.sleep(0.5)
        train(i)

def countScore():
    score = 0
    image_collaped_same_tags = init()
    for i in range(0,len(image_collaped_same_tags)):
        score+=image_collaped_same_tags[i]
    return score

def writeScore():
    f2 = open("out","w")
    f2.write(str(imageNumber))
    for i in range(0,imageNumber):
        f2.write(str(image_name[i]) +"\n")
    f2.close()

getImages("b_lovely_landscapes.txt")
print(countScore())
loopTrain(600)
print(countScore())
writeScore()





