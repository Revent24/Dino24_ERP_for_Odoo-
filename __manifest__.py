#
# --- /dino_erp_stock/__manifest__.py ---
#

{
    'name': "Dino ERP Stock: Кастомный Склад",
    'summary': "Модуль для внедрения логики 'Склада' из презентации.",
    # ... остальные метаданные ...
    'version': '1.0',

    # ЗАВИСИМОСТИ
    'depends': [
        'base', # база
        'stock', # склад
        'mrp', # управление запасами
    ],

    # Файлы, которые будут загружены в базу при установке. Порядок важен!
    'data': [
 

    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}