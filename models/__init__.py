# # --- dino_erp_stock/models/__init__.py ---

# 1. Загрузка новой модели 'product.origin.type'
from . import product_origin_type 

# 2. Загрузка Категории (product.category) - зависит от product_origin_type
from . import product_category 

# 3. Загрузка Товарного Шаблона (product.template) - зависит от product_category
from . import product_template