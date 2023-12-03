# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):

        for item in self.items:
            if item.name == "Aged Brie":
                if item.quality < 50:
                    item.quality += 1
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.sell_in > 10:
                    item.quality += 1
                elif 5 < item.sell_in <= 10:
                    item.quality += 2
                elif 0 < item.sell_in <= 5:
                    item.quality += 3


            elif item.name == "Sulfuras, Hand of Ragnaros":
                item.quality = 80
                item.sell_in = 0
                pass  # Sulfuras quality remains constant at 80
            elif item.name == "Conjured Mana Cake":
                if item.quality > 1:
                    if item.sell_in <= 0:
                        item.quality -= 4  # After sell-in date passes, quality degrades by 4
                    else:
                        item.quality -= 2  # Quality degrades by 2 for Conjured items
            else:  # For regular items
                if item.quality > 0:
                    if item.sell_in <= 0:
                        item.quality -= 2  # After sell-in date passes, quality degrades by 2
                    else:
                        item.quality -= 1

            # Enforce quality limits
            if item.quality < 0:
                item.quality = 0
            elif item.quality > 50 and item.name != "Sulfuras, Hand of Ragnaros":
                item.quality = 50

            # Update sell-in value for all items except Sulfuras
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in -= 1

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class StandardItem(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)
    pass

class AgedBrie(Item):
    def __initls__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)
    pass

class Sulfuras(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)
    pass

class ConjuredItem(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)
    pass
