def remove_duplicates(some_list):
    no_duplicates = set(some_list)
    return list(no_duplicates)

def run():
    random_list = [1, 1, 2, 2, 4]
    for element in remove_duplicates(random_list):
        print(element)

if __name__ == '__main__':
    run()