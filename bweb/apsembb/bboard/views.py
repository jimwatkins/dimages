from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views import generic
from django.urls import reverse
from django.shortcuts import render_to_response
from .models import Comment
from django.contrib import messages
from django import forms
from django.db import models
from django.contrib import admin
import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


#class ChoiceInline(admin.TabularInline):
 #   model = Comment
 #   extra = 3#


#class commentUser(admin.ModelAdmin):
#    fieldsets = [
#        (None,               {'fields': ['comment_text']}),
#        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#    ]
#    list_display = ('comment_text', 'pub_date', 'was_published_recently')
#    list_filter = ['pub_date']
#    search_fields = ['comment_text']
    
#    inlines = [ChoiceInline]

#admin.site.register(Comment, commentUser)

class LoginView(generic.ListView):
    template_name = 'bboard/Login.html'
    model = Comment

class WelcomeView(generic.ListView):
    template_name = 'bboard/Welcome.html'
    model = Comment

class RegisterView(generic.ListView):
    template_name = 'bboard/Register.html'
    model = Comment

class ForumView(generic.ListView):
    template_name = 'bboard/Forum.html'
    #comment_list = Comment.objects.all
    #context_object_name = 'comment_list'
    model = Comment
    def get_queryset(self):
        """Return the last five published questions."""
        
        return Comment.objects.all()   #order_by('-pub_date')
    


class commentForm(forms.Form):
    comment_text = forms.CharField(label='Enter comment', max_length=500)
    comment_user = forms.CharField(label='Enter user', max_length=50)

def postComment(request):
#        # Always return an HttpResponseRedirect after successfully dealing
#       # with POST data. This prevents data from being posted twice if a
#        # user hits the Back button.
#        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    if request.method == 'POST':
        enteredText = request.POST.get('textfield', None)
        c= Comment(comment_text = enteredText, comment_user = request.user.username, pub_date = datetime.datetime.now())
        c.save()
     #   form = commentForm(request.POST)
     #   if form.is_valid():
     #           form.save()
    #return HttpResponseRedirect(reverse('bboard:forum'))
     #   else:
     #           messages.error(request, "Error")
    return redirect('forum/')

def createAccount(request):
    if request.method == 'POST':
        enteredUsername = request.POST.get('textfield2', None)
        enteredPassword = request.POST.get('textfield3', None)
        user = User.objects.create_user(username=enteredUsername, password=enteredPassword)
        user.save()
        user = authenticate(request, username=enteredUsername, password=enteredPassword)
        login(request, user)
        return redirect('forum/')

def loginUser(request):
    context = request.POST
    if request.method == 'POST':
        loginUsername = request.POST['textfield4']
        loginPassword = request.POST['textfield5']
        user = authenticate(request, username=loginUsername, password=loginPassword)
       # user = User.objects.get_by_natural_key(loginUsername)
        #choice_set.get(pk=request.POST['choice'])
    # if user is not None:
        #    login(request, user)
        # return redirect('forum/')
        print(user)
        if user: 
           # if user.password == loginPassword:
                if user.is_active:
                    login(request, user)
                    return redirect('forum/')
                else:
                    return HttpResponse("Not active")
          #  else:
           #     return HttpResponse("Incorrect Password")
        else:
            return HttpResponse("Invalid")
    else:
        return render(request, 'bboard/Login.html', {}, context)