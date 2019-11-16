
#  Import Tree modules
from Node import Node
from Leaf import Leaf
from Root import Root


def main():

    t = Root("Racine")
    t.createNode("Antoine")
    t.createNode("Loic")
    t.createNode("Caca")
    t.createNode("Deee")

    s = t.childrens["Antoine"]
    s.createNode("PAPA")

    r  = t.childrens["Loic"]
    r.createNode("MAMAN")

    u = s.childrens["PAPA"]
    u2 = r.childrens["MAMAN"]

    #print(Node.inDeepthSearch(t,"MAMAN"))
    


main()
