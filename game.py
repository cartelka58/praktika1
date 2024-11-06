import random

def start_game():
  print("Добро пожаловать в приключенческую игру!")
  print("Вы - герой, который отправляется в опасное путешествие.")
  first_choice()

def first_choice():
  print("Этап 1: Вы на лайнере. Вы провалились в трюм.")
  print("Вам нужно найти ключ, чтобы выбраться.")
  choice = input("Вы хотите (1) искать ящики или (2) искать меч? ")

  if choice == '1':
    find_key()
  elif choice == '2':
    find_sword()
  else:
    print("Неверный выбор. Попробуйте снова.")
    first_choice()

def find_key():
  print("Вы ищете ящики и находите ключ!")
  print("Теперь вы можете выбраться из трюма.")
  inventory['key'] = True
  attack_by_pirates()

def find_sword():
  print("Вы нашли меч! Это может пригодиться.")
  print("Теперь вы можете выбраться из трюма.")
  inventory['sword'] = True
  attack_by_pirates()

def attack_by_pirates():
  print("Этап 2: Лайнер атакуют пираты!")
  print("Вся команда попадает в плен, но вы уцелели.")
  choice = input("Вы хотите (1) сразиться с пиратом или (2) спрятаться? ")

  if choice == '1':
    fight_pirate()
  elif choice == '2':
    hide_and_escape()
  else:
    print("Неверный выбор. Попробуйте снова.")
    attack_by_pirates()

def fight_pirate():
  print("Вы сражаетесь с пиратом и побеждаете!")
  print("Вы получаете доступ к лодке.")
  if 'sword' in inventory:
    print("Ваш меч помог вам победить!")
  solve_riddle_for_boat()

def hide_and_escape():
  print("Вы спрятались и смогли избежать пирата!")
  print("Теперь вы можете покинуть лайнер.")
  solve_riddle_for_boat()

def solve_riddle_for_boat():
  print("Этап 3: Чтобы завести лодку, нужно разгадать загадку.")
  answer = input("Когда Джошу было 8 лет, его брат был вдвое моложе. Теперь, когда Джошу 14 лет, сколько лет его брату? ")

  if answer == '10':
    print("Правильно! Вы завели лодку и отправляетесь в путь.")
    inventory['boat'] = True
    island_of_riddles()
  else:
    print("Неправильно. Попробуйте еще раз.")
    solve_riddle_for_boat()

def island_of_riddles():
  print("Этап 4: Вы прибыли на необитаемый остров.")
  print("Чтобы выбраться с острова, нужно решить три загадки.")

  if 'key' in inventory:
    print("Ключ, который вы нашли, может пригодиться для сундука на острове.")

  items = input("Найдите три предмета на букву 'К' (например, камень, кокос, корень): ")
  if all(item in items for item in ['камень', 'кокос', 'корень']):
    print("Вы нашли все предметы!")
    
    riddle_answer = input("Что имеет шею, но не имеет головы? ")
    
    if riddle_answer.lower() == 'бутылка':
      print("Правильно! Теперь найдите три вещи, которые могут быть красными и белыми: ")
      colors = input("Введите три вещи: ")
      
      if all(item in colors for item in ['яблоко', 'клубника', 'ягоды малины']):
        print("Вы прошли все испытания и можете продолжать путешествие!")
        north_journey()
      else:
        print("Неправильно. Попробуйте снова.")
        island_of_riddles()
    else:
      print("Неправильно. Попробуйте снова.")
      island_of_riddles()
  else:
    print("Не все предметы найдены. Попробуйте снова.")
    island_of_riddles()

def north_journey():
  print("Этап 5: Старик дает вам компас и карту.")
  print("Вы направляетесь на север.")

  choice = input("Вы проходите через (1) лес или (2) болото? ")

  if choice == '1':
    forest_challenge()
  elif choice == '2':
    swamp_challenge()
  else:
    print("Неверный выбор. Попробуйте снова.")
    north_journey()

def forest_challenge():
  print("Вы успешно прошли через лес и нашли ключ от сундука!")
  inventory['treasure_key'] = True
  return_home()

def swamp_challenge():
  print("Вы успешно прошли через болото, избегая нечисти!")
  return_home()

def return_home():
  print("Этап 7: Вы возвращаетесь домой и воссоединяетесь с близкими.")
  
  if 'treasure_key' in inventory:
    print("Вы открыли сундук с сокровищами, которые нашли в лесу!")
  
  next_adventure = input("Хотите начать новое приключение? (да/нет) ")
  if next_adventure.lower() == 'да':
    new_adventure()
  else:
    print("Спасибо за игру!")

def new_adventure():
  print("Продолжение следует...")

inventory = {}
start_game()
