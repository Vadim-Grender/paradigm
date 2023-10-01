
#императивный
def bubble_sort_descending(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] < numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                
numbers = [10, 9, 43, 15, 1, 88, 105]
bubble_sort_descending(numbers)
print('Сортировка по убыванию:', numbers)
#декларативный
def sort_descending(numbers):
    return sorted(numbers, reverse=True)
numbers = [10, 9, 43, 15, 1, 88, 105]
sorted_descending_numbers = sort_descending(numbers)
print("Сортировка по убыванию:", sorted_descending_numbers)