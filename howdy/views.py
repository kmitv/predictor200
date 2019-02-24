#  # howdy/views.py
# from django.shortcuts import render
# from django.views.generic import TemplateView

# # Create your views here.
# class HomePageView(TemplateView):
#     def get(self, request, **kwargs):
#         return render(request, 'index.html', context=None)


from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic

from howdy.models import Experience

class IndexView(generic.ListView):
        template_name = 'index.html'
        context_object_name = 'experience_list'

        def get_queryset(self):
                """Return the last five published questions."""
                return Experience.objects.all()


def data_add(request):
        if request.method == 'POST':
            if request.POST.get('years') and request.POST.get('salary'):
                post=Experience()
                post.years= request.POST.get('years')
                post.salary= request.POST.get('salary')
                post.save()
                return redirect('/') 
        else:
                return redirect('/') 

def data_remove(request):
        if request.method == 'POST':
            if request.POST.get('index'):
                to_del = Experience.objects.get(id = request.POST.get('index'))
                to_del.delete()
                return redirect('/') 
        else:
                return redirect('/') 

