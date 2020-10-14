from django import forms
from django.forms.models import ModelForm
from .models import Exercise,Category
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
class NewUserForm(UserCreationForm):
    email = forms.EmailField(required = True)
    class Meta:
        model = User
        fields = ("username","email","password1","password2")
    def save(self,commit= True):
        user = super(NewUserForm,self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            return user
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = ["shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" ]
        self.fields['email'].widget.attrs['class'] = "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" 
        self.fields['password1'].widget.attrs['class'] = "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" 
        self.fields['password2'].widget.attrs['class'] = "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" 

class NewLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ("username","password")
    
    def __init__(self, *args, **kwargs):
        super(AuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = ["shadow appearance-none border rounded w-full py-4 px-4 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" ]
        self.fields['password'].widget.attrs['class'] = "shadow appearance-none border rounded w-full py-4 px-4 mb-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" 
  
        
     
    def clean(self):
        cleaned_data = super(AuthenticationForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            pass
        else:
            self.add_error('username','Username and Password required.')
            pass
    def clean_username(self):
        self.username = self.cleaned_data.get('username')
        return self.username
    def clean_password(self):
        self.password = self.cleaned_data.get('password')
        return self.password
    

class SolveExercise(forms.Form):
    CHOICES=[('opt_1',Exercise.opt_1),
                    ('opt_2',Exercise.opt_2),
                    ('opt_3',Exercise.opt_3),
                    ('opt_4',Exercise.opt_4)]
    choices = forms.ChoiceField(choices = CHOICES,widget = forms.RadioSelect() )

    class Meta:
        model = Exercise
        fields = ['choices']
    def __init__(self, *args, **kwargs):
        super(forms.Form, self).__init__(*args, **kwargs)

    def clean(self):
        answer = super(forms.Form, self).clean()
        return answer



class AddExercise(ModelForm):
    name = forms.CharField(max_length=200)
    opt_1 = forms.CharField(max_length=200)
    opt_2 = forms.CharField(max_length=200)
    opt_3 = forms.CharField(max_length=200)
    opt_4 = forms.CharField(max_length=200)
    correct= forms.CharField(max_length=200)
    hint = forms.CharField(max_length=200)
    category = forms.ModelChoiceField(queryset= Category.objects.all())



    class Meta:
        model = Exercise
        fields = ['name','opt_1','opt_2','opt_3','opt_4','correct','hint','category']
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = ["shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" ]
        self.fields['opt_1'].widget.attrs['class'] = "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" 
        self.fields['opt_2'].widget.attrs['class'] = "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" 
        self.fields['opt_3'].widget.attrs['class'] = "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" 
        self.fields['opt_4'].widget.attrs['class'] = "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" 
        self.fields['correct'].widget.attrs['class'] = "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" 
        self.fields['hint'].widget.attrs['class'] = "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" 
        self.fields['correct'].widget.attrs['class'] = "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" 
    
class AddCategory(ModelForm):
    name = forms.CharField(max_length=200)
   


    class Meta:
        model = Category
        fields = ['name']
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = ["shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" ]
    def save(self,commit= True):
        category = super(ModelForm,self).save(commit=False)
        category.slug = self.cleaned_data['name'].lower()
        if commit:
            category.save()
            return category