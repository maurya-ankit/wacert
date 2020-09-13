from django.shortcuts import render,HttpResponse
from django.views import View
import mimetypes
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from .models import Count

# Create your views here.
class home(View):
    def get(self,request):
        obj=Count.object.filter(name="visits")[0]
        count=obj.count
        context={'count':count}
        return render(request,'index.html',context)
    def post(self,request):
        name=request.POST.get('name')
        img = Image.open("static/cert.png")
        draw = ImageDraw.Draw(img)
        # font = ImageFont.truetype(<font-file>, <font-size>)
        font = ImageFont.truetype("static/Roboto-Regular.ttf", 100)
        fontd = ImageFont.truetype("static/Roboto-Regular.ttf", 20)
        # draw.text((x, y),"Sample Text",(r,g,b))
        draw.text((740, 550),f"{name}",(0,0,0),font=font)
        draw.text((650,1370),f"* This is just for fun. Make yours from here : { request.build_absolute_uri() }",(0,0,0),font=fontd)


        response = HttpResponse(content_type ="image/png")
        img.save(response, "PNG")
        obj=Count.object.filter(name="visits")[0]
        n=obj.count
        n=n+1
        obj.count=n
        obj.save()
        return response

        


# def download_file(request):
#     # fill these variables with real values
#     fl_path = ‘/file/path'
#     filename = ‘downloaded_file_name.extension’

#     fl = open(fl_path, 'r’)
#     mime_type, _ = mimetypes.guess_type(fl_path)
#     response = HttpResponse(fl, content_type=mime_type)
#     response['Content-Disposition'] = "attachment; filename=%s" % filename
#         return r