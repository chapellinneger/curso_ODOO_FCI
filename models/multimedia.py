# -*- coding: utf-8 -*-

from openerp.osv import osv, fields


class multimedia(osv.osv):
	"""docstring for multimedia"""
	_name = 'co.multimedia'
	_description = 'CO Multimedia'
	_rec_name = 'titulo'
	_order = 'fecha_publicacion desc'

	_columns = {
		'titulo': fields.char('Título', required="true"),
		'fecha_publicacion': fields.date('Fecha de publicación'),
		'codigo': fields.char('Código'),
		'categoria_id': fields.many2one('co.categoria', 'Categoria'),
		'medio_ids': fields.many2many(
			'co.tipo.medio',
			'co_multimedia_medio_rel',
			'multimedia_id',
			'medio_id'),
	}


multimedia()