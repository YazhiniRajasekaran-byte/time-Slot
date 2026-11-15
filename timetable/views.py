from django.shortcuts import render, redirect, get_object_or_404
from .models import TimeSlot

def timetable_view(request):
    slots = TimeSlot.objects.all()
    return render(request, 'timetable/timetable.html', {'slots': slots})

def add_slot(request):
    if request.method == 'POST':
        TimeSlot.objects.create(
            day=request.POST.get('day'),
            start_time=request.POST.get('start_time'),
            end_time=request.POST.get('end_time'),
            subject_name=request.POST.get('subject_name'),
            faculty_name=request.POST.get('faculty_name'),
            classroom=request.POST.get('classroom')
        )
        return redirect('timetable')
    return render(request, 'timetable/timetable_form.html')

def update_slot(request, pk):
    slot = get_object_or_404(TimeSlot, pk=pk)
    if request.method == 'POST':
        slot.day = request.POST.get('day')
        slot.start_time = request.POST.get('start_time')
        slot.end_time = request.POST.get('end_time')
        slot.subject_name = request.POST.get('subject_name')
        slot.faculty_name = request.POST.get('faculty_name')
        slot.classroom = request.POST.get('classroom')
        slot.save()
        return redirect('timetable')
    return render(request, 'timetable/timetable_form.html', {'slot': slot})

def delete_slot(request, pk):
    slot = get_object_or_404(TimeSlot, pk=pk)
    slot.delete()
    return redirect('timetable')