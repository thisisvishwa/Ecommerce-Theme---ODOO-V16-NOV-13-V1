{
    "name": "ecommerce_theme_v1_nov_13",
    "version": "1.0",
    "category": "Theme/Ecommerce",
    "summary": "Ecommerce theme for selling gaming PCs, laptops, PC components, gaming consoles, and related products",
    "sequence": 1,
    "description": """
    This is an eCommerce website theme for selling gaming PCs, laptops, PC components, gaming consoles, and related products.
    """,
    "depends": ["base", "website_sale"],
    "data": [
        "views/product_template_views.xml",
        "views/website_templates.xml"
    ],
    "demo": [],
    "installable": True,
    "application": False,
    "auto_install": False,
    "qweb": ["static/src/xml/*.xml"],
    "css": ["static/src/css/theme.css"],
    "js": ["static/src/js/theme.js"],
    "images": ["static/description/icon.png", "static/description/index.html"],
    "external_dependencies": {
        "python": [],
        "bin": []
    }
}