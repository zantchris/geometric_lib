# Тестирование

## План тестирования

**Цель: проверить корректность выполнения расчётов, а также поведения программы;

**Стратегия тестирования: тестирование функциональности с помощью unittest;

# Критерии приемки и ожидаемые результаты:

Назание файла и функции:|Входные данные:|Ожидаемый вывод:|Фактический результат:|Результат тестов:|Дата:
---|---|---|---|---|---
circle.perimetr()|4|25.13|25.13|OK|13.11.2024
circle.perimetr()|0|0|0|OK|13.11.2024
circle.perimetr()|-4|25.13|-25.13|FAILED|13.11.2024
circle.area()|4|50.26|50.26|OK|13.11.2024
circle.area()|0|0|0|OK|13.11.2024
circle.area()|-4|50.26|50.26|OK|13.11.2024
square.perimetr()|4|16|16|OK|13.11.2024
square.perimetr()|0|0|0|OK|13.11.2024
square.perimetr()|-4|16|-16|FAILED|13.11.2024
square.area()|4|16|16|OK|13.11.2024
square.area()|0|0|0|OK|13.11.2024
square.area()|-4|16|16|OK|13.11.2024
rectangle.perimetr()|4 2|12|12|OK|13.11.2024
rectangle.perimetr()|0 2|0|4|FAILED|13.11.2024
rectangle.perimetr()|-4 2|12|-4|FAILED|13.11.2024
rectangle.area()|4 2|8|8|OK|13.11.2024
rectangle.area()|0 2|0|0|OK|13.11.2024
rectangle.area()|-4 2|8|-8|FAILED|13.11.2024
triangle.perimetr()|4 2 2|8|8|OK
triangle.perimetr()|0 2 2|0|4|FAILED|13.11.2024
triangle.perimetr()|-4 2 2|8|0|FAILED
triangle.area()|4 2|4|4|OK
triangle.area()|0 2|0|0|OK
triangle.area()|-4 2|4|-4|FAILED
