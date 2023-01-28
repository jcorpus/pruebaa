from django.shortcuts import render, HttpResponse

# Create your views here.

#Cada vista se corresponde con una función del fichero views.py
#request es una peticion y contiene mucha informacion.


html_base = """ 
    <h1>Mi web personal </h1>
    <ul>
        <li><a href="/">Portada</a></li>
        <li><a href="/about/">Acerca de</a></li>
        <li><a href="/portafolio/">Portafolio</a></li>
        <li><a href="/contact/">Contacto</a></li>
    <ul>
 """

def home(request):
    return render(request, "core/index.html")
    # return HttpResponse(html_base + """ 
    # <h2>Bienvenidos<h2/>
    # <p> Esto es la portada Portadaaaa</p> """)
    
    # html_response = "<h1>Mi web personal</h1>"
    # for i in range(10):
    #     html_response = html_response + "<p>Esto es la portada</p>" 
    # return HttpResponse(html_response)

    
def about(request):
    return render(request, "core/about.html")
    # return  HttpResponse( html_base+ """ 
    #     <h2>Acerca de </h2>
    #     <p>Me llamo Julio y ando aprendiendo :D</p> 
    # """  )


def portafolio(request):
    return render(request, "core/portafolio.html")


def contact(request):
    return render(request, "core/contact.html")
