print("--- Simple Reflex Agent ---")

environment = {'A': 'Dirty', 'B': 'Dirty'}
location = 'A'

for step in range(4):
    status = environment[location]
    print(f"Step {step}: Location={location}, Status={status}")

    if status == 'Dirty':
        print("Action: Suck")
        environment[location] = 'Clean'
    elif location == 'A':
        print("Action: Move Right")
        location = 'B'
    else:
        print("Action: Move Left")
        location = 'A'

print("Final environment:", environment)
