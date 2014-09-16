# -*- coding: utf-8 -*-

from openerp.osv import osv, fields

tipos_suscripcion = [
	('oro','Plan Oro'),
	('plata', 'Plan Plata'),
	('bronce','Plan Bronce')
]
class suscripcion(osv.osv):
	"""Esta clase se  relaciona con  la clase de suscriptor"""
	_name = 'co.suscripcion'
	_description = 'CO suscripcion'

	_columns = {
		'codigo': fields.char('Código'),
		'tipo': fields.selection(tipos_suscripcion,'Tipos de Suscripción'),
		'fecha_inicio': fields.date('Inicio Suscripción'),
		'fecha_fin': fields.date('Fin Suscripción'),
		'activo': fields.boolean('activo'),
		'suscriptor_id': fields.many2one('co.subcriptor','Afiliado'),
	}

suscripcion()	