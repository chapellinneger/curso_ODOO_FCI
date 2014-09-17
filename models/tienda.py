# -*- coding: utf-8 -*-

from openerp.osv import osv, fields


class tienda(osv.osv):
	"""docstring for tienda"""
	_name = 'co.tienda'
	_description = 'CO tienda'
	_rec_name = 'nombre'

	_columns = {
		'nombre': fields.char('Tienda', required="true"),
		'direccion':  fields.char('Dirección')
	}

tienda()