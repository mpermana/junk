# There are 10 people at a wizard meetup. 
# Each wizard has levels 0 - 9 (the index of the input) and 
# knows a few other wizards there. 
# Your job is to find the cheapest way for wizard 0 to meet wizard 9.
# Introductions have a cost that equals the square of the difference in levels. 

# Goal: Level 0 wizard wants to meet level 9 using the fewest possible magic points.
# Cost: square of difference of levels
# The index of the array represents the level (0-9)
# the value is an array with the index of the other people each person knows. 
# Note that relationships are one directional (e.g. 2 can introduce you to 3 but not vice versa)
# e.g. Min cost: 23 Min path: [0, 1, 4, 6, 9]

wizards = [
  [1, 2, 3],   # wizard 0 knows 1, 2, 3
  [8, 6, 4],   # wizard 1 knows 8, 6, 4
  [7, 8, 3],   # wizard 2 knows 7, 8, 3
  [8, 1],      # wizard 3 knows 8, 1
  [6],         # wizard 4 knows 6
  [8, 7],      # wizard 5 knows 8, 7
  [9, 4],      # wizard 6 knows 9, 4
  [4, 6],      # wizard 7 knows 4, 6
  [1],         # wizard 8 knows 1 
  [1, 4],      # wizard 9 knows 1, 4
]


minimum_cost = None
minimum_path = None

def dfs(wizard_index, visited, current_cost, current_path, target):
    global minimum_cost
    global minimum_path
    if minimum_cost is not None and current_cost > minimum_cost:
        return
    if wizard_index == target:
        # save the minimum
        if minimum_cost is None or current_cost < minimum_cost:
            minimum_cost = current_cost
            minimum_path = current_path
            minimum_path.append(target)
    # visit this wizard
    if wizard_index in visited:
        # dont visit if already
        return
    next_path = [i for i in current_path]
    next_path.append(wizard_index)
    visited.add(wizard_index)
    # get the wizard he knows, and add the cost, and recursive
    for next_wizard in wizards[wizard_index]:
        level_difference = next_wizard - wizard_index
        cost = level_difference * level_difference
        dfs(next_wizard, visited, current_cost + cost, next_path, target)
    visited.remove(wizard_index)

def search_wizard(start_wizard=0, stop_wizard=9):
    visited = set()
    dfs(start_wizard, visited, 0, [], stop_wizard)
    
search_wizard(2, 1)
print 'found', minimum_cost, minimum_path

