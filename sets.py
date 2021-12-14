# crear una función que elimine los duplicados de una lista
# [1, 1, 2, 2, 4] -> [1, 2, 3]

def remove_duplicates(some_list):
    without_duplicates = []
    for elements in some_list:
        if elements not in without_duplicates:
            without_duplicates.append(elements)
    return without_duplicates

def run():
    random_list = [1, 1, 2, 2, 4]
    print(remove_duplicates(random_list))

if __name__ == '__main__':
    run()
