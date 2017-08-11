# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Romain Deheele
#    Copyright 2015 Camptocamp SA
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from odoo import models, fields, api


class crm_lead(models.Model):
    """Add third field in lead address"""

    _inherit = "crm.lead"

    @api.multi
    def _lead_create_contact(self, name, is_company, parent_id=False):

        context = self.env.context.copy()

        partner = (
            super(crm_lead, self.with_context(context))._lead_create_contact(
                name, is_company, parent_id=parent_id,
            )
        )

        partner.with_context(context).write({'street3': self.street3})

        return partner

    street3 = fields.Char('Street 3')

    def _onchange_partner_id_values(self, partner_id):

        context = self.env.context.copy()

        res = (
            super(crm_lead, self.with_context(context)).
            _onchange_partner_id_values(partner_id)
        )

        if partner_id:
            partner = self.env['res.partner'].with_context(context).browse(
                partner_id
            )
            res.update({'street3': partner.street3})

        return res
