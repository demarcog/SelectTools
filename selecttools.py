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
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
# Initialize Qt resources from file resources.py
import resources
import os.path, re
import sys
import pdb
from aboutdialog import AboutDialog
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/tools")
from selectall import SelectAll
from selectinverse import SelectInverse
from menuselectall import MenuSelectAll
from menuselectinverse import MenuSelectInverse

class SelectTools:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        self.canvas = self.iface.mapCanvas()
        self.dlg = AboutDialog()

    def initGui(self):
        #toolbar-----------------------------------------------------------------
        # Add toolbar 
        self.toolBar = self.iface.addToolBar("SelectTools")
        self.toolBar.setObjectName("SelectTools")
        
        #Get the tools external module version--
        self.selector = SelectAll(self.iface, self.toolBar)
        self.invselector = SelectInverse (self.iface, self.toolBar)
        #--
        """
        # Get the tools simple version---
        self.act1 = QAction(QIcon(":/plugins/SelectTools/icons/SelectAll.png"),"SelectAll", self.iface.mainWindow())
        self.act2 = QAction(QIcon(":/plugins/SelectTools/icons/SelectInverse.png"),"SelectInverse", self.iface.mainWindow())
        # connect the action to the run method
        QObject.connect(self.act1, SIGNAL("triggered()"), self.selectall)
        QObject.connect(self.act2, SIGNAL("triggered()"), self.selectinverse)
        self.toolBar.addAction(self.act1)
        self.toolBar.addAction(self.act2)
        #----
        """
        #/toolbar------------------------------------------------------------------
        
        #Menu items---------------------------------------------------------------
        self.menu = QMenu()
        self.menu.setTitle( QCoreApplication.translate("SelectTools","SelectTools"))
        #add here help or ther info gettable from menu...
        self.act3 = QAction( QCoreApplication.translate("SelectTools", "SelectAll" ), self.iface.mainWindow() )
        self.act4 = QAction( QCoreApplication.translate("SelectTools", "SelectInverse" ), self.iface.mainWindow() )
        self.about = QAction( QCoreApplication.translate("About", "About" ), self.iface.mainWindow() )
        self.menu.addActions( [self.act3, self.act4, self.about]) 
        menu_bar = self.iface.mainWindow().menuBar()
        actions = menu_bar.actions()
        lastAction = actions[ len( actions ) - 1 ]
        menu_bar.insertMenu(lastAction, self.menu)
        """        
        #internal fx version---
        QObject.connect( self.act3, SIGNAL("triggered()"), self.selectall )
        QObject.connect( self.act4, SIGNAL("triggered()"), self.selectinverse )
        #---
        """
        #external fx version---
        QObject.connect( self.act3, SIGNAL("triggered()"), self.dosel )
        QObject.connect( self.act4, SIGNAL("triggered()"), self.doinv )
        QObject.connect( self.about, SIGNAL("triggered()"), self.doabout )
        #---
        
        #/Menu Items---------------------------------------------------------------

    def dosel(self):
        MenuSelectAll(self.iface)
        
    def doinv(self):
        MenuSelectInverse(self.iface)

    def doabout(self):
        self.dlg.show()
     
         
    def unload(self):
        # Remove the plugin menu item and icon
        del self.toolBar
        del self.menu
        

    def selectall(self):
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
    # run method that performs all the real work

    def selectinverse(self):
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

