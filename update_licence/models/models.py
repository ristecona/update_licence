# -*- coding: utf-8 -*-
from time import gmtime, strftime
from odoo import models, fields, api
import datetime
import logging
_logger = logging.getLogger(__name__)
class UpdateLicence(models.Model):
	_inherit = 'ir.config_parameter'
	_name='ir.config_parameter'

	@api.multi
	def _update_licence(self):
		from datetime import datetime
		from dateutil.relativedelta import relativedelta

		now = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
		
		exp = datetime.today()+ relativedelta(months=1)
		
		keys = self.env['ir.config_parameter'].search([])
		
		
		for key in keys:
			if key.key=='database.create_date':
				key.value = now
				
			if key.key=='database.expiration_date':
				key.value = exp


		return True