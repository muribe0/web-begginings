# Web Applications

Software that runs on a web server such that users make request to the server, the server process the request and sends data back.

## GET

The most common method used to retrieve data from a server. It is used to request data from a specified resource.

## Codes

| Number | Meaning           |
|--------|-------------------|
| 200    | OK                |
| 301    | Moved Permanently |
| 403    | Forbidden         |
| 404    | Not Found         |
| 500    | Internal Server Error |

## Set-Up Django
1. Create a virtual environment `python3 -m venv <env_name>` in Django folder
2. Activate the virtual environment `source <env_name>/bin/activate` This activates our script folder
3. Install Django in your pc `pip3 install Django` 
4. Create a django project `django-admin startproject <project_name>`. Django creates some starter files for us
   * `__init__.py` - Tells python that this is a package
   * `settings.py` - Contains all the settings for the project
   * `urls.py` - Contains all the urls for the project
   * `wsgi.py` - Web Server Gateway Interface
   * `asgi.py` - Asynchronous Server Gateway Interface
   * `manage.py` - Used to run commands for the project

Anytime you want to run the project:
1. You run `Scripts/activate` to activate the virtual environment from the <env_name> folder. (my_venv)
2. you run `python3 manage.py runserver` in <project_name> folder. (lecture3)

### Create an App
One project tends to have several different apps.

1. Create an app `python3 manage.py startapp <app_name>`. This creates a folder with the app name
2. Add the app to the project in the `settings.py` file in the `INSTALLED_APPS` list:
   ```python
   # Application definition
   
   INSTALLED_APPS = [
   '<app_name>', # <--- here goes the <app_name> (hello)
   'django.contrib.admin',
   'django.contrib.auth',
   'django.contrib.contenttypes',
   'django.contrib.sessions',
   'django.contrib.messages',
   'django.contrib.staticfiles',
   ]
   ```
4. Create a view in the app folder in the `views.py` file:
   * Something the users can see
   * First view we will create in the example is:
    ```python
    from django.http import HttpResponse
    def index(request):
        return HttpResponse("Hello, world.")
    ```
   * `HttpResponse`: An HttpResponse object in Django represents the response that a Django view sends back to the client. This response consists of the content that will be displayed to the user, along with metadata such as HTTP headers. The primary purpose of an HttpResponse is to encapsulate the HTTP response data, allowing you to customize what is returned to the user. You can specify the content, status code, and headers of the response
   * `index()` is a function that takes a request and returns a response.
   * We will need to map this view to a URL so that users can access it.
5. Inside the `<app_name>` folder, we will create an `url.py` directory. This file will contain the URL patterns for the app.
   * Create a file called `urls.py` in the `<app_name>` folder
   * Add the following code to the `urls.py` file:
    ```python
    from django.urls import path
    from . import views 

    urlpatterns = [ # <--- name here is important!
        path('', views.index, name='index'),
    ]
    ```
   * `path()`: This function is used to map URLs to views. It takes three arguments:
   * `route`: A string that contains a URL pattern. When a user requests a URL, Django will use this pattern to match the requested URL.
   * `view`: The view function that Django should call when the URL pattern is matched.
   * `name`: A unique name for the URL pattern. This is used to identify the URL pattern in the project.
   * `from . import view` imports the view function from the current folder or package.


6. We need to include the app's URL patterns in the project's URL patterns. This is done in the `urls.py` file in the `<name_project>` folder. (lecture3)
   * Add the following code to the `urls.py` file in the project folder:
    ```python
    from django.contrib import admin
    from django.urls import include, path # <---- need to add include 

    urlpatterns = [
        path('hello/', include('hello.urls')), # <---- need to add this line where hello is the <app_name>
        path('admin/', admin.site.urls),
    ]
    ```
   * `include()`: This function is used to include URL patterns from other apps. It takes two arguments:
   * `module`: The module containing the URL patterns to include.
   * `namespace`: An optional argument that allows you to specify a namespace for the included URL patterns.


   * In summary, when someone visits a web address that starts with hello/, Django should not decide what to do by itself. 
   * Instead, Django should look inside a separate file named hello.urls to find out what to do next. 
   * This setup helps keep things organized, especially when your website grows bigger, by letting each part of your website (each app) handle its own web addresses.


So `urls.py` in the <app_name> contains the urls for that particular <app_name>.
While `urls.py` in the <project_name> contains the urls for the entire project.

7. Now, we can run the server with `python3 manage.py runserver` and visit `http://127.0.0.1:8000/hello/` will show the message `Hello, world.` as specified in the app view `'hello'`.
   * Try changing how the view works in the `views.py` file in the app folder and see the changes in the browser. 

