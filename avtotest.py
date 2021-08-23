from bokin import add_new_doc, get_doc_owner_name, get_doc_shelf, delete_doc
from yandex import creat_folder

class TestBookkeeping:

    def test_sbook1(self):
        assert add_new_doc('777','visa', 'Max M', '3') == '3'

    def test_book2(self):
        assert get_doc_owner_name('10006') == 'Аристарх Павлов'

    def test_book3(self):
        assert  get_doc_shelf('10006') == '2'

    def test_book4(self):
        assert delete_doc('10006') == ('10006', True)

    def test_book5(self):
        assert  get_doc_shelf('10006') == None

    def test_ya(self):
        assert creat_folder('API', 'default') == 'Создана папка на Яндекс.Диске: default' #Нужно передать API Яндекс диска.

    def test_ya1(self):
        assert creat_folder('API_error', 'default') == f'Указанный вами токен Яндекс.Диска неверен или у вас нет прав на загрузку фотографий.' #Нужно передать неверный API Яндекс диска.