my_string = "csca08 quiz 04"
my_dict = {}

for i in range(0, len(my_string) -1):
    current_char = my_string[i]
    next_char = my_string[i+1]
    my_dict[current_char] = next_char
    
for key in my_dict:
    print(key + "->" + my_dict[key])