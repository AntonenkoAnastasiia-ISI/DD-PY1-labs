# TODO Найдите количество книг, которое можно разместить на дискете
floppy_disc_capacity_Mb = 1.44*(1024**2)
amount_of_pages = 100
amount_of_str = 50
amount_of_symbols = 25
weidgh_of_one_symbol = 4
amount_of_kb_for_1_book = (amount_of_pages*amount_of_str*amount_of_symbols*weidgh_of_one_symbol)
amount_of_books = round(floppy_disc_capacity_Mb/amount_of_kb_for_1_book)
print("Количество книг, помещающихся на дискету:", amount_of_books)
