from django.http import HttpResponse
from .models import  problems, submissions
from django.forms import formset_factory
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from .forms import submission_form
from django.contrib import messages
import docker, subprocess
from docker.models.containers import Container
import os 
import filecmp

client = docker.from_env()

def home(request):
    problems_list=problems.objects.all()
    context = {
        'problems_list':problems_list,
    }
    return render(request, 'ojApp/home.html', context)


def problem(request, problem_id):
    if request.method == 'POST':
        form=submission_form(request.POST, request.FILES)
        if form.is_valid():
            if request.user.is_authenticated:
                new_submission=submissions()
                new_submission.user_name = request.user.username
                new_submission.problem=problems.objects.get(pk=problem_id)
                new_submission.submitted_code=request.FILES["submitted_code"]
                code_file = r"oj_received\try_code.cpp"
                input_file = r"oj_test_cases\input_oj.txt"
                e_out_file = r"oj_expected_outputs\output_oj.txt"
                received_out = r"received_outputs"
                #os.system('dir')
                container:Container=client.containers.get("myojcompiler")
                if container.status != 'running':
                    container.start()

                os.system('docker cp '+code_file+' '+container.id + ':code_file.cpp')
                os.system('docker cp '+input_file+' '+container.id + ':input_file.txt')
                # probably error at line 43 and 44
                #os.system('docker exec myojcompiler g++ --version')

                os.system('docker exec myojcompiler g++ code_file.cpp')
                os.system('docker exec myojcompiler ./a.out > rec_out.txt')
                os.system('docker cp '+container.id +':rec_out.txt '+received_out)

                container.stop()

                # os.system('g++ '+code_file)
                # os.system('a.exe <'+input_file+' >'+received_out)
                if (filecmp.cmp(e_out_file, r"rec_out.txt", shallow=False)):
                    new_submission.verdict ='Accepted'
                else:
                    new_submission.verdict = 'Not Accepted'
                new_submission.save()
                return redirect('submission_page')
            else:
                messages.warning(request, f'Please login to make a subnmission')
                return redirect('home_page')

            # C:\Users\pratik shukla\Desktop\Oj\Online_judge\oj_test_cases\input_oj.txt
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
    recent_submissions = submissions.objects.order_by('-time_stamp')

    template = loader.get_template('ojApp/submission_page.html')
    context = {
        'recent_submissions': recent_submissions,
    }
    return HttpResponse(template.render(context, request))

# Create your views here.
