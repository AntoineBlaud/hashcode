
class Evalue:

    @staticmethod
    def countCollapse2ImageTags(tags_1,tags_2):
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

