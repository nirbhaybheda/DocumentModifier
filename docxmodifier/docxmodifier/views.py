from django.shortcuts import render
import os
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

import mimetypes
from django.core.servers.basehttp import FileWrapper
from django.http import HttpResponse, Http404, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from serializers import *
import modify

class ModifyFile(APIView):
    def post(self, request, format=None):
        serializer = ModifySerializer(data=request.data)
        if not serializer.is_valid():
            return Response(str(serializer.errors))
        filename = "input.docx"
        modify.replace_string(filename, serializer.data)
        fpath="modify_input.docx"
    	wrapper = FileWrapper(file(fpath))
    	response = HttpResponse(wrapper)
    	format_name = os.path.basename(fpath)
    	filesize = os.path.getsize(fpath)
    	content_disposition = 'attachment; filename="%s"'%(format_name)
    	response['Content-Disposition'] = content_disposition
    	content_type = mimetypes.guess_type(fpath)[0]
    	response['Content-Type'] = content_type
    	response['Content-Length'] = str(filesize)
    	
        #response = HttpResponse(mimetype='application/force-download')
        #response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(file_name)
        #response['X-Sendfile'] = smart_str(path_to_file)
        return response
