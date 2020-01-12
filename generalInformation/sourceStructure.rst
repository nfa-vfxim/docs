.. _Conventies:

Source File Naam Conventies
---------------------------
*Jurrian van Vuuren, November 2019*

Plates & Shots
==============

Naamgeving
++++++++++

``{projectcode}_sc{scene###}_sh{shot###}_p/v{pull/versie###}_{plate}_{colourspace}.{frame####}.{bestandstype}``

Voorbeeld
+++++++++

**tst_sc001_sh010_v001_ACEScg.1001.exr**

Projectcode
+++++++++++

De projectcode is een drie-klein-letterige code die voor elk project
uniek is. Deze afkorting moet het project vertegenwoordigen.
Voor *Puur Vuil* zou je bijvoorbeeld ``prv`` kunnen gebruiken.
Voor *Mania* werd ``man`` gebruikt. De drie letters zorgen voor 17576
mogelijke combinaties. Maar is tegelijkertijd ook kort
genoeg om te onthouden en attent te zijn op typefouten.

Scene Nummer
++++++++++++

Afhankelijk van de grootte van het project kun je het scène nummer
gebruiken in de map en bestandsnamen.
Hiervoor is het gebruikelijk om de scenenummers van het shooting
script te hanteren. Dit zorgt voor een consistente benaming tijdens
de pre-productie, het draaien en de post-productie. Een scène nummer
wordt genoteerd als ``sc###`` waar *###* vervangen wordt door het
scène nummer van de sequentie.

Wanneer er sprake is van kleine projecten, zoals commercials
of poetsshots, kan een scène nummer overbodig zijn. Wel kun je een
onderscheid maken tussen bepaalde sequenties in het project
en artificiële scène nummers gebruiken.
In het geval van poetsshots, titelsequenties en
andere overige shots bij producties waar wel gebruik
gemaakt wordt van scène nummers voor de reguliere vfx
shots, kun je deze apart classificeren doormiddel van
bijvoorbeeld ``sc000`` of ``sc999``.

Shot Nummer
+++++++++++

Shot nummers worden genoteerd als ``sh###``. Hierbij begint
het eerste shot bij 010 en gaat steeds met 10 omhoog. Dus, ``sh010``,
``sh020``, ``sh030``. Alleen VFX shots worden meegerekend in de nummering.
De stappen van 10 zorgen ervoor dat er na de eerste indexatie
van VFX shots (het moment dat bepaalde shots al een definitieve nummering
krijgen) er nog ruimte is voor nieuwe VFX shots.
Deze krijgen dan bijvoorbeeld de naam ``sh011`` of ``sh015``.

Versie en Pull Nummer
+++++++++++++++++++++++++

Het versie- en pull nummer zijn belangrijk om
verschillende versies/pulls uit elkaar te houden.
Voor overdracht van montage naar VFX wordt gebruik gemaakt van
een pull nummer. Genoteerd als ``p###`` optellend vanaf 001.
Bij een wijziging van de frames die overgedragen worden,
(denk aan andere framerange, colourspace of resolutie)
verhoogt het pull nummer met 1.
Hetzelfde geldt voor versienummers, die intern gebruikt worden
bij VFX en voor de overdracht naar montage.
Deze staan genoteerd als ``v###``. Overigens is het goed om op
zijn minst deze versienummers leidend te maken voor de
naamgeving van *Shotgun* versies.

Plate
+++++

Soms moeten er meerdere plates geleverd worden vanuit montage
naar VFX of bijvoorbeeld een alpha terug vanuit VFX. Ook pre-renders
kunnen op deze plek aangeduid worden. Omdat het plate nummer relatief
is aan het versie/pull nummer komt het na
het versie/pull nummer.
Bij afwezigheid van verschillende plates hoeft het plate nummer
niet meegenomen worden in de naamgeving.
Het plate nummer kan je op meerdere manieren noteren.
Bijvoorbeeld ``pA``, ``pB``, ``p001``, ``p002``
of als ``prerender``, ``alpha``, ``bg``, etc.

Colourspace
+++++++++++

Aangezien colourspaces van beeld materiaal niet in metadata
wordt meegegeven, is het belangrijk dat deze in de naamgeving zitten.
Afhankelijk van de colourspace noteer je dit als
``sRGB``, ``rec709``, ``ACEScg``, ``sLog1``, ect.
Omdat de colourspace afhangt van het pull/versie nummer en plate nummer,
zit de colourspace naamgeving daarna.

Frame Nummer
++++++++++++

Framenummers worden genoteerd als *####*.
Deze beginnen altijd met tellen vanaf *1001*.
Wanneer er sprake is van handles komen de handle frames ervoor,
zodat frame 1001 nog steeds de eerste frame is van de cut.

Mappen Structuur
================

Bij het overdragen van materiaal worden vaak hele mappen versleept.
Het is daarom belangrijk dat de mappenstructuur lijkt
op de naamgeving van de data.
In principe houdt je de volgende structuur aan:

| **Hoofd map (root)**
| -> **map per vfx shot** (``tst_sc001_sh010``)
| -> **map per pull of versie** (``tst_sc001_sh010_v001``)
| -> **map per plate** (``tst_sc001_sh010_v001_pA``)
| -> **map met resolutie** (``3840x2160``)
| -> **map met file type** (``JPG``)
| -> **de losse bestanden van alle frames**

Wanneer er sprake is van één of maar enkele plates,
kunnen de mappen voor verschillende plates ter hoogte van de
versies opgeslagen worden, dan krijg je:

| **Hoofd map (root)**
| -> **map per vfx shot** (``tst_sc001_sh010``)
| -> **map per plate van pull of versie + Plate** (``tst_sc001_sh010_v001_pA``)
| -> **map met resolutie** (``3840x2160``)
| -> **map met file type** (``JPG``)
| -> **de losse bestanden van alle frames**
