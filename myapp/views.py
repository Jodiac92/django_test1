from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("최초 요청 처리")

def hello_func(request):
    msg = "창민 힘드니?"
    ss = "<html><body>장고 만세<br><b>%s</b></body></html>"%(msg)
    return HttpResponse(ss)

def hello_template(request):
    msg = "강원도에 눈"
    return render(request, 'show.html', {'msg':msg})

def world_func(request):
    return render(request, 'disp.html')
