import csv
import sys

def AddContact(): 
    name = input("Имя: ").strip()
    number = int(input("Номер телефона: ").strip())
   
    # упорядочиваем в формате словаря
    contactInfo = dict(name=name, number=number)

    # эта же информация в csv файл
    with open('data.csv', 'a', newline='') as contact:
        fieldnames = ['name', 'number']
        writer = csv.DictWriter(contact, fieldnames=fieldnames)
        writer.writerow(contactInfo)

def ContactSearch():
    
    with open('data.csv', newline='') as file:
        #  преобразуем csv в читаемый словарь
        reader = list(csv.DictReader(file))
        q = input("Введите имя или номер: ")  # запрос поиска
        for i in range(0, len(reader)):
            if q in reader[i].values(): 
                print(("#")*20, "Результат поиска", ("#")*20, end=None)
                result = reader[i].items()
                print(result)
                print(("#")*20, "Готово", ("#")*20, end=None)
                break
            if q not in reader[i].values():
                
                continue
        else:
            print(("#")*20, end=None)
            print("Контакт не найден!")
            print(("#")*20, end=None)

            # запрос доп. действия
            search_query = input("Ищем ещё? Y/N: ")
            if search_query == 'Y':
                search = ContactSearch()
            elif search_query == 'N':

                print(("*")*20, end=None)

                search = "Вы вышли из справочника"
                print(search)
                print(("*")*20, end=None)
              
                sys.exit()
            return search

def contactdelete():
    lines = list()
    members = input("Введите удаляемый номер")
    with open('data.csv', newline='') as delfile:
        reader = csv.reader(delfile)
        for row in reader:
            lines.append(row)
            for field in row:
                if field == members:
                    lines.remove(row)

    # обновляем  CSV
    with open("data.csv", 'w', newline="") as writeFile:
        writer = csv.writer(writeFile)
        writer.writerow(lines)
        print("удалено.")
        print(lines)
        sys.exit()

def main():
    question = input(
        "Что делаем? C: Добавляеи контакт, S: Поиск, D: Удаляем ")
    if question == "C":
        run_def = AddContact()
    elif question == "S":
        run_def = ContactSearch()
    elif question == "D":
        run_def = contactdelete()
    return run_def

main()