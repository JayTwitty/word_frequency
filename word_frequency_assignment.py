
with open("sample") as sample_file:
    contents = sample_file.read`()

contents = contents.lower().replace("\n", " ").replace("*"," ").replace("/", " ").replace("."," ").replace("?"," ").replace("("," ").replace(")"," ").replace("'"," ").replace("\""," ").replace(";"," ").replace("-"," ").replace("!"," ").replace("]"," ").replace("["," ").replace("@"," ").replace("#"," ").replace(","," ").replace("$"," ").replace(":"," ").replace("%"," ")

contents = contents.split()

histogram = {}

for word in contents:
    histogram[word] = contents.count(word)

list_values = histogram.items()

def value_sort(val):
    return val[1]

list_values_sorted = sorted(list_values, reverse=True, key=value_sort)

list_values_sorted_20 = list_values_sorted[:20]

for key,val in list_values_sorted_20:
    print (key,val)
#print(*list_values_sorted_20, sep="\n")

