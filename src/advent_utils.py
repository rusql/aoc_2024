from pathlib import Path

def day_str(day):
    if day < 10:
        return f"0{day}"
    else:
        return f"day"
    
def get_path_to_day(day):
    return f"{Path(__file__).resolve().parents[1]}/input/day{day_str(day)}.txt"

def get_day_input_as_string(day):
    with open (get_path_to_day(day), 'r') as f:
        return f.read()
        
        
#print (get_day_input_as_string(3))