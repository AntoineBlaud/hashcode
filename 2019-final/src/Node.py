import uuid
from queue import Queue

class Node: 

    def __init__(self, name,father=None):

        self.father = father
        self.name = name
        self.childrens = {}
        self.packs = {}
        self.uuid = uuid.uuid4()
        self.branchValue = {}
        # Only for this project
        self.target = False
        self.visited = []
        self._initDeepth()



    def __str__(self):
        s = self.name + "   "
        for node in self.childrens.values():
            s+=node.__str__()
        return s

    def __repr__(self):
        return self.name

    def _initDeepth(self):
        if(self.father == None):
            self.deepth = 0
        else:
            self.deepth = self.father.getDeepth() + 1


    def add(self, name, node):
        '''
             a element to children's node
        '''
        self.childrens[name] = node

    def createNode(self, name):
        '''
        Create node and add to children
        '''
        node = Node(self, name)
        self.childrens[name] = node

    def _update(self):
        '''
        Update Deepth value after move 
        '''
        self.deepth = self.father.getDeepth() + 1
        # parcourir element en dessous et update


    def getDeepth(self):
        '''
        Get deepth
        '''
        return self.deepth

    def createLeaf(self, name):
        '''
        Create lead and add to children
        '''
        leaf = Leaf(self, father, name)
        self.childrens[name] = leaf

    def setBranchValue(self, value, node):
        '''
        Set a value between the father and the current value
        '''
        if(node in self.childrens.values):
            self.branchValue[node] = value
        else:
            raise Exception("node not exist")

    def delete(self, name):
        '''
        Delete a node or a leaf to children 
        '''
        for item in self.childrens:
            if(name == item.name):
                self.childrens.remove(name)

    def rename(self, name):
        '''
        Rename the current node
        '''
        self.name = name

    def getUuid(self):
        '''
        Get the uuid of the current node
        '''
        return self.uuid

    def getRoot(self):
        '''
        Return root
        '''
        node = self
        while(node.deepth != 0):
            node = node.father
        return node

    def addToPack(self, item, value):
        '''
        Add a item
        '''
        self.packs[item] = value

    def getToPack(self, item):
        '''
        Get a item value
        '''
        return self.packs[item]

    @staticmethod
    def inDeepthSearch(node, name, visited=[]):
        '''
        Search a Node a return the full path off a Node.
        '''
        visited.append(node.uuid)

        for  key, value in node.childrens.items():
            # key = name
            # value = Object node
            if(name == key):
                return value
            if value.uuid not in visited:
               fathers = Node.inDeepthSearch(value, name, visited)
               # if a deeper call return something different of false
               if (fathers!=False):
                   return fathers

        return False

    def updateChildrens(self):
        '''
        Update children in Deepth 
        '''
        visited.append(self)
        self._update()

        for  key, value in self.childrens.items():
            # key = name
            # value = Object node
            if value not in visited:
               visited.append(value)
               value.updateChildrens()

    def count(self):
        '''
        Return the numbers of all node in the graph
        '''
        c = 0
        for node in self.childrens.values():
            c+=1
            c+=node.count()
        return c

        

    @staticmethod
    def widthSearch(node, name):
        q = Queue.Queue()
        for n in node.childrens:
            q.put(n)

        while(q.empty):
            item = q.get()
            if name == item.name:
                return item
            else:
                for n in item.childrens:
                    if(n != None):
                        q.put(n)

    @staticmethod
    def getAllFathers(node, visited_fathers=[]):
        '''
        Return all Fathers node of a node or a leaf
        '''
        if(node.father != None):
            name = node.father.name
            visited_fathers.insert(0,node.father)
            return Node.getAllFathers(node.father, visited_fathers)
        else:
            return visited_fathers

    @staticmethod
    def move(node_1, node_2):
        '''
        We move node_2 to node_1 childrens
        and we update
        '''
        #move
        node_1.childrens.append(node_2)
        node_2.father.childrens.remove(node_2)

        #update
        node_1._update()
        node_2.branchValue = None
        node_1._updateChildrens()

    @staticmethod
    def firstCommonAncestor(node_1, node_2):
        '''
        Return the first common ancestor between 2 node or
        2 leaf
        '''
        while(node_1.deepth > node_2.deepth):
            node_1 = node_1.father

        while(node_2.deepth > node_1.deepth):
            node_1 = node_1.father

        while(node_1.getUuid() != node_2.getUuid()):
            node_1 = node_1.father
            node_2 = node_2.father

        return node_1


    # mettre a jour deepth

    def __contains__(self, v):
        if v in self.childrens.keys():
            return True
        return False

    def __len__(self):
        return len(self.childrens)

