from main.models import Content


def my_context_processor(request):
    # Здесь вы можете выполнить любые вычисления или получить данные, которые вы хотите передать в шаблон
    content = Content.objects.first()



    return {
        'content': content,

    }