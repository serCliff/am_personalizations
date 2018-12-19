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
        
        FACTURAS
            - Cambia css de las facturas para tener los colores de audiomedical
            - Cambia foto de fondo para poner el logo de audiomedical
            - Cambia texto de la factura Saldo por Saldo pendiente
        
        MARGENES SOBRE VENTAS
            - Definir
            
        CLIENTES
            - Definir
            
        PERMISOS
            - Definir
        
        
    """,

    'author': "Sergio Del Castillo Baranda",
    'website': "http://www.sergiodelcastillo.com",

    'category': 'Sales',
    'version': '0.1',

    'depends': ['sale', 'web_digital_sign'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/sale_order.xml',
        'views/res_partner.xml',
    ],

}