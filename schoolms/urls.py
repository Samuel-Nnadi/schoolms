from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views, hod_views, staff_views, students_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name='base'),

    # Login Path
    path('', views.LOGIN, name='login'),
    path('doLogin', views.doLogin, name='doLogin'),
    path('doLogout', views.doLogout, name='logout'),

    # Profile Update
    path('profile', views.PROFILE, name='profile'),
    path('profile/update', views.PROFILE_UPDATE, name='profile_update'),

    # HOD Panel Url
    path('hod/home', hod_views.HOME, name='hod_home'),
    path('hod/student/add', hod_views.ADD_STUDENT, name='add_student'),
    path('hod/student/view', hod_views.VIEW_STUDENT, name='view_student'),
    path('hod/student/edit/<str:id>', hod_views.EDIT_STUDENT, name='edit_student'),
    path('hod/student/update', hod_views.UPDATE_STUDENT, name='update_student'),
    path('hod/student/delete/<str:admin>', hod_views.DELETE_STUDENT, name='delete_student'),
    path('hod/staff/add', hod_views.ADD_STAFF, name='add_staff'),
    path('hod/staff/view', hod_views.VIEW_STAFF, name='view_staff'),
    path('hod/staff/edit/<str:id>', hod_views.EDIT_STAFF, name='edit_staff'),
    path('hod/staff/update', hod_views.UPDATE_STAFF, name='update_staff'),
    path('hod/staff/delete/<str:admin>', hod_views.DELETE_STAFF, name='delete_staff'),
    path('hod/course/add', hod_views.ADD_COURSE, name='add_course'),
    path('hod/course/view', hod_views.VIEW_COURSE, name='view_course'),
    path('hod/course/edit/<str:id>', hod_views.EDIT_COURSE, name='edit_course'),
    path('hod/course/update', hod_views.UPDATE_COURSE, name='update_course'),
    path('hod/course/delete/<str:id>', hod_views.DELETE_COURSE, name='delete_course'),
    path('hod/subject/add', hod_views.ADD_SUBJECT, name='add_subject'),
    path('hod/subject/view', hod_views.VIEW_SUBJECT, name='view_subject'),
    path('hod/subject/edit/<str:id>', hod_views.EDIT_SUBJECT, name='edit_subject'),
    path('hod/subject/update', hod_views.UPDATE_SUBJECT, name='update_subject'),
    path('hod/subject/delete/<str:id>', hod_views.DELETE_SUBJECT, name='delete_subject'),
    path('hod/session/add', hod_views.ADD_SESSION, name='add_session'),
    path('hod/session/view', hod_views.VIEW_SESSION, name='view_session'),
    path('hod/session/edit/<str:id>', hod_views.EDIT_SESSION, name='edit_session'),
    path('hod/session/update', hod_views.UPDATE_SESSION, name='update_session'),
    path('hod/session/delete/<str:id>', hod_views.DELETE_SESSION, name='delete_session'),
    path('hod/staff/send_notification', hod_views.STAFF_SEND_NOTE, name='staff_send_note'),
    path('hod/staff/save_notification', hod_views.SAVE_STAFF_NOTE, name='staff_save_note'),
    path('hod/staff/leave_view', hod_views.STAFF_LEAVE_VIEW, name='staff_leave_view'),
    path('hod/staff/approve_leave/<str:id>', hod_views.APPROVE_LEAVE, name='approve_leave'),
    path('hod/staff/disapprove_leave/<str:id>', hod_views.DISAPPROVE_LEAVE, name='disapprove_leave'),
    path('hod/staff/feedback', hod_views.STAFF_FEEDBACK, name='staff_feedback_reply'),
    path('hod/staff/feedback/save', hod_views.STAFF_FEEDBACK_SAVE, name='staff_feedback_reply_save'),
    path('hod/student/send_notification', hod_views.STUDENT_SEND_NOTIFICATION, name='student_send_notification'),
    path('hod/student/save_notification', hod_views.STUDENT_SAVE_NOTIFICATION, name='student_save_notification'),
    path('hod/student/feedback', hod_views.STUDENT_FEEDBACK, name='student_feedback_reply'),
    path('hod/student/feedback/save', hod_views.STUDENT_FEEDBACK_SAVE, name='student_feedback_reply_save'),
    path('hod/student/leave_view', hod_views.STUDENT_LEAVE_VIEW, name='student_leave_view'),
    path('hod/student/approve_leave/<str:id>', hod_views.STUD_APPROVE_LEAVE, name='stud_approve_leave'),
    path('hod/student/disapprove_leave/<str:id>', hod_views.STUD_DISAPPROVE_LEAVE, name='stud_disapprove_leave'),

    # Staff Panel Url
    path('staff/home', staff_views.HOME, name='staff_home'),
    path('staff/notifications', staff_views.NOTIFICATIONS, name='notifications'),
    path('staff/mark_as_done/<str:status>', staff_views.STAFF_MARK_AS_DONE, name='staff_mark_as_done'),
    path('staff/apply_leave', staff_views.STAFF_LEAVE_APPLY, name='staff_leave_apply'),
    path('staff/apply_leave_save', staff_views.STAFF_LEAVE_SAVE, name='staff_leave_save'),
    path('staff/feedback', staff_views.STAFF_FEEDBACK, name='staff_feedback'),
    path('staff/feedback/save', staff_views.STAFF_FEEDBACK_SAVE, name='staff_feedback_save'),
    path('staff/take_attendance', staff_views.STAFF_TAKE_ATTENDANCE, name='staff_take_attendance'),
    path('staff/save_attendance', staff_views.STAFF_SAVE_ATTENDANCE, name='staff_save_attendance'),
    path('staff/view_attendance', staff_views.VIEW_ATTENDANCE, name='view_attendance'),

    # Student Panel Url
    path('student/home', students_views.HOME, name='student_home'),
    path('student/notifications', students_views.NOTIFICATIONS, name='notifications'),
    path('student/mark_as_done/<str:status>', students_views.STUDENT_MARK_AS_DONE, name='student_mark_as_done'),
    path('student/feedback', students_views.STUDENT_FEEDBACK, name='student_feedback'),
    path('student/feedback/save', students_views.STUDENT_FEEDBACK_SAVE, name='student_feedback_save'),
    path('student/apply_leave', students_views.STUDENT_LEAVE_APPLY, name='student_leave_apply'),
    path('student/apply_leave_save', students_views.STUDENT_LEAVE_SAVE, name='student_leave_save'),
    path('student/view_attendance', students_views.VIEW_ATTENDANCE, name='view_attendance'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)