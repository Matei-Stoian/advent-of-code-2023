from collections import Counter

lines = open('input.txt').read().splitlines()
hands = [(line.split()[0],int(line.split()[1])) for line in lines]
def hand_type(hand):
    count = Counter(hand)
    if 5 in count.values():
        return "Five of a kind"
    if 4 in count.values():
        return "Four of a kind"
    if 3 in count.values() and 2 in count.values():
        return "Full house"
    if 3 in count.values():
        return "Three of a kind"
    if 2 in count.values():
        temp = Counter(count.values())
        if 3 in temp.values():
            return "One pair"
        return "Two pair"
    return "High card"
def hand_typej(hand,rankj):
    count = Counter(hand)
    def get_rank(card):
        return rankj[card]
    jcount = count.pop('J',0)
    if jcount > 0 and jcount != 5:
        max_count = max(count.values())
        max_rank = max(get_rank(card) for card in count if count[card] == max_count)
        rez = None
        for card in count:
            if get_rank(card) == max_rank:
                rez = card
                break
        hand = hand.replace('J',rez,jcount)
    return hand_type(hand)

def sort_hands(hands,ranks):
    def hand_comp(item):
        hand,score = item
        key = [ranks[card] for card in hand]
        return (tuple(key),score)
    return sorted(hands,key=hand_comp,reverse=True)

def part1():
    poker_hands = {
    'Five of a kind': [],
    'Four of a kind': [],
    'Full house': [],
    'Three of a kind': [],
    'Two pair': [],
    'One pair': [],
    'High card': []
    }
    ranks_card = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
    for hand,score in hands:
        poker_hands[hand_type(hand)].append((hand,score))
    ans = 0
    thand = len(hands)
    for key,value in poker_hands.items():
        sorted_hands = sort_hands(value,ranks_card)
        for hand,score in sorted_hands:
            ans += thand*score
            thand -=1
    print(f'Part 1: {ans}')

def part2():
    poker_hands = {
    'Five of a kind': [],
    'Four of a kind': [],
    'Full house': [],
    'Three of a kind': [],
    'Two pair': [],
    'One pair': [],
    'High card': []
    }
    ranks_card = {'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
    
    for hand,score in hands:
        poker_hands[hand_typej(hand,ranks_card)].append((hand,score))
    ans = 0
    thand = len(hands)
    for key,value in poker_hands.items():
        sorted_hands = sort_hands(value,ranks_card)
        for hand,score in sorted_hands:
            ans += thand*score
            thand-=1
    print(f'Part 2: {ans}')
    
part1()
part2()