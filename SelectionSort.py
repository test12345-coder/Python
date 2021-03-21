def SelectionSort(liste):
  for i in range(len(liste) - 1):
    minimum = i 
    for j in range(i +  1, len(liste) - 1):
      if(liste[j] < liste[minimum]):
        minimum = j
    if(minimum != i):
      liste[i], liste[minimum] = liste[minimum], liste[i]
    return liste
          
if __name__ == '__main__':
  liste = [12, 40, 8, 33, 52, 3, 10, 83]
  print(SelectionSort(liste))
