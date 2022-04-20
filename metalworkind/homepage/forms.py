from django import forms

class SearchForm(forms.Form):
    search_field = forms.CharField(max_length=255,
                                   widget=forms.TextInput(attrs={'class': 'form-control rounded', 'id': 'formName',
                                                                 'name': 's', 'placeholder': 'Поиск материалов',
                                                                 'type': 'search', 'aria-label': 'Search',
                                                                 'aria-describedby': 'search-addon', 'itemprop': 'query-input'}))

class AboutForm(forms.Form):
    name = forms.CharField(max_length=50, label="Имя", widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'formName',
                                                                        'name': 'name'}))

    email = forms.EmailField(max_length=50, label="Email", widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingInput',
                                                                          'name': 'email'}))

    CHOICES = (('Ошибка на сайте', 'Ошибка на сайте'), ('Запрос на размещение рекламы', 'Запрос на размещение рекламы'),
               ('Сказать Спасибо или оставить совет', 'Сказать Спасибо или оставить совет'), ('Другое', 'Другое'),)
    subject = forms.ChoiceField(choices=CHOICES, label="Тема",
                                widget=forms.Select(attrs={'class': 'form-select', 'id': 'floatingSelect',
                                                           'name': 'subject', 'aria-label': 'Выберите тему письма'}),
                                initial='Другое',)

    message = forms.CharField(widget=forms.Textarea(attrs={'style': 'height: 150px;', 'id': 'formText', 'name': 'message',
                                                           'class': 'form-control'}), label="Сообщение",)

class SubscribeForm(forms.Form):
    email = forms.EmailField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'form5Example2',
                                                                          'name': 'email', 'placeholder': 'Введите email адрес'}))
