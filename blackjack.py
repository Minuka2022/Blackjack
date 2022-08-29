from multiprocessing import reduction
from operator import is_
import random
from secrets import choice



def deal_card ():
 card = [11,2,3,4,5,6,7,8,9,10,10,10,10]

 card =  random.choice(card)
 return card


def play_game():
    user_card = []
    computer_card = []
    is_game_over = False

    while not is_game_over:

        def calculate_score(card):

            if sum(card) ==21 and len(card) == 2:
                return 0
            if 11 in card and sum(card) > 21:
                card.remove(11)
                card.append(1)
            
            return  sum(card)


        def compare(user_score,computer_score):
            if user_score == computer_score:
                return "Draw"
            elif computer_score == 0:
                return "Lose, opponent has black jack"
            elif user_score == 0:
                return "You win a Black Jack"
            elif user_score > 21:
                return "You went over. you loss"
            elif computer_score > 21:
                return "Oppenent went over. you win"




        for _ in range(2):
            new_card = deal_card()

            user_card.append(new_card)
            computer_card.append(new_card)

        user_should_play = input("Type 'y' to get another card, type 'n' to pass: ")

        if user_should_play == "y":
            user_card.append(deal_card())
        else:
            is_game_over = True


        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f" Your card: {user_card}, current score: {user_score}")
        print(f" Compter's fitst card: {computer_card[0]}")


        if user_score == 0 or computer_score == 0 or user_score>21:
            is_game_over = True
        else:

         while computer_score != 0 and computer_score < 17:
            computer_card.append(deal_card())
            computer_score = calculate_score(computer_card)
        

        print(f" Your final hand:{user_card}, final score: {computer_score}")
        print(f"Compter's final hand: {computer_card}, final score: {computer_score}")
        print(compare(user_score,computer_score))




