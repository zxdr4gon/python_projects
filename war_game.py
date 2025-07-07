import random

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6,
          'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six',
          'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']

war_counter = 0

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.all_cards = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def remove_card(self):
        return self.cards.pop(0)

    def add_cards(self, new_cards):
        if isinstance(new_cards, list):
            self.cards.extend(new_cards)
        else:
            self.cards.append(new_cards)

    def __str__(self):
        return f"{self.name} has {len(self.cards)} cards."

if __name__ == "__main__":

    player_1 = Player("Ronaldo")
    player_2 = Player("Messi")

    deck = Deck()
    deck.shuffle()

    # Deal 26 cards to each player
    for i in range(26):
        player_1.add_cards(deck.deal_one())
        player_2.add_cards(deck.deal_one())

    game_on = True
    round_num = 0

    # Maximum number of rounds to prevent infinite loops
    max_rounds = 10000

    # Main game loop
    while game_on and round_num < max_rounds:
        round_num += 1
        print(f"\nRound {round_num}")

        if len(player_1.cards) == 0:
            print(f"{player_1.name} is out of cards! {player_2.name} wins the game!")
            game_on = False
            break

        if len(player_2.cards) == 0:
            print(f"{player_2.name} is out of cards! {player_1.name} wins the game!")
            game_on = False
            break

        # Start a new round
        player_1_cards = [player_1.remove_card()]
        player_2_cards = [player_2.remove_card()]

        at_war = True

        while at_war:
            
            print(f"{player_1.name} plays: {player_1_cards[-1]}")
            print(f"{player_2.name} plays: {player_2_cards[-1]}")

            if player_1_cards[-1].value > player_2_cards[-1].value:
                print(f"{player_1.name} wins this round!")
                player_1.add_cards(player_1_cards)
                player_1.add_cards(player_2_cards)
                at_war = False
            elif player_2_cards[-1].value > player_1_cards[-1].value:
                print(f"{player_2.name} wins this round!")
                player_2.add_cards(player_1_cards)
                player_2.add_cards(player_2_cards)
                at_war = False
            else:
                print("WAR!")
                war_counter += 1
                # If it's a tie, we go to war
                # Check if players have enough cards for war
                if len(player_1.cards) < 5:
                    print(f"{player_1.name} cannot continue war. {player_2.name} wins!")
                    game_on = False
                    break
                elif len(player_2.cards) < 5:
                    print(f"{player_2.name} cannot continue war. {player_1.name} wins!")
                    game_on = False
                    break
                else:
                    # Each player places 5 cards face down
                    for _ in range(5):
                        player_1_cards.append(player_1.remove_card())
                        player_2_cards.append(player_2.remove_card())

    print(f"\n\nWar counter: {war_counter}")
    # The game has ended, print the final scores
    print(f"{player_1.name} has {len(player_1.cards)} cards.")
    print(f"{player_2.name} has {len(player_2.cards)} cards.")

    #This creates/updates a txt file to hold record of how many times each player won a game of War
    
    """ def read_win_counts(filename="war_wins_count.txt"):
        counts = {"Ronaldo": 0, "Messi": 0}
        try:
            with open(filename, "r") as f:
                for line in f:
                    name, count = line.strip().split(":")
                    counts[name.strip()] = int(count.strip())
        except FileNotFoundError:
            pass
        return counts

    def write_win_counts(counts, filename="war_wins_count.txt"):
        with open(filename, "w") as f:
            for name, count in counts.items():
                f.write(f"{name}: {count}\n")

    # This code reads the win counts from a file, updates them based on the game results,

    # At the end, after determining the winner:
    win_counts = read_win_counts()

    if len(player_1.cards) > len(player_2.cards):
        print(f"{player_1.name} wins the game!")
        win_counts[player_1.name] += 1

    elif len(player_2.cards) > len(player_1.cards):
        print(f"{player_2.name} wins the game!")
        win_counts[player_2.name] += 1

    else:
        print("It's a tie!")

    write_win_counts(win_counts)
 """
