import random

num_doors = input('How many doors (3)? ')
num_doors = 3 if not num_doors else int(num_doors)

runs = input('How many runs (1000)? ')
runs = 1000 if not runs else int(runs)

wins = 0

for count in range(1, int(runs) + 1):
    prize = random.randint(1, num_doors) # prize door
    guess = random.randint(1, num_doors) # guess a door

    # Create a set of doors, then remove door which hides
    # the prize and also remove door that we guessed. That
    # way we have a set of all doors we flip over and show
    # the player.

    doors_to_show = set(range(1, num_doors + 1))

    # Now, doors will be a set like {1, 2, 3}. So now we
    # remove door which hides the prize. e.g., if prize is
    # behind door 1, we'll remove it, and the doors set will 
    # look like this–{2, 3}.

    doors_to_show.remove(prize)

    # If player guessed wrong, we remove the door that player 
    # chose (e.g., perhaps 2, in this example, leaving the
    # doors set to be {3}). Then host will show player what's 
    # behind door 3 and player will switch to the door which
    # hides the prize.

    if guess != prize:
        doors_to_show.remove(guess)
        switch = prize

    # The other case is that player guessed right, and will
    # switch to a non-prize door, which in this case will be
    # the last door from the set above, i.e., 3.

    else:
        switch = doors_to_show.pop()

    # If we have > 3 doors, the host will open up ALL the
    # doors except for the player's original choice and the
    # one hiding the prize. If there are more than 10 doors,
    # this leads to voluminous output, so we'll just write
    # 'all others'.

    if num_doors > 10:
            doors = '[all others]'

    print(f'\nRun {count}: prize is behind door {prize} (and you picked {guess})')
    print(f"Take a look at what's behind door {doors_to_show} ... a goat!")
    print(f'You switched to door {switch}', 'WIN!' if guess != prize else 'LOSE')
        
    if guess != prize:
        wins += 1

print(f'\nSwitching yielded {wins} wins / {count} attempts = {wins / count:.3f}')
