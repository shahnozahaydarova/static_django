from django.shortcuts import render

def car(request):
    return render(request,'index.html')
def home(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def furnitures(request):
    return render(request,'furnitures.html')
def testimonial(request):
    return render(request,'testimonial.html')
