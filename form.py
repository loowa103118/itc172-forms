 BIN +914 Bytes TechReviewProject/TechReviewApp/__pycache__/forms.cpython-36.pyc 
Binary file not shown.
  BIN +103 Bytes (120%) TechReviewProject/TechReviewApp/__pycache__/urls.cpython-36.pyc 
Binary file not shown.
  BIN +641 Bytes (150%) TechReviewProject/TechReviewApp/__pycache__/views.cpython-36.pyc 
Binary file not shown.
  13  TechReviewProject/TechReviewApp/forms.py 
@@ -0,0 +1,13 @@
from django import forms
from .models import TechType, Product, Review

class ProductForm(forms.ModelForm):

    class Meta:
        model=Product
        fields='__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields='__all__' 
  13  TechReviewProject/TechReviewApp/templates/TechReviewApp/newproduct.html 
@@ -0,0 +1,13 @@
{% extends 'base.html' %}
{% block content %}
<h2>Add Product</h2>
<form method='POST' class='post-form'>
<table class='table'>
    {% csrf_token %}
    {{ form.as_table }}
</table>
<button type='submit' class='save btn btn-default'>
    Save
</button>
</form>
{% endblock %} 
  13  TechReviewProject/TechReviewApp/templates/TechReviewApp/newreview.html 
@@ -0,0 +1,13 @@
{% extends 'base.html' %}
{% block content %}
<h2>Add Product</h2>
<form method='POST' class='post-form'>
<table class='table'>
    {% csrf_token %}
    {{ form.as_table }}
</table>
<button type='submit' class='save btn btn-default'>
    Save
</button>
</form>
{% endblock %} 
  2  TechReviewProject/TechReviewApp/templates/base.html 
@@ -18,6 +18,8 @@ <h1>Tech Reviews</h1>
<ul class="nav navbar-nav"> 
<li><a href="{% url 'types' %}">Types</a></li>
<li><a href="{% url 'products' %}">Products</a></li> 
<li><a href="{% url 'newproduct' %}">Add Products</a></li> 
<li><a href="{% url 'newreview' %}">Add Review</a></li>
</ul> 
</div> 
</nav> 
  2  TechReviewProject/TechReviewApp/urls.py 
@@ -7,5 +7,7 @@
    path('getTypes/', views.getTypes, name='types'),
    path('getProducts/', views.getProducts, name='products'),
    path('productDetail/<int:id>',views.productDetail, name='productdetail'),
    path('newProduct/', views.newProduct, name='newproduct'),
    path('newReview/', views.newReview, name='newreview'),
]

  27  TechReviewProject/TechReviewApp/views.py 
@@ -1,5 +1,6 @@
from django.shortcuts import render, get_object_or_404
from .models import TechType, Product, Review
from .forms import ProductForm, ReviewForm

# Create your views here.
def index(request):
@@ -23,4 +24,28 @@ def productDetail(request, id):
         'reviewcount' : reviewcount,
         'reviews': reviews,
    }
    return render (request, 'TechReviewApp/productdetail.html', context=context) 
    return render (request, 'TechReviewApp/productdetail.html', context=context)

def newProduct(request):
     form=ProductForm
     if request.method=='POST':
          form=ProductForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=ProductForm()
     else:
          form=ProductForm()
     return render(request, 'TechReviewApp/newproduct.html', {'form' : form})

def newReview(request):
     form=ReviewForm
     if request.method=='POST':
          form=ReviewForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=ReviewForm()
     else:
          form=ReviewForm()
     return render(request, 'TechReviewApp/newreview.html', {'form' : form}) 
