```commandline
This Project: Django Forms, Model Forms, Template Tags and Default templates

```


```commandline

django forms 

we are going to import 
    from django import forms
    from django.forms import ModelForm

django Forms
    class FormName(forms.Form):
       fields as simillar to django fields
    - Forms saving little diffrent than model form
        - first use name = form.cleaned_dat['field']
            - assign this name model.name
            - save model object
   
model forms
    class FormName(ModelForm):
        check forms.py
```
```
template tags
    {% open template tag
    %} close template tag
    {{ variable open tag
    }} variable close tag
    
    - Extending template using this
        {% extsnds 'html file'%}
        
        {% block content%}
        {% end block%}
    - load static
        {% load static %}
    - url configration
        {% url 'url_name' %}  (<a href="{% url 'url_name' %} ">name</a>
    - Looping query set
        {% for data in queryset %}
            {{object.field_name}}
        {% endfor %}
    - Direct object of variable
        {{object.field_name}}
    - conditions
        {% if condtion %}
            
        {% endif %}
    - filters
        {{object.field_name |upper | lower | length | add "value" | date }} check documanetation
    
```