# -*- coding: utf-8 -*-
{
    'name': "pos_custom_buttons",
    'summary': """ """,
    'description': """ """,
    'author': "Me",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'point_of_sale'],
    'data': [
        # 'views/pos_template.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'pos_custom_buttons/static/src/js/pos_product_button.js',
        ],
    },
}
