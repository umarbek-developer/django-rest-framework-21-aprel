from rest_framework.viewsets import ModelViewSet
from .serializer import NotebookSerializer
from .models import Notebook

# Create your views here.


class NotebookViewSet(ModelViewSet):
    queryset = Notebook.objects.all()
    serializer_class = NotebookSerializer

