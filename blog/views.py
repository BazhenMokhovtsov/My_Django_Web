from django.shortcuts import render, redirect
from .models import News, Comments
from django.http import HttpResponse, Http404
from .forms import CreateCommendForm

def index(request):
    news = News.objects.all()
    return render(request, "blog/news.html", {"news": news})


def single_new(request, new_id):
    single_new = News.objects.get(pk=new_id)
    new_comment = Comments.objects.filter(new=new_id) #обращаемся к полю 
    

    if request.method == "POST":
        print(request.POST)
        commend_form = CreateCommendForm(request.POST)
        if commend_form.is_valid():
            new_comment = commend_form.save(commit=False)
            new_comment.author = request.user
            new_comment.new = single_new
            new_comment.save()
            return redirect('blog:single_new', new_id)
    else:
        commend_form = CreateCommendForm()
        
# django work with Forms
        
    context = {
        'single_new': single_new,
        'commend_form': commend_form,
        'new_comment' : new_comment
    
        }
    
    return render(request, "blog/single_new.html", context)


def delete_comment(request, comment_id):
    comment = Comments.objects.get(pk=comment_id)
    new_id = comment.new.pk
    comment.delete()
    return redirect('blog:single_new', new_id)
