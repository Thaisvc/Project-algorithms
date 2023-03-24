def is_anagram(first_string, second_string):
    # https://www.datacamp.com/tutorial/case-conversion-python
    first_string = first_string.lower()
    first_string = merge_sort(list(first_string))
    second_string = second_string.lower()
    second_string = merge_sort(list(second_string))

    it_is_anagram = first_string == second_string and (
        first_string != "" and second_string != ""
    )
    return (first_string, second_string, it_is_anagram)


def merge_sort(string, start=0, end=None):
    if end is None:
        end = len(string)

    if end - start > 1:  # se não reduzi o suficiente, continua
        mid = (start + end) // 2   # encontrando o meio
        merge_sort(string, start, mid)  # dividindo as listas
        merge_sort(string, mid, end)
        string = merge(string, start, mid, end)  # unindo as listas

    return "".join(string)


def merge(string, start, mid, end):
    left = string[start:mid]  # indexando a lista da esquerda
    right = string[mid:end]  # indexando a lista da direita

    left = 0
    right = 0  # as duas listas começarão do início

    for index_general in range(start, end):  # curse dia 3. bloco-4
        if left >= len(left):
            string[index_general] = right[right]
            right += 1
        elif right >= len(right):
            string[index_general] = left[left]
            left += 1
        elif left[left] < right[right]:
            string[index_general] = left[left]
            left += 1
        else:
            string[index_general] = right[right]
            right += 1

    return string
