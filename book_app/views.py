from django.shortcuts import render,redirect
from .models import book
from .forms import bookcreate
from django.http import HttpResponse

# Create your views here.

def index(request):
    shelf = book.objects.all()
    return render(request,"book_app/library.html",{"shelf":shelf})

def upload(request):
    upload = bookcreate()
    if request.method == "POST":
        upload = bookcreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect("index")
        else:
            return HttpResponse("""something went wrong, please reload the webpage by 
                                clicking <a href="{{url:"index"}}">reload</a>""")
    else:
        return render(request, "book_app/upload_form.html", {
            "upload_form":upload
        })      
              
def update_book(request, book_id):
    book_id = int(book_id)
    try:
        book_shelf = book.objects.get(id = book_id)
    except book.DoesNotExist:
        return redirect("index")
    book_form = bookcreate(request.POST or None, instance=book_shelf)
    if book_form.is_valid():
        book_form.save()
        return redirect("index")
    return render(request, "book_app/upload_form.html", {
        "upload_form":book_form
    })
      
def delete_book(request, book_id):
    book_id = int(book_id)
    try:
        book_shelf = book.objects.get(id = book_id)
    except book.DoesNotExist:
        return redirect("index")
    book_shelf.delete()
    return redirect("index")