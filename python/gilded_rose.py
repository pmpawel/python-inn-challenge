# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
    
        for item in self.items:
            item.update_quality()

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

    def update_quality(self):        

        if self.sell_in <= 0:
            self.quality -= 2  # After sell-in date passes, quality degrades by 2
        else:
            self.quality -= 1
        self.sell_in -= 1    

        # Enforce quality limits
        if self.quality < 0:
            self.quality = 0
        elif self.quality > 50:
            self.quality = 50


class AgedBrie(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        if self.quality < 50:
            self.quality += 1
        self.sell_in -= 1

        # Enforce quality limits
        if self.quality < 0:
            self.quality = 0
        elif self.quality > 50:
            self.quality = 50

class Sulfuras(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)
    
    def update_quality(self):
        pass

class Backstage(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        print(self)
        if self.sell_in > 10:
            self.quality += 1
        elif 5 < self.sell_in <= 10:
            self.quality += 2
        elif 0 < self.sell_in <= 5:
            self.quality += 3
        else:
            self.quality = 0

        if self.quality > 50:
            self.quality = 50
        self.sell_in -= 1
        print(self)

class ConjuredItem(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)
    
    def update_quality(self):
        if self.quality > 1:
            if self.sell_in <= 0:
                self.quality -= 4  # After sell-in date passes, quality degrades by 4
            else:
                self.quality -= 2  # Quality degrades by 2 for Conjured items
        self.sell_in -= 1    

        # Enforce quality limits
        if self.quality < 0:
            self.quality = 0
        elif self.quality > 50:
            self.quality = 50

