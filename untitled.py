import shutil
import os
# Каталог с набором данных
data_dir = 'E:\Губка Боб и бпп\fresh-food-vs-spoiled-food-classification\train'
# Каталог с данными для обучения
train_dir = 'train'
# Каталог с данными для проверки
val_dir = 'val'
# Каталог с данными для тестирования
test_dir = 'test'
# Часть набора данных для тестирования
test_data_portion = 0.15
# Часть набора данных для проверки
val_data_portion = 0.15
# Количество элементов данных в одном классе
nb_images = 3

def create_directory(dir_name):
    if os.path.exists(dir_name):
        shutil.rmtree(dir_name)
    os.makedirs(dir_name)
    os.makedirs(os.path.join(dir_name, "fresh"))
    os.makedirs(os.path.join(dir_name, "spoiled"))    


create_directory(train_dir)
create_directory(val_dir)
create_directory(test_dir)

def copy_images(start_index, end_index, source_dir, dest_dir):
    for i in range(start_index, end_index):
        shutil.copy2(os.path.join(source_dir, "cat." + str(i) + ".jpg"), 
                    os.path.join(dest_dir, "cats"))
        shutil.copy2(os.path.join(source_dir, "dog." + str(i) + ".jpg"), 
                   os.path.join(dest_dir, "dogs"))

copy_images(0, 2, data_dir, train_dir)
copy_images(0, 2, data_dir, val_dir)
copy_images(0, 2, data_dir, test_dir)
