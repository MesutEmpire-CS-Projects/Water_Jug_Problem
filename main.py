from collections import deque

# Initial State
INITIAL_STATE = (0, 0)

'''
Perform pour action
'''


def pour(from_container, to_container, container_1_capacity, container_2_capacity, state):
    container_1, container_2 = state
    if from_container == 1:
        if container_1 > 0 and container_2 < container_2_capacity:
            amount_poured = min(container_1, container_2_capacity - container_2)
            new_container_1 = container_1 - amount_poured
            new_container_2 = container_2 + amount_poured
            return new_container_1, new_container_2
    else:
        if container_2 > 0 and container_1 < container_1_capacity:
            amount_poured = min(container_2, container_1_capacity - container_1)
            new_container_1 = container_1 + amount_poured
            new_container_2 = container_2 - amount_poured
            return new_container_1, new_container_2
    return None


'''
Solves the problem using Breadth First Search Algorithm
'''


def water_prob(container_1_capacity, container_2_capacity, target_capacity):
    visited = set()
    queue = deque()

    queue.append((INITIAL_STATE, []))

    while queue:
        current_state, actions = queue.popleft()

        if current_state[0] == target_capacity or current_state[1] == target_capacity:
            return actions

        visited.add(current_state)

        for action in [
            "Fill Container 1",
            "Fill Container 2",
            "Empty Container 1",
            "Empty Container 2",
            "Pour Container 1 to Container 2",
            "Pour Container 2 to Container 1"]:

            new_state = None
            if action == "Fill Container 1":
                new_state = (container_1_capacity, current_state[1])
            elif action == "Fill Container 2":
                new_state = (current_state[0], container_2_capacity)
            elif action == "Empty Container 1":
                new_state = (0, current_state[1])
            elif action == "Empty Container 2":
                new_state = (current_state[0], 0)
            elif action == "Pour Container 1 to Container 2":
                new_state = pour(1, 2, container_1_capacity, container_2_capacity, current_state)
            elif action == "Pour Container 2 to Container 1":
                new_state = pour(2, 1, container_1_capacity, container_2_capacity, current_state)

            # print(f'C.0 : {current_state[0]} ,C.1 : {current_state[1]}')
            # print(
            #     f'N.0 : {new_state[0] if new_state is not None else ""} ,N.1 : {new_state[1] if new_state is not None else ""}')

            if new_state is not None and new_state not in visited:
                new_actions = actions + [action]
                queue.append((new_state, new_actions))

    return None


if __name__ == "__main__":

    container_1_capacity = int(input('Enter Container 1 Capacity : '))
    container_2_capacity = int(input('Enter Container 2 Capacity : '))
    target_capacity = int(input('Enter Target Capacity : '))

    # Solve the water jug problem
    solution = water_prob(container_1_capacity, container_2_capacity, target_capacity)
    if solution:
        print("Solution Found:")
        for i, action in enumerate(solution, start=1):
            print(f"Step {i}: {action}")
    else:
        print("No solution found.")
