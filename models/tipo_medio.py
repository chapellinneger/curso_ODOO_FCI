# -*- coding: utf-8 -*-

from openerp.osv import osv, fields


class tipo_medio(osv.osv):
	"""docstring for ClassName"""
	_name = 'co.tipo.medio'
	_description = 'CO Tipo Medio'
	_rec_name = 'nombre'

	_columns = {
		'nombre': fields.char('Nombre'),
	}

tipo_medio()