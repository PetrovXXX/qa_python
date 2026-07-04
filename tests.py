from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_set_book_genre_setting_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.books_genre['Оно'] == 'Ужасы'

    def test_get_book_genre_find_genre(name):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        gener = collector.get_book_genre('Оно')
        assert gener == 'Ужасы'

    def test_get_books_with_specific_genre_see_list(genre):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        book_genre = collector.get_books_with_specific_genre('Ужасы')
        assert book_genre == ['Оно']

    def test_get_books_genre_get_dictionary(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        expected_result = {
            'Оно':'Ужасы'
        }
        genre = collector.get_books_genre()
        assert genre == expected_result

    def test_get_books_for_children_suitable_children(self):
        collector = BooksCollector()
        collector.add_new_book('Душа')
        collector.set_book_genre('Душа', 'Мультфильмы')
        expected_result = [
            'Душа'
        ]
        books_for_children = collector.get_books_for_children()
        assert books_for_children == expected_result

    def test_add_book_in_favorites_added_favorites(name):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        collector.add_book_in_favorites("Властелин колец")
        assert "Властелин колец" in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_delete_books(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец 2')
        collector.add_book_in_favorites("Властелин колец 2")
        collector.delete_book_from_favorites("Властелин колец 2")
        assert "Властелин колец 2" not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_empty_list(self):
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_multiple(self):
        collector = BooksCollector()
        collector.books_genre['Властелин колец 1'] = 'Фантастика'
        collector.add_book_in_favorites("Властелин колец 1")
        collector.books_genre['Властелин колец 2'] = 'Фантастика'
        collector.add_book_in_favorites("Властелин колец 2")
        assert collector.get_list_of_favorites_books() == ["Властелин колец 1", "Властелин колец 2"]