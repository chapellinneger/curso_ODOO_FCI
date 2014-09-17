# -*- coding: utf-8 -*-

from openerp.osv import osv, fields
from datetime import datetime

tipos_suscripcion = [
	('oro','Plan Oro'),
	('plata', 'Plan Plata'),
	('bronce','Plan Bronce')
]
class suscripcion(osv.osv):
	"""Esta clase se  relaciona con  la clase de suscriptor"""
	_name = 'co.suscripcion'
	_description = 'CO suscripcion'
	_rec_name = 'codigo'

	_columns = {
		'codigo': fields.char('Código'),
		'tipo': fields.selection(tipos_suscripcion,'Tipos de Suscripción'),
		'fecha_inicio': fields.date('Inicio Suscripción'),
		'fecha_fin': fields.date('Fin Suscripción'),
		'activo': fields.boolean('activo'),
		'suscriptor_id': fields.many2one('co.subcriptor','Afiliado'),
	}

	_defaults = {
		'activo': True,
		'fecha_inicio': datetime.now().strftime('%Y-%m-%d'),
	}

	def create(self,cr,uid,values,context=None):
		if context is None:
			context = {}
		# esto sirve para llamar a cualquier meodo de OPENERP
		values.update({ 'codigo': 
			self.pool.get('ir.sequence').get(cr, uid, 'seq.suscripcion')})
		return super(suscripcion, self).create(cr,uid,values,context=context)

suscripcion()	