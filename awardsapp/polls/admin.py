# from django.contrib import admin
# from .models import Question, Choice


# admin.site.register([Question, Choice])

from django.contrib import admin
from .models import Question,Choice
from django import forms
from django.forms.models import BaseInlineFormSet

class AtLeastOneRequiredInlineFormSet(BaseInlineFormSet):

    def clean(self):
        """Check that at least one choice has been entered."""
        super(AtLeastOneRequiredInlineFormSet, self).clean()
        if any(self.errors):
            return
        if not any(cleaned_data and not cleaned_data.get('DELETE', False)
            for cleaned_data in self.cleaned_data):
            raise forms.ValidationError('At least one choice required.')


class ChoicesInline(admin.TabularInline):
    model = Choice
    formset= AtLeastOneRequiredInlineFormSet
    extra = 1
    exclude= ['votes']
    

class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]
    inlines=(ChoicesInline,)
    # Allows you to edit the question list format
    list_display = ("question_text", "pub_date", "was_published_recently")
    # Enable a filter in the admin view
    list_filter = ["pub_date"]
    # Enable a search box
    search_fields = ["question_text"]

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for obj in formset.deleted_objects:
            obj.delete()        
        for instance in instances:
            instance.save()            

# If QuestionAdmin is not added, formatting and other changes will not take place
admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice)