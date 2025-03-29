from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = "sale.order"

    residuos_a_recolectar_ids = fields.Many2many(
        comodel_name="residuo.catalogo",
        string="Residuos a recolectar",
        help="Selecciona los residuos que serán recolectados en esta orden de venta."
    )
