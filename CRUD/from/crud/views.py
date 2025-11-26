from django.shortcuts import render, redirect, get_object_or_404
from .models import student
from .forms import studentform


def add_student(request):
    form = studentform()
    if request.method == 'POST':
        form = studentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('read')

    return render(request, 'create.html', {'form': form})


def read_student(request):
    students = student.objects.all()
    return render(request, 'read.html', {'students': students})


def update_student(request, pk):
    Student = get_object_or_404(student, pk=pk)
    form = studentform(instance=Student)

    if request.method == 'POST':
        form = studentform(request.POST, instance=Student)
        if form.is_valid():
            form.save()
            return redirect('read')

    return render(request, 'update.html', {'form': form})


def delete_student(request, pk):
    Student = get_object_or_404(student, pk=pk)
    Student.delete()
    return redirect('read')
