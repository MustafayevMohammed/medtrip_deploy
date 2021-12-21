from django.contrib.auth.models import User
from django.shortcuts import render
from account.models import CustomUserModel
# Create your views here.
from django.shortcuts import redirect, render

from market.models import Customer, Item, ProductCategory

#from market.models import  Product

from . models import CategoryModel, CommentModel, EnterpriseModel, TourModel, CountryModel
from .forms import CommentForm,EnterpriseRegisterForm
from django.views.decorators.csrf import csrf_protect

# Create your views here.

@csrf_protect
def company_registration(request):
    countries = CountryModel.objects.all()
    categories = CategoryModel.objects.all()
    if request.method == "POST":
        form = EnterpriseRegisterForm(request.POST)
        print(form.errors)
        if form.is_valid():
            data = EnterpriseModel()
            owner = CustomUserModel.objects.filter(
                email = request.user
            ).first()
            data.owner = owner
            data.name = form.cleaned_data["name"]
            data.authorized_person = form.cleaned_data["authorized_person"]
            data.number = form.cleaned_data["number"]
            data.category = form.cleaned_data["category"]
            data.country = form.cleaned_data["country"]
            data.save()
            return redirect("/")
        else:
            print(form)
            print("Invalid Form")
            print(form.errors)
            return render (request, 'company_registration.html',{'form':form})

    context = {
        "countries":countries,
        "categories":categories
    }
    return render(request,'company_registration.html',context)

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

#"def advice_send(request):
    #data = AdviceForm(data=request.POST)
    #if data.is_valid():
    #    data
    

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

def detailpage(request):
    #enterprise_query = EnterpriseModel.objects.get(id=id)
    #comments = CommentModel.objects.filter(enterprise=enterprise_query)
    #user_comment = CommentModel.objects.filter(author = request.user).first

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
            return redirect('enterprises:detail')
            
    return render(request,'tours1.html',context={
        #'enterprise_query':enterprise_query,
        #'comments':comments,
        #"user_comment":user_comment
        })



# def tours(request):
#     return render(request,'tours1.html')

def sanatory(request):
    return render(request,'sanatory.html')

