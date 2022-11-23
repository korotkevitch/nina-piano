from django.contrib import admin


from piano.models import Head
class HeadAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image_1_preview', 'text_1', 'image_2_preview', 'text_2')
    list_display_links = ('id', 'title')
admin.site.register(Head, HeadAdmin)


from piano.models import Contact
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone', 'address', 'email')
    list_display_links = ('id', 'phone')
admin.site.register(Contact, ContactAdmin)


from piano.models import Info
class InfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'icon_preview', 'bg')
    list_display_links = ('id', 'title')
admin.site.register(Info, InfoAdmin)


from piano.models import Task
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'icon_preview')
    list_display_links = ('id', 'title')
admin.site.register(Task, TaskAdmin)


from piano.models import Welcome
from piano.forms import WelcomeForm
class WelcomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text')
    form = WelcomeForm
    list_display_links = ('id', 'title')
admin.site.register(Welcome, WelcomeAdmin)


from piano.models import Trial
class TrialAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text')
    list_display_links = ('id', 'title')
admin.site.register(Trial, TrialAdmin)


from piano.models import TrialForm
class TrialFormAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text')
    list_display_links = ('id', 'title')
admin.site.register(TrialForm, TrialFormAdmin)


from piano.models import Price
class PriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'subtitle', 'section', 'intro', 'price', 'image_preview', 'description')
    list_display_links = ('id', 'subtitle')
admin.site.register(Price, PriceAdmin)


from piano.models import Stuff
from piano.forms import StuffForm
class StuffAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'section', 'intro', 'image_preview', 'position', 'description')
    form = StuffForm
    list_display_links = ('id', 'name')
admin.site.register(Stuff, StuffAdmin)


from piano.models import Testimonial
from piano.forms import TestimonialForm
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'section', 'intro', 'image_preview', 'testimonial')
    form = TestimonialForm
    list_display_links = ('id', 'name')
admin.site.register(Testimonial, TestimonialAdmin)


from piano.models import ContactForm
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('id', 'f_name', 'l_name', 'age', 'phone', 'message')
    list_display_links = ('id', 'l_name')
admin.site.register(ContactForm, ContactFormAdmin)


from piano.models import InterestingInfo
from piano.forms import InterestingInfoForm
class InterestingInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text')
    form = InterestingInfoForm
    list_display_links = ('id', 'title')
admin.site.register(InterestingInfo, InterestingInfoAdmin)


from piano.models import Gallery
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_preview')
    list_display_links = ('id', 'image_preview')
admin.site.register(Gallery, GalleryAdmin)