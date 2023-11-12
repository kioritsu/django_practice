from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from  .forms import LoginForm
from .models import Member, Method, BigCategory, SmallCategory, Payment
import datetime


class Login(LoginView):
    form_class = LoginForm
    template_name = 'app/login.html'
    

class Logout(LogoutView):
    template_name = 'app/login.html'


class TopView(LoginRequiredMixin, TemplateView):
    template_name = "top.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["members"] = Member.objects.filter(user=self.request.user)
        return context
    
    def post(self, request, *args, **kwargs):
        print(request.POST.get("name"))
        Member.objects.create(name=request.POST.get("name"), user=self.request.user)
        return redirect("home")


def calendar(request):
    return render(request, 'calendar.html')


class MoneyView(LoginRequiredMixin, TemplateView):
    template_name = "money.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["today"] = datetime.datetime.now().strftime('%Y-%m-%d')
        context["methods"] = Method.objects.filter(user=self.request.user)
        context["small_categories"] =  SmallCategory.objects.filter(user=self.request.user)
        context["members"] = Member.objects.filter(user=self.request.user)
        
        return context
    
    def post(self, request, *args, **kwargs):
        print(request.POST.get("method"))
        method = Method.objects.get(name=request.POST.get("method"), user=self.request.user)
        small_category = SmallCategory.objects.get(name=request.POST.get("small_category"), user=self.request.user)
        members = request.POST.getlist("member")
        
        payment = Payment.objects.create(
            balance = request.POST.get("balance"),
            price = request.POST.get("price"),
            date = request.POST.get("date"),
            method = method,
            small_category = small_category,
            memo = request.POST.get("memo"),            
        )
        for member_id in members:
            payment.member.add(Member.objects.get(id=member_id))
        
        return redirect("money")
    



class AddCategoryView(LoginRequiredMixin, TemplateView):
    template_name = "add_category.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["payments"] = Method.objects.filter(balance=False,user=self.request.user)
        context["incomes"] = Method.objects.filter(balance=True,user=self.request.user)
        context["big_categories"] = {}
        big_categories = BigCategory.objects.filter(user=self.request.user)
        for big_category in big_categories:
            context["big_categories"][big_category] = SmallCategory.objects.filter(big_category=big_category, user=self.request.user)
        
        return context
    
    def post(self, request, *args, **kwargs):
        if request.POST.get("payment"):
            Method.objects.create(
                balance = False,
                name = request.POST.get("payment"),
                user = self.request.user
            )
        
        if request.POST.get("income"):
            Method.objects.create(
                balance = True,
                name = request.POST.get("income"),
                user = self.request.user
            )
            
        if request.POST.get("big_category"):
            BigCategory.objects.create(
                name = request.POST.get("big_category"),
                user = self.request.user
            )
        
            
        if request.POST.get("small_category"):
            big_category = BigCategory.objects.get(name=request.POST.get("small_category_base"),user=self.request.user)
            SmallCategory.objects.create(
                name = request.POST.get("small_category"),
                big_category = big_category,
                user = self.request.user
            )
            
            
        return redirect("add_category")  