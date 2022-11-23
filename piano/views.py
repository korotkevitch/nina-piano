from django.shortcuts import render
from django.views.generic import View, ListView
from .models import Head, Contact, Info, Task, Welcome, Trial, Stuff, Testimonial, ContactForm, InterestingInfo, Gallery, \
    TrialForm, Price
from .forms import UserForm
from django.core.mail import BadHeaderError
from django.views.generic.edit import FormView
from django.core.mail import send_mail


class HomeView(ListView):
    model = Head
    template_name = 'index.html'
    context_object_name = 'head'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['contact'] = Contact.objects.all()
        context['info'] = Info.objects.all()
        context['task'] = Task.objects.all()
        context['welcome'] = Welcome.objects.all()
        context['trial'] = Trial.objects.all()
        context['trial_form'] = TrialForm.objects.all()
        context['price'] = Price.objects.all()
        context['stuff'] = Stuff.objects.all()
        context['testimonial'] = Testimonial.objects.all()
        context['interesno'] = InterestingInfo.objects.all()
        context['gallery'] = Gallery.objects.all()

        return context


class ContactFormView(FormView):
    model = ContactForm
    form_class = UserForm
    success_url = 'thanks'

    def form_valid(self, myform):
        myform.send_mail()
        myform.save()  # сохранение в БД
        return super().form_valid(myform)

