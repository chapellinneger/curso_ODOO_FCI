# -*- coding: utf-8 -*-

from openerp.osv import osv, fields


class categoria(osv.osv):
	"""docstring for categoria"""
	_name = 'co.categoria'
	_description = 'CO Categoria'
	_rec_name = 'nombre'

	_columns = {
		'nombre': fields.char('Nombre', required="true"),
		'descripcion': fields.text('Descripción'),
		'parent_id' :fields.many2one('co.categoria','Padre'),
		'child_ids': fields.one2many(
			'co.categoria',
			'parent_id', 
			'Sub-categoría'),
	}

categoria()