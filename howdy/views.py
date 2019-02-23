#  # howdy/views.py
# from django.shortcuts import render
# from django.views.generic import TemplateView

# # Create your views here.
# class HomePageView(TemplateView):
#     def get(self, request, **kwargs):
#         return render(request, 'index.html', context=None)


from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from howdy.models import Experience

# from .models import Choice, Question

# class IndexView(generic.ListView):
#     template_name = 'index.html'
#     # context_object_name = 'latest_question_list'



#     def get_queryset(self):
#         """Return the last five published questions."""
#         return 0


def index(request):
    # experience = Experience.objects.all()
    # experience = get_object_or_404(Experience, pk=4)
    experience = Experience.objects.all()
    return render(request, 'index.html', {'experience': experience})

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))

# def getData(request):
#         data = salary.objects.all()
#         name_list = []
#         for x in users:
#                 name_list.append(x.first_name + ' ' + x.last_name)
#         return name_list


# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'detail.html'

# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'results.html'

# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('howdy:results', args=(question.id,)))