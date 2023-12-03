# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)
        # for stardard item the vallue of sell_in should decrease
        self.assertEqual(-1, items[0].sell_in)
        # quality should remain 0 as described in requirements. quality value 0 - 50
        self.assertEqual(0, items[0].quality)


        
if __name__ == '__main__':
    unittest.main()
