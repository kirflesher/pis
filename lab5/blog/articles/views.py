from .models import Article
from django.shortcuts import render, redirect
from django.http import Http404

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



# Create your views here.
