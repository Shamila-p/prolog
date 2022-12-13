import mimetypes
import os
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from member.models import Student
from assignment.models import Assignment, AssignmentMark, SubmittedAssignment, module
from course.models import Class, Semester, Subject

# Create your views here.


@login_required
def assignment(request, class_id, semester_id, subject_id):
    if request.method == 'GET':
        assignments = Assignment.objects.filter(
            teacher_id=request.user.id, subject_id=subject_id, class_belongs_id=class_id, semester_id=semester_id)
        context = {'assignments': assignments, 'subject_id': subject_id,
                   'class_id': class_id, 'semester_id': semester_id,'title': 'Assignments'}
        return render(request, 'assignment.html', context)

@login_required
def add_assignment(request, class_id, semester_id, subject_id):
    if request.method == 'GET':
        module_list = module.objects.all()
        context = {'types': Assignment.ASSIGNMENT_CHOICES,
                   'modules': module_list,'title': 'Add Assignment'}
        return render(request, 'add-assignment.html', context)
    if request.method == 'POST':
        topic = request.POST.get('topic')
        type = request.POST.get('type')
        modulename = request.POST.get('modulename')
        submission = request.POST.get('submission')
        upload = request.FILES.get('upload')
        # class_belongs=Class.objects.get(tutor_id=request.user.id)
        # subjects=Subject.objects.filter(assigned_to_id=request.user.id ,class_belongs_id=class_belongs.id)
        # for subject in subjects:
        #     print(subject)
        #     id=subject.id
        #     print(id)
        subject = subject_id
        Assignment.objects.create(topic=topic, submission_date=submission, type=type, questions=upload, module=modulename,
                                  teacher_id=request.user.id, subject_id=subject, class_belongs_id=class_id, semester_id=semester_id)
        return redirect('assignment', subject_id=subject_id, class_id=class_id, semester_id=semester_id)

@login_required
def edit_assignment(request, class_id, semester_id, subject_id, assignment_id):
    if request.method == 'GET':
        assignment = Assignment.objects.get(id=assignment_id)
        modules = module.objects.all()
        context = {'assignment': assignment,
                   'types': Assignment.ASSIGNMENT_CHOICES, 'modules': modules,'title': 'Edit Assignment'}
        return render(request, 'edit_assignment.html', context)
    if request.method == 'POST':
        topic = request.POST.get('topic')
        type = request.POST.get('type')
        modulename = request.POST.get('modulename')
        submission = request.POST.get('submission')
        upload = request.FILES.get('upload')
        assignment = Assignment.objects.get(id=assignment_id)
        assignment.topic = topic
        assignment.type = type
        assignment.module = modulename
        assignment.submission_date = submission
        if upload is not None:
            assignment.questions = upload
        assignment.save()
        return redirect('assignment', subject_id=subject_id, class_id=class_id, semester_id=semester_id)

@login_required
def remove_assignment(request, assignment_id):
    print(assignment_id)
    if request.method == 'POST':
        assignment = Assignment.objects.get(id=assignment_id)
        assignment.delete()
        return redirect('assignment', subject_id=assignment.subject_id, class_id=assignment.class_belongs_id)

@login_required
def list_module(request):
    if request.method == 'GET':
        # context={'types':Assignment.ASSIGNMENT_CHOICES}
        modules = module.objects.all()
        context = {'modules': modules,'title': 'List Module'}
        return render(request, 'list_module.html', context)

@login_required
def add_module(request):
    if request.method == 'GET':
        context={'title': 'Add Module'}
        return render(request, 'add_module.html',context)
    if request.method == 'POST':
        modulename = request.POST.get('modulename')
        module.objects.create(modulename=modulename)
        return redirect(list_module)

@login_required
def remove_module(request, module_id):
    modulename = module.objects.get(id=module_id)
    modulename.delete()
    return redirect('list_module')

@login_required
def view_assignments(request):
    if request.method == 'GET':
        student=Student.objects.get(user_id=request.user.id)
        current_semester=student.semester.order
        print(current_semester)
        semester_list=[]
        semesters = Semester.objects.all()
        for semester in semesters:
            if semester.order<=current_semester:
                semester_list.append(semester)
        # semesters = Semester.objects.all()
        # print(semesters)
        context = {'semester_list': semester_list,'title': 'Performance'}
        return render(request, 'view_assignment_semester.html', context)

def view_assignment_semester(request,semester_id):
 if request.method == 'GET':
        student = Student.objects.get(user_id=request.user.id)
        assignments = Assignment.objects.filter(
            class_belongs_id=student.batch_id, semester_id=semester_id)
        if len(assignments)==0:
            messages.info(request,"No data available")
            context={}
        else:
            context = {'assignments': assignments,'title': 'View Assignments'}
        return render(request, 'view_assignments.html', context)


   

