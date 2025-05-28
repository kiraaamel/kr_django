from django.shortcuts import render
from .models import kmexam

def kmexam_list(request):
    exams = kmexam.objects.filter(is_public=True)
    context = {
        'exams': exams,
        'fio': 'Макарова Кира Игоревна',
        'group': '241-671',
    }
    return render(request, 'kmexam_list.html', context)
