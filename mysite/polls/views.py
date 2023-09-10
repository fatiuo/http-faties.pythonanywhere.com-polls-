from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from polls.models import Choice, Question
from django.template import loader
from django.urls import reverse 

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        try:
          choice_id=request.POST['choice']
          selected_choice = question.choice_set.get(pk=choice_id)
        except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
             return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
        else:
           selected_choice.votes += 1
           selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    #return HttpResponse(template.render(context, request))
    return render(request , 'polls/index.html' , context)
def ear(request):
    return render(request,'polls/ear.html')
def khodemeni(request):
    return render(request,'polls/khodemeni.html')

def quaresh(request):
    return render(request,'polls/quaresh.html')
def tanafos(request):
    return render(request,'polls/tanafos.html')
def galu(request):
    return render(request,'polls/galu.html')
def falaj(request):
    return render(request,'polls/falaj.html')
