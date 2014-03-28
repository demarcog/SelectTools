"""
/***************************************************************************
 SelectTools
                                 A QGIS plugin
 extra selection feature for vector layers
                             -------------------
        begin                : 2012-03-28
        copyright            : (C) 2012 by Giuseppe De Marco
        email                : info@pienocampo.it
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""
def name():
    return "SelectTools"
def description():
    return "extra selection feature for vector layers"
def version():
    return "Version 0.2"
def icon():
    return "tools/icons/SelectAll.png"
def qgisMinimumVersion():
    return "2.0"
def classFactory(iface):
    # load SelectTools class from file SelectTools
    from selecttools import SelectTools
    return SelectTools(iface)
