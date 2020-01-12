Folder Naam Conventies
======================
*Jurrian van Vuren, Januari 2020*

*Last updated by: Bo Kamphues, Januari 2020*

Read Server
+++++++++++

De structuur voor project folders ziet
er op de read als volgt uit:

* prj_ProjectNaam

    - 01_pre

        - 01_script

            - latest
            - archive

        - 02_breakdown
        - 03_concept
        - 04_visie
        - 05_planning

    - 02_ref

    - 01_setdata

        - photogrammetry
        - reports
        - setimages
        - hdri
        - lens

    - 02_schematics
    - 03_images
    - 04_video
    - 05_anim
    - 06_picturelock

- 03_source

    Hierin speelt zich de mappenstructuur
    af aangegeven in :ref:`sourceFolderConventies`.

- 04_elements

    - 01_assets

        - {prj_assetname}

            - model

                - highpoly
                - lowpoly

            - textures
            - rig
            - usd

                - geo
                - materials

    - 02_caches

        - anim
        - sim

    - 03_hdri
    - 04_mattepainting
    - 05_stock

        - images
        - sequences
        - models

- 05_workfiles

    - assets

        - {asset}

            - {software}

    - shots

        - {shot}

            - {software}

                - (template software project map)

- 06_renders

    - prerender
    - cg
    - delivery

- _pipeline

    - templates

        - Nuke
        - Houdini
        - Maya
