import os
import sys
import datetime
from docxtpl import DocxTemplate
from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL, 'Russian')
def check_miss(): #Проверка по количеству символов для: серийного номера оборудования и неисправности
    if len(wrong)>=5 and len(sn)>=5 and len(note)>=10 and snsrv:
        print("Продолжаем работу")
    else:
        print('"ERROR!" Невозможно сохранить файл, вводите данные полностью!!!')
        print('Серийный номер должен иметь 5 символов! Ваше количество:', len(sn), '. Ошибки, количество символов (минимум 5):', len(wrong), '. Проверьте правильность введения SN Сервера или рабочей станции: ', snsrv)
        sys.exit(1)        
def yes_not(): #Возможность перезаписи файла (отказались)
    print("Вы хотите перезаписать файл?")
    answer = input('Введите Y или N: ')
    answer = answer.title()
    if answer == "Y":
        print("Создаём новый файл")
        doc.save(f'D:/Documents/{act}приёмЮР.docx')  # Место куда сохраняется этот файл
    else:
        print("Оставлено без изменений")
def folders(): #Проверка и создание папки
    folder_way = f'D:/Documents/{data_y}/{data_f}/{snsrv}'
    if not os.path.exists(folder_way):
        os.makedirs(folder_way)
        print("Папка создана")
    else:
        print("Папка уже существует")
def sn_server(): # Находим индекс "SSF" и ещё 6 цифр серийного номера сервера или рабочей станции из примечания (код этой функции задействован, сама функция - нет)
    index = note.find("SSF")  
    snserv_dir = note[index:index+9]  
    print(snserv_dir)
def check_file(): #Проверка на наличие файла
    test = f'D:/Documents/{data_y}/{data_f}/{snsrv}/{act}приёмЮР.docx'
    if os.path.exists(test) and os.path.isfile(test): 
        print(f"Есть файл с таким названием {act}приёмЮР.docx")
        print('Размер:', os.path.getsize(test) // 1024, 'Кб')
        print('Перезаписать файл нельзя, отредактируйте квитанцию', f'{act}приёмЮР.docx вручную!')
        sys.exit(1)
    else:
        doc.save(f'D:/Documents/{data_y}/{data_f}/{snsrv}/{act}приёмЮР.docx')  # Место куда сохраняется этот файл
        print("Сохранён новый файл")

doc = DocxTemplate("Акт приема.docx")
print("Акт приёма для юридических лиц")
act = input('Акт №: ')
sn = input('Serial Number оборудования: ')
wrong = input('Заявленная Неисправность: ')
note = input('Примечание (Обязательно ввести SN Сервера или рабочей станции, далее по желанию): ')

index = note.find("SSF")  # Находим индекс начала "SSF"
snserv_dir = note[index:index+9]  
print(snserv_dir)  # Выводим результат
snsrv = snserv_dir

check_miss()

data = (input('Введите дату: '))
data_object = datetime.strptime(data, '%Y%m%d')
data = data_object.strftime('%d %B %Y')
data_f = data_object.strftime('%m %Y')
data_y = data_object.strftime('%Y')

folders()

context = {'act': act, 'model': input('модель: '), 'sn': sn, 'wrong': wrong , 'note': note , 'date': data}
doc.render(context)

check_file()
