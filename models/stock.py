# -*- coding: utf-8 -*-

from openerp.osv import osv, fields


class lineas_stock(osv.osv):
	"""docstring for lineas_stok"""
	_name = 'co.linea.stock'
	_description = 'CO Stock'

	_columns = {
		'multimedia_id': fields.many2one('co.multimedia','Multimedia',required="true"),
		'medio_id': fields.many2one('co.tipo.medio','Medio',required="true"),
		'tienda_id':fields.many2one('co.tienda', 'Tienda'),
		'cantidad': fields.integer('Cantidad',required="true"),
	}

	def onchange_medio_id(self,cr,uid,ids,medio_id):
		return {
			'value' : {
				'multimedia_id': False,
				'cantidad': 0
			}
		}

	def _check_qty(self,cr, uid, ids, context=None):
		if isinstance(ids , (int,long)):
			ids = [ids]
		for s in self.browse(cr, uid, ids, context=context):
			if s.cantidad < 0:
				return False
		return True

	_constraints = [
		(_check_qty,'La Cantidad no puede ser negativa',['cantidad',])
	]

	_sql_constraints = [
		(	
			'medios_tienda',
			'unique(medio_id,tienda_id,multimedia_id)',
			u'Esta multimedia ya está presente es este medio'
		)
	]

lineas_stock()

class tienda(osv.osv):
	"""docstring for tienda"""
	_inherit = 'co.tienda'

	_columns = {
		'tienda_ids': fields.one2many(
			'co.linea.stock',
			'tienda_id',
			'stock'), 
	}

	def unlink(self, cr, uid, ids, context=None):
		if  isinstance(ids, (int,long)):
			ids = [ids]

		for e in self.browse(cr, uid, ids, context=context):
			tienda_ids = [l.id for l in e.tienda_ids]
			if self.pool.get('co.linea.stock').unlink(cr, uid, tienda_ids):
				if super(tienda,self).unlink(cr, uid, e.id, context=context):
					continue
			return False
		return True

tienda()