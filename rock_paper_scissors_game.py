import random

choices = ['rock','paper','scissors']

computer = random.choice(choices)

count_win = 0
count_lose = 0
count_tie = 0

while True:
    player = input('Enter rock, paper,scissor! ').lower()


    if player == computer:
        print('computer: ',computer )
        print('player: ', player)
        print('Tie')
        count_tie += 1
    elif player == 'rock':
        if computer == 'paper':
            print('computer: ',computer )
            print('player: ', player)  
            print('You lose!')
            count_lose += 1  
    
        if computer == 'scissor':
            print('computer: ',computer )
            print('player: ', player)
            print('You win!')
            count_win += 1

    elif player == 'paper':
        if computer == 'rock':
            print('computer: ',computer )
            print('player: ', player)  
            print('You win!')
            count_win += 1  
    
        if computer == 'scissor':
            print('computer: ',computer )
            print('player: ', player)
            print('You lose!')
            count_lose += 1

    elif player == 'scissor':
        if computer == 'rock':
            print('computer: ',computer )
            print('player: ', player)  
            print('You lose!')
            count_lose += 1  
    
        if computer == 'paper':
            print('computer: ',computer )
            print('player: ', player)
            print('You win!')
            count_win += 1
    
    play_again = input('Do you play again (yes/no) ? ')
    if play_again != 'yes':
        break

print('Thank you for playing')
print(f'You {count_lose} times lose')
print(f'You {count_win} times win')
print(f'You {count_tie} times tie')
print(f'overal {count_lose + count_win + count_tie} attending')


