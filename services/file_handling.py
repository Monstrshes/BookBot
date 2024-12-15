import os
import sys

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, page_size: int):
    sl = ['.', ',', '!', '?', ';', ':']
    if start + page_size - 1 > len(text) - 1:
        page_size = len(text) - start
    if start + page_size - 1 <= len(text) - 3 and text[start + page_size - 1] in sl and text[start + page_size] in sl:
        if text[start + page_size + 1] in sl:
            page_size -= 1
        else:
            page_size -= 2
    if text[start+page_size - 1] not in sl:
        while text[start+page_size - 1] not in sl:
            page_size -= 1
    return text[start:start+page_size], page_size


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(path, 'r', encoding='utf-8') as file:
        text = file.read()
    i = 1
    start = 0
    last = PAGE_SIZE
    while True:
        a, b = _get_part_text(text, start, PAGE_SIZE)
        book[i] = a.lstrip()
        if last >= len(text) - 1:
            break
        last += b
        start += b + 1
        i += 1

# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))