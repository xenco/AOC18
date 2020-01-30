num_marbles = 71700 #70953
available_marbles = [x for x in range(1, num_marbles + 2)]

# init players with 0 score
num_players = 405
players = {i: 0 for i in range(1, num_players + 1)}

state = []

# initial turn
state.append(0)
i_current_marble = 0
current_marble = available_marbles.pop(0)
current_player = 1

print("[-] %s" % (state))

while len(available_marbles) > 0:
    print(current_marble)
    if current_marble % 23 == 0:
        players[current_player] += current_marble

        i_seven_left = i_current_marble - 7
        while i_seven_left < 0: i_seven_left += len(state)
        players[current_player] += state[i_seven_left]

        i_current_marble = (i_seven_left) % len(state)

        del state[i_seven_left]
    else:
        i_one_right = (i_current_marble + 1) % len(state)
        i_two_right = (i_current_marble + 2) % len(state)

        if i_one_right < i_two_right:
            state = state[:i_one_right + 1] + [current_marble] + state[i_two_right:]
        elif i_one_right == len(state) - 1 and i_two_right == 0:
            state.append(current_marble)

        i_current_marble = state.index(current_marble)

    # print("[%s] %s" % (current_player, state))

    current_player = current_player + 1 if current_player + 1 <= num_players else 1
    current_marble = available_marbles.pop(0)

max_score = 0
for i in sorted(players):
    if players[i] > max_score:
        max_score = players[i]

print("---")
print(max_score)