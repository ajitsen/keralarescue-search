from unittest import TestCase
import common.data as data


class Test_Data(TestCase):

    def test_get_dist_name(self):
        self.assertEqual(data.get_dist_name('ekm'), 'Ernakulam')
        self.assertEqual(data.get_dist_name(None), None)
        self.assertEqual(data.get_dist_name(''), None)
        self.assertEqual(data.get_dist_name('   '), None)
        self.assertEqual(data.get_dist_name('ekl'), None)
        self.assertEqual(data.get_dist_name('          ERNAKULAM'), 'Ernakulam')
        self.assertEqual(data.get_dist_name('alappuzha'), 'Alappuzha')

    def test_get_location_concact(self):
        loc = ("Apporu,Madrassa Palli,Mannancheery", "Apporu,Madrassa Palli,North aryad P.O,Mannancheery", None)
        self.assertEqual("Apporu,Madrassa Palli,Mannancheery, North aryad P.O", data.get_location_concact(loc))

    def test_get_camp_id(self):
        self.assertEqual("chinmaya-vidyapeet",
                         data.get_camp_id("Chinmaya Vidyapeet", "123"))

        self.assertEqual("chinmaya-vidyapeet",
                         data.get_camp_id("Chinmaya Vidyapeet - people have started to leave", ""))

        self.assertEqual("124-345",
                         data.get_camp_id("", "124, 345"))

        self.assertEqual("124-345",
                         data.get_camp_id("a", "124, 345"))

        self.assertEqual("124-345",
                         data.get_camp_id(None, "124, 345"))

    def test_get_clean_str(self):
        self.assertEqual("hello ajit", data.get_clean_str(" hello  \r \n ajit \n \r"))
