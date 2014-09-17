# -*- coding: utf-8 -*-

from openerp.osv import osv, fields


class solicitud(osv.osv):
	"""docstring for solicitud"""
	_name = 'co.solicitud'
	_description = 'CO Solicitud'
	_rec_name = 'codigo'

	_columns = {
		'suscriptor_id': fields.many2one('co.subcriptor', 'Suscriptor'),
		'multimedia_id': fields.many2one('co.multimedia','Multimedia'),
		'medio_id': fields.many2one('co.tipo.medio', 'Medio'),
		'tienda_id': fields.many2one('co.tienda','Origen'),
		'fecha_solicitud': fields.date('Fecha Solicitada'),
		'duracion_dia': fields.integer('Duración de Dias'),
		'codigo': fields.char('Código de la solicitud'),
	}


solicitud()