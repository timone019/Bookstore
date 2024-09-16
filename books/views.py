from django.shortcuts import render
from django.views.generic import ListView, DetailView   #to display lists & details
from .models import Book   

#to protect class-based view
from django.contrib.auth.mixins import LoginRequiredMixin #to access Book model

# Create your views here.
class BookListView(LoginRequiredMixin, ListView):            #class-based "protected" view
    model = Book                         #specify model
    template_name = 'books/main.html'  #specify template
    
class BookDetailView(LoginRequiredMixin,DetailView):        #class-based "protected" view
    model = Book
    template_name = 'books/detail.html' 
    
def home(request):
    return render(request, 'books/home.html')