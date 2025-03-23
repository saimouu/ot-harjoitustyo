import unittest

from maksukortti import Maksukortti


class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_on_luonnin_jalkeen_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_saldo_naytetaan_teksti_muodossa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_lataaminen_lisaa_oikean_maaran(self):
        self.maksukortti.lataa_rahaa(300)

        self.assertEqual(self.maksukortti.saldo_euroina(), 13.0)

    def test_rahan_ottaminen_vahentaa_oikean_maaran(self):
        self.maksukortti.ota_rahaa(500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 5.0)

    def test_rahan_ottaminen_ei_muuta_saldoa_jos_rahaa_ei_ole_tarpeeksi(self):
        kortti = Maksukortti(500)
        kortti.ota_rahaa(600)

        self.assertEqual(kortti.saldo_euroina(), 5.0)

    def test_rahan_ottaminen_palauttaa_true_kun_rahaa_on_riittavasti(self):
        tulos = self.maksukortti.ota_rahaa(900)

        self.assertEqual(tulos, True)

    def test_rahan_ottaminen_palauttaa_false_kun_rahaa_ei_ole_riittavasti(self):
        tulos = self.maksukortti.ota_rahaa(1200)

        self.assertEqual(tulos, False)
