from course.models import Class

def is_tutor(request):
    is_tutor=Class.objects.filter(tutor_id=request.user.id).exists()
    return {'is_tutor':is_tutor} 
