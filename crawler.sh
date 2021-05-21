#!/bin/bash

# Dies erzeugt eine Variable die immer einen neuen Wert zwischen 0-32767 erzeugt
RANDOM=$$

# Wir setzen die $response auf 0
response=0 

# Erzeugen einer tmpFile um die Response der Request zwischenzuspeichern 
# Die Response der Request ist die Anzahl der Items im Warenkorb
touch tmpFile

# Bis die Anzahl der Items 200 ist wird versucht eine Random id in den Warenkorn zu legen
until [ $response == 200 ] 
do
    # Die Response von curl wind in tmpfile gespeichert
    curl -o .\tmpFile "https://fotoarchiv-stadtarchiv.kiel.de/ax_Downd.FAU?sid=8D8F20621&dm=1&qpos=${RANDOM}&erg=H"
    # Und in unsere Variable geladen
    response=`cat .tmpFile`
    # Konsolenoutput der Response (meißtens ein langer Fehler, dass das Item nicht existiert, sonst die Anzahl der Items im Warenkorb)
    echo $response
    # Sleepfunktion um den Server nicht zu überlasten (auch bei einer Sekunde schmiert der Server ab... als nächstes 5s ausprobieren)
    sleep 1
done

# Den fertigen Warenkorb kann man dann unter https://fotoarchiv-stadtarchiv.kiel.de/fl_dload.FAU?sid=8D8F20621&dm=1 herunterladen