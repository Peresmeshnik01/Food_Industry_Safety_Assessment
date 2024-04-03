import numpy as np
from sklearn import preprocessing
# Предоставление меток входных данных
input_labels = ['помидор', 'пикули', 'cыр', 'котлета', 'салат']

# Создание кодировщика и установление соответствия
# между метками и числами
encoder = preprocessing.LabelEncoder()
encoder.fit(input_labels)

# Вывод отображения
print("Нумерапция продуктов:")
for i, item in enumerate(encoder.classes_):
    print(item, '-->', i)
    
#преобразование меток с помощью кодировщика
test_labels = ['котлета', 'пикули', 'помидор']
encoded_values = encoder.transform(test_labels )
print("\nПатрик, на столде лежат следующие продукты: =", test_labels)
print("Какому номеру соответствует каждый продукт?")
print("Их номера =", list (encoded_values))

# Декодирование набора чисел с помощью декодера
encoded_values = [3, 0, 4, 1]
decoded_list = encoder.inverse_transform(encoded_values)
print("\nПатрик, вот номера ящиков с продуктами =", encoded_values)
print("Какой вид продуктов лежит в каждом ящике?")
print("Вид продукта в каждом ящике =", list (decoded_list))
