"""
/***************************************************************************
 SelectAll
                                 A QGIS plugin
 Select all features of active layer
                              -------------------
        begin                : 2012-03-21
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


class SelectAll:

    def __init__(self, iface, toolBar):
        # Save reference to the QGIS interface
        self.iface = iface
        # Create action that will start plugin configuration
        self.action = QAction(QIcon(":/plugins/SelectTools/tools/icons/SelectAll.png"),"SelectAll", self.iface.mainWindow())
        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)
        # Add actions to the toolbar
        toolBar.addAction(self.action)

    # run method that performs all the real work
    def run(self):
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
                        # if there are selected features deselect them and invert selection
                        layer.setSelectedFeatures([])
                        layer.invertSelection()
                    else:
                        # since there isn't any selected feature simply invert selection
                        layer.invertSelection()
