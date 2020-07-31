from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate

from .models import Noticia

# Create your views here.
def view(request, noticia_id):
    noticia = Noticia.objects.extra(where=["id= %s" ], params=[noticia_id])
    context = {'noticia': noticia}
    return render(request, 'scmp/partials/noticia.html', context)

def index(request):
    ultimas_noticias = Noticia.objects.order_by('data')[:5]
    context = {'ultimas_noticias': ultimas_noticias}
    return render(request, 'scmp/partials/noticias.html',context)

def home(request):
    return render (request, 'scmp/home.html')

def logout(request):
    auth.logout(request)
    return redirect ('home')

def dashboard(request):
    if request.user.is_authenticated:
        return render (request,'scmp/dashboard.html')
    else:
        return redirect('home')

def novousuario(request):
    if request.method == 'POST':
        Nome = request.POST['Nome']
        email = request.POST['email']
        Senha1 = request.POST['Senha1']
        Senha2 = request.POST['Senha2']
        
        #Validações
        if not Nome.strip():
            print('LOG_err: O CAMPO "NOME" NÃO PODE FICAR VAZIO!\n CASTRO NÃO REALIZADO')
            return redirect ('novousuario')

        if not email.strip():
            print('LOG_err: O CAMPO "EMAIL" NÃO PODE FICAR VAZIO!\n CASTRO NÃO REALIZADO')
            return redirect ('novousuario')

        if Senha1 != Senha2:
            print('LOG_err: AS SENHAS NÃO CORRESPONDEM!\n CASTRO NÃO REALIZADO')

        if User.objects.filter(email=email).exists(): #dentro do parentese ele filtra a Matricula(variavel) em matricula(BD)
            print('LOG_err: USUARIO JÁ CADASTRADO')
            return redirect ('novousuario')
        user = User.objects.create_user(username=Nome, password=Senha1, email=email)
        user.save()
        print('DADOS SALVOS')
        return render(request, 'scmp/home.html')
        
    else:
        return render(request,'scmp/novousuario.html')

def equipamentos(request):
    #ADCIONAR REGRA DE USER.IS_AUTHENTICATED PARA HAVER A REGRA DE USUARIO ESTAR LOGADO PARA UTILIZAR ESSA PAGINA
    return render(request, 'scmp/equipamentos.html')

def sobrenos(request):
    return render(request, 'scmp/sobrenos.html')
