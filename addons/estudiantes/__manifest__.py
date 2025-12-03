# -*- coding: utf-8 -*-
{
    'name': "Estudiantes",

    'summary': "Tarea 15 del módulo de SXE",

    'description': """
Ejercicio que nos pide crear nuestro propio modulo en odoo centrandonos en unos
estudiantes y el nivel de sueño que tienen y cuanta cafeina necesitan
    """,

    'author': "Oliver Miguez Alonso",
    'website': "https://www.olivermiguez.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

