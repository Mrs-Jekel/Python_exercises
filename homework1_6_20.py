list = [3, 6, 8, 2, 34, 379, 98, 7, 355, 6, 73]
list.sort()

print(list)
def find(sorted_list, num_to_find):
    for i in list:
        if i == num_to_find:
            return True
            print(i)
    return False
  

print(find(2, 5))