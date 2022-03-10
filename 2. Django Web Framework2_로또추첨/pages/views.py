import random
from django.shortcuts import render

# Create your views here.
def lotto(request):
    lotto = random.sample(range(1, 46), 6)
    context = {'lotto': lotto}        
    return render(request, 'lotto.html', context)


