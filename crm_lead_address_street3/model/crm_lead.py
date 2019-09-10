# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class CrmLead(models.Model):
    """Add third field in lead address"""

    _inherit = "crm.lead"

    @api.multi
    def _create_lead_partner_data(self, name, is_company, parent_id=False):

        ret = super(CrmLead, self)._create_lead_partner_data(
            name, is_company, parent_id=parent_id,
        )

        ret.update({'street3': self.street3})

        return ret

    street3 = fields.Char('Street 3')

    def _onchange_partner_id_values(self, partner_id):

        res = super(CrmLead, self)._onchange_partner_id_values(partner_id)

        if partner_id:
            partner = self.env['res.partner'].browse(partner_id)
            res.update({'street3': partner.street3})

        return res
