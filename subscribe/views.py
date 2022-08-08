from django.shortcuts import render
from .forms import SubscribeForm
from django.contrib import messages
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
# Create your views here.


def subscribe_form(request):

    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        messages.info(request, 'You have successfully subscribed to timetable.')
        return render(request, 'subscribe/subscribe_form.html', context={'form':form})
    form = SubscribeForm()
    return render(request, 'subscribe/subscribe_form.html', context={'form':form})


class DoneView(TemplateView):
        template_name =  'subscribe/done.html'


class SubscribeView(FormView):    # ФормВью сам валидирует данные
        template_name = 'subscribe/subscribe_form.html'
        form_class = SubscribeForm
        success_url = 'done'

        def form_valid(self, form):
            form.save()
            return super(SubscribeView, self).form_valid(form)
