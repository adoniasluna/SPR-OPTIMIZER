from django.template import loader
from django.http import HttpResponse
from facade import facade


def index(request):
    template = loader.get_template('spr_optimizer/index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def upload(request):
    template = loader.get_template('spr_optimizer/upload.html')
    file_list = []

    for count, x in enumerate(request.FILES.getlist("img")):
        print(count, x)
        facade.upload_files("/home/adonias/PycharmProjects/mysite/media/" + str(count), x)
        file_list.append(count)

    #the context has all the files names so it could be show at the index page
    context = {"files": file_list}

    return HttpResponse(template.render(context, request))


def optimize(request):
    template = loader.get_template('spr_optimizer/result.html')
    best_position = facade.optimize()

    context = {"results": best_position}
    print(best_position)
    return HttpResponse(template.render(context, request))


def setting(request):
    template = loader.get_template('spr_optimizer/setting.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def get_help(request):
    template = loader.get_template('spr_optimizer/get_help.html')
    context = {
    }
    return HttpResponse(template.render(context, request))
