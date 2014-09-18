# -*- coding: utf-8 -*-

from openerp.osv import osv, fields


class subcriptor(osv.osv):
	_name = 'co.subcriptor'
	_description = 'CO Subcriptor'
	_rec_name = 'nombre_subcritor'

	_columns = {
		'nombre_subcritor': fields.char('Nombre y apellido Suscriptor', required="true"),
		'cedula':fields.char('Cédula de Identidad', required="true"),
		'direccion': fields.text('Dirección del Suscriptor', required="true")
	}

	_sql_constraints = [
		('cedula_unique','unique(cedula)',
			u'El Número de cédula ya existe!!!'),
	]

subcriptor()