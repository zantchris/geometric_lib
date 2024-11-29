# Тестирование

## План тестирования

- Цель: проверить корректность выполнения расчётов, а также поведения программы;

- Стратегия тестирования: тестирование функциональности с помощью unittest;

# Критерии приемки и ожидаемые результаты:

Назание файла и функции:|Входные данные:|Ожидаемый вывод:|Фактический результат:|Результат тестов:
---|---|---|---|---
circle.perimetr()|4|25.13|25.13|OK
circle.perimetr()|0|0|0|OK
circle.perimetr()|-4|25.13|-25.13|FAILED
circle.area()|4|50.26|50.26|OK
circle.area()|0|0|0|OK
circle.area()|-4|50.26|50.26|OK
square.perimetr()|4|16|16|OK
square.perimetr()|0|0|0|OK
square.perimetr()|-4|16|-16|FAILED
square.area()|4|16|16|OK
square.area()|0|0|0|OK
square.area()|-4|16|16|OK
rectangle.perimetr()|4 2|12|12|OK
rectangle.perimetr()|0 2|0|4|FAILED
rectangle.perimetr()|-4 2|12|12|OK
rectangle.area()|4 2|8|8|OK
rectangle.area()|0 2|0|0|OK
rectangle.area()|-4 2|8|-8|FAILED
triangle.perimetr()|4 2 2|8|8|OK
triangle.perimetr()|0 2 2|0|-4|FAILED
triangle.perimetr()|-4 2 2|8|8|OK
triangle.area()|4 2|4|4|OK
triangle.area()|0 2|0|0|OK
- triangle.area()|-4 2|4|-4|FAILED