8. Add a new function to try:
   * Add a new function to the `views.py` file in the `<app_name>` folder:
    ```python
    def greet(request, name):
        return HttpResponse(f"Hello, {name.capitalize()}.")
    ``` 
   * Add a new path to the `urls.py` file in the `<app_name>` folder (hello):
    ```python
    path('<str:name>/', views.greet, name='greet'),
    ```
   where `<str:name>` is a path converter that captures the value in the URL and passes it to the view function as an argument `greet(_,name)`. So it passes as `name` arguement. This in turn, makes the page show whatever is after the `/` in the URL.
   * For example, given `http://127.0.0.1:8000/hello/Mau`, the page will show `Hello, Mau.`
   * So instead of hardcoding the name in the view, we can pass it as an argument in the URL.

> For today (day 3) we are done.

-- Day 4 begins here --

## Templates

Separate the response "the html" from the python code. Instead of returning a HttpResponse,
we can return a render function that takes the request, the template file, and a dictionary
of variables to pass to the template.

1. Create a folder called `templates` in the `<app_name>` folder.
2. Create a file called `index.html` in the `templates` folder.
3. Add the following code to the `index.html` file:
   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta http-equiv="X-UA-Compatible" content="IE=edge">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Hello</title>
   </head>
   <body>
       <h1>Hello, world.</h1>
   </body>
   </html>
   ```
4. Update the `index()` function in the `views.py` file in the `<app_name>` folder to use the template:
   ```python
   from django.shortcuts import render
   def index(request):
       return render(request, 'hello/index.html') # <--- this is the change as opposed to httmlresponse
   ``` 
   
    * `render()`: This function is used to render a template with the given context. It takes three arguments:
    * `request`: The request object that represents the current HTTP request.
    * `template_name`: The name of the template file to render.
    * `context`: A dictionary containing the variables to pass to the template.
    * The `render()` function loads the template file `hello/index.html` and returns an `HttpResponse` object with the rendered template content.

### Another Example
1. Create a new file called `greet.html` in the `templates` folder.
2. Add the following code to the `greet.html` file:
   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta http-equiv="X-UA-Compatible" content="IE=edge">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Greet</title>
   </head>
   <body>
       <h1>Hello, {{ name }}.</h1>
   </body>
   </html>
   ```
   
    * `{{ name }}`: This is a template variable that displays the value of the `name` variable passed to the template.
3. Update the `greet()` function in the `views.py` file in the `<app_name>` folder to use the template:
   ```python
   def greet(request, name):
       return render(request, 'hello/greet.html', {
           'name': name,
       })
   ```
   
    * The `render()` function loads the template file `hello/greet.html` and passes the `name` variable to the template. The `name` variable is displayed in the template using the `{{ name }}` template variable.
    * The `name` variable is passed to the template as a key-value pair in a dictionary. The key is the name of the variable in the template, and the value is the value of the variable.
    * `render()` returns an `HttpResponse` object with the rendered template content.
    

### Another Example

1. We will create a new app: `python manage.py startapp newyear`
2. Add it to the installed apps in `settings.py` in the project folder.
3. Add `urls.py` to the new app folder and add the following code:
   ```python
   from django.urls import path
   from . import views

   urlpatterns = [
       path('', views.index, name='index'),
   ]
   ```
4. Create a `views.py` file in the new app folder and add the following code:
   ```python
    from django.shortcuts import render
    from datetime import datetime
    def index(request):
        now = datetime.now()
        return render(request, "newyear/index.html", {
            "newyear": now.month == 1 and now.day == 1 # This will return True if the current month is January and the current day is the first day of the month
        })
   ```
5. Create a `templates` folder in the new app folder.
6. Create an `index.html` file in the `templates` folder and add the following code:
   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta http-equiv="X-UA-Compatible" content="IE=edge">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>New Year</title>
   </head>
   <body>
       {% if newyear %}
           <h1>Happy New Year!</h1>
       {% else %}
           <h1>Not New Year Yet</helse>
       {% endif %}
   </body>
   </html>
   ```
   
    * `{% if newyear %}`: This is a template tag that checks if the `newyear` variable is `True`. If it is `True`, the content inside the `{% if %}` block is displayed. If it is `False`, the content inside the `{% else %}` block is displayed.
    * `{% endif %}`: This is a template tag that marks the end of the `{% if %}` block.

7. Add the new app's URL patterns to the project's URL patterns in the `urls.py` file in the project folder
   ```python
   urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include('hello.urls')), # This is a path that will be used to access the hello app
    path('newyear/', include('newyear.urls')), # This is a path that will be used to access the newyear app
    ]
    ```
   
### Another example

