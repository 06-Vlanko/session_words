# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render (request, 'session_words/index.html')

def process(request):
    if 'content' not in request.session:
        request.session['content'] = []
    
    request.session['content'].append ( (request.POST['word'], request.POST['color'], request.POST.get('big_fonts', False)) )
    request.session['content']

    # if request.POST['content'][0][0]=='word':
    #     print '-----> word matches!'
    print '------> session: content', request.session['content']
    print '------> content[0]:', request.session['content'][0]
    print '------> content[0][0]:', request.session['content'][0][0]

    print '------> content.length: ', len(request.session['content'])
    return redirect ('/')

def clear(request):
    request.session.clear()
    return redirect ('/')