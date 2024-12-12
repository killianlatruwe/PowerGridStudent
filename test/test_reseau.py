
import unittest
import xmlrunner

from Reseau import Reseau
from Terrain import Terrain, Case

class TestReseau(unittest.TestCase):

    def test_definition_entree(self):
        reseau=Reseau()
        reseau.ajouter_noeud(0,(0,0))
        reseau.ajouter_noeud(1,(0,1))
        reseau.ajouter_noeud(2,(1,0))
        reseau.definir_entree(0)
        self.assertEqual(noeud_entree,0,"le noeud d'entree est 0")
        reseau.definir_entree(3)
        self.assertEqual(noeud_entree,-1,"le noeud d'entree est à -1")

    def test_ajout_noeud(self):
        reseau=Reseau()
        reseau.ajouter_noeud(0,(0,0))
        reseau.ajouter_noeud(1,(0,1))
        reseau.ajouter_noeud(2,(1,0))
        self.assertIn(0,self.noeuds,"le noeud 0 existe")
        self.assertIn(1,self.noeuds,"le noeud 1 existe")
        self.assertIn(2,self.noeuds,"le noeud 2 existe")
        self.assertEqual(reseau.noeuds[0],(0,0),"le noeud 0 a pour coordonnees (0,0)")
        self.assertEqual(reseau.noeuds[2],(1,0),"le noeud 2 a pour coordonnees (1,0)")
        
    def test_ajout_arc(self):
        reseau.Reseau()
        reseau.ajouter_noeud(0,(0,0))
        reseau.ajouter_noeud(1,(0,1))
        reseau.ajouter_noeud(2,(1,0))
        reseau.ajouter_arc(0,1)
        self.assertIn((0,1),reseau.arcs,"l'arc en 0 et 1 est ajoute au reseau")
        reseau.ajouter_arc(0,2)
        self.assertIn((0,2),reseau.arcs,"l'arc en 0 et 2 est ajoute au reseau")
        reseau.ajouter_arc(0,3)
        self.assertNotIn((0,3),reseau.arcs,"le noeud 3 n'existe pas")
        reseau.ajouter_arc(3,4)
        self.assertNotIn((3,4),reseau.arcs,"les noeuds 3 et 4 n'existe pas")

    def test_validation_correcte(self):
        r = Reseau()
        r.noeuds[0] = (0, 0)
        r.noeud_entree = 0

        r.noeuds[1] = (1, 0)
        r.arcs.append((0, 1))

        r.noeuds[2] = (0, 1)
        r.arcs.append((0, 2))

        r.noeuds[3] = (0, 2)
        r.arcs.append((2, 3))

        r.noeuds[4] = (1, 2)
        r.arcs.append((3, 4))

        self.assertTrue(r.valider_reseau())

    def test_validation_incorrecte(self):
        r = Reseau()
        r.noeuds[0] = (0, 0)
        r.noeud_entree = 0

        r.noeuds[1] = (1, 0)
        r.arcs.append((0, 1))

        r.noeuds[2] = (0, 1)
        r.arcs.append((0, 2))

        r.noeuds[3] = (0, 2)
        r.arcs.append((2, 3))

        r.noeuds[4] = (1, 2)

        self.assertFalse(r.valider_reseau())

    def test_distribution_correcte(self):
        r = Reseau()
        r.noeuds[0] = (0, 0)
        r.noeud_entree = 0

        r.noeuds[1] = (1, 0)
        r.arcs.append((0, 1))

        r.noeuds[2] = (0, 1)
        r.arcs.append((0, 2))

        r.noeuds[3] = (0, 2)
        r.arcs.append((2, 3))

        r.noeuds[4] = (1, 2)
        r.arcs.append((3, 4))

        t = Terrain()
        t.cases = [
                [Case.ENTREE, Case.VIDE, Case.VIDE],
                [Case.CLIENT, Case.VIDE, Case.CLIENT],
        ]

        self.assertTrue(r.valider_distribution(t))

    def test_distribution_incorrecte(self):
        r = Reseau()
        r.noeuds[0] = (0, 0)
        r.noeud_entree = 0

        r.noeuds[1] = (1, 0)
        r.arcs.append((0, 1))

        r.noeuds[2] = (0, 1)
        r.arcs.append((0, 2))

        r.noeuds[3] = (0, 2)
        r.arcs.append((2, 3))

        r.noeuds[4] = (1, 2)
        r.arcs.append((3, 4))

        t = Terrain()
        t.cases = [
                [Case.ENTREE, Case.VIDE, Case.VIDE],
                [Case.CLIENT, Case.CLIENT, Case.CLIENT],
        ]

        self.assertFalse(r.valider_distribution(t))

if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="test-reports"))

