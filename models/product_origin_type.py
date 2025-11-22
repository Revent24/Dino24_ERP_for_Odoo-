# product_origin_type.py
# МОДЕЛЬ ПРОИСХОЖДЕНИЕ ТОВАРА
# (используется как выпадающий список в Категории товара)
#
# -*- coding: utf-8 -*-
from odoo import models, fields

class DinoOriginType(models.Model):
    _name = 'product.origin.type'
    _description = 'Тип Происхождения Товара'
    _order = 'name'

    name = fields.Char(string="Название типа", required=True)
    
    code = fields.Char(
        string="Технический код", 
        required=True, 
        help="Уникальный код для использования в Python-логике (например, 'purchase', 'service').",
    )
    
    _sql_constraints = [
        ('code_unique', 'unique(code)', 'Технический код должен быть уникальным!'),
    ]