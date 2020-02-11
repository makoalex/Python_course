from myChickenClass import Chicken
import unittest


class TestChicken(unittest.TestCase):
    def setUp(self):
        self.chicken = Chicken('chicky', 'Silkie', 1)

    def test_innit(self):
        self.assertEqual(self.chicken.name, 'chicky')
        self.assertEqual(self.chicken.species, 'Silkie')
        self.assertEqual(self.chicken.eggs, 1)

    def test_lay_eggs(self):
        self.assertIsInstance(self.chicken.total_eggs, int)
        eggs = self.chicken.total_eggs + 1
        self.chicken.lay_egg()
        self.assertEqual(self.chicken.total_eggs, eggs)

    if __name__ == '__main__':
        unittest.main()
