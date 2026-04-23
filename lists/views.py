from django.shortcuts import render
from lists.models import Item

def home_page(request):
    if request.method == 'POST':
        text = request.POST.get('item_text', '').strip()

        if text:  # só salva se tiver conteúdo
            Item.objects.create(text=text)

        return render(request, 'lists/home.html', {
            'new_item_text': text
        })

    return render(request, 'lists/home.html')