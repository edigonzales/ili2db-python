import java

Config = java.type('ch.ehi.ili2db.gui.Config')
Ili2db = java.type('ch.ehi.ili2db.base.Ili2db')
Ili2dbException = java.type('ch.ehi.ili2db.base.Ili2dbException')
GpkgMain = java.type('ch.ehi.ili2gpkg.GpkgMain')

settings = Config()
GpkgMain().initConfig(settings)
settings.setFunction(Config.FC_IMPORT)
settings.setDoImplicitSchemaImport(True)
settings.setModels("DM01AVCH24LV95D")
settings.setDefaultSrsCode("2056")
settings.setNameOptimization(Config.NAME_OPTIMIZATION_TOPIC)
settings.setCreateEnumDefs(Config.CREATE_ENUM_DEFS_MULTI)
settings.setDbfile("254900.gpkg")
# https://github.com/claeis/ili2db/blob/11e48f5493ebaef6bd7613522ddf1725cf7f244e/src/ch/ehi/ili2db/gui/Config.java#L493
# Es gibt zwei Methoden mit dem gleichen Namen. Eine davon ist statisch.
# settings.setStrokeArcs(Config.STROKE_ARCS_ENABLE)
# oder
Config.setStrokeArcs(settings, Config.STROKE_ARCS_ENABLE)
settings.setValidation(False)
settings.setItfTransferfile(True)
settings.setDburl("jdbc:sqlite:" + settings.getDbfile())
settings.setXtffile("254900.itf")
try:
    Ili2db.run(settings, None)
except Ili2dbException as value: 
    print(fubar)
    print(value)



