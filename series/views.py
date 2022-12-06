from audioop import reverse
from unittest import loader

from django.http import HttpResponseRedirect
from django.shortcuts import render
from . import models
from django.shortcuts import render,get_object_or_404
from django.views.generic.edit import CreateView
from . forms import AddForm
from .models import Series
from django.shortcuts import render, get_object_or_404
from . import models
from django.views import generic
from . import models, forms


def main_page(request):
   info = models.Series.objects.all()
   print(info)
   return render(request, "index.html", {"info": info})


def home(request):
   head = models.Home.objects.all()
   return render(request, 'index.html', {'head': head})


def show_details(request, id):
   seria = get_object_or_404(models.Series, id=id)
   return render(request, 'seria.html', {'seria': seria})


class Create(generic.CreateView):
   template_name = 'add.html'
   form_class = forms.AddForm
   queryset = models.Series.objects.all()
   success_url = '/main/'

   def form_valid(self, form):
      print(form.cleaned_data)
      return super(Create, self).form_valid(form=form)


class Update(generic.UpdateView):
   template_name = 'update.html'
   form_class = forms.AddForm
   success_url = '/main/'

   def get_object(self, **kwargs):
      note_id = self.kwargs.get('id')
      return get_object_or_404(models.Series, id=note_id)

   def form_valid(self, form):
      return super(Update, self).form_valid(form=form)



class Delete(generic.DeleteView):
   template_name = 'delete.html'
   success_url = '/main/'

   def get_object(self, **kwargs):
      _id = self.kwargs.get('id')
      return get_object_or_404(models.Series, id=_id)



# def update(request, id):
#   mymember = Series.objects.get(id=id)
#   template = loader.get_template('update.html')
#   context = {
#     'mymember': mymember,
#   }
#   return HttpResponse(template.render(context, request))