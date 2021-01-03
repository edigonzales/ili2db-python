# ili2db-python

## prerequisites

## Jython
1. Download and install Jython
2. Add `jython2.7.2/bin` directory to your path.
3. Download and unzip ili2gpkg

- What about wildcard in JYTHONPATH?

Classpath separator:
- Linux `:`
- Windows `;`

## GraalVM
1. Install GraalVM, e.g. with https://sdkman.io/
2. Install Python `gu install Python`

## jython-simple
```
cd jython-simple
```

```
export JYTHONPATH=~/apps/ili2gpkg-4.4.5/ili2gpkg-4.4.5.jar:~/apps/ili2gpkg-4.4.5/libs/antlr-2.7.7.jar:~/apps/ili2gpkg-4.4.5/libs/base64-2.3.9.jar:~/apps/ili2gpkg-4.4.5/libs/ehibasics-1.4.0.jar:~/apps/ili2gpkg-4.4.5/libs/ehisqlgen-1.13.8.jar:~/apps/ili2gpkg-4.4.5/libs/ili2c-core-5.1.5.jar:~/apps/ili2gpkg-4.4.5/libs/ili2c-tool-5.1.5.jar:~/apps/ili2gpkg-4.4.5/libs/ili2db-4.4.5.jar:~/apps/ili2gpkg-4.4.5/libs/iox-api-1.0.3.jar:~/apps/ili2gpkg-4.4.5/libs/iox-ili-1.21.4.jar:~/apps/ili2gpkg-4.4.5/libs/jackson-core-2.9.7.jar:~/apps/ili2gpkg-4.4.5/libs/jts-core-1.14.0.jar:~/apps/ili2gpkg-4.4.5/libs/sqlite-jdbc-3.8.11.2.jar  
```

Runs successully the first time and the gpkg file is created.
```
./ili2db.py
```

Throws an exception since it tries to insert the settings a second time:
```
./ili2db.py
```

## graalvm-simple
```
cd graalvm-simple
```

```
export CLASSPATH=~/apps/ili2gpkg-4.4.5/ili2gpkg-4.4.5.jar:~/apps/ili2gpkg-4.4.5/libs/antlr-2.7.7.jar:~/apps/ili2gpkg-4.4.5/libs/base64-2.3.9.jar:~/apps/ili2gpkg-4.4.5/libs/ehibasics-1.4.0.jar:~/apps/ili2gpkg-4.4.5/libs/ehisqlgen-1.13.8.jar:~/apps/ili2gpkg-4.4.5/libs/ili2c-core-5.1.5.jar:~/apps/ili2gpkg-4.4.5/libs/ili2c-tool-5.1.5.jar:~/apps/ili2gpkg-4.4.5/libs/ili2db-4.4.5.jar:~/apps/ili2gpkg-4.4.5/libs/iox-api-1.0.3.jar:~/apps/ili2gpkg-4.4.5/libs/iox-ili-1.21.4.jar:~/apps/ili2gpkg-4.4.5/libs/jackson-core-2.9.7.jar:~/apps/ili2gpkg-4.4.5/libs/jts-core-1.14.0.jar:~/apps/ili2gpkg-4.4.5/libs/sqlite-jdbc-3.8.11.2.jar  
```

```
graalpython --jvm --vm.cp=$CLASSPATH ili2db.py
```