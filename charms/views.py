from django.shortcuts import render
from django.views import View
from django.views.generic.detail import SingleObjectMixin
from django.http import FileResponse
from django.core.files.storage import FileSystemStorage
from .models import *
# Create your views here.


class FileDownloadView(SingleObjectMixin, View):
    queryset = Charm.objects.all()

    def get(self, request, document_id):
        object = self.get_object(document_id)
        
        file_path = object.attached.path
        file_type = object.content_type  # django file object에 content type 속성이 없어서 따로 저장한 필드
        fs = FileSystemStorage(file_path)
        response = FileResponse(fs.open(file_path, 'rb'), content_type=file_type)
        response['Content-Disposition'] = f'attachment; filename={object.get_filename()}'
        
        return response
