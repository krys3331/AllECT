about_model = 'about_model'
list_model = 'list_model'

URL_PROCESSOR = 'processor'
URL_ECT = 'ect'
URL_ARCHITECTURE = 'architecture'
URL_CATHEGORY = 'cathegory'
URL_ABOUT = 'about'
URL_ADD = 'add'


up_menu = (
    {'title':'Про сайт', 'url_page':URL_ABOUT},
    {'title':'Додати', 'url_page':URL_ADD}
)

ect_menu = (
    {'title':'Архітектури', 'url_page':URL_ARCHITECTURE},
    {'title':'Процесори', 'url_page':URL_PROCESSOR},
    {'title':'Категорії', 'url_page':URL_CATHEGORY}
)


add_menu = (                #size must be 4
    {'title':'Архітектури', 'img':'main/images/arch.png','slug':URL_ARCHITECTURE},
    {'title':'Процесори', 'img':'main/images/Proc.png', 'slug':URL_PROCESSOR},
    {'title':'Категорії', 'img':'main/images/other.png', 'slug':URL_CATHEGORY},
    {'title':'Пристрої', 'img':'main/images/other.png', 'slug':URL_ECT}
)