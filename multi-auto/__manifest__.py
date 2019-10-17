# -*- coding: utf-8 -*-
{
    'name': "multi pos category",

    'summary': """
        add multiple POS categories on the same product""",

    'description': """
It's very suitable for accessories that works on multiple type of product which have a categories    """,

    'author': "Mohamed Fouad",
    'website': "https://www.linkedin.com/in/mohamed-fouad1995/",
    'application': True,

    'price': '20',
    "currency": 'USD',
    "license": "OPL-1",
    'post_init_hook': '_auto_clean_cache_when_installed',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Point of Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','point_of_sale','stock'],
    'images': ['static/description/banner.png'],


    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
                
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
