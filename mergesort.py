import matplotlib.pyplot as plt
import numpy as np


def assignment(new_list, i, old_list, j):
    """
    Diese Funktion weist den Wert an Position j in old_list der Position i in new_list zu.

    Parameters:
    new_list (list): Die Liste, in die der Wert eingefügt wird.
    i (int): Der Index in new_list, an dem der Wert eingefügt wird.
    old_list (list): Die Liste, aus der der Wert genommen wird.
    j (int): Der Index in old_list, von dem der Wert genommen wird.
    """
    new_list[i] = old_list[j]


def merge_sort(list_to_sort_by_merge):
    """
    Diese Funktion sortiert eine Liste in aufsteigender Reihenfolge mit dem Merge-Sort-Algorithmus.

    Parameters:
    list_to_sort_by_merge (list): Die zu sortierende Liste.
    """
    # Wenn die Liste nur ein Element oder kein Element enthält, ist sie bereits sortiert
    if len(list_to_sort_by_merge) <= 1:
        return
    
    # Teilen der Liste in zwei Hälften
    list_mid = len(list_to_sort_by_merge) // 2
    left_list_part = list_to_sort_by_merge[:list_mid]
    right_list_part = list_to_sort_by_merge[list_mid:]

    # Sortieren der beiden Hälften der Liste
    merge_sort(left_list_part)
    merge_sort(right_list_part)

    # Initialisieren der Indizes für die linke und die rechte Liste sowie dem aktuellen Index
    left_index = 0
    right_index = 0
    current_index = 0

    # Zusammenführen der beiden Hälften in die ursprüngliche Liste
    while left_index < len(left_list_part) and right_index < len(right_list_part):
        if left_list_part[left_index] <= right_list_part[right_index]:
            assignment(list_to_sort_by_merge, current_index, left_list_part, left_index)
            left_index += 1
        else:
            assignment(list_to_sort_by_merge, current_index, right_list_part, right_index)
            right_index += 1
        current_index += 1

    # Hinzufügen der restlichen Elemente der linken Liste, falls vorhanden
    while left_index < len(left_list_part):
        list_to_sort_by_merge[current_index] = left_list_part[left_index]
        left_index += 1
        current_index += 1
    
    # Hinzufügen der restlichen Elemente der rechten Liste, falls vorhanden
    while right_index < len(right_list_part):
        list_to_sort_by_merge[current_index] = right_list_part[right_index]
        right_index += 1
        current_index += 1


# Dieser Code wird nur ausgeführt, wenn das file direkt ausgeführt wird und nicht, wenn es als Modul importiert wird
if __name__ == "__main__": 
    unsorted_values = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    sorted_values = unsorted_values.copy()
    merge_sort(sorted_values)

    x_values = np.arange(len(unsorted_values))

    # set title and labels
    plt.title("Unsorted vs Sorted Values")
    plt.xlabel("Index")
    plt.ylabel("Value")

    # use grid
    plt.grid()

    # show plot (x values offset by 0.2 for two bars next to each other; width of bars: 0.4)
    plt.bar(x_values - 0.2, unsorted_values, 0.4, label='Unsorted')
    plt.bar(x_values + 0.2, sorted_values, 0.4, label='Sorted')

    plt.legend()
    plt.show()
    