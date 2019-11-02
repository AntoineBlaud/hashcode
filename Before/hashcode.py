
from ImageOrganizerHorizontal import ImageOrganizerHorizontal
from DataImage import DataImage


def main():


    print("Recuperation des images")
    a = DataImage()
    a.readData("b_lovely_landscapes.txt", 0, 20000)

    b = DataImage()
    b.readData("b_lovely_landscapes.txt", 20001, 40000)

    c = DataImage()
    c.readData("b_lovely_landscapes.txt", 40001, 60000)

    d = DataImage()
    d.readData("b_lovely_landscapes.txt", 60001, 80000)

    print("Rangement")
    sub_a = ImageOrganizerHorizontal(a,1)
    sub_b = ImageOrganizerHorizontal(b,2)
    sub_c = ImageOrganizerHorizontal(c,3)
    sub_d = ImageOrganizerHorizontal(d,4)

    sub_a.start()
    sub_b.start()
    sub_c.start()
    sub_d.start()

    sub_a.join()
    sub_b.join()
    sub_c.join()
    sub_d.join()

    while(sub_a.end == False or sub_b.end == False or sub_c.end == False or sub_d.end == False):
        pass
    
    print("Enrergistrement des resulats")

    a = sub_a.getResult()
    b = sub_b.getResult()
    c = sub_c.getResult()
    d = sub_d.getResult()

    a.writeScore("out.txt", True, 80000)
    b.writeScore("out.txt")
    c.writeScore("out.txt")
    d.writeScore("out.txt")

    TotalScore = sub_a.countScore() + sub_b.countScore() + sub_c.countScore() + sub_d.countScore()

    print("Score result: " + str(TotalScore))


main()
