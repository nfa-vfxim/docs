=======================
Montage Workflow
=======================
*Bo Kamphues, November 2019*

Om zo gestroomlijnd mogelijk tussen montage en VXF data
te delen is het van belang de volgende workflow te volgen:

Montage -> VFX
--------------

Alle shots worden via een breakdown document opnieuw
ingedeeld vanaf shot 001.

+++++++++++++
Stappen
+++++++++++++

1. Alle VFX worden volgens een breakdown opgedeeld in
   een nieuw "VFX" shot lijst.
2. De montage student rendert deze shots los volgens onderstaande
   specificaties (wordt gecheckt en gemonitord door VFX student).
3. De shots worden via de ``nfa-productieserver.ahk.nl`` overgedragen aan VFX.
4. De shots worden gekopieëerd naar de ``read`` server en gerenamed
   volgens de :ref:`Conventies` met gebruik van een tool als `Lupas Rename`_.

.. _`Lupas Rename`: http://rename.lupasfreeware.org/zips/setupEN.exe

++++++++++++++++++++
Import Specificaties
++++++++++++++++++++

* **Format:** Half float (16 bit), ZIP compression, EXR sequence
* **Colorspace:** ACEScg

VFX -> Montage
--------------

+++++++++++++
Stappen
+++++++++++++

1. Alle deliverables worden goed volgens de :ref:`Conventies` uitgerenderd.
2. De VFX student kopieëert deze deliverables naar de
   ``nfa-productieserver.ahk.nl``
   (zorg dat je de originele deliverables ook op de read laat staan).
3. Onder toezicht van de VFX student kopieëert
   de montage student de deliverables
   naar hun lokale werkomgeving
   en conformen deze in de edit.

++++++++++++++++++++
Export Specificaties
++++++++++++++++++++

* **Format:** Half float (16 bit), ZIP compression, EXR sequence
* **Colorspace:** ACEScg
