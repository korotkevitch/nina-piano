from django import forms
from django.forms import ModelForm, Textarea
from piano.models import Welcome, Stuff, Testimonial, InterestingInfo
from django.core.mail import send_mail as django_send_mail
from .models import ContactForm


class WelcomeForm(ModelForm):

    class Meta:
        model = Welcome
        fields = '__all__'
        widgets = {
            'text': Textarea(attrs={'cols': 80,
                                    'rows': 20})
        }


class StuffForm(ModelForm):

    class Meta:
        model = Stuff
        fields = '__all__'
        widgets = {
            'description': Textarea(attrs={'cols': 80,
                                    'rows': 20})
        }


class TestimonialForm(ModelForm):

    class Meta:
        model = Testimonial
        fields = '__all__'
        widgets = {
            'testimonial': Textarea(attrs={'cols': 80,
                                    'rows': 20})
        }


class UserForm(forms.ModelForm):
    # captcha = ReCaptchaField(
    #     public_key='6LdbmQkeAAAAADPuywAjtXN4u-Pd31SfkXBUAHxm',
    #     private_key='6LdbmQkeAAAAAN2ZnJ3-PPe3VkZzScSbyd3AVjKm',
    # )

    class Meta:
        model = ContactForm
        fields = '__all__'  # вместо перечисления всех полей: fields = ['name', 'phone', 'message']

    def send_mail(self):
        return django_send_mail('Запись на бесплатный урок',
                    str('Имя: ') + self.cleaned_data['f_name'] + '\n' + str('Фамилия: ') + self.cleaned_data['l_name'] +
                                '\n' + str('Возраст: ') + self.cleaned_data['age'] + '\n' + str('Телефон: ') +
                                self.cleaned_data['phone'] + '\n' + str('Сообщение: ') + self.cleaned_data['message'],
                    'no-reply@ninapiano.by',
                    ['ninapiano@iko-studio.com'])


class InterestingInfoForm(ModelForm):

    class Meta:
        model = InterestingInfo
        fields = '__all__'
        widgets = {
            'text': Textarea(attrs={'cols': 80,
                                    'rows': 20})
        }