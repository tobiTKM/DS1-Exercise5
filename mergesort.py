import matplotlib.pyplot as plt

# Funktion zum Zuweisen eines Werts von einer Liste zu einer anderen
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

# Funktion zum Sortieren einer Liste mit dem Merge-Sort-Algorithmus
def merge_sort(list_to_sort_by_merge):
    """
    Diese Funktion sortiert eine Liste in-place mit dem Merge-Sort-Algorithmus.

    Parameters:
    list_to_sort_by_merge (list): Die zu sortierende Liste.
    """
    # Wenn die Liste nur ein Element oder kein Element enthält, ist sie bereits sortiert
    if(len(list_to_sort_by_merge) <= 1):
        return
    
    # Teilen der Liste in zwei Hälften
    list_mid = len(list_to_sort_by_merge) // 2
    left_list_part = list_to_sort_by_merge[:list_mid]
    right_list_part = list_to_sort_by_merge[list_mid:]

    # Sortieren der beiden Hälften der Liste
    merge_sort(left_list_part)
    merge_sort(right_list_part)

    # Initialisieren der Indizes für die linke Liste, die rechte Liste und die Gesamtliste
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


# Dieser Code wird nur ausgeführt, wenn dieses Skript direkt ausgeführt wird und nicht, wenn es als Modul importiert wird
if __name__ == "__main__": 
    # Initialisieren der zu sortierenden Werte
    y_values = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # Erstellen einer Liste von Indizes für die Werte
    x_values = range(len(y_values))
    
    # Erstellen eines Plots der unsortierten Werte
    plt.plot(x_values, y_values)
    plt.title("Unsorted values")  
    plt.xlabel("Index")  
    plt.ylabel("Value") 
    plt.grid()  
    plt.show()  
    
    # Sortieren der Werte mit dem Merge-Sort-Algorithmus
    merge_sort(y_values)
    
    # Erstellen eines Plots der sortierten Werte
    plt.plot(x_values, y_values)
    plt.title("Sorted values") 
    plt.xlabel("Index")  
    plt.ylabel("Value") 
    plt.grid() 
    plt.show() 