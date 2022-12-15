# 4 - Дан список URL различных сайтов. Нужно составить список доменных имен сайтов.


url_list = ('https://lk.rpn.gov.ru/login',
'https://kod-fkko.ru/poisk/',
'https://e-ecolog.ru/groro/',
'https://ecoproverka.ru/category/othod/',
'https://eco-profi.info/index.php/primeri-proektov/primeri-proektov.html')

domen_list = list(map(lambda i: i[:i.find('/')], [i for i in map(lambda i: i.replace('https://',''), url_list)]))
print(*domen_list,sep = "\n")
