from django.http import HttpResponse
from .models import User, problems, submissions
from django.forms import formset_factory
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from .forms import submission_form


def home(request):
    problems_list=problems.objects.all()
    template = loader.get_template('ojApp/home.html')
    context = {
        'problems_list':problems_list,
    }
    return render(request, 'ojApp/home.html', context)


def problem(request, problem_id):
    if request.method == 'POST':
        form=submission_form(request.POST, request.FILES)
        if form.is_valid():
            new_submission=submissions()
            new_submission.problem=problems.objects.get(pk=problem_id)
            new_submission.submitted_code=request.FILES["submitted_code"]
            new_submission.save()

            return redirect('/submission')
    else:
        form=submission_form()

    problem_object = get_object_or_404(problems, pk=problem_id)
    context={
            'problem_title': problem_object.problem_title, 
            'problem_statement': problem_object.problem_statement,
            'form': form,
        }
    return render(request, 'ojApp/problem_detail.html', context)


def submission(request):
    return HttpResponse('not abl to solve')

# Create your views here.
