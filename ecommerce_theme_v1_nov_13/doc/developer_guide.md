# Developer Guide

## Setup

1. Clone the repository containing the theme.
2. Navigate to the Odoo addons directory.
3. Create a symbolic link to the `ecommerce_theme_v1_nov_13` directory.

```bash
ln -s /path/to/ecommerce_theme_v1_nov_13 .
```

4. Restart the Odoo server.

## Module Installation

1. Navigate to the Apps menu in Odoo.
2. Remove the 'Apps' filter in the search bar.
3. Search for `ecommerce_theme_v1_nov_13`.
4. Click on Install.

## Code Structure

The codebase is structured as follows:

- `__init__.py`: Initializes the Python module.
- `__manifest__.py`: Contains metadata about the module.
- `models/`: Contains the Python models.
- `views/`: Contains the XML views.
- `static/src/js/theme.js`: Contains the JavaScript code for the theme.
- `static/src/css/theme.css`: Contains the CSS for the theme.
- `static/src/img/`: Contains the images used in the theme.
- `static/description/index.html`: Contains the module description.
- `doc/`: Contains the documentation.

## Custom Fields

Custom fields specific to gaming products are added in `models/product_template.py`. These fields are then used in `views/product_template_views.xml` to display on the product page.

## Error Handling

Error handling is implemented throughout the theme. Errors are linked to relevant modules for easy debugging. Refer to the code in `models/` and `static/src/js/theme.js` for more details.

## Custom Views

Custom views are defined in `views/website_templates.xml` and `views/product_template_views.xml`. These views are used to highlight product features.

## Theme Customization

The theme's color scheme and typography can be customized in `static/src/css/theme.css`.

## Deployment

1. Push the changes to the repository.
2. On the server, pull the latest changes.
3. Restart the Odoo server.
4. Upgrade the module from the Apps menu in Odoo.

For more details on managing the site, adding products, and customization, refer to the `user_guide.md`.