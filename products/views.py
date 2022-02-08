from django.shortcuts import render


def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'GeekShop - Продукты',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090,
             'text': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'},
            {'name': 'Синяя куртка The North Face', 'price': 23725,
             'text': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 3390,
             'text': 'Материал с плюшевой текстурой. Удобный и мягкий.'},
            {'name': 'Черный рюкзак Nike Heritage', 'price': 2340, 'text': 'Плотная ткань. Легкий материал.'},
            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': 13590,
             'text': 'Гладкий кожаный верх. Натуральный материал.'},
            {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': 2890,
             'text': 'Легкая эластичная ткань сирсакер Фактурная ткань.'},
        ],
    }
    return render(request, 'products/products.html', context)
