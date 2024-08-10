from .mytools import *
from django.template import loader
from django.http import HttpResponse
from .forms import *
import shutil

def main(request):
    template = loader.get_template("Home/home.html")
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            projectName = form.cleaned_data['projectName']
            if checkAvailability(projectName):
                print("Available")
            else:
                system(f"django-admin startproject {projectName}")
                
            chdir(projectName)
            system("py manage.py makemigrations")
            system("py manage.py migrate")
            # system("py manage.py createsuperuser")
            
            system("py manage.py startapp Home") if not checkAvailability("Home") else print("file available")
            system("py manage.py startapp Users") if not checkAvailability("Users") else print("file available")
            
            chdir("Home")
            HomeFiles = ['urls.py', 'forms.py']
            FileCreation(HomeFiles)
            system("mkdir templates")
            chdir("templates")
            system("mkdir Home")
            chdir("../..")
            
            
            #user directories
            chdir("Users")
            Userfiles = ['forms.py', 'urls.py']
            FileCreation(Userfiles)
            system("mkdir templates")
            chdir("templates")
            system("mkdir Users")
            chdir("../..")
            
            #settings
            chdir(f"./{projectName}")
            settings_path = "./settings.py"
            url_path = './urls.py'
            
            insertions = {
                'django.contrib.staticfiles': '\t"Home.apps.HomeConfig",\n\t"Users.apps.UsersConfig"\n',
                'django.middleware.clickjacking.XFrameOptionsMiddleware': "\t'whitenoise.middleware.WhiteNoiseMiddleware',\n",
                'STATIC_URL': "\nSTATIC_ROOT = BASE_DIR / 'staticfiles'\n\nMEDIA_URL = '/media/'\n\nimport os\nMEDIA_ROOT = os.path.join(BASE_DIR, 'media')\n\n"
            }
            
            insertions2 = {
                'admin.site.urls': 'path("", include("Home.urls")),\n\tpath("", include("Users.urls"))\n',
                ']': 'if settings.DEBUG:\n\turlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)\n',
                'from django.urls import path': 'from django.conf import settings\nfrom django.conf.urls.static import static\nfrom django.urls import include\n'
            }
            
            append_line(settings_path, insertions)
            append_line(url_path, insertions2)
            
            # Create a zip file of the project
            chdir("../..")
            shutil.make_archive(projectName, 'zip', projectName)
            
            # Serve the zip file for download
            zip_file_path = f"{projectName}.zip"
            # Open the zip file in binary read mode
            with open(zip_file_path, 'rb') as zip_file:
                # Read the content of the zip file
                response = HttpResponse(zip_file.read(), content_type='application/zip')
                 # Set the content disposition to attachment, so the file is downloaded
                response['Content-Disposition'] = f'attachment; filename="{zip_file_path}"'
                return response
        
        #activate
        system(f"rmdir /s {projectName}")
            

            
    else:
        form = ProjectForm()
    context = {
        'form': form
    }
    return HttpResponse(template.render(context, request))
        