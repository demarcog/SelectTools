"""
/***************************************************************************
 MenuSelectInverse
                                 A QGIS plugin
 Select all unselected features of active layer
                              -------------------
        begin                : 2012-03-22
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
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
# Import the code for the dialog
#from selectinversedialog import SelectInverseDialog

class MenuSelectInverse:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        #browse layer registry and retrieve vector layers----------------------------------------------------
        layermap = QgsMapLayerRegistry.instance().mapLayers()
        layerlist = []
        for name, layer in layermap.iteritems():
            if layer.type() == QgsMapLayer.VectorLayer:
                layerlist.append(layer)
        #----------------------------------------------------------------------------------------------------
        # if the layer list is not empty retrieve legend Interface layer properties to check if the layer is visible
        if layerlist!= []:
            legend = self.iface.legendInterface()
            layer = self.iface.activeLayer()
            if (legend.isLayerVisible(layer)):
                    # if the active layer is visible check for already selected features
                    n = layer.selectedFeatureCount()
                    if n >0:
                        # invert selection
                        #layer.setSelectedFeatures([])
                        layer.invertSelection()
                    else:
                        # since there isn't any selected feature simply invert selection is not useful...
                        QMessageBox.information(None,"SelectInverse","No features selected in active layer!!!")
                        pass
