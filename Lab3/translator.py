import os

def find_files(filename):
   plan_files = []
# Wlaking top-down from the root
   for root, dir, files in os.walk(os.getcwd()):
      for name in files:
        if filename in name:
            plan_files.append(name)
   return plan_files

def translate():
    plans = find_files("myplan.txt")
    if len(plans) == 0:
        message = "NO SOLUTION FOUND IN 1 minute"
        print(message)
        return "no solution"
    plans = [plans[0]]
    for plan_file in plans:
        plan = open(plan_file, 'r')
        actions = plan.readlines()
        print('\n\n------ BEST FOUND PLAN START ------')
        for action in actions:
            #print(action)
            if 'move' in action:
                list = action.split()
                initial_posx = list[1][4]
                initial_posy = list[1][1]
                final_posx = list[2][4]
                final_posy = list[2][1]
                if initial_posx < final_posx:
                    print('MOVE RIGHT: ('+initial_posx+','+initial_posy+') -> ('+final_posx+','+final_posy+')')
                elif initial_posx > final_posx:
                    print('MOVE LEFT: ('+initial_posx+','+initial_posy+') -> ('+final_posx+','+final_posy+')')
                elif initial_posy < final_posy:
                    print('MOVE DOWN: ('+initial_posx+','+initial_posy+') -> ('+final_posx+','+final_posy+')')
                elif initial_posy > final_posy:
                    print('MOVE UP: ('+initial_posx+','+initial_posy+') -> ('+final_posx+','+final_posy+')')
                #print(list)
            elif 'push' in action:
                list = action.split()
                initial_posx = list[2][4]
                initial_posy = list[2][1]
                final_posx = list[3][4]
                final_posy = list[3][1]
                if initial_posx < final_posx:
                    print('PUSH BOX RIGHT: ('+initial_posx+','+initial_posy+') -> ('+final_posx+','+final_posy+') | NEW USER LOCATION: ('+initial_posx+','+initial_posy+')')
                elif initial_posx > final_posx:
                    print('PUSH BOX LEFT: ('+initial_posx+','+initial_posy+') -> ('+final_posx+','+final_posy+') | NEW USER LOCATION: ('+initial_posx+','+initial_posy+')')
                elif initial_posy < final_posy:
                    print('PUSH BOX DOWN: ('+initial_posx+','+initial_posy+') -> ('+final_posx+','+final_posy+') | NEW USER LOCATION: ('+initial_posx+','+initial_posy+')')
                elif initial_posy > final_posy:
                    print('PUSH BOX UP: ('+initial_posx+','+initial_posy+') -> ('+final_posx+','+final_posy+') | NEW USER LOCATION: ('+initial_posx+','+initial_posy+')')
                #print(list)
            elif 'teleport' in action:
                list = action.split()
                initial_posx = list[1][4]
                initial_posy = list[1][1]
                final_posx = list[2][4]
                final_posy = list[2][1]
                print('SUPER TELEPORT: ('+initial_posx+','+initial_posy+') -> ('+final_posx+','+final_posy+')')
            elif 'cost' in action:
                list = action.split()
                print('The total cost of the plan is: '+list[3]+' unit cost')
                print('------ BEST PLAN END ------\n')
    return "SOLUTION found"+" cost: "+str(list[3])