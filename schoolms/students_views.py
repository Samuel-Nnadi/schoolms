from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core.models import Student_Notification, Student, Student_Feedback, Student_Leave, Subject
from django.contrib import messages

@login_required(login_url='/')
def HOME(request):
    return render(request, 'student/home.html')

@login_required(login_url='/')
def NOTIFICATIONS(request):
    student = Student.objects.filter(admin = request.user.id)
    for i in student:
        student_id = i.id
        notification = Student_Notification.objects.filter(student_id = student_id)

        context = {
            'notification':notification,
        }
        return render(request, 'student/notification.html', context)
    
@login_required(login_url='/')
def STUDENT_MARK_AS_DONE(request, status):
    notification = Student_Notification.objects.get(id = status)
    notification.status = 1
    notification.save()
    messages.success(request, 'Notification Has Been Read!')
    return redirect('notifications')

@login_required(login_url='/')
def STUDENT_FEEDBACK(request):
    student_id = Student.objects.get(admin=request.user.id)

    feedback_history = Student_Feedback.objects.filter(student_id=student_id)

    context = {
        'feedback_history':feedback_history,
    }
    return render(request, 'student/feedback.html', context)

@login_required(login_url='/')
def STUDENT_FEEDBACK_SAVE(request):
    if request.method == "POST":
        feedback = request.POST.get('feedback')
        
        student = Student.objects.get(admin=request.user.id)
        feedback = Student_Feedback(
            student_id = student,
            feedback = feedback,
            feedback_reply = "",
        )
        feedback.save()
        messages.success(request, 'Feedback Was Successfully Sent!')
        return redirect('student_feedback')
    
@login_required(login_url='/')
def STUDENT_LEAVE_APPLY(request):
    student = Student.objects.filter(admin=request.user.id)
    for i in student:
        student_id = i.id

        student_leave_history = Student_Leave.objects.filter(student_id=student_id)

        context = {
            'student_leave_history':student_leave_history,
        }
        return render(request, 'student/apply_leave.html', context)
    
@login_required(login_url='/')
def STUDENT_LEAVE_SAVE(request):
    if request.method == "POST":
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('leave_message')

        student = Student.objects.get(admin=request.user.id)

        leave = Student_Leave(
            student_id = student,
            data = leave_date,
            message = leave_message,
        )
        leave.save()
        messages.success(request, 'Leave Successfully Sent!')
        return redirect('student_leave_apply')
    
@login_required(login_url='/')
def VIEW_ATTENDANCE(request):
    student = Student.objects.get(admin = request.user.id)
    subjects = Subject.objects.filter(course = student.course_id)
    action = request.GET.get('action')

    get_subject = None
    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get('subject_id')
            get_subject = Subject.objects.get(id = subject_id)

    context = {
        'subjects':subjects,
        'action':action,
        'get_subject':get_subject,
    }
    return render(request, 'student/view_attendance.html', context)