
from bokin import secretary_program_start
from yandex import creat_folder

if __name__ == '__main__':
   token_ya = ''#API Яндекс диска
   name = 'default'#Имя папки
   secretary_program_start()
   print(creat_folder(token_ya, name))
