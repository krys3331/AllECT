from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseNotFound
from main.forms import AddArchitectureForm, AddCathegoryForm, AddECTForm, AddProcessorForm
from main.models import *
from main.custom_setting import *
from main.templatetags.main_tags import *

# Create your views here.


############################
def Index(request):
    path = 'main/main.html'
    urls = {
        'arch':URL_ARCHITECTURE,
        'proc':URL_PROCESSOR,
        'cat':URL_CATHEGORY
    }
    return render(request, path,  Context({'urls':urls}))

##########################
def About(request):
    
    about = '''
    Сайт показує деякі технології в світі IT (ЕОМ, процессори, архітектури....)
    Сайт зроблений за допомогою Framework Django
    Source code - https://github.com/krys3331/AllECT
    '''
    return render(request, 'main/about.html',  Context({'about':about}))

#############################################
def ShowECT(request, str, slug):
        ect = get_object_or_404(ECT, slug=slug)
        return render(request,'main/' +about_model + '.html', Context({'object':ect}))

def ECTList(request, slug):
    cat = get_object_or_404(Cathegory, slug=slug)
    ect =  get_list_or_404(ECT, cathegory_id = cat.id)
    return render(request, 'main/' + list_model +'.html', Context({'list':ect, 'title':cat.name}) )

######################################################################################################

def AddModel(request, slug):
    form = None 
    model = None 
    if slug == URL_ARCHITECTURE:
        form = AddArchitectureForm
        model = Architecture
    elif slug == URL_CATHEGORY:
        form = AddCathegoryForm
        model = Cathegory
    elif slug == URL_ECT:
        form = AddECTForm
        model = ECT
    elif slug == URL_PROCESSOR:
        form = AddProcessorForm
        model = Proccessor
    form = form(request.POST) if request.method == 'POST' else form()
    
    if form.is_valid():
        try:
            model.objects.create(**form.cleaned_data)
            return redirect(slug)
        except:
            form.add_error(None, "Помилка при додатку")
    
    return render(request, 'main/add_model.html', Context({'form':form, 'add_name': URL_ADD, 'slug':slug}))

def AddChoose(request):
    return render(request, 'main/add_choose.html', Context({'add_menu':add_menu, 'add_name':URL_ADD}))
##################################################

def PageNotFound(request, exception):
    # return render(request, 'main/notfound.html')
    return HttpResponseNotFound("PAGE NOT FOUND")


def AboutModel(request, slug):
    object = GetObject(slug)
    object = get_object_or_404(object, slug=slug)
    return render(request, 'main/'+about_model+'.html', Context({'object':object}))

def GetObject(slug):
    lst = (Cathegory, Proccessor, ECT, Architecture)
    for object in lst:
        obj = object.objects.filter(slug=slug)
        if obj:
            return object

def ListModel(request):
    list, name = GetList(request.path_info)
    cont = Context({'list':list, 'title':name})
    if type(list[0]) is Cathegory:
        cont['cathegory'] = URL_ECT         
    return render(request, 'main/'+ list_model + '.html', cont)

def GetList(path):
    tpath = path[1:-2]
    if tpath == URL_ARCHITECTURE:
        return get_architectures(), 'Архітектури'
    elif tpath == URL_PROCESSOR:
        return get_processors(), 'Процессори'
    elif tpath == URL_CATHEGORY:
        return get_cathegorys(), 'Категорії'
           

def Context(context : dict):
    main_context = {'menu':up_menu, 'left_menu':ect_menu, 'add_menu':add_menu,  'add_menu_name':URL_ADD}
    if context is not None:
        for obj in context:
            main_context[obj] = context[obj]
    return main_context




