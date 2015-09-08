"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

from Card import *
import pdb


class PokerHand(Hand):

    all_labels = ['straight_flush', 'four_kind', 'full_house', 'flush',
                  'straight', 'three_kind', 'twopair', 'pair']

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def rank_hist(self):
        """Builds a histogram of the ranks that appear in the hand."""
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def create_hist(self):
        self.suit_hist()
        self.rank_hist()

    def has_highcard(self):
        if len(self.cards) > 0:
            return True
        else:
            return False

    def has_pair(self):
        for val in self.ranks.values():
            if val >= 2:
                return True
        return False

        
    def has_twopair(self):
        t = 0
        for val in self.ranks.values():
            if val >= 2:
                t += 1
        return t >= 2

    def has_three_kind(self):
        for val in self.ranks.values():
            if val >= 3:
                return True
        return False

    def has_straight(self):
        count = 0
        for i in range(1,14):
            if self.ranks.get(i,0):
                count += 1
            else:
                count = 0
            if count == 5:
                return True
        if count == 4 and self.ranks.get(1,0) and self.ranks.get(13,0):
            return True
        return False
                
            

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def has_full_house(self):
        rank_count = self.ranks.values()
        n = 0
        m = 0
        for i in rank_count:
            if i >= 2:
                n += 1
            if i >= 3:
                m += 1
        if m >= 1 and n >= 2:
            return True
        return False
            
        
    def has_four_kind(self):
       for val in self.ranks.values():
           if val >= 4:
               return True
       return False

   
    def has_straight_flush(self):
        for suit in range(0,4):
            same_suit = []
            for card in self.cards:
                if card.suit == suit:
                    same_suit.append(card)
            # pdb.set_trace()
            if len(same_suit) < 5:
                continue
            else:
                same_suit.sort()
                ranks = {}
                for card in same_suit:
                    ranks[card.rank] = ranks.get(card.rank, 0) + 1
                count = 0
                for i in range(1,14):
                    if ranks.get(i,0):
                        count += 1
                        if count == 5:
                            return True
                    else:
                        count = 0
                if count == 4 and self.ranks.get(1,0) and self.ranks.get(13,0):
                    return True
        return False

    def classify(self):
        self.create_hist()
        for label in PokerHand.all_labels:
            f = getattr(self, 'has_' + label)
            if f():
                return label
                
        

if __name__ == '__main__':

    n = 60000
    z = {}
    for i in range(n):
        deck = Deck()
        deck.shuffle()
        hand = PokerHand()
        deck.move_cards(hand,7)
        
        c =  hand.classify()
        z[c] = z.get(c,0) + 1
        del hand

    print '=====7 card poker======'
    print 'One pair:', z.get('pair')/float(n)*100,'%'
    print 'Two pair:', z.get('twopair')/float(n)*100, '%'
    print 'Three kind:', z.get('three_kind')/float(n)*100, '%'
    print 'Straight:', z.get('straight')/float(n)*100, '%'
    print 'Flush', z.get('flush')/float(n)*100, '%'
    print 'Full house:', z.get('full_house')/float(n)*100, '%'
    print 'Four kind:', z.get('four_kind')/float(n)*100, '%'
    print 'Straight flush:', z.get('straight_flush')/float(n)*100, '%'
    print '======================='

    
    
