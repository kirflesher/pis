from .models import Article
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Представление для вывода всех статей в архиве
def archive(request):
    # Получаем все статьи и передаём их в шаблон archive.html
    return render(request, 'archive.html', {"posts": Article.objects.all()})

# Представление для отображения отдельной статьи по её ID
def get_article(request, article_id):
    try:
        # Пытаемся получить статью с указанным ID
        post = Article.objects.get(id=article_id)
        # Если успешно, рендерим страницу article.html с данной статьёй
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        # Если статьи с таким ID нет, возвращаем ошибку 404
        raise Http404

def create_post(request):
    # Проверяем, что пользователь авторизован
    if not request.user.is_anonymous:
        # Если метод запроса POST (форма отправлена)
        if request.method == "POST":
            # Получаем данные из формы
            form = {
                'text': request.POST["text"],
                'title': request.POST["title"]
            }
            # Проверяем, что поля заполнены
            if form["text"] and form["title"]:
                # Проверяем уникальность названия статьи
                if Article.objects.filter(title=form["title"]).exists():
                    # Если статья с таким названием есть, возвращаем ошибку
                    form['errors'] = "Такая статья уже существует!"
                    return render(request, "create_post.html", {"form": form})
                # Создаём новую статью
                article = Article.objects.create(
                    text=form["text"],
                    title=form["title"],
                    author=request.user
                )
                # Перенаправляем на страницу новой статьи
                return redirect("get_article", article_id=article.id)
            else:
                # Если не все поля заполнены, выдаём ошибку
                form['errors'] = "Заполните все поля!"
                return render(request, "create_post.html", {"form": form})
        else:
            # Если запрос GET, просто показываем пустую форму
            return render(request, "create_post.html", {})
    else:
        # Если пользователь не авторизован, возвращаем ошибку 404
        raise Http404

def register(request):
    # Проверяем тип запроса: если это POST, работаем с данными формы
    if request.method == "POST":
        # Получаем данные из присланной формы
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        #Проверка на заполненность всех полей
        if not (username and email and password and confirm_password):
            # Если хотя бы одно поле пустое, выводим ошибку и возвращаем заполненные поля
            return render(request, 'register.html', {
                'error': 'Заполните все поля!',
                'username': username,
                'email': email,
            })
        #Проверка совпадения паролей
        if password != confirm_password:
            # Если пароли не совпадают, выводим ошибку и возвращаем заполненные поля
            return render(request, 'register.html', {
                'error': 'Пароли не совпадают!',
                'username': username,
                'email': email,
            })
        #Проверка уникальности имени пользователя
        try:
            # Пробуем найти пользователя с таким именем
            User.objects.get(username=username)
            # Если найден, показываем ошибку и очищаем поле имени
            return render(request, 'register.html', {
                'error': 'Пользователь с таким именем уже существует!',
                'username': '',
                'email': email,
            })
        # Если не найден, продолжаем регистрацию
        except User.DoesNotExist:
            #Создание нового пользователя
            user = User.objects.create_user(username, email, password)
            # Аутентифицируем и сразу логиним нового пользователя
            user = authenticate(username=username, password=password)
            login(request, user)
            # Перенаправляем на страницу архива
            return redirect('archive')
    # Если GET-запрос, просто показываем форму регистрации
    return render(request, 'register.html')

def user_login(request):
    # Проверяем, был ли отправлен POST-запрос (пользователь отправил форму)
    if request.method == "POST":
        # Получаем имя пользователя и пароль из формы
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Проверка: оба поля должны быть заполнены
        if not (username and password):
            # Если хотя бы одно из полей пустое, возвращаем ошибку и введённые значения
            return render(request, 'login.html', {
                'error': 'Заполните все поля!',
                'username': username,
            })

        # Аутентификация пользователя по введённым данным
        user = authenticate(username=username, password=password)
        if user is not None:
            # Если данные верны, авторизуем пользователя и переходим на главную
            login(request, user)
            return redirect('archive')
        else:
            # Если данные неверны, возвращаем ошибку
            return render(request, 'login.html', {
                'error': 'Неверное имя пользователя или пароль!',
                'username': username,
            })

    # Если GET-запрос — просто показываем страницу входа
    return render(request, 'login.html')

def user_logout(request):
    # Разлогиниваем пользователя
    logout(request)
    # Перенаправляем на главную страницу
    return redirect('archive')


# Create your views here.
