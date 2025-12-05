# Dino ERP: Склад (dino_erp_stock)

Модуль **dino_erp_stock** — расширение для Odoo, предназначенное для управления складской номенклатурой, компонентами, спецификациями (BOM) и параметрами продукции.

## Описание

Модуль автоматизирует процессы ведения складской номенклатуры, категорий и параметров компонентов, а также спецификаций сборки (BOM). Подходит для производственных и торговых предприятий, где требуется детализированный учет компонентов и их структуры.

## Основные возможности
- Ведение иерархии компонент и категорий
- Управление спецификациями (BOM) для продукции
- Хранение и настройка параметров компонентов
- Расширение стандартных моделей Odoo для работы с товарами и их атрибутами
- Локализация интерфейса (русский, украинский)
- Гибкая настройка прав доступа

## Структура модуля

```
dino_erp_stock/
├── __init__.py
├── __manifest__.py
├── SPECIFICATION.md
├── data/
│   └── ir_sequence_data.xml
├── i18n/
│   ├── ru.po
│   └── uk.po
├── models/
│   ├── __init__.py
│   ├── dino_bom.py
│   ├── dino_component_category.py
│   ├── dino_component.py
│   ├── dino_nomenclature.py
│   └── dino_parameter.py
├── security/
│   └── ir.model.access.csv
├── views/
│   ├── dino_component_category_views.xml
│   ├── dino_component_views.xml
│   ├── dino_nomenclature_views.xml
├── www/
│   ├── product_attribute_views.xml
│   ├── product_component_attribute.py
│   ├── product_component_bom_views.xml
│   ├── product_component_bom.py
│   ├── product_component_views.xml
│   ├── product_component.py
│   ├── product.template.md
│   ├── ru.po
│   └── uk.po
```

## Краткое описание моделей

- **dino.component.category** — категории компонентов (иерархия, фильтрация)
- **dino.component** — компоненты (товары, детали, полуфабрикаты)
- **dino.nomenclature** — номенклатура склада (основной справочник)
- **dino.bom** — спецификации сборки (BOM)
- **dino.parameter** — параметры компонентов (размеры, характеристики)

## Установка

1. Скопируйте модуль в директорию `addons` вашего Odoo:
   ```bash
   cp -r dino_erp_stock /path/to/odoo/addons/
   ```
2. Перезагрузите сервер Odoo:
   ```bash
   sudo systemctl restart odoo
   # или
   ./odoo-bin --reload-modules
   ```
3. Обновите список модулей и установите модуль через интерфейс Odoo или командой:
   ```bash
   odoo-bin -d database_name -i dino_erp_stock
   ```

## Использование

1. Перейдите в меню **Склад > Компоненты** для работы с компонентами
2. Используйте категории для группировки и фильтрации
3. Создавайте и редактируйте спецификации (BOM) для продукции
4. Настраивайте параметры компонентов для детального учета
5. Используйте переводы для работы на русском и украинском языках

## Права доступа
- **base.group_user** — чтение, создание, редактирование (без удаления)
- **stock.group_stock_manager** — полный доступ (включая удаление)

## Локализация
- Русский (ru.po)
- Украинский (uk.po)

## Зависимости
- `base` — базовый модуль Odoo
- `product` — товары
- `stock` — склад

## Авторство
Разработано командой **Revent24**

## Лицензия
LGPL-3
