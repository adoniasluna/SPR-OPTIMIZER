import hashlib
from datetime import datetime
from django.template import loader
from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, JsonResponse, HttpResponse
from facade import facade



def index(request):
    template = loader.get_template('spr_optimizer/index.html')
    context = {}

    return HttpResponse(template.render(context, request))


def upload(request):
    template = loader.get_template('spr_optimizer/upload.html')
    file_list = []
    date = datetime.now()

    for count, x in enumerate(request.FILES.getlist("file_opt")):
        file_name = hashlib.sha224(str(date).encode('utf-8')).hexdigest() + str(count)
        facade.upload_files("media/" + str(file_name) + ".txt", x)
        file_list.append(file_name +'-'+  str(x))

    #the context has all the files names so it could be show at the index page
    context = {"files": file_list}

    return HttpResponse(template.render(context, request))


def optimize(request):
    files = request.POST.getlist('file_uploads')

    # It separates the file name used in this application from the uploaded one
    files_system_name = [elem.split("-")[0] + '.txt' for elem in files]

    best_position = facade.optimize(files_system_name)

    template = loader.get_template('spr_optimizer/result.html')
    files = []
    for key, value in request.POST.items():
        if key == 'file_uploads':
            files.append(value.split("-")[0]+'.txt')
    best_position = facade.optimize(files)

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
