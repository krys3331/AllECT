from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseNotFound
from main.models import *
from main.custom_setting import *
from main.templatetags.main_tags import *

# Create your views here.


############################
def Index(request):
    path = 'main/main.html'
    urls = {
        'arch':URL_NAME_ARCHITECTURE_LIST,
        'proc':URL_NAME_PROCESSOR_LIST,
        'cat':URL_NAME_CATHEGORY_LIST
    }
    return render(request, path, {'menu':menu, 'urls':urls})

##########################
def About(request):
    
    about = '''
    Сайт показує деякі технології в світі IT (ЕОМ, процессори, архітектури....)
    Сайт зроблений за допомогою Framework Django
    Source code - https://github.com/krys3331/AllECT
    '''
    return render(request, 'main/about.html', {'menu':menu, 'about':about})

#############################################
def ShowECT(request, str, slug):
        ect = get_object_or_404(ECT, slug=slug)
        return render(request,'main/' +about_model + '.html', {'menu':menu, 'object':ect})

def ECTList(request, slug):
    cat = get_object_or_404(Cathegory, slug=slug)
    ect =  get_list_or_404(ECT, cathegory_id = cat.id)
    return render(request, 'main/' + list_model +'.html', {'menu':menu, 'list':ect, 'title':cat.name})

def ECTAdd(request):
    return HttpResponse("ADD")
##################################################

def PageNotFound(request, exception):
    # return render(request, 'main/notfound.html')
    return HttpResponseNotFound("PAGE NOT FOUND")


def AboutModel(request, slug):
    object = GetObject(slug)
    object = get_object_or_404(object, slug=slug)
    return render(request, 'main/'+about_model+'.html', {'menu':menu, 'object':object})

def GetObject(slug):
    lst = (Cathegory, Proccessor, ECT, Architecture)
    for object in lst:
        obj = object.objects.filter(slug=slug)
        if obj:
            return object

def ListModel(request):
    list, name = GetList(request.path_info)
    cont = {'menu':menu, 'list':list, 'title':name}
    if type(list[0]) is Cathegory:
        cont['cathegory'] = URL_NAME_ECT_LIST         
    return render(request, 'main/'+ list_model + '.html', cont)

def GetList(path):
    tpath = path[1:-2]
    if tpath == URL_PATH_ARCHITECTURE:
        return get_architectures(), 'Архітектури'
    elif tpath == URL_PATH_PROCESSOR:
        return get_processors(), 'Процессори'
    elif tpath == URL_PATH_CATHEGORY:
        return get_cathegorys(), 'Категорії'
           





