import hashlib
from datetime import datetime
from django.template import loader
from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, JsonResponse, HttpResponse, HttpResponseRedirect
from facade import facade
from spr_optimizer.forms import PSOSettingForm


def index(request):
    template = loader.get_template('spr_optimizer/index.html')
    context = {}

    return HttpResponse(template.render(context, request))


def upload(request):
    file_list = []
    date = datetime.now()

    for count, x in enumerate(request.FILES.getlist("file_opt")):
        file_name = hashlib.sha224(str(date).encode('utf-8')).hexdigest() + str(count)
        facade.upload_files("media/" + str(file_name) + ".txt", x)
        file_list.append(file_name + '-' + str(x))

    template = loader.get_template('spr_optimizer/upload.html')

    # the context has all the files names so it could be show at the index page
    context = {"files": file_list}

    return HttpResponse(template.render(context, request))


def optimize(request):
    files = request.POST.getlist('file_uploads')

    # It separates the file name used in this application from the uploaded one
    files_system_name = [elem.split("-")[0] + '.txt' for elem in files]

    num_particles = request.session['particle_number']
    max_iterations = request.session['iteration_number']
    inertia_weight = request.session['inertia_weight']
    cognitive_constant = request.session['cognitive_constant']
    social_constant = request.session['social_constant']
    initial_position = request.session['initial_position']

    opt_result = facade.optimize(files_system_name, num_particles, max_iterations, inertia_weight,
                                    cognitive_constant, social_constant, initial_position)

    # Getting the name of the file
    files_uploaded_name = [elem.split("-")[1].split(".")[0] for elem in files]

    # Combining the error, best position and cell name to be put on the context
    result_contex = []
    for i in range(len(files_uploaded_name)):
        best_position, error = opt_result[i]
        context_elem = (files_uploaded_name[i], best_position, error)
        result_contex.append(context_elem)

    context = {"results": result_contex}

    template = loader.get_template('spr_optimizer/result.html')
    return HttpResponse(template.render(context, request))


def setting(request):
    template = loader.get_template('spr_optimizer/setting.html')

    # If this is a POST request then process the Form data
    print(request.method)
    if request.method == 'POST':
        form = PSOSettingForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)

            # Set up PSO parameter for the session
            for key in form.cleaned_data:
                request.session[key] = form.cleaned_data[key]

            return HttpResponseRedirect("/spr_optimizer/")

        # Reload the form with the previous value
        else:
            context = {'form': form}
            return HttpResponse(template.render(context, request))

    # If this is a GET (or any other method) load the form with default values
    else:
        form = PSOSettingForm()
        context = {
            'form': form,
        }

    return HttpResponse(template.render(context, request))


def get_help(request):
    template = loader.get_template('spr_optimizer/get_help.html')
    context = {
    }
    return HttpResponse(template.render(context, request))
