from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from django.http import HttpResponse

from .models import WorkExp
from .forms import WorkExpForm

# Create your views here.

def cv_view(request):
    work_exps = WorkExp.objects.all().order_by('startTime')
    return render(request, "cv/cv_view.html", {'work_exps':work_exps})

def work_exp_detail(request):
    return HttpResponse("v02")

def work_exp_new(request):
    if request.method == "POST":
        form = WorkExpForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/cv')
        else:
            return redirect('/')
    else:
        form = WorkExpForm()
    return render(request, 'cv/work_exp_edit.html', {'form':form})

def work_exp_edit(request, pk):
    post = get_object_or_404(WorkExp, pk=pk)
    if request.method == 'POST':
        form = WorkExpForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/cv')
    else:
        form = WorkExpForm(instance = post)
    return render(request, 'cv/work_exp_edit.html', {'form':form})