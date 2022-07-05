from django.http import HttpResponse
from .models import User, problems, submission
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
    # if request.method == 'POST':
    #     form=submission_form(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save(commit=False)
    #         new_submission=submission(problem_id=problem_id)
    #         form.submission_id=new_submission.id
    #         form.problem_id=problem_id
    #         return redirect('submission')
    # else:
    #     form=submission_form()

    problem_object = get_object_or_404(problems, pk=problem_id)
    context={
            'problem_title': problem_object.problem_title, 
            'problem_statement': problem_object.problem_statement,
            'form': form,
            }
    return render(request, 'ojApp/problem_detail.html', context)


def submission(request):
    return HttpResponse("this is submission page")

# Create your views here.
