from django import forms
from .models import Parent, Child

class ParentForm(forms.ModelForm):
    
    class Meta:
        model = Parent
        fields = ['name']

class ChildForm(forms.ModelForm):
    
    class Meta:
        model = Child
        fields = ['name', 'parent', 'favorite_siblings']
        widgets = {
            'favorite_siblings': forms.CheckboxSelectMultiple,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        child_id, parent_id = None, None
        
        if "instance" in kwargs:
            parent_id = kwargs.get("instance").parent.id
            child_id = kwargs.get("instance").id
        elif "initial" in kwargs :
            parent_id = kwargs["initial"].get("parent_id", None)

        self.fields["parent"] = forms.ModelChoiceField(
            widget=forms.HiddenInput, initial=parent_id, queryset=Parent.objects.all()
        )
        # self.fields["parent"] = forms.ModelChoiceField(
        #     widget=forms.HiddenInput,
        #     initial=kwargs["initial"]["parent_id"]
        #     if "parent_id" in kwargs["initial"]
        #     else None,
        #     queryset=Parent.objects.all(),
        # )

        queryset = Child.objects.filter(parent=parent_id)
        if child_id:
            queryset = queryset.exclude(id=child_id)
        self.fields["favorite_siblings"].queryset = queryset