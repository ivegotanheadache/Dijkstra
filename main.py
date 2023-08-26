import pandas as pd

class Vertex():
    '''
    define one single vertex of the map
    '''

    def __init__(self, name, id, file):
        '''
        in a network, id in four-dotted format
        in a network, neighbors are discovered via arp -> implement api
        '''
        self.name = name
        self.id = id
        self.routeTable = pd.read_csv(file)
        
        '''if the cost is not 0, the node is directly connected and it is not the starting point itself'''
        #self.neighbors = [globals()[self.routeTable.at[x,"NodeID"]] for x in range(0,self.routeTable.shape[0]) if (self.routeTable.at[x,"Cost"] != 0)]
        def gen():
            for x in range(0,self.routeTable.shape[0]):
                if (self.routeTable.at[x,"Cost"] != (0 or 255)):
                    yield globals()[self.routeTable.at[x,"NodeID"]]
        self.neighbors = gen()
        '''
        for bugging reason is useful to sort the neighbors in crecent mode to 
        iterate the graph. In this case this step is omitted because already sorted,
        but must be done everytime
        ''' #self.neighbors.sort() 
    #def __lt__(self, other): #used to sort the neighbors 
    #   return self.id < other.id
    def next(self, nodes): #iterating over nodes where self is the starting point
        for index in nodes:
            for neighbor in index.neighbors:

                z=self.routeTable.at[(index.id), "Cost"]
                y=index.routeTable.at[(neighbor.id), "Cost"]
                w = self.routeTable.at[(neighbor.id), "Cost"]

                sumCost = z + y

                if (sumCost<w):
                    self.routeTable.at[(neighbor.id), "Cost"] = sumCost
                    neighbor.routeTable.at[(self.id), "Cost"] = sumCost
                    
                    
A = Vertex("A", 0, "atab.csv")
B = Vertex("B", 1, "btab.csv")
C = Vertex("C" ,2, "ctab.csv")
D = Vertex("D", 3, "dtab.csv")
E = Vertex("E", 4, "etab.csv")
F = Vertex("F", 5,"ftab.csv")
G = Vertex("G", 6, "gtab.csv")

B.next([A,B,C,D,E,F,G])
print(B.routeTable)

