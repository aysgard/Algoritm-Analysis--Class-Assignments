# Simulate 3-door game
import random

# Simulate the game N times
# Return the number of times a game player guessed correctly by switching

def simulate(N):
    correct_guess_count = 0
    all_doors_set = {"A", "B", "C"}

    for i in range(0, N):

        # Game organizers select a door randomly and places a car behind it
        door_with_car = select_door()

        # Game player selects a door randomly hoping that the car is behind it
        player_initial_guess = select_door()

        # Host opens one of the doors that is empty
        host_opened_door = host_opens_door(door_with_car, player_initial_guess)

        # The player switches their choice
        remaining_door = all_doors_set - {player_initial_guess, host_opened_door}
        player_switched_guess = remaining_door.pop()

        # Check if the player guessed correctly after switching
        if player_switched_guess == door_with_car:
            correct_guess_count += 1

    return correct_guess_count

# Simulate the choice of the door with a car behind it
def select_door():
    # Draw a random number between 0 and 1. If between 0 and 1/3, then
    # door 1 selected, if between 1/3 and 2/3, then door 2, otherwise
    # door 3.
    r = random.random()
    if r < (1.0 / 3.0):
        return "A"
    elif (1.0 / 3.0) <= r < (2.0 / 3.0):
        return "B"
    # r > 2/3
    return "C"

# Simulate host opening a door
# Host opens a door that is empty and not the player's initial choice

def host_opens_door(door_with_car, player_guess):
    all_doors = ["A", "B", "C"]

    doors_host_can_open = []
    for door in all_doors:
        if door != door_with_car and door != player_guess:
            doors_host_can_open.append(door)

    return random.choice(doors_host_can_open)


N_values_to_test = [10000, 100000, 1000000]
for N in N_values_to_test:

    hits = simulate(N)
    print("Total games played:", N)
    print("Wins by switching: ", hits)
    print("Percentage of times guess was right = %", (100.0 * hits) / N)

