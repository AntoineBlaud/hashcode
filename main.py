

#declare list 
imageNumber = 0
image_name = []
image_number_tags = []
image_tags = []
image_type = []

def getImages(filename):
    f = open(filename,"r")
    line_index = 1
    for line in f:

        line = line.replace("\n", "")
        image_name.append(line_index)

        if(line_index==1):
            number = line[0]
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



getImages("a_example.txt")
print("hllo")


