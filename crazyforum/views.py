from django.http.response import JsonResponse
from django.db.models.functions import Extract
from django.http import HttpResponse
from django.template import loader
from crazyforum.models import Post


def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render({"posts_count": Post.objects.count()}, request))

def login(request):
    template = loader.get_template("hackers.html")
    return HttpResponse(template.render())

def register(request):
    template = loader.get_template("hackers.html")
    return HttpResponse(template.render())

def posts_on(request):
    parameter = request.GET.get('scale')
    if parameter == None:
        return JsonResponse({"message": "Need parameter 'scale'"}, status=400)
    
    # Our super safe function to split dates based on the parameter
    truncated = Extract('publish_date', parameter)
    
    posts = Post.objects.annotate(formatted_date=truncated)
    rendered_posts = []
    for p in posts:
        post = {}
        post["title"] = p.title
        post["content"] = p.content
        post["formatted_date"] = p.formatted_date
        try:
            post["author"] = p.author.username
        except:
            post["author"] = "Anonymous"
        rendered_posts.append(post)
        
    return JsonResponse({"posts": rendered_posts})