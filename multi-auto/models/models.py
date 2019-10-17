from odoo import api, models, fields, registry
import logging

_logger = logging.getLogger(__name__)

class product_template(models.Model):

    _inherit = 'product.template'

    pos_categ_ids = fields.Many2many('pos.category', string='POS Categories')
    is_related = fields.Boolean(string="related product",  )

    @api.onchange('available_in_pos','is_related')
    def _onchange_is_related(self):
        if self.is_related == True:
            print('ssssssssssssssssssss')
            self.available_in_pos = True

    @api.multi
    def related_button(self):
        for record in self:
            record.is_related = not record.is_related
