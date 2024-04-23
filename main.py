import pandas as pd
#-GESTIONE DELLE ECCEZIONI
#-IMPLEMENTAZIONE PER SCOPRIRE AUTOMATICAMENTE I NEIGHBORS
#-IMPLEMENTAZIONE REALISTICA DEL FUNZIONAMENTO DEL PROTOCOLLO OSFP CON i DR BDR E DROTHERS
#-RISOLVERE MAPPATURA CON I NEIGHBOR
class Graph():
    def __init__(self, verteces = []):
        self.verteces = verteces
    
    def discoverPaths(self, startingPoint): #iterating over nodes 
        for index in self.verteces:
            for neighbor in index.neighbors:

                z=startingPoint.routeTable.at[(index.id), "Cost"]
                y=index.routeTable.at[(neighbor.id), "Cost"]
                w = startingPoint.routeTable.at[(neighbor.id), "Cost"]

                sumCost = z + y

                if (sumCost<w):
                    startingPoint.routeTable.at[(neighbor.id), "Cost"] = sumCost
                    neighbor.routeTable.at[(startingPoint.id), "Cost"] = sumCost
                
class Vertex():
    '''
    define one single vertex of the map
    '''

    def __init__(self, name, id, file,): #(... , graph)
        '''
        in a network, id in four-dotted format
        '''
        #self.obj_graph = Graph(graph)
        self.name = name
        self.id = id
        self.routeTable = pd.read_csv(file)
        
        '''if the cost is not 0 it is not the starting point itself, and if isn't 255
        the node is not  directly connected and it is not the starting point itself'''
    
        
        def gen():
            for x in range(self.routeTable.shape[0]):
                if self.routeTable.at[x, "Cost"] not in (0, 255):
                    yield globals()[self.routeTable.at[x, "NodeID"]]
        
        self.neighbors  = gen()

        '''
        for bugging reason is useful to sort the neighbors in crecent mode to 
        iterate the graph. In this case this step is omitted because already sorted,
        but must be done everytime  


        ''' #self.neighbors.sort() 
    #def __lt__(self, other): #used to sort the neighbors 
    #   return self.id < other.id
    
                  
        
A = Vertex("A", 0, "atab.csv")
B = Vertex("B", 1, "btab.csv")
C = Vertex("C" ,2, "ctab.csv")
D = Vertex("D", 3, "dtab.csv")
E = Vertex("E", 4, "etab.csv")
F = Vertex("F", 5,"ftab.csv")
G = Vertex("G", 6, "gtab.csv")

grafo = Graph([A,B,C,D,E,F,G]) 
grafo.discoverPaths(C)
print(C.routeTable)
