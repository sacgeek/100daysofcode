# Grant Armstrong
# 01/12/2021
# Day011 Blackjack Game

import os
import random
from art import logo
from cards import *

deck = ['ace', 'ace', 'ace', 'ace', 'two', 'two', 'two', 'two', 'three', 'three', 'three', 'three', 'four', 'four',
        'four', 'four', 'five', 'five', 'five', 'five', 'six', 'six', 'six', 'six', 'seven', 'seven', 'seven', 'seven',
        'eight', 'eight', 'eight', 'eight', 'nine', 'nine', 'nine', 'nine', 'ten', 'ten', 'ten', 'ten', 'jack', 'jack',
        'jack', 'jack', 'queen', 'queen', 'queen', 'queen', 'king', 'king', 'king', 'king']

points = {'ace': 11, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
          'ten': 10, 'jack': 10, 'queen': 10, 'king': 10}

display = {'ace': cards[0], 'two': cards[1], 'three': cards[2], 'four': cards[3], 'five': cards[4], 'six': cards[5],
           'seven': cards[6], 'eight': cards[7], 'nine': cards[8], 'ten': cards[9], 'jack': cards[10],
           'queen': cards[11], 'king': cards[12]}


# Function will clear command prompt window on Linux and Windows machines
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Function to deal a card from deck to player and remove it from the deck
def deal_card(current_deck):
    card = random.choice(current_deck)
    current_deck.remove(card)
    return card


# Function returns the total score of the handed that is passed in
def score_hand(hand):
    hand_sum = 0
    low_sum = 0
    high_sum = 0
    # Return sum of hand that doesn't contain an Ace
    if 'ace' not in hand:
        for card in hand:
            hand_sum += points[card]
        return hand_sum
    # Return tuple of potential scores if hand contains an Ace
    elif 'ace' in hand:
        for card in hand:
            high_sum += points[card]
        low_sum = high_sum - 10
        return low_sum, high_sum


# Function returns the total score of hand passed to it. If Aces are present it returns the highest score <= 21
def score_final_hand(hand):
    hand_sum = 0
    high_sum = 0
    # Return sum of hand that doesn't contain an Ace
    if 'ace' not in hand:
        for card in hand:
            hand_sum += points[card]
        return hand_sum
    # Return tuple of potential scores if hand contains an Ace
    elif 'ace' in hand:
        for card in hand:
            high_sum += points[card]
        low_sum = high_sum - 10
        return high_sum if high_sum <= 21 else low_sum


# Check a hands score to see if it busts
def bust(hand):
    score = score_hand(hand)
    if isinstance(score, int):
        if score <= 21:
            return False
    elif isinstance(score, tuple):
        if score[0] <= 21 or score[1] <= 21:
            return False
    else:
        return True


playing = 'y'

while playing.lower() in ['y', 'yes']:
    clear()
    print(logo, '\n')

    player_hand = [deal_card(deck), deal_card(deck)]
    computer_hand = [deal_card(deck), deal_card(deck)]

    print(f'Your cards: {player_hand} - Current Score: {score_hand(player_hand)}')
    print(f"Computer's visible cards: {computer_hand[0:len(computer_hand)-1]}")

    hitting = True
    while hitting:
        hit = input("Type 'hit' to get another card, type 'stay' to pass: ")
        # If the player decides to hit, append another card to their hand
        if hit.lower() in ['hit', 'yes', 'y']:
            player_hand.append(deal_card(deck))
            print(f'Your cards: {player_hand} - Current Score: {score_hand(player_hand)}')

            # If the user immediately busts... tell them they lost
            if score_final_hand(player_hand) > 21:
                print(f'Your final cards: {player_hand} - Final Score: {score_hand(player_hand)}')
                print(f"Computer's final cards: {computer_hand} - Final Score: {score_hand(computer_hand)}")
                print('You went over. You lose!')
                break

            # If the player decides to hit, have the computer check if its 17 or over and hit if they're not
            if score_final_hand(computer_hand) < 17:
                computer_hand.append(deal_card(deck))
                print(f"Computer's visible cards: {computer_hand[0:len(computer_hand) - 1]}")
            else:
                print(f"Computer's visible cards: {computer_hand[0:len(computer_hand) - 1]}")

        # The sequence if the player chooses to stay
        elif hit.lower() in ['stay', 'no', 'n']:
            # Let the computer hit until its satisfied with its hand (17 or over)
            while score_final_hand(computer_hand) < 17:
                print("The computer has hit...")
                computer_hand.append(deal_card(deck))
                print(f"Computer's visible cards: {computer_hand[0:len(computer_hand) - 1]}")

            # Finally, compare the computers hand to the players hand
            player_final_score = score_final_hand(player_hand)
            computer_final_score = score_final_hand(computer_hand)
            if player_final_score <= 21 >= computer_final_score:
                print(f'\n\nYour final cards: {player_hand} - Final Score: {score_final_hand(player_hand)}')
                print(f"Computer's final cards: {computer_hand} - Final Score: {score_final_hand(computer_hand)}")
                print('You beat the dealer!' if player_final_score > computer_final_score else 'The dealer beat you!')
                break
            elif player_final_score <= 21 < computer_final_score:
                print(f'\n\nYour final cards: {player_hand} - Final Score: {score_final_hand(player_hand)}')
                print(f"Computer's final cards: {computer_hand} - Final Score: {score_final_hand(computer_hand)}")
                print('You beat the dealer! You win!')
                break
            elif computer_final_score <= 21 < player_final_score:
                print(f'\n\nYour final cards: {player_hand} - Final Score: {score_final_hand(player_hand)}')
                print(f"Computer's final cards: {computer_hand} - Final Score: {score_final_hand(computer_hand)}")
                print('You busted! The dealer wins!')
                break

    player = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ")