Introduction
============

Iconpicker widget for Plone based on http://victor-valencia.github.io/bootstrap-iconpicker/

![image](http://victor-valencia.github.io/bootstrap-iconpicker/bootstrap-iconpicker.png)


Installation
============
Add it in the add-ons control panel


Controlpanel
============
Important: You need to choose font in:
http://yoursite/@@medialog_controlpanel


Iconpicker Behavior
===================
In the dexterity control panel: add 'iconpicker behavior'

Colorpicker Behavior
====================
In the dexterity control panel: add 'colorpicker behavior'


Iconpicker Tile
================
In mosaic you can add Iconpicker tile


Usage
=====

- A widget to be uses in your custom views
- Helper view to load the selected fonts/icons: /@@fontload
- A view to load the icons: <tal:icons tal:replace="structure item/iconfield/@@iconload" />
- A simple example view: http:/site/folder/@@iconview

If you add the colorpicker behavior, you can choose color of the icon


Control panel
=============
The medialog control panel let you choose between 8 different icon-fonts:


- glyphicon
- typicon
- elusiveicon
- ionicon
- fontawesome
- weathericon
- mapicon
- octicon
- typicon


Author:
=======
Espen Moe-Nilssen
