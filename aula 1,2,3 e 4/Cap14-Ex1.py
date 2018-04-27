#Return only those items that are present in both lists.
def find_itens_present_both_list(list1, list2):
    """ Both the list must be sorted.  Return a new
        list with itens that are present in both lists.
    """

    result = []
    xi = 0
    yi = 0

    while xi < len(list1) and yi < len(list2):
        if list1[xi] == list2[yi]:
            if list1[xi] != list1[xi-1]:
                result.append(list1[xi])
            xi += 1
            yi += 1

        elif list1[xi] > list2[yi]:
            yi += 1

        else:
            xi += 1

    return result


#Return only those items that are present in the first list,
# but not in the second.
def find_itens_present_only_first_list(list1, list2):
    """ Both the list must be sorted.  Return a new
        list with itens that are present only in the
         firs lists.
    """

    result = []
    xi = 0
    yi = 0

    while xi < len(list1):
        if yi >= len(list2):
            while xi < len(list1):
                if list1[xi] != list1[xi-1]:
                    result.append(list1[xi])
                xi += 1
            return result

        if list1[xi] > list2[yi]:
            yi += 1

        elif list1[xi] == list2[yi]:
            xi +=1
            yi +=1

        else:
            if list1[xi] != list1[xi-1]:
                result.append(list1[xi])
            xi += 1

    return result

#Return only those items that are present in the second list,
# but not in the first.
def find_itens_present_only_second_list(list1, list2):
    """ Both the list must be sorted.  Return a new
        list with itens that are present only in the
        second lists.
    """

    result = []
    xi = 0
    yi = 0

    while yi < len(list2):
        if xi >= len(list1):
            while yi < len(list2):
                if list2[yi] != list2[yi - 1]:
                    result.append(list2[yi])
                yi += 1
            return result

        if list1[xi] < list2[yi]:
            xi += 1

        elif list1[xi] == list2[yi]:
            xi +=1
            yi +=1

        else:
            if list2[yi] != list2[yi - 1]:
                result.append(list2[yi])
            yi += 1

    return result

#Return items that are present in either the first or the second list.
def merge_list (list1, list2):
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(list1):
            while yi < len(list2):
                if list2[yi] != list2[yi-1]:
                    result.append(list2[yi])
                yi += 1
            return result

        if yi >= len(list2):
            while xi < len(list1):
                if list1[xi] != list1[xi - 1]:
                    result.append(list1[xi])
                xi += 1
            return result

        sz = len(result)

        if list1[xi] == list2[yi]:
            if list1[xi] != result[sz -1]:
                result.append(list1[xi])
            xi += 1
            yi += 1

        elif list1[xi] > list2[yi]:
            if list2[yi] != result[sz -1]:
                result.append(list2[yi])
            yi += 1

        elif list1[xi] < list2[yi]:
            if list1[xi] != list1[xi -1]:
                result.append(list1[xi])
            xi += 1

    return result


#Return items from the first list that are not eliminated by a
# matching element in the second list. In this case, an item in
# the second list “knocks out” just one matching item in the
# first list. This operation is sometimes called bagdiff.
# For example bagdiff([5,7,11,11,11,12,13], [7,8,11])
# would return [5,11,11,12,13]
def bagdiff(list1, list2):
    """ Both the list must be sorted.  Return a new
        list with itens that are present only in the
         firs lists.
    """

    result = []
    xi = 0
    yi = 0

    while xi < len(list1):
        if yi >= len(list2):
            result.extend(list1[xi:])
            return result

        if list1[xi] > list2[yi]:
            yi += 1

        elif list1[xi] == list2[yi]:
            xi +=1
            yi +=1

        else:
            result.append(list1[xi])
            xi += 1

    return result


#Test
list1 = [1,2,3,3,3,4,5,5,5,7,7,7,8,9,10,12, 20]
list2 = [5,5,5,6,6,6,7,9,10,10,10,11,12]

print("lista1 = {}".format(list1))
print("lista2 = {}\n".format(list2))

lista = find_itens_present_both_list(list1, list2)
print("find_itens_present_both_list(list1, list2)={}\n".format(lista))

lista = find_itens_present_only_first_list(list1, list2)
print("find_itens_present_only_first_list(list1, list2)={}\n".format(lista))

lista = find_itens_present_only_second_list(list1, list2)
print("find_itens_present_only_second_list(list1, list2)={}\n".format(lista))

lista = merge_list(list1, list2)
print("merge_list(list1, list2 = {}\n".format(lista))

lista = bagdiff(list1, list2)
print("bagdiff(list1, list2 = {}".format(lista))