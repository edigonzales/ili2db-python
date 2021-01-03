#!/usr/bin/env jython
import sys

from ch.ehi.ili2db.base import Ili2db
from ch.ehi.ili2db.base import Ili2dbException
from ch.ehi.ili2db.gui import Config
from ch.ehi.ili2gpkg import GpkgMain

print sys.path

settings = Config()
GpkgMain().initConfig(settings)
settings.setFunction(Config.FC_IMPORT)
settings.setDoImplicitSchemaImport(True)
settings.setModels("DM01AVCH24LV95D")
settings.setDefaultSrsCode("2056")
settings.setNameOptimization(settings.NAME_OPTIMIZATION_TOPIC)
settings.setCreateEnumDefs(Config.CREATE_ENUM_DEFS_MULTI)
settings.setDbfile("254900.gpkg")
settings.setStrokeArcs(settings, settings.STROKE_ARCS_ENABLE)
settings.setValidation(False)
settings.setItfTransferfile(True)
settings.setDburl("jdbc:sqlite:" + settings.getDbfile())
settings.setXtffile("254900.itf")
try:
    Ili2db.run(settings, None)
except Ili2dbException, value: 
    print "fubar" 
    print value
