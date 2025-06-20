import unittest
from unittest import result
from fonctions import additionner, convertir_temperature, est_pair, valider_email, calculer_moyenne

class TestFonctions(unittest.TestCase):

    # Test additionner
    def test_additionner_cas_positif(self):
        """Test addition avec nombres positifs"""
        resultat = additionner(2, 3)
        self.assertEqual(resultat, 5)
        if not isinstance(resultat, int):
            raise TypeError("Le résultat doit être un nombre entier")

    def test_additionner_cas_negatif(self):
        """Test addition avec nombres négatifs"""
        resultat = additionner(-2, -3)
        self.assertEqual(resultat, -5)
        if not isinstance(resultat, int):
            raise TypeError("Le résultat doit être un nombre entier")

    # Test est_pair
    def test_est_pair_nombre_pair(self):
        """Test avec un nombre pair"""
        self.assertTrue(est_pair(4))

    def test_est_pair_nombre_impair(self):
        """Test avec un nombre impair"""
        self.assertFalse(est_pair(3))

    def test_est_pair_zero(self):
        """Test avec zéro"""
        self.assertTrue(est_pair(0))

    # Test valider_email
    def test_valider_email_valide(self):
        """Test avec un email valide"""
        self.assertTrue(valider_email("test@example.com"))

    def test_valider_email_sans_arobase(self):
        """Test avec un email sans @"""
        self.assertFalse(valider_email("testexample.com"))

    def test_valider_email_sans_point(self):
        """Test avec un email sans point"""
        self.assertFalse(valider_email("test@example"))

    # Test calculer_moyenne
    def test_calculer_moyenne_cas_positif(self):
        """Test si la moyenne est calculée correctement"""
        resultat = calculer_moyenne([10, 20, 30])
        self.assertEqual(resultat, 20)

    def test_calculer_moyenne_cas_negatif(self):
        """Test si la moyenne est calculée correctement"""
        resultat = calculer_moyenne([])
        self.assertEqual(resultat, 0)
        if not isinstance(resultat, int):
            raise TypeError("Le résultat doit être un nombre entier")

    def test_calculer_moyenne_liste_normale(self):
        """Test avec une liste de notes normales"""
        resultat = calculer_moyenne([10, 15, 20])
        self.assertEqual(resultat, 15)
        if not isinstance(resultat, int):
            raise TypeError("Le résultat doit être un nombre entier")

    def test_calculer_moyenne_liste_vide(self):
        """Test avec une liste vide"""
        resultat = calculer_moyenne([])
        self.assertEqual(resultat, 0)
        if not isinstance(resultat, int):
            raise TypeError("Le résultat doit être un nombre entier")

    def test_calculer_moyenne_une_note(self):
        """Test avec une seule note"""
        resultat = calculer_moyenne([18])
        self.assertEqual(resultat, 18)
        if not isinstance(resultat, int):
            raise TypeError("Le résultat doit être un nombre entier")

    # Test convertir_temperature
    def test_convertir_temperature_cas_positif(self):
        """Test si la température est convertie correctement"""
        resultat = convertir_temperature(0)
        self.assertEqual(resultat, 32)
        if not isinstance(resultat, int):
            raise TypeError("Le résultat doit être un nombre entier")

    def test_convertir_temperature_cas_negatif(self):
        """Test si la température est convertie correctement"""
        resultat = convertir_temperature(-10)
        self.assertEqual(resultat, 14)
        if not isinstance(resultat, int):
            raise TypeError("Le résultat doit être un nombre entier")

    def test_convertir_temperature_zero(self):
        """Test conversion 0°C = 32°F"""
        resultat = convertir_temperature(0)
        self.assertEqual(resultat, 32)
        if not isinstance(resultat, int):
            raise TypeError("Le résultat doit être un nombre entier")

    def test_convertir_temperature_eau_bouillante(self):
        """Test conversion 100°C = 212°F"""
        resultat = convertir_temperature(100)
        self.assertEqual(resultat, 212)
        if not isinstance(resultat, int):
            raise TypeError("Le résultat doit être un nombre entier")

if __name__ == '__main__':
    unittest.main()