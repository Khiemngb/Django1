from django.http import HttpResponse

# Function will return to client
def home_page(request):
    return HttpResponse('Hello World!')

def about_page(request):
    return HttpResponse('about home')

def contact_page(request):
    return HttpResponse('contact page')




