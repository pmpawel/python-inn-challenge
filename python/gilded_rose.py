# -*- coding: utf-8 -*-

class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        # Loop through Items list
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
    
    # Do nothing as values don't change. 
    def update_quality(self):
        pass

class Backstage(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        # Increase item requirement by 1 as normal when sellin is more than 10
        if self.sell_in > 10:
            self.quality += 1
        # possibly better apporach would be to use range
        # value increases by 2 when sell in 6-10
        elif 5 < self.sell_in <= 10:
            self.quality += 2
        # value increases by 3 when sell in 1-5    
        elif 0 < self.sell_in <= 5:
            self.quality += 3
        else:
            # concert
            self.quality = 0 

        if self.quality > 50:
            self.quality = 50
        self.sell_in -= 1

class ConjuredItem(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)
    
    def update_quality(self):
        if self.quality > 1:
            # quality degrades twice as fast after sell_in data pass below 0
            if self.sell_in <= 0:
                self.quality -= 4  # After sell-in date passes, quality degrades by 4
            else:
                # quality decreases by 2 in normal when product within sell in > 0
                self.quality -= 2  # Quality degrades by 2 for Conjured items
        self.sell_in -= 1    

        # Enforce quality limits
        if self.quality < 0:
            self.quality = 0
        elif self.quality > 50:
            self.quality = 50
