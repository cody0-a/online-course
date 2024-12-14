from django import forms

class CourseRegisterForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title','description','category']
    
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 5:
            raise forms.ValidationError("Title must be at least 5 characters long.")
        return title

    def clean_description(self):
        description = self.cleaned_data['description']
        if len(description) < 10:
            raise forms.ValidationError("Description must be at least 10 characters long.")
        return description  

    def clean_category(self):
        category = self.cleaned_data['category']
        
        if not category:
            raise forms.ValidationError("Category is required.")

        elif not category in ['python', 'django', 'html', 'css', 'javascript', 'flask', 'react']:
            raise forms.ValidationError("Category must be one of the following: python, django, html, css, javascript, flask, react.")

        elif len(category) < 3:
            raise forms.ValidationError("Category must be at least 3 characters long.")
        return category

class  UserProfileForm(forms.ModelForm):
    class Meta:
        model = userProfile
        fields = ['first_name', 'email', 'phone', 'last_name', 'date_of_birth', 'photo', 'bio', 'education_level', 'interest_in', 'hobby']
