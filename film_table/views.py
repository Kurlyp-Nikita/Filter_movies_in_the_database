from django.shortcuts import render, redirect
from .forms import *
from .models import *




def index(req):
    data = {}
    return render(req, 'index.html', data)


def films(req):
    film = Film.objects.all()
    forma = FilmForm()
    formapoisk = FilmPoisk()
    if req.POST:
        forma = FilmForm(req.POST)
        k1 = req.POST.get('country')
        k2 = req.POST.get('title')
        k3 = req.POST.get('year')
        print(k1, k2, k3)
        forma = FilmForm()
        if not k3:
            k3 = 0

        Film.objects.create(country=k1, title=k2, year=k3)

    data = {'database_films': film, 'forma': forma, 'formapoisk': formapoisk}
    return render(req, 'film.html', data)


def poisk_film(req):
    films = Film.objects.all()
    forma = FilmForm()
    formapoisk = FilmPoisk(req.POST)

    country = req.POST.get('country')
    year = req.POST.get('year')
    ex1 = req.POST.get('ex')

    basepoisk = films

    if country:
        if ex1:
            basepoisk = basepoisk.exclude(country=country)
        else:
            basepoisk = basepoisk.filter(country=country)

    if year: 
        if ex1:
            basepoisk = basepoisk.exclude(year=year)
        else:
            basepoisk = basepoisk.filter(year=year)

    print(req.POST.get('name'))

    data = {'database': films, 'forma': forma, 'formapoisk': formapoisk, 'databasepoisk': basepoisk}
    return render(req, 'film.html', data)


def edit_film(req, id):
    print(id)
    onefilm = Film.objects.get(id=id)
    forma = FilmForm()
    data = {'forma': forma}
    if req.POST:
        onefilm.country = req.POST.get('country')
        onefilm.title = req.POST.get('title')
        onefilm.year = req.POST.get('year')
        onefilm.save()
        return redirect('films')
    return render(req, 'edit.html', data)


def addfilms(req):
    Film.objects.create(country='USA', title='Джанго освобождённый', year='2012')
    film1 = Film()
    film1.country = 'USA'
    film1.title = 'Джанго освобождённый'
    film1.year = 2012
    film1.save()
    return redirect('films')


def delete_film(req, id):
    print(id)
    onefilm = Film.objects.get(id=id)
    onefilm.delete()
    return redirect('films')




    # if title:
    #     basepoisk = Film.objects.filter(id=title)

    # elif country and title and year:
    #     if not ex:
    #         basepoisk = Film.objects.filter(country=country, title=title, year=year)
    #
    #     elif ex:
    #         basepoisk = Film.objects.filter(country=country, title=title, year=year).exclude(year=year)
    #
    # elif country and not title and not year:
    #     basepoisk = Film.objects.filter(country=country)
    #
    # elif year and not country and not title:
    #     basepoisk = Film.objects.filter(year=year, country=country, title=title)
    #
    # else:
    #     basepoisk = {}


