from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render

from market.models import Item, ProductCategory

#from market.models import  Product
from . models import CommentModel, EnterpriseModel, TourModel
from .forms import CommentForm,EnterpriseRegisterForm
# Create your views here.

def company_registration(request):
    return render(request,'company_registration.html')

def index(request):
    """market = Item.objects.all()
    enterprise_data = EnterpriseModel.objects.all()
    tourmodel = TourModel.objects.all()
    return render(request,'index.html',context ={
        'enterprises':enterprise_data,
        'tourmodel_data':tourmodel,
        'market_items':market,
    })"""
    return render(request,'index.html')


# def detailpage(request,id):
#     enterprise_query = EnterpriseModel.objects.get(id=id)
#     comments = CommentModel.objects.filter(enterprise=enterprise_query)
#     comment_form = CommentForm()
#     if request.method =='POST':
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#             comment = comment_form.save(commit=False)
#             comment.author = request.user
#             comment.enterprise = enterprise_query
#             comment.save()
#             return redirect('enterprises:detail',id=id)
#     return render(request,'detailpage.html',context={
#       'enterprise_query':enterprise_query,
#      'commentform':comment_form,
#      'comments':comments
#     })

def detailpage(request,id):
    enterprise_query = EnterpriseModel.objects.get(id=id)
    comments = CommentModel.objects.filter(enterprise=enterprise_query)
    user_comment = CommentModel.objects.filter(author = request.user).first

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            current_user = request.user
            data = CommentModel()

            data.author_id = current_user.id
            data.enterprise_id = id
            data.content = form.cleaned_data["content"]
            data.rating = form.cleaned_data["rating"]
            data.count += 1
            data.save()
            return redirect('enterprises:detail',id=id)
            
    return render(request,'detailpage.html',context={
        'enterprise_query':enterprise_query,
        'comments':comments,
        "user_comment":user_comment
        })

def create_enterprise(request):
    form = EnterpriseRegisterForm()

    if request.method == "POST":
        form = EnterpriseRegisterForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            return redirect("/")


    context = {
        "form":form
    }

    return render(request,"create_enterprise.html",context)

def tours(request):
    return render(request,'tours1.html')

def sanatory(request):
    return render(request,'sanatory.html')

