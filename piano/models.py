from django.db import models
from django.utils.safestring import mark_safe
from datetime import datetime
from django.utils.safestring import mark_safe
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.phonenumber import PhoneNumber


class Head(models.Model):
    title = models.CharField('Title страницы', max_length=120, blank=True)
    image_1 = models.FileField('Первый слайд 2000*1333', blank=True)
    text_1 = models.CharField('Текст на первом слайде', max_length=120, blank=True)
    image_2 = models.FileField('Второй слайд 2000*1333', blank=True)
    text_2 = models.CharField('Текст на втором слайде', max_length=120, blank=True)

    def image_1_preview(self):
        if self.image_1:
            return mark_safe('<img src="%s" style="width:100px; height:60px;" />' % self.image_1.url)
        else:
            return 'No Image Found'

    image_1_preview.short_description = 'Первый слайд'

    def image_2_preview(self):
        if self.image_2:
            return mark_safe('<img src="%s" style="width:100px; height:60px;" />' % self.image_2.url)
        else:
            return 'No Image Found'

    image_2_preview.short_description = 'Второй слайд'

    class Meta:
        verbose_name = '          Верхняя часть с фото'
        verbose_name_plural ='          Верхняя часть с фото'

    def __str__(self):
        return self.title


class Contact(models.Model):
    phone = models.CharField('Телефон', max_length=50, blank=True)
    address = models.CharField('Адрес', max_length=100, blank=True)
    email = models.EmailField('Email', max_length=50, blank=True)

    def phone_link(self):
        return PhoneNumber.from_string(phone_number=self.phone, region='RU').as_e164

    phone_link.short_description = 'Телефон для ссылки'

    class Meta:
        verbose_name = '         Контактные данные'
        verbose_name_plural = '         Контактные данные'

    def __str__(self):
        return "Телефоны"


class Info(models.Model):
    icon = models.FileField('Иконка', blank=True, default='')
    bg = models.CharField('Цвет блока', max_length=50, blank=True, default='')
    title = models.CharField('Заголовок', max_length=120, blank=True)
    text = models.CharField('Текст', max_length=150, blank=True)

    def icon_preview(self):
        if self.icon:
            return mark_safe('<img src="%s" style="width:60px; height:60px;" />' % self.icon.url)
        else:
            return 'Нет изображения'

    icon_preview.short_description = 'Картинка'

    class Meta:
        verbose_name = '        Инфо'
        verbose_name_plural = '        Инфо'

    def __str__(self):
        return self.title


class Task(models.Model):
    icon = models.FileField('Иконка', blank=True, default='')
    title = models.CharField('Заголовок', max_length=120, blank=True)
    text = models.CharField('Текст', max_length=150, blank=True)

    def icon_preview(self):
        if self.icon:
            return mark_safe('<img src="%s" style="width:60px; height:60px;" />' % self.icon.url)
        else:
            return 'Нет изображения'

    icon_preview.short_description = 'Картинка'

    class Meta:
        verbose_name = '       Задача обучения'
        verbose_name_plural = '       Задачи обучения'

    def __str__(self):
        return self.title


class Welcome(models.Model):
    title = models.CharField('Заголовок', max_length=120, blank=True)
    text = models.CharField('Текст', max_length=1000, blank=True)

    class Meta:
        verbose_name = '      Добро пожаловать'
        verbose_name_plural = '      Добро пожаловать'

    def __str__(self):
        return self.title


class Trial(models.Model):
    title = models.CharField('Заголовок', max_length=120, blank=True)
    text = models.CharField('Текст', max_length=1000, blank=True)

    class Meta:
        verbose_name = '     Пробный урок'
        verbose_name_plural = '     Пробный урок'

    def __str__(self):
        return self.title


class Stuff(models.Model):
    section = models.CharField('Название раздела', max_length=50, blank=True)
    intro = models.CharField('Описание раздела', max_length=1000, blank=True)
    image = models.FileField('Фото', blank=True, default='')
    name = models.CharField('Имя, фамилия', max_length=50, blank=True)
    position = models.CharField('Должность', max_length=50, blank=True)
    description = models.CharField('О преподавателе', max_length=500, blank=True)

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:100px; height:80px;" />' % self.image.url)
        else:
            return 'Нет фото'

    image_preview.short_description = 'Фото'

    class Meta:
        verbose_name = '    Преподаватель'
        verbose_name_plural = '    Преподаватели'

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    section = models.CharField('Название раздела', max_length=50, blank=True)
    intro = models.CharField('Описание раздела', max_length=1000, blank=True)
    image = models.FileField('Фото', blank=True, default='')
    name = models.CharField('Имя, фамилия', max_length=50, blank=True)
    testimonial = models.CharField('Отзыв', max_length=1500, blank=True)

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:80px; height:100px;" />' % self.image.url)
        else:
            return 'Нет фото'

    image_preview.short_description = 'Фото'

    class Meta:
        verbose_name = '   Отзыв'
        verbose_name_plural = '   Отзывы'

    def __str__(self):
        return self.name


class TrialForm(models.Model):
    title = models.CharField('Заголовок', max_length=120, blank=True)
    text = models.CharField('Текст', max_length=1000, blank=True)

    class Meta:
        verbose_name = '     Пробный урок (форма записи)'
        verbose_name_plural = '     Пробный урок (форма записи)'

    def __str__(self):
        return self.title


class Price(models.Model):
    section = models.CharField('Название раздела', max_length=50, blank=True)
    intro = models.CharField('Описание раздела', max_length=1000, blank=True)
    subtitle = models.CharField('Название цены', max_length=30, blank=True)
    price = models.CharField('Цена', max_length=10, blank=True)
    image = models.FileField('Фото', blank=True, default='')
    description = models.CharField('Описание', max_length=300, blank=True)

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:80px; height:50px;" />' % self.image.url)
        else:
            return 'Нет фото'

    image_preview.short_description = 'Фото'

    class Meta:
        verbose_name = '     Цена (ровно 4 цены)'
        verbose_name_plural = '     Цены (ровно 4 цены)'

    def __str__(self):
        return self.subtitle


class ContactForm(models.Model):
    f_name = models.CharField('Имя', max_length=50, blank=True)
    l_name = models.CharField('Фамилия', max_length=50, blank=True)
    age = models.CharField('Возраст', max_length=50, blank=True)
    phone = models.CharField('Телефон', max_length=50, blank=True)
    message = models.TextField('Сообщение', max_length=500, blank=True)

    class Meta:
        verbose_name = '  Сообщение, заказ'
        verbose_name_plural = '  Сообщения, заказы'

    def __str__(self):
        return self.l_name


class InterestingInfo(models.Model):
    title = models.CharField('Заголовок', max_length=120, blank=True)
    text = models.CharField('Текст', max_length=2000, blank=True)

    class Meta:
        verbose_name = ' Интересная информация'
        verbose_name_plural = ' Интересная информация'

    def __str__(self):
        return self.title


class Gallery(models.Model):
    image = models.FileField('Фото', blank=True, default='')

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:100px; height:70px;" />' % self.image.url)
        else:
            return 'Нет фото'

    image_preview.short_description = 'Фото'

    def __str__(self):
        return str("Фото ") + str(self.id)

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерея'