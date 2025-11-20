from odoo import models, fields, api
from odoo.exceptions import UserError

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # --- Поля Себестоимости и Запасов ---
    
    calculated_cost = fields.Float(
        string="Расчетная себестоимость (BOM)",
        digits='Product Price',
        compute='_compute_cost_fields',
        store=True,
        help="Расчетная себестоимость на основе данных Спецификации (BOM). (Пока плоская логика)."
    )
    
    actual_cost = fields.Float(
        string="Фактическая себестоимость",
        digits='Product Price',
        help="Фактическая себестоимость, полученная из производственных заказов."
    )
    
    min_qty = fields.Float(
        string="Неснижаемый остаток (Dino)",
        help="Минимальное количество, включая аналоги, ниже которого генерируется запрос на закупку.",
    )
    
    qty_available_with_analogs = fields.Float(
        string="Доступно (с Аналогами)",
        compute='_compute_qty_with_analogs',
        store=True,
        digits='Product Unit of Measure',
        help="Суммарное количество в наличии (Qty Available) основного товара и всех его утвержденных аналогов."
    )
    
    purchase_required = fields.Boolean(
        string="Требуется закупка (Dino)",
        compute='_compute_purchase_required',
        store=True,
        search='_search_purchase_required',
        help="Отмечено, если суммарный запас (с аналогами) ниже неснижаемого остатка."
    )

    # --- Поля для Аналогов (Обновлено) ---
    
    # НОВЫЙ ФЛАГ: Управляет видимостью вкладки и домена
    apply_analogs = fields.Boolean(
        string="Применить аналоги",
        default=False,
        help="Отметьте, если для этого товара может быть утвержден список аналогов. "
             "Контролирует видимость вкладки и домен выбора."
    )
    
    # Старое поле 'is_analog' удалено.
    
    analog_ids = fields.Many2many(
        'product.template',
        'product_template_analog_rel',
        'template_id',
        'analog_id',
        string="Аналогичные товары",
        # ДОМЕН: 1. Товары той же категории. 2. Товары, которые сами не имеют аналогов.
        domain="['&', ('categ_id', '=', categ_id), ('apply_analogs', '=', False)]",
        help="Список товаров, которые могут быть использованы как аналоги."
    )
    
    # ----------------------------------------------------------------------------------------
    # ЛОГИКА РАСЧЕТА ЗАПАСОВ С АНАЛОГАМИ
    # ----------------------------------------------------------------------------------------
    
    @api.depends('qty_available', 'analog_ids.qty_available')
    def _compute_qty_with_analogs(self):
        """Рассчитывает суммарное количество основного товара и его утвержденных аналогов."""
        for product in self:
            total_qty = product.qty_available
            
            # Добавляем доступное количество всех утвержденных аналогов
            for analog in product.analog_ids:
                total_qty += analog.qty_available
                
            product.qty_available_with_analogs = total_qty

    # ----------------------------------------------------------------------------------------
    # ЛОГИКА КОНТРОЛЯ ЗАКУПОК
    # ----------------------------------------------------------------------------------------

    @api.depends('min_qty', 'qty_available_with_analogs')
    def _compute_purchase_required(self):
        """Проверяет, требуется ли закупка на основе суммарного запаса и неснижаемого остатка."""
        for product in self:
            # Проверка выполняется, только если товар использует аналоги И имеет установленный остаток
            if product.apply_analogs and product.min_qty > 0:
                # Требуется закупка, если суммарный запас ниже неснижаемого остатка
                product.purchase_required = product.qty_available_with_analogs < product.min_qty
            else:
                product.purchase_required = False

    def _search_purchase_required(self, operator, value):
        """Метод поиска для поля 'purchase_required'."""
        # (Оставлю здесь как заглушку, поскольку это сложный метод для реального использования в Odoo)
        return [(0, '=', 1)] 
            
    # ----------------------------------------------------------------------------------------
    # ЛОГИКА РАСЧЕТА СЕБЕСТОИМОСТИ (ПЛОСКАЯ ЛОГИКА)
    # ----------------------------------------------------------------------------------------
    
    @api.depends('bom_ids', 'bom_ids.bom_line_ids.product_id.standard_price')
    def _compute_cost_fields(self):
        """Временная плоская логика расчета себестоимости."""
        for product in self:
            if product.bom_ids:
                product.calculated_cost = sum(
                    line.product_id.standard_price * line.product_qty
                    for bom in product.bom_ids
                    for line in bom.bom_line_ids
                )
            else:
                product.calculated_cost = 0.0