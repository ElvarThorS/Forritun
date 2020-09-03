p1_move = input("Player 1's move: ")
p2_move = input("Player 2's move: ")

# ...now fill in the rest
if p1_move == 'rock' and p2_move == 'scissors':
    print('Winner: Player 1')
elif p1_move == 'paper' and p2_move == 'rock':
    print('Winner: Player 1')
elif p1_move == 'scissors' and p2_move == 'paper':
    print('Winner: Player 1')
elif p2_move == 'rock' and p1_move == 'scissors':
    print('Winner: Player 2')
elif p2_move == 'paper' and p1_move == 'rock':
    print('Winner: Player 2')
elif p2_move == 'scissors' and p1_move == 'paper':
    print('Winner: Player 2')
elif p1_move == p2_move:
    print("It's a draw")