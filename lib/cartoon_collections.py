def roll_call_dwarves(dwarves):
    [print(f"{(index+1)}. {dwarf}")for index, dwarf in enumerate(dwarves)]
    

def summon_captain_planet(calls):
    return [f"{call.capitalize()}!" for call in calls]
    pass

def long_planeteer_calls(calls):
    return len([call for call in calls if len(call)>4 ]) > 0

def find_the_cheese(check_list):
    cheese_list = ["cheddar", "gouda", "thyme"]
    for check in check_list:
        if check in cheese_list:
            return check
    return None
