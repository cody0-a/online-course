from django.db import models
from django.urls import reverse
import datetime
from django.utils import timezone


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title


class question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return se;f.pub_date >= timezone.now() - datetime.timedelta(days=1)

class choice(models.Model):
    question = models.ForeignKey(question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


    

class answer(models.Model):
    question = models.ForeignKey(question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text

class student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    sex = models.CharField(max_length=200, choices=[('M', 'Male'), ('F', 'Female')])
    date_registered = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('student-detail', args=[str(self.id)])

    def get_student_count(self):
        return student.objects.count()

    def get_student_name(self):
        return ''.join(self.first_name + ' ' + self.last_name)


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('publisher-detail', args=[str(self.id)])

    def display_book(self):
        return ', '.join(book.title for book in self.book_set.all()[:3])
