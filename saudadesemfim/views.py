from django.shortcuts import render
from .models import Title, Photos, HomepagePhotos, HomepagePhotosMobile, QuemSomos,AlforrecaTexto,AlforrecaImagens,ComoChegar
import random


def getRandomImage(model):
    photosObjects = model.objects.all()
    numberPhotos = len(photosObjects)
    index = random.randint(0,numberPhotos-1)
    return photosObjects[index]


def index(request):
    webTitle = Title.objects.all()[0]
    mainImageDesktop = getRandomImage(HomepagePhotos)
    mainImageMobile = getRandomImage(HomepagePhotosMobile)
    context = {'webTitle':webTitle, 'mainImageDesktop':mainImageDesktop, 'mainImageMobile':mainImageMobile}
    return render(request,'saudadesemfim/homepageRefront.html', context)

def quemsomos(request):
    photosObjects = QuemSomos.objects.all()[0]
    context = {'quemSomos':photosObjects}
    return render(request,'saudadesemfim/quemSomos.html', context)

def alforreca(request):
    alforrecaTexto = AlforrecaTexto.objects.all()[0]
    images = AlforrecaImagens.objects.all()
    context = {'alforrecaTexto':alforrecaTexto,"images": images}
    return render(request,'saudadesemfim/alforreca.html', context)

def galeria(request):
    images = Photos.objects.all()
    images = images[:len(images)-1]
    context = {"images": images}
    return render(request,'saudadesemfim/galeriaBaseTemplate.html', context)

def comoChegar(request):
    guide = ComoChegar.objects.all()
    context = {'guide':guide}
    return render(request,'saudadesemfim/comoChegar.html', context)
