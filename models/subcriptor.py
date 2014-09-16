# -*- coding: utf-8 -*-

from openerp.osv import osv, fields


class subcriptor(osv.osv):
	_name = 'co.subcriptor'
	_description = 'CO Subcriptor'

	_columns = {
		'nombre_subcritor': fields.char('Nombre y apellido Subcriptor'),
		'cedula':fields.char('Cédula de Identidad'),
		'direccion': fields.text('dirección del Subcriptor')
	}

subcriptor()