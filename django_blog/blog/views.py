from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
posts = [
    {
        'author': 'Redha Noormansyah',
        'title': 'Blog Post 1',
        'content': 'Konten Kesatu ini Masih dalam dump variabel belum di simpan di Database',
        'date_posted': '12 September 2018'
    },

    {
        'author': 'John Noormansyah',
        'title': 'Blog Post 2',
        'content': 'Konten Kedua ini Masih dalam dump variabel belum di simpan di Database',
        'date_posted': '25 September 2018'
    }
]
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html',{'title':'About'})



