from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.views.generic import ListView

from .models import University
from .forms import UniversityForm

class IndexTab(ListView):
    paginate_by = 5
    model = University
    template_name = 'main/index_tab.html'
    context_object_name = 'universities'
    extra_context = {'numbers': 'is ' + str(len(University.objects.all()))}
    allow_empty = False

def index(request):
    # universities = University.objects.all()
    # universities = University.objects.filter(year=1993)
    # universities = University.objects.filter(id__gt=1)
    # universities = University.objects.filter(id__gt=20)
    universities = University.objects.order_by('id')
    return render(request, 'main/index.html', {'title': 'Головна сторінка', 'universities': universities})

def index_tab(request):
    universities = University.objects.order_by('-id')
    return render(request, 'main/index_tab.html', {'title': 'Університети', 'universities': universities})

def university_view(request, id=1):
    try:
        university = University.objects.get(id=id)
    except University.DoesNotExist:
        raise Http404
    return render(request, 'main/university_view.html', {'title': 'Університети', 'university': university})

def about(request):
    return render(request, 'main/about.html')

def index_start(request):
    return render(request, 'main/start.html')

def create(request):
    if request.method == 'POST':
        form = UniversityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = UniversityForm(initial={'ownership': 'Державна'})
    context = {
        'form': form
    }
    return render(request, 'main/create.html', context)

def university_edit(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = UniversityForm()
        else:
            university = University.objects.get(id=id)
            form = UniversityForm(instance=university)
        return render(request, 'main/university_edit.html', {'form': form})
    else:
        if id == 0:
            form = UniversityForm(request.POST)
        else:
            university = University.objects.get(id=id)
            form = UniversityForm(request.POST, instance=university)
        if form.is_valid():
            form.save()
            return redirect('main')

def university_delete(request, id=0):
    try:
        university = University.objects.get(id=id)
        university.delete()
    except University.DoesNotExist:
        raise Http404
    universities = University.objects.order_by('-id')
    return render(request, 'main/index_tab.html', {'title': 'Університети', 'universities': universities})
