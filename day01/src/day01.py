from pathlib import Path

def get_distance (list1, list2):
    list1.sort()
    list2.sort()
    i = 0
    distance=0
    while i < len(list1):
        distance += abs(list1[i]-list2[i])
        i += 1
    return distance

def get_data(path_to_file):
    list1=[]
    list2=[]
    with open(path_to_file) as f:
        for line in f:
            items = line.split("   ")
            list1.append(int(items[0].strip())) 
            list2.append(int(items[1].strip()))
    return (list1, list2)


def get_occurrences(list):
    occurences = {}
    for item in set(list):
        occurences[item] = list.count(item)
    return occurences

def get_similarity_total(source_list, destination_list):
    similarity = 0
    occurrences = get_occurrences(destination_list)
    for score in source_list:
        if score in occurrences:
            similarity += score*occurrences[score]
    return similarity


#sample data accusition
list1, list2 = get_data(f"{Path(__file__).resolve().parents[1]}/input.txt")

#part 1
distance = get_distance(list1, list2)
print(f"Distance = {distance}")

#part 2
simalarity_total = get_similarity_total(list1, list2)
print(f"Simalarity Total = {simalarity_total}")
