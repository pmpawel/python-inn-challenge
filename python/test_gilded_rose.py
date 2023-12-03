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

    def test_quality_value_not_over_50(self):
        items = [Item("Aged Brie", 12, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        # for stardard item the vallue of sell_in should decrease
        self.assertEqual(11, items[0].sell_in)
        # quality should remain 0 as described in requirements. quality value 0 - 50
        self.assertEqual(50, items[0].quality)

    def test_aged_brie_quality_increase(self):
        items = [Item(name="Aged Brie", sell_in=23, quality=0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()        
        self.assertEqual(22, items[0].sell_in)
        self.assertEqual(1, items[0].quality)

    def test_backstage_passes_quality_increase(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()        
        self.assertEqual(14, items[0].sell_in)
        self.assertEqual(21, items[0].quality)

    def test_backstage_passes_quality_increase_by_2(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=8, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()        
        self.assertEqual(7, items[0].sell_in)
        self.assertEqual(22, items[0].quality)

    def test_backstage_passes_quality_increase_by_3(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=2, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()        
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(23, items[0].quality)

    def test_conjured_decrease_quality_by_2(self):
        items = [Item("Conjured Mana Cake", sell_in=2, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality() 
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(8, items[0].quality)         

    def test_conjured_decrease_quality_by_4(self):
        items = [Item("Conjured Mana Cake", sell_in=-2, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality() 
        self.assertEqual(-3, items[0].sell_in)
        self.assertEqual(6, items[0].quality)             

if __name__ == '__main__':
    unittest.main()
