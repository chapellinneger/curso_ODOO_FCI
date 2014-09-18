# -*- coding: utf-8 -*-

from openerp.osv import osv, fields


class multimedia(osv.osv):
	"""docstring for multimedia"""
	_name = 'co.multimedia'
	_description = 'CO Multimedia'
	_rec_name = 'titulo'
	_order = 'fecha_publicacion desc'

	def _compute_stock(self, cr, uid, ids, fields_name, arg, context):
		stock_obj = self.pool.get('co.linea.stock')
		if isinstance(ids, (int,long)):
			ids = [ids]
		res = {}
		for i in ids:
			lineas_ids = stock_obj.search(cr,uid,[
				('multimedia_id','=', i),])
			lineas_brw = stock_obj.browse(cr,uid,lineas_ids)
			res[i] = sum([l.cantidad for l in lineas_brw])

		return res


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
		'stock':fields.function(_compute_stock,type='integer')
	}


multimedia()