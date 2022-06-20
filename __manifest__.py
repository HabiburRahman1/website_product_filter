{
    'name': 'Advanced Product Filter',
    'description': """Advanced Product Filter help your customer to filter and choose products collection to save their time and fast.
	Your customer can view applied filters on top. You can display attibutes by category wise and display products count each of attribute. 
	Categorty Attrbutes, attribute groups , product feature , group features , Website Sale Category For Attribute ,Website Product Features , Product Filter , Product Attribute
	Attribute filter ,
	Category Attribute ,
	Horizontal Attributes Filters ,
	Advanced Variant Prices ,
	Product attributes categorized , 
    E-commerce filters 
	""",
    'summary': 'Website Product Filter',
    'category': 'Website',
    'version': '10.0.2.0',
    'license': 'OPL-1',
    'author': 'Atharva System',
    'website': 'https://www.atharvasystem.com/',
    'depends': ['website_sale', 'website'],
    'data': [
        'views/website_setting.xml',
        'views/product_view.xml',
        'views/product_filter_view.xml',
        'views/templates.xml',
        'security/ir.model.access.csv',
    ],
    'images': ['static/description/banner.png'],
    'support': 'support@atharvasystem.com',
    'installable': True,
    'price': 49.00,
    'currency': 'EUR',
    'application': True,

}
