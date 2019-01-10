# -*- coding: utf-8 -*-
{
    'name': "Am Personalizations",

    'summary': """
        Modificaciones para adaptar odoo a la empresa audiomedical
        """,

    'description': """
        Multitud de modificaciones para adaptar en términos generales odoo para la empresa audiomedical
        
        PEDIDOS
            - Elimina opciones de facturacion en pedidos, directamente factura.
            - Modifica la extensión de los presupuestos al ser confirmados PRE -> PV
            - Al registrar el pago final de una factura valida el albarán de salida si es posible
            - Modifica dominio presupuestos a únicamente presupuestos
        
        PERMISOS
            - Comercial: Bloqueo de edicion de productos, pedidos y facturas (en estados sensibles)
            - Recepcion, Responsable, Director: Únicamente tiene heredados permisos necesarios.
        
        # TODO
        
        FACTURAS
            - Cambia css de las facturas para tener los colores de audiomedical
            - Cambia foto de fondo para poner el logo de audiomedical
            - Cambia texto de la factura Saldo por Saldo pendiente
        
        MARGENES SOBRE VENTAS
            - Definir
            
        CLIENTES
            - Definir
            
        
        
        
    """,

    'author': "Sergio Del Castillo Baranda",
    'website': "http://www.sergiodelcastillo.com",

    'category': 'Sales',
    'version': '0.2',

    'depends': ['sale',
                'stock',
                'sales_team',
                'point_of_sale',
                'account',
                'product',
                'purchase',
                'web_digital_sign',
                ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/audiomedical_security.xml',
        'views/commercial_permissions.xml',
        'views/sale_order.xml',
        'views/res_partner.xml',
        'views/res_users.xml',
        'views/purchase_order.xml',
    ],

}
