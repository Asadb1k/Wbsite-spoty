from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import DetailView,View
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.models import User

from .models import SingMod,CommentMod

def LogoutPage(request):
    logout(request)
    return redirect('home')

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'spoty/login.html')

def SignUp(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('pass1')
        password2 = request.POST.get('pass2')
        if User.objects.filter(username=username).exists():
            return render(request,'spoty/signup.html')
        if password1 == password2:
            user = User.objects.create_user(username=username,email=email,password=password1)
            login(request,user)
            return redirect('home')
    return render(request,'spoty/login1.html')

def HomePage(request):
    sing = SingMod.objects.all()
    return render(request,'spoty/index.html',{'songs':sing})



def Private(request,id):
    song = SingMod.objects.all()
    sing = get_object_or_404(SingMod, id=id)
    
    if request.method == "POST":
        user = request.user
        comment = request.POST.get('comment')
        if len(comment) != 0 :
            CommentMod.objects.create(username=user,comment=comment,song_author=sing)
    Tom = CommentMod.objects.filter(song_author=sing)
    context = {
        'songs': song,
        'sing': sing,
        'tom':Tom
    }
    return render(request,'spoty/private.html',context)


# class Private(DetailView):
#     model = SingMod
#     template_name = 'spoty/private.html'
#     context_object_name = 'sing'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         users = SingMod.objects.all()
#         context['songs'] = users
#         return context
    
#     def post(self, request, *args, **kwargs):
#         if request.method == 'POST':
#             comment = request.POST.get('comment')
#             print(comment)
#         # self.object = self.get_object()
#         # comment_text = request.POST.get('comment')
#         # if comment_text:
#         #     Comment.objects.create(
#         #         sing=self.object,
#         #         user=request.user,
#         #         text=comment_text
#         #     )
#         return self.get(request, *args, **kwargs)

class CategoryPage(View):
    def get(self,request, id):
        products = SingMod.objects.filter(id=id)            
        return render(request, 'spoty/category.html', {'sing': products})

