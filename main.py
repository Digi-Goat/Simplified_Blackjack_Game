card1 = int(input("What is your first card up to 11?"))
card2 = int(input("What is your second card up to 11?"))
card_sum = card1 + card2
is_21_or_over = 21

if card_sum > is_21_or_over:
    print("Bust!")
elif card_sum == is_21_or_over:
    print("Blackjack!")
else:
    print("No Bust!")