from django.shortcuts import render, redirect
from django.http import HttpResponse
import urllib.request
from bs4 import BeautifulSoup


def forces_simplified(request, id, slug):
    url = 'https://codeforces.com/problemset/problem/' + str(id) + '/' + slug
    try:
        fhand = urllib.request.urlopen(url).read()
        soup= BeautifulSoup(fhand, 'html.parser')
        problem = str(soup(class_ = 'ttypography')[0])
        sideboxes = str(soup(class_ = 'roundbox sidebox')[-1])
        contest_material = str(soup(class_ = 'roundbox sidebox sidebar-menu')[0])
        response = problem + sideboxes + contest_material
    except:
        return redirect(url)

    return render(request, 'codeforces/simplified.html', {'response':response, 'url':url})

def page(request, pg):
    url = 'https://codeforces.com/problemset/page/' + str(pg)
    if request.GET.get('minDifficulty'):
        url += '?tags=' + str(request.GET.get('minDifficulty')) + '-' + str(request.GET.get('maxDifficulty'))
    elif request.GET.get('tags'):
        url += '?tags=' + urllib.parse.quote_plus(request.GET.get('tags'))
    else:
        url += '/'

    try:
        fhand = urllib.request.urlopen(url).read()
        soup= BeautifulSoup(fhand, 'html.parser')
        problems = str(soup(class_ = 'problems')[0])
        pagination = str(soup(class_ = 'pagination')[0])
        filter_by_tag = str(soup(class_ = "roundbox sidebox _FilterByTagsFrame_main")[0])
    except:
        return redirect(url)

    return render(request, 'codeforces/problemset.html', {'problems': problems, 'pagination':pagination, 'filter': filter_by_tag, 'url':url})

def pset(request):
    url = 'https://codeforces.com/problemset'
    if request.GET.get('minDifficulty'):
        url += '?tags=' + str(request.GET.get('minDifficulty')) + '-' + str(request.GET.get('maxDifficulty'))
    elif request.GET.get('tags'):
        url += '?tags=' + urllib.parse.quote_plus(request.GET.get('tags'))
    else:
        url += '/'

    try:
        fhand = urllib.request.urlopen(url).read()
        soup= BeautifulSoup(fhand, 'html.parser')
        problems = str(soup(class_ = 'problems')[0])
        pagination = str(soup(class_ = 'pagination')[0])
    except:
        return redirect(url)

    return render(request, 'codeforces/problemset.html', {'problems': problems, 'pagination':pagination, 'url':url})


def blog(request, pg):
    url = 'https://codeforces.com/blog/entry/' + str(pg)
    return redirect(url)

def noblog(request):
    response = '<h1>404 not found </h1>'
    return HttpResponse(response)