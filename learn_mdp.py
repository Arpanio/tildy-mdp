# author Vipul Vaibhaw - vaibhaw.vipul@gmail.com
# Feel free to reach out

# This code is inspired from this talk https://www.youtube.com/watch?v=ggqnxyjaKe4
# Thanks a lot richard sutton - http://incompleteideas.net/

import random
import numpy as np
# np.random.choice(4, 1000, p=[0.1, 0.2, 0.3, 0.4])

ACTIONS_TO_TAKE = [1, 2]
STATES = ["A", "B"]

# define global counter for time step

TIME_STEP = 0
INITIAL_STATE = STATES[0]

print("\nWelcome to a simulation!")
print("This code is inspired from this talk - https://youtu.be/ggqnxyjaKe4?t=934\n")

print("Actions={1, 2}")

MDP = {"time": TIME_STEP, "state": INITIAL_STATE}

CURRENT_STATE = INITIAL_STATE


def rewards(amount):
    if amount == "small pos":
        print("\treward: +" + str(random.randint(10, 15)))
    elif amount == "small neg":
        print("\treward: " + str(random.randint(-15, -10)))
    elif amount == "big pos":
        print("\treward: +" + str(random.randint(37, 50)))
    else:
        print("\treward: +" + str(random.randint(0, 5)))


def change_state(current_state, user_input):
    global CURRENT_STATE
    # if current State is A and user presses 1, come back to A 100% times. small reward.
    if current_state == "A" and user_input == 1:
        CURRENT_STATE = STATES[0]
        rewards("small pos for A") 
    # if current State is A and user presses 2,
    # 80% chances that it goes to B and 20% that it comes back to A.
    # Small negative reward.
    elif current_state == "A" and user_input == 2:
        CURRENT_STATE = np.random.choice(STATES, 1, p=[0.2, 0.8])[0]
        if CURRENT_STATE == "A":
            rewards("small pos")
        else:
            rewards("small neg")
    # if current state is B and user presses 1,
    # 80% chances that it goes to A and 20% that it comes back to B.
    # Big reward.
    elif current_state == "B" and user_input == 1:
        CURRENT_STATE = np.random.choice(STATES, 1, p=[0.8, 0.2])[0]
        if CURRENT_STATE == "B":
            rewards("small neg")
        else:
            rewards("big pos")
    # if current state is B and user presses 1,
    # 80% chances that it goes to A and 20% that it comes back to B.
    # Small reward.
    elif current_state == "B" and user_input == 2:
        CURRENT_STATE = np.random.choice(STATES, 1, p=[0.8, 0.2])[0]
        if CURRENT_STATE == "A":
            rewards("small pos")
        else:
            rewards("small neg")
    else:
        print("Boo!")


def update_mdp(time_step, current_state):
    global MDP
    MDP = {"time": time_step, "state": current_state}


def print_msg(mdp):
    print("time = "+str(mdp["time"])+", state = "+mdp["state"]+", action = ")


def get_globals():
    global ACTIONS_TO_TAKE
    global STATES
    return ACTIONS_TO_TAKE, STATES


if __name__ == "__main__":
    ACTIONS_TO_TAKE, _ = get_globals()
    while True:
        print_msg(MDP)
        user_input = int(input())
        if user_input not in ACTIONS_TO_TAKE:
            print("Invalid action. Please choose an option from {}".format(ACTIONS_TO_TAKE))
            continue
        change_state(CURRENT_STATE, user_input)
        TIME_STEP = TIME_STEP + 1
        update_mdp(TIME_STEP, CURRENT_STATE)

