from django.shortcuts import get_object_or_404, render
from django.http import Http404

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls.base import reverse

from django.views.generic import ListView, DetailView

from . models import Choice, Question

# Create your views here.

class IndexView(ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        '''Return last 5 published questions'''
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisply the question voting form
        context = {
            'question': question,
            'error_message': "You didn't select a choice",
        }
        return render(request, 'polls/detail.html', {'context': context})
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))


'''
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[0:]
    # output = ', '.join([q.question_text for q in latest_question_list])
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'questioin': question})


'''