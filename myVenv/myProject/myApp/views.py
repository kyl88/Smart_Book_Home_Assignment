from rest_framework import generics, permissions
from .models import User
from .models import UserPreferences
import requests
from .serializers import UserSerializer
from django.shortcuts import render
from django.contrib.auth.decorators import login_required



# Create your views here.

# Create User Courses API View 

GUTENDEX_API = 'https://gutendex.com/books'

class UserCoursesView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(username=self.request.user)
    


    @login_required
    def book_recommendations(request):
        user = request.user
        try:
            preference = UserPreferences.objects.get(user=user)
            subjects = preference.get_subject_list()
        except UserPreferences.DoesNotExist:
            subjects = ['fiction']    

        books = []
        for subject in subjects : 
            response = requests.get(f'{GUTENDEX_API}?topic={subject}')   
            if response.status_code == 200:
              results = response.json().get('results',[])
              for book in results:
                title = book.get('title','untitled')
                authors =[author.get('name') for author in book.get('authors',[])]

                # Try to get a readable link

                formats = book.get('formats',{})
                link = formats.get('text/html') or formats.get('text/plain') or formats.get('application/pdf')

                books.append({
                    'title': title,
                    'author': authors,
                    'link': link
                })

        return render(request, 'book_recommendations.html', {'books': books})   