@login_required
def download_file(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'test.txt'
    filepath = BASE_DIR + '/downloadapp/Files/' + filename
    path = open(filepath, 'r')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

@login_required
def upload_file(request, class_id, semester_id, subject_id, assignment_id):
    assignment = Assignment.objects.get(id=assignment_id)
    answer = request.FILES.get('answer')
    print(answer)
    SubmittedAssignment.objects.create(answer=answer, class_belongs_id=class_id, subject_id=subject_id,
                                       semester_id=semester_id, student_id=request.user.id, assignment_id=assignment.id)
    messages.info(request, "File uploaded Succesfully")
    return redirect('view_assignments')

@login_required
def view_mark(request, assignment_id):
    if request.method == 'GET':
        assignments = SubmittedAssignment.objects.filter(
            assignment_id=assignment_id).exists()
        if assignments:
            mark = True
        else:
            mark=False
        print(assignments)
        print(assignment_id)
        # assigned=AssignmentMark.objects.filter(student_id=request.user.id,assignment_id=assignment_id,class_belongs_id)
        # if AssignmentMark.objects.filter(assignment_id=assignment_id, student_id=request.user.id, semester_id=assignment.semester_id, subject_id=assignment.subject_id, class_belongs_id=assignment.class_belongs_id).exists():
        #     mark = True
        # else:
        #     mark = False
        if mark:
            print('djv')
            assignment = SubmittedAssignment.objects.get(
            assignment_id=assignment_id)
            submitted_assignments = SubmittedAssignment.objects.filter(
            assignment_id=assignment_id)
            marks = AssignmentMark.objects.filter(assignment_id=assignment_id, student_id=request.user.id,
                                                  semester_id=assignment.semester_id, subject_id=assignment.subject_id, class_belongs_id=assignment.class_belongs_id)
            print(marks)

        else:
            messages.info(request, "Mark not assigned yet!!")
            marks=""
        print(assignments)
        print(marks)
        context = {'submitted_assignments': submitted_assignments, 'marks': marks,'title': 'View Mark'}

        return render(request, 'view_assignment_mark.html', context)

@login_required
def submitted_assignment(request, class_id, semester_id, subject_id):
    if request.method == 'GET':
        assignments = SubmittedAssignment.objects.filter(
            subject_id=subject_id, class_belongs_id=class_id, semester_id=semester_id)
        print(class_id)
        print(semester_id)
        print(subject_id)
        # print(assignments)
        # is_submitted=[]
        # for assignment in assignments:
        #     submitted=AssignmentMark.objects.filter(assignment_id=assignment.assignment_id,class_belongs_id=class_id,subject_id=subject_id,semester_id=semester_id,student_id=assignment.student_id).exists()
        #     is_submitted.append(submitted)
        # print(is_submitted)
        student_marks = AssignmentMark.objects.filter(
            class_belongs_id=class_id, subject_id=subject_id, semester_id=semester_id)
        print(student_marks)
        context = {'assignments': assignments, 'student_marks': student_marks,'title': 'Submitted Assignments'}
        return render(request, 'submitted_assignment.html', context)

@login_required
def assign_mark(request, class_id, semester_id, subject_id, student_id, assignment_id):
    if request.method == 'GET':
        print(class_id)
        print(semester_id)
        print(subject_id)
        print(student_id)
        print(assignment_id)
        student = Student.objects.get(user_id=student_id)
        assignment = SubmittedAssignment.objects.get(id=assignment_id)
        # is_submitted=AssignmentMark.objects.filter(assignment_id=assignment_id,class_belongs_id=class_id,subject_id=subject_id,semester_id=semester_id,student_id=student_id).exists()
        # print(is_submitted)
        # if is_submitted is True:
        #     messages.info(request,"Mark already added. If you want to edit please go for edit option")

        # is_assigned=SubmittedAssignment.objects.filter(id=assignment_id,).exists()
        # submitted=0
        context = {'assignment': assignment, 'class_id': class_id, 'semester_id': semester_id, 'subject_id': subject_id,
                   'student_id': student_id, 'submitted_assignment_id': assignment_id, 'student': student,'title': 'Add Mark'}
        return render(request, 'assign_mark.html', context)
    if request.method == 'POST':
        print('hg')
        scored = request.POST.get('scored')
        print(scored)
        outof = request.POST.get('outof')
        print(outof)
        assignment = SubmittedAssignment.objects.get(id=assignment_id)
        print(assignment_id)
        print(class_id)
        print(subject_id)
        print(semester_id)
        print(student_id)
        is_submitted = AssignmentMark.objects.filter(
            assignment_id=assignment.assignment_id, class_belongs_id=class_id, subject_id=subject_id, semester_id=semester_id, student_id=student_id).exists()
        print(is_submitted)
        if is_submitted is True:
            messages.info(
                request, "Mark already added. If you want to edit please go for edit option")

        else:
            AssignmentMark.objects.create(scored=scored, outof=outof, assignment_id=assignment.assignment_id,
                                          class_belongs_id=class_id, subject_id=subject_id, semester_id=semester_id, student_id=student_id)
        return redirect('submitted_assignment', class_id, semester_id, subject_id)

@login_required
def edit_mark(request, class_id, semester_id, subject_id, student_id, assignment_id, mark_id):
    if request.method == 'GET':
        submitted = AssignmentMark.objects.get(id=mark_id)
        if submitted is None:
            messages.info(request, "Mark not assigned yet")

        assignment = Assignment.objects.get(id=submitted.id)
        print(submitted.assignment_id)
        context = {'submitted': submitted, 'assignment': assignment,'title': 'Edit Mark'}
        return render(request, 'edit_assignmentmark.html', context)
    if request.method == 'POST':
        scored = request.POST.get('scored')
        outof = request.POST.get('outof')
        submitted = AssignmentMark.objects.get(id=mark_id)
        submitted.scored = scored
        submitted.outof = outof
        submitted.save()
        return redirect('submitted_assignment', class_id, semester_id, subject_id)
