from .models import University
from django.forms import ModelForm, TextInput, Textarea, NumberInput

class UniversityForm(ModelForm):
    class Meta:
        model = University
        fields = ['title', 'code', 'ownership', 'rector', 'location',
                  'phone', 'email', 'website', 'military_department', 'grants', 'year']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть повну назву закладу вищої освіти'
            }),
            'code': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть код вищого закладу освіти в ЄДБО'
            }),
            'ownership': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть форму власності ЗВО'
            }),
            'rector': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть ім`я ректора'
            }),
            'location': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть місцерозташування ЗВО'
            }),
            'phone': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть номер/и телефону/ів гарячої лінії'
            }),
            'email': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть пошту ЗВО'
            }),
            'website': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть посилання на вебсайт'
            }),
            'military_department': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вкажіть, чи є військова кафедра у ЗВО'
            }),
            'grants': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вкажіть, чи бере заклад участь в програмі державних грантів на здобуття вищої освіти'
            }),
            'year': TextInput(attrs={
                'class': 'col-xs-4',
                'id': 'ex1',
                'placeholder': 'Введіть рік заснування закладу'
            }),
        }