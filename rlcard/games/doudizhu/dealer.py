# -*- coding: utf-8 -*-
''' Implement Doudizhu Dealer class
'''

import functools

from rlcard.utils import init_54_deck
from rlcard.games.doudizhu.utils import cards2str, doudizhu_sort_card


class DoudizhuDealer(object):
    ''' Dealer will shuffle, deal cards, and determine players' roles
    '''

    def __init__(self, np_random):
        '''Give dealer the deck

        Notes:
            1. deck with 54 cards including black joker and red joker
        '''
        self.np_random = np_random
        self.deck = init_54_deck()
        self.deck.sort(key=functools.cmp_to_key(doudizhu_sort_card))
        self.landlord = None
        self.landlord_score = False
        self.landlord_agent = -1

    def get_landlord_agent(self):
        return self.landlord_agent

    def set_landlord_score(self, landlord_score):
        self.landlord_score = landlord_score

    def shuffle(self):
        ''' Randomly shuffle the deck
        '''
        self.np_random.shuffle(self.deck)

    def deal_cards(self, players):
        ''' Deal cards to players

        Args:
            players (list): list of DoudizhuPlayer objects
        '''
        hand_num = (len(self.deck) - 3) // len(players)
        for index, player in enumerate(players):
            current_hand = self.deck[index*hand_num:(index+1)*hand_num]
            current_hand.sort(key=functools.cmp_to_key(doudizhu_sort_card))
            player.set_current_hand(current_hand)
            player.initial_hand = cards2str(player.current_hand)

    def determine_role(self, players):
        ''' Determine landlord and peasants according to players' hand

        Args:
            players (list): list of DoudizhuPlayer objects

        Returns:
            int: landlord's player_id
        '''
        # deal cards
        self.shuffle()
        self.deal_cards(players)
        players[0].role = 'landlord'
        self.landlord = players[0]
        players[1].role = 'peasant'
        players[2].role = 'peasant'
        #players[0].role = 'peasant'
        #self.landlord = players[0]
        self.landlord_agent = 0
        ## determine 'landlord'
        if(self.landlord_score==True):

            max_score = self.get_landlord_score(
                cards2str(self.landlord.current_hand))

            counter = 1
            for player in players[1:]:
                player.role = 'peasant'
                score = self.get_landlord_score(
                    cards2str(player.current_hand))
                if score > max_score:
                    max_score = score
                    self.landlord = player
                    if(counter==1):

                        self.landlord_agent = 1
                    if(counter==2):
                        self.landlord_agent = 2
                counter += 1

            self.landlord.role = 'landlord'

        # give the 'landlord' the  three cards
        self.landlord.current_hand.extend(self.deck[-3:])
        self.landlord.current_hand.sort(key=functools.cmp_to_key(doudizhu_sort_card))
        self.landlord.initial_hand = cards2str(self.landlord.current_hand)

        return self.landlord.player_id

    def get_landlord_score(self, current_hand):
        ''' Roughly judge the quality of the hand, and provide a score as basis to
        bid landlord.

        Args:
            current_hand (str): string of cards. Eg: '56888TTQKKKAA222R'

        Returns:
            int: score
        '''

        score_map = {'A': 1, '2': 2, 'B': 3, 'R': 4}
        score = 0
        # rocket
        if current_hand[-2:] == 'BR':
            score += 8
            current_hand = current_hand[:-2]
        length = len(current_hand)
        i = 0
        while i < length:
            # bomb
            if i <= (length - 4) and current_hand[i] == current_hand[i+3]:
                score += 6
                i += 4
                continue
            # 2, Black Joker, Red Joker
            if current_hand[i] in score_map:
                score += score_map[current_hand[i]]
            i += 1
        return score
