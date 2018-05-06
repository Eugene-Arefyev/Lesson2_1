
cook_book = {
  'пельмени': [
  {'ingridient_name': 'тесто', 'quantity': 200, 'measure': 'гр'},
  {'ingridient_name': 'фарш', 'quantity': 200, 'measure': 'гр'},
  {'ingridient_name': 'лук', 'quantity': 10, 'measure': 'гр'},
  {'ingridient_name': 'специи', 'quantity': 10, 'measure': 'гр'}
  ],
  'грибной суп': [
  {'ingridient_name': 'бульон', 'quantity': 200, 'measure': 'мл'},
  {'ingridient_name': 'грибы', 'quantity': 50, 'measure': 'гр'},
  {'ingridient_name': 'картошка', 'quantity': 50, 'measure': 'гр'},
  {'ingridient_name': 'лук', 'quantity': 10, 'measure': 'гр'},
  {'ingridient_name': 'соль', 'quantity': 5, 'measure': 'гр'}
  ],
  'хворост': [
  {'ingridient_name': 'яйца', 'quantity': 2, 'measure': 'шт'},
  {'ingridient_name': 'сахар', 'quantity': 200, 'measure': 'гр'},
  {'ingridient_name': 'мука', 'quantity': 200, 'measure': 'гр'},
  {'ingridient_name': 'соль', 'quantity': 200, 'measure': 'гр'}
  ]
}
  

def get_shop_list_by_dishes(person_count, dishes): # Функция Получить список покупок из блюд Аргументы(к-во людей и dishes)
  shop_list = {} #Словарь этот помещаем внутрь функции
  for dish in dishes:
    for ingridient in cook_book[dish]:   #dict[key]=value 
        new_shop_list_item = dict(ingridient)
        new_shop_list_item['quantity'] *= person_count
        #shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item 
        if new_shop_list_item['ingridient_name'] not in shop_list:
          shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
        else:
          shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']  
  return shop_list #Возвращает данная функция заполненный shop_list      Запоминает результат который функция Нам возвращает, чтобы потом работать с Ним
  
def print_shop_list(shop_list):
  for new_shop_list_item in shop_list.values():
    print('{} {} {}'.format(new_shop_list_item['ingridient_name'], new_shop_list_item['quantity'], new_shop_list_item['measure']))


def main():          #создаём функцию Функция точка входа в программу. Обьявляем в Ней две глобальные переменные
  person_count = int(input('Ввести кол-во человек: '))  #Для удобства пользователя совершеним код. команда input. Вводим кол-во персон
  dishes = input('Введите блюдо в расчёте на одного человека через запятую: ').lower().split(',')  #split это метод строк , который прменяется к строке и по разделителю, разбивает эту строку по элементам и эти элименты помещает в словарь      #Для того чтобы записать каждое блюдо на человека ,используем метод split
  shop_list = get_shop_list_by_dishes(person_count, dishes)                    #Так же применяем метод lower который все вводимые буквы будет делать маленькими. Противоположенный ему метод upper     
  print_shop_list(shop_list)

main()        
