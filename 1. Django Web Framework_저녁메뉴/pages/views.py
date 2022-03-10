from django.shortcuts import render

# Create your views here.
def throw(request):
    return render(request, 'throw.html')

def dinner(request):
    menu = request.GET.get('menu')
    people = request.GET.get('people')
    context = {
        'menu': menu,
        'people': people,
    }
    return render(request, 'dinner.html', context)
