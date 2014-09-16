# -*- coding: utf-8 -*-

from openerp.osv import osv, fields


class lineas_stock(osv.osv):
	"""docstring for lineas_stok"""
	_name = 'co.linea.stock'
	_description = 'CO Stock'

	_columns = {
		'multimedia_id': fields.many2one('co.multimedia','Multimedia'),
		'mendio_id': fields.many2one('co.tipo.medio','Medio'),
		'tienda_id':fields.many2one('co.tienda', 'Tienda'),
		'cantidad': fields.integer('Cantidad'),
	}

lineas_stock()

class tienda(osv.osv):
	"""docstring for tienda"""
	_inherit = 'co.tienda'

	_columns = {
		'liena_id': fields.one2many(
			'co.linea.stock',
			'tienda_id',
			'stock'), 
	}

tienda()