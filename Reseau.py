
from Terrain import Terrain, Case
from StrategieReseau import StrategieReseau, StrategieReseauAuto

class Reseau:
    def __init__(self):
        self.strat = StrategieReseauAuto()
        self.noeuds = {}
        self.arcs = []

        self.noeud_entree = -1

    def definir_entree(self, n: int) -> None:
        if n in self.noeuds.keys():
            self.noeud_entree = n
        else:
            self.noeud_entree = -1

    def ajouter_noeud(self, n: int, coords: tuple[int, int]):
        if n >= 0:
            self.noeuds[n] = coords

    def ajouter_arc(self, n1: int, n2: int) -> None:
        if n1 > n2:
            tmp = n2
            n2 = n1
            n1 = tmp
        if n1 not in self.noeuds.keys() or n2 not in self.noeuds.keys():
            return
        if (n1, n2) not in self.arcs:
            self.arcs.append((n1, n2))

    def set_strategie(self, strat: StrategieReseau):
        self.strat = strat

    def noeud_proche(i,j):
        return (noeuds[i][0]==noeuds[j][0]-1 and noeuds[i][1]==noeuds[j][1]) or (noeuds[i][0]==noeuds[j][0]+1 and noeuds[i][1]==noeuds[j][1]) or (noeuds[i][1]==noeuds[j][1]-1 and noeuds[j][0]==noeuds[i][0]) or (noeuds[i][1]==noeuds[j][1]+1 and noeuds[i][0]==noeuds[j][0])
    
    def valider_noeud(self,i,l={}):
        if i in self.noeuds and (i not in l):
            if i==self.noeud_entree:
                l[i]=True
            else :
                for j in self.noeuds:
                    if i!=j and noeud_proche(i,j):
                        if (i,j) in self.arcs and (i not in l):
                            if j in l and l[j]:
                                l[i]=True
                            else:
                                l=self.valider_noeud(j,l=l)
                                if l[j]:
                                    l[i]=True    
        if i not in l:
            l[i]=False
        return l
    
    def valider_reseau(self) -> bool:
        if len(self.arcs)>=(len(self.noeuds)-1):
            l={}
            for i in self.noeuds:
               l=self.valider_noeud(i,l=l) 
            for i in l:
                if not(l[i]):
                    return False
            return True
        else :
            return False

    def valider_distribution(self, t: Terrain) -> bool:
        l={}
        x=0
        for i in t.get_clients():
            x=0
            for j in self.noeuds:
                if i==self.noeuds[j]:
                    x=1
                    l=self.valider_noeud(j,l=l) 
            if x==0:
                return False
        for i in l:
            if not(l[i]):
                return False
            
        return True

    def configurer(self, t: Terrain):
        self.noeud_entree, self.noeuds, self.arcs  = self.strat.configurer(t)

    def afficher(self) -> None:
        for i in self.noeuds:
            for j in self.noeuds:
                if (i,j) in self.arcs:
                    print(self.arcs((i,j)))
        

    def afficher_avec_terrain(self, t: Terrain) -> None:
        for ligne, l in enumerate(t.cases):
            for colonne, c in enumerate(l):
                if (ligne, colonne) not in self.noeuds.values():
                    if c == Case.OBSTACLE:
                        print("X", end="")
                    if c == Case.CLIENT:
                        print("C", end="")
                    if c == Case.VIDE:
                        print("~", end="")
                    if c == Case.ENTREE:
                        print("E", end="")
                    else:
                        print(" ", end="")
                else:
                    if c == Case.OBSTACLE:
                        print("T", end="")
                    if c == Case.CLIENT:
                        print("C", end="")
                    if c == Case.VIDE:
                        print("+", end="")
                    if c == Case.ENTREE:
                        print("E", end="")
                    else:
                        print(" ", end="")
            print()

    def calculer_cout(self, t: Terrain) -> float:
        cout = 0
        for _ in self.arcs:
            cout += 1.5
        for n in self.noeuds.values():
            if t[n[0]][n[1]] == Case.OBSTACLE:
                cout += 2
            else:
                cout += 1
        return cout

