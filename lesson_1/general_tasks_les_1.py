#task1
lst = [12, 5, 2, 3, 4, 5, 9]
def get_statistics(lst):
    lst.sort()
    return f'{round(sum(lst)/len(lst),1), lst[0], lst[-1]}'
result = get_statistics(lst)
print(result)

#task2
list1 = ['apple', 'banana', 'cherry']
list2 = ['ant', 'bat', 'carrot', 'dog', 'elephant', 'autoban', 'bruno']
def get_words_by_letter(list1, list2):
    letters_dict = {}
    letters = set()
    for i in list1:
        letters.add(i[0])
    for i in letters:
        words_to_be_added = []
        for e in list2:
            if e[0] == i:
                words_to_be_added.append(e)
        letters_dict[i] = words_to_be_added
    return letters_dict

result = get_words_by_letter(list1, list2)
print(result)
