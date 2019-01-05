from django.shortcuts import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello,world.You are at the Polls index")


def detail():
    return HttpResponse('You are looking at question %s.' %question_id)


def results(request,question_id):
    response='You are looking at the results of question %s.'
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse('you are voting on question %s.' % question_id)
