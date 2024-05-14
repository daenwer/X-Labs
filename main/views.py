from rest_framework import filters, generics, viewsets
from main.models import Author, Book
from main.serializers import AuthorSerializer, BookSerializer


class AuthorAPIList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    

class AuthorPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name', 'date_of_birth']


class BookAPIList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    

class BookPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = [
        'name', 'description', 'year_of_publishing', 
        'authors__first_name', 'authors__last_name'
    ]
