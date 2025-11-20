{
    'name': "Dino ERP Stock: Кастомный Склад",
    'summary': "Модуль для внедрения логики 'Склада' из презентации.",
    # ... остальные метаданные ...
    'version': '1.0',

    # ОСТАВЛЯЕМ ТОЛЬКО ЭТОТ ОДИН БЛОК ЗАВИСИМОСТЕЙ
    'depends': [
        'base', 
        'stock',
        'mrp', # Убедитесь, что mrp действительно нужен вашему модулю
    ],

    # Файлы, которые будут загружены в базу при установке. Порядок важен!
    'data': [
        'security/ir.model.access.csv', 
        'views/product_template_view.xml', 
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}