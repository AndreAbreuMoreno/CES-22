#Return only those items that are present in both lists.
def find_itens_present_both_list(list1, list2):
    """ Both the vocab and wds must be sorted.  Return a new
        list of words from wds that do not occur in vocab.
    """

    result = []
    xi = 0
    yi = 0

    while xi < len(list1) and yi < len(list2):
        if list1[xi] == list2[yi]:
            result.append(list1[xi])

        elif list1[xi] > list2[yi]:
            yi += 1

        else:
            xi += 1


#Return only those items that are present in the first list,
# but not in the second.
#Return only those items that are present in the second list,
# but not in the first.
#Return items that are present in either the first or the second list.
#Return items from the first list that are not eliminated by a
# matching element in the second list. In this case, an item in
# the second list “knocks out” just one matching item in the
# first list. This operation is sometimes called bagdiff.
# For example bagdiff([5,7,11,11,11,12,13], [7,8,11])
# would return [5,11,11,12,13]


list1 = [1,2,3,4,5,6,7,8,9]
list2 = [5,6,7,8,9,10,11,12]

lista = find_itens_present_both_list(list1,list2)

print("{0}".format(lista))