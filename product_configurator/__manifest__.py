{
    "name": "Product Configurator",
    "version": "13.0.1.0.0",
    "category": "Generic Modules/Base",
    "summary": "Base for product configuration interface modules",
    "author": "Pledra",
    "license": "AGPL-3",
    "website": "http://www.pledra.com/",
    "depends": ["account", "stock"],
    "data": [
        "security/configurator_security.xml",
        "data/menu_configurable_product.xml",
        "data/product_attribute.xml",
        "data/ir_sequence_data.xml",
        "data/ir_config_parameter_data.xml",
        "security/ir.model.access.csv",
        "views/assets.xml",
        "views/product_view.xml",
        "views/product_attribute_view.xml",
        "views/product_config_view.xml",
        "wizard/product_configurator_view.xml",
    ],
    "demo": [
        "demo/product_template.xml",
        "demo/product_attribute.xml",
        "demo/product_config_domain.xml",
        "demo/product_config_lines.xml",
        "demo/product_config_step.xml",
        "demo/config_image_ids.xml",
    ],
    "images": ["static/description/cover.png"],
    "post_init_hook": "post_init_hook",
    "qweb": ["static/xml/create_button.xml"],
    "installable": True,
    "application": True,
    "auto_install": False,
}
