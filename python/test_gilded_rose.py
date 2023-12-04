# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRose, AgedBrie, Sulfuras, StandardItem, ConjuredItem, Backstage


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [StandardItem("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)
        # for stardard item the vallue of sell_in should decrease
        self.assertEqual(-1, items[0].sell_in)
        # quality should remain 0 as described in requirements. quality value 0 - 50
        self.assertEqual(0, items[0].quality)

    def test_quality_value_not_over_50(self):
        items = [AgedBrie("Aged Brie", 12, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        # for stardard item the vallue of sell_in should decrease
        self.assertEqual(11, items[0].sell_in)
        # quality should remain 0 as described in requirements. quality value 0 - 50
        self.assertEqual(50, items[0].quality)

    def test_conjured_decrease_quality_by_2(self):
        items = [ConjuredItem("Conjured Mana Cake", sell_in=2, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality() 
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(8, items[0].quality)         

    def test_conjured_decrease_quality_by_4(self):
        items = [ConjuredItem("Conjured Mana Cake", sell_in=-2, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality() 
        self.assertEqual(-3, items[0].sell_in)
        self.assertEqual(6, items[0].quality)             


class BackstageTest(unittest.TestCase):
    def test_backstage_passes_quality_increase_by_1(self):
        item = Backstage("Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20)
        gilded_rose = item.update_quality()  
        self.assertEqual(14, item.sell_in)
        self.assertEqual(21, item.quality)

    def test_backstage_passes_quality_increase_by_2(self):
        item = Backstage("Backstage passes to a TAFKAL80ETC concert", sell_in=8, quality=20)
        item.update_quality()        
        self.assertEqual(7, item.sell_in)
        self.assertEqual(22, item.quality)

    def test_backstage_passes_quality_increase_by_3(self):
        item = Backstage("Backstage passes to a TAFKAL80ETC concert", sell_in=2, quality=20)
        item.update_quality()      
        self.assertEqual(1, item.sell_in)
        self.assertEqual(23, item.quality)

    def test_backstage_quality_drops_to_0_after_concert(self):
        item = Backstage("Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=20)
        item.update_quality()
        self.assertEqual(-1, item.sell_in)
        self.assertEqual(0, item.quality)

class AgedBrieTest(unittest.TestCase):
    def test_aged_brie_quality_increase(self):
        item = AgedBrie(name="Aged Brie", sell_in=23, quality=0)
        item.update_quality()        
        self.assertEqual(22, item.sell_in)
        self.assertEqual(1, item.quality)

if __name__ == '__main__':
    unittest.main()
