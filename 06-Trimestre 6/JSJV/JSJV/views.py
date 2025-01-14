from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib import messages

#Importar el form de la creacion de Usuarios 
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

#Nesesario paara que sea obligatorio el registrarse 
from django.contrib.auth.decorators import login_required
#correos
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings

#PDF
import os
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from django.contrib.staticfiles import finders
from actividades.models import Activity
from inventario.models import Inventory

def quienes(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        
        template = render_to_string('email_template.html', {
            'name': name,
            'email': email,
            'message': message
        })
    
        email = EmailMessage(
            subject,
            template,
            settings.EMAIL_HOST_USER,
            ['vs157918@gmail.com',]
        )
    
        email.fail_silently = False
        email.send()
    
    return render(request, 'quienes.html',{

    })
def index(request):
    return render(request, 'index.html',{
                  
    })

def actividad(request):
    return render(request, 'actividad.html',{
                  
    })

def admin(request):
    return render(request, 'admin.html',{
                  
    })

def catalogoServicios(request):
    return render(request, 'catalogoServicios.html',{
                  
    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'registration/login.html', {})

def exit_view(request):
    logout(request)
    return redirect('index')

def quienes(request):
    return render(request, 'quienes.html',{
                  
    })

def recordarContra(request):
    return render(request, 'recordarContra.html',{
                  
    })

# Creación de usuarios
def registros(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Puedes redirigir a la página que desees después del registro
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/registros.html', {'form': form})

def roles(request):
    return render(request, 'roles.html',{
                  
    })

def servicios(request):
    return render(request, 'servicios.html',{
                  
    })

@login_required
def crudInventario(request):
    return render(request, 'crudInventario.html',{
                  
    })

def crudOT(request):
    return render(request, 'crudOT.html',{
                  
    })

def crudPago(request):
    return render(request, 'crudPago.html',{
                  
    })

#PDF Actividades 
class PDFacti(View):

    def link_callback(self, uri, rel):
            result = finders.find(uri)
            if result:
                    if not isinstance(result, (list, tuple)):
                            result = [result]
                    result = list(os.path.realpath(path) for path in result)
                    path=result[0]
            else:
                    sUrl = settings.STATIC_URL       
                    sRoot = settings.STATIC_ROOT     
                    mUrl = settings.MEDIA_URL       
                    mRoot = settings.MEDIA_ROOT      

                    if uri.startswith(mUrl):
                            path = os.path.join(mRoot, uri.replace(mUrl, ""))
                    elif uri.startswith(sUrl):
                            path = os.path.join(sRoot, uri.replace(sUrl, ""))
                    else:
                            return uri

            if not os.path.isfile(path):
                    raise RuntimeError(
                            'media URI must start with %s or %s' % (sUrl, mUrl)
                    )
            return path
    
    def get(self, request, *args, **kwargs):
        try:
            actividades = Activity.objects.all()  
            template = get_template('PDFS/pdfActi.html')
            context = {
                'actividades': actividades
            }

            html = template.render(context)
            
            response = HttpResponse(content_type='application/pdf')
            #response['Content-Disposition'] = 'attachment; filename="reporte de actividades.pdf"'
            pisa_status = pisa.CreatePDF(
                 html, dest=response,
                 link_callback=self.link_callback
                 )
         
            if pisa_status.err:
                return HttpResponse('We had some errors <pre>' + html + '</pre>')
            
            return response
        except Exception as e:
            print(f"Error: {e}")
            return HttpResponse('Error al generar el PDF')


#PDF Inventario
class PDFinve(View):

    def link_callback(self, uri, rel):
            result = finders.find(uri)
            if result:
                    if not isinstance(result, (list, tuple)):
                            result = [result]
                    result = list(os.path.realpath(path) for path in result)
                    path=result[0]
            else:
                    sUrl = settings.STATIC_URL       
                    sRoot = settings.STATIC_ROOT     
                    mUrl = settings.MEDIA_URL       
                    mRoot = settings.MEDIA_ROOT      

                    if uri.startswith(mUrl):
                            path = os.path.join(mRoot, uri.replace(mUrl, ""))
                    elif uri.startswith(sUrl):
                            path = os.path.join(sRoot, uri.replace(sUrl, ""))
                    else:
                            return uri

            if not os.path.isfile(path):
                    raise RuntimeError(
                            'media URI must start with %s or %s' % (sUrl, mUrl)
                    )
            return path
    
    def get(self, request, *args, **kwargs):
        try:
            inventarios = Inventory.objects.all()  
            template = get_template('PDFS/pdfInve.html')
            context = {
                'inventarios': inventarios
            }

            html = template.render(context)
            
            response = HttpResponse(content_type='application/pdf')
            #response['Content-Disposition'] = 'attachment; filename="reporte de actividades.pdf"'
            pisa_status = pisa.CreatePDF(
                 html, dest=response,
                 link_callback=self.link_callback
                 )
         
            if pisa_status.err:
                return HttpResponse('We had some errors <pre>' + html + '</pre>')
            
            return response
        except Exception as e:
            print(f"Error: {e}")
            return HttpResponse('Error al generar el PDF')
