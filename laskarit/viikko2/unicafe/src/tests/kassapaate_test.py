import unittest

from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

        self.maksukortti = Maksukortti(450)
        self.maksukortti_2 = Maksukortti(100)

    def test_konstruktori_asettaa_oikean_raha_maaran(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_konstruktori_asettaa_myytyjen_edullisten_lounaiden_maaran_nollaan(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_konstruktori_asettaa_myytyjen_maukkaiden_lounaiden_maaran_nollaan(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullisen_lounaan_kateisosto_lisaa_kassan_rahamaaraa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.40)

    def test_edullisen_lounaan_kateisosto_lisaa_myytyjen_edullisten_lounaiden_maaraa(
        self,
    ):
        self.kassapaate.syo_edullisesti_kateisella(240)

        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukkaan_lounaan_kateisosto_lisaa_kassan_rahamaaraa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004.0)

    def test_maukkaan_lounaan_kateisosto_lisaa_myytyjen_edullisten_lounaiden_maaraa(
        self,
    ):
        self.kassapaate.syo_maukkaasti_kateisella(400)

        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_edullisen_kateisosto_antaa_oikean_maaran_vaihtorahaa(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(600)

        self.assertEqual(vaihtoraha, 360.0)

    def test_maukkaan_kateisosto_antaa_oikean_maaran_vaihtorahaa(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(600)

        self.assertEqual(vaihtoraha, 200.0)

    def test_kassan_rahamaara_ei_muutu_jos_edullisen_lounaan_kateismaksu_ei_ole_riittava(
        self,
    ):
        self.kassapaate.syo_edullisesti_kateisella(100)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_vaihtoraha_oikein_kun_edullisen_lounaan_kaiteismaksu_ei_ole_riittava(
        self,
    ):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(100)

        self.assertEqual(vaihtoraha, 100)

    def test_kassan_rahamaara_ei_muutu_jos_maukkaan_lounaan_kaitesmaksu_ei_ole_riittava(
        self,
    ):
        self.kassapaate.syo_maukkaasti_kateisella(200)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_vaihtoraha_oikein_kun_maukkaan_lounaan_kaitesmaksu_ei_ole_riittava(
        self,
    ):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(200)

        self.assertEqual(vaihtoraha, 200)

    def test_edullisen_lounaan_korttiosto_riittavalla_saldolla_vahentaa_lounaan_hinnan_saldosta(
        self,
    ):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.maksukortti.saldo_euroina(), 2.1)

    def test_edullisen_lounaan_korttiosto_riittavalla_saldolla_palauttaa_true(self):
        tulos = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(tulos, True)

    def test_edullisen_lounaan_korttiosto_riittavalla_saldolla_lisaa_myytyjen_edullisten_lounaiden_maaraa(
        self,
    ):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullisen_lounaan_korttiosto_riittamattomalla_saldolla_ei_muuta_saldoa(
        self,
    ):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti_2)

        self.assertEqual(self.maksukortti_2.saldo_euroina(), 1)

    def test_edullisen_lounaan_korttiosto_riittamattomalla_saldolla_palauttaa_false(
        self,
    ):
        tulos = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti_2)

        self.assertEqual(tulos, False)

    def test_edullisen_lounaan_korttiosto_riittavalla_ei_muuta_kassan_rahamaaraa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_maukkaan_lounaan_korttiosto_riittavalla_saldolla_vahentaa_lounaan_hinnan_saldosta(
        self,
    ):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.maksukortti.saldo_euroina(), 0.5)

    def test_maukkaan_lounaan_korttiosto_riittavalla_saldolla_palauttaa_true(self):
        tulos = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(tulos, True)

    def test_maukkaan_lounaan_korttiosto_riittavalla_saldolla_lisaa_myytyjen_edullisten_lounaiden_maaraa(
        self,
    ):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukkaan_lounaan_korttiosto_riittamattomalla_saldolla_ei_muuta_saldoa(
        self,
    ):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti_2)

        self.assertEqual(self.maksukortti_2.saldo_euroina(), 1)

    def test_maukkaan_lounaan_korttiosto_riittamattomalla_saldolla_palauttaa_false(
        self,
    ):
        tulos = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti_2)

        self.assertEqual(tulos, False)

    def test_maukkaan_lounaan_korttiosto_riittavalla_ei_muuta_kassan_rahamaaraa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_rahan_lataaminen_kortille_lisaa_kortin_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti_2, 100)

        self.assertEqual(self.maksukortti_2.saldo_euroina(), 2.0)

    def test_rahan_lataaminen_kortille_lisaa_kassan_rahamaaraa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti_2, 500)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1005.0)

    def test_negatiivisen_summan_lataaminen_ei_muuta_kortin_saloda(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti_2, -100)

        self.assertEqual(self.maksukortti_2.saldo_euroina(), 1.0)

    def test_negatiivisen_summan_lataaminen_ei_muuta_kassan_rahamaaraa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti_2, -100)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
