import re

Karl_May = [
    "Winnetou I (1893)",
    "Winnetou II (1893)",
    "Winnetou III (1893)",
    "Orangen und Datteln (1893)",
    "Am Stillen Ocean (1894)",
    "Am Rio de la Plata (1894)",
    "In den Cordilleren (1894)",
    "Old Surehand I (1894)",
    "Old Surehand II (1895)",
]
sorted_books = []
pattern = re.compile(
    r'([\w ]+) \((\d{4})\)+')  # we add a paranthesis around the \d{4} so wecan reverse without paranthesis
for book in Karl_May:
    res = pattern.sub('\g<2>- \g<1>', book)
    sorted_books.append(res)
sorted_books.sort()
print(sorted_books)
