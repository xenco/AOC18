from blist import blist

num_marbles = 70953 * 100

# init players with 0 score
num_players = 405
players = {i: 0 for i in range(1, num_players + 1)}

state = blist([0])

# initial turn
i_current_marble = 0
current_marble = 1
current_player = 1
# print("[-] %s" % (state))

l_state = 1
while current_marble <= num_marbles:
    if current_marble % 23 == 0:
        players[current_player] += current_marble

        i_seven_left = (i_current_marble - 7 + l_state) % l_state
        players[current_player] += state[i_seven_left]

        i_current_marble = (i_seven_left) % l_state
        state.pop(i_seven_left)

        l_state -= 1
    else:
        i_one_right = (i_current_marble + 1) % l_state
        i_two_right = (i_current_marble + 2) % l_state

        if i_one_right < i_two_right:
            state.insert(i_one_right + 1, current_marble)
            i_current_marble = i_two_right
        elif i_one_right == l_state - 1 and i_two_right == 0:
            state.append(current_marble)
            i_current_marble = l_state
            # print("[%s] %s" % (current_player, state))
        l_state += 1

    current_player = (current_player) % num_players + 1
    current_marble += 1

max_score = 0
for i in sorted(players):
    if players[i] > max_score:
        max_score = players[i]

print("---")
print(max_score)