.. _maintenance:

==============================
Maintenance
==============================

As with any long standing project, this documentation needs maintenance every once in a while. This maintenance is done by
curators who add, edit and, if necessary, delete articles. The following sections describe how said maintenance is done
and the conventions surrounding it.

**************************
Curator Information
**************************

This documentation is hosted through `Read the Docs <readthedocs.org>`_, an industry-standard way of creating documentation for software or in-house guides.
Some examples of companies using *RTD* are:

- `Shotgun <https://developer.shotgunsoftware.com/>`_
- `OpenColorIO <https://opencolorio.readthedocs.io/en/latest/>`_
- `Alembic <https://docs.alembic.io/>`_

*RTD* documentation pages are written in a format called `ReStructuredText <https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html>`_. 
*ReST* is a markup language which means that some characters like an asterisk (#) or an underscore (_) have a different meaning. You may have seen a similiar
markup language like *HTML* or *Markdown* in use on websites or GitHub repositories. It takes time to get the hang of writing in *ReST*, 
but with the help of this `cheatsheet <https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html>`_ you'll get the gist of it quickly.
It is recommended to use an *IDE* that supports syntax highlighting for *ReST* so it will tell you when you correctly type directives. This
`Visual Studio Code extension <https://marketplace.visualstudio.com/items?itemName=lextudio.restructuredtext>`_ takes care of that for you.

This documentation is hosted through *RTD*, but the actual working code resides in a `GitHub repository <https://github.com/nfa-vfxim/docs>`_.
The website automatically builds itself whenever a commit is pushed to one of the branches of the repository. It is highly recommended to get the hang of Git through your *IDE* and/or the
commandline to accurately curate the documentation.

.. tip:: If you need a primer on how to use GitHub and Git, `this <https://guides.github.com/introduction/git-handbook/>`_ might be a good place to start.

In order to work on this documentation, you should have a working version of ``poetry``, the *Python* dependency manager that installs all necessary software. You can install ``poetry`` through ``pip``.
If you do not have pip installed, you should first check if you have a working version of *Python*.

Install poetry through pip:

.. code-block:: bash

    pip install poetry

*********************************
Maintenance Process
*********************************

The process for adding or editing the current documentation is as follows:

- The curator forks the main repository or creates a new branch for the edits in mind [#f1]_.
- The curator edits or adds articles, pages and sections according to the `Conventions`_.
- The curator generates translations and/or manually translates the article.
- The curator commits all changes.
- The curator creates a pull request with another curator as reviewer so the edits can be double checked before merged into the entire documentation.

**********************************
Maintenance Guide
**********************************

.. note:: Please note that this guide is meant for simple edits or the addition of just one page. If really big edits are to be done it would be recommended to checkout the other files first to see how their *ReStructuredText* is formatted.

First, fork the repository or create a branch [#f1]_ from the main repository. After that, clone the repository:

.. code-block:: bash

    git clone <repository link>

``<repository link>`` should be replaced with the appropriate link for the repository. If a new branch was created for the 
edits you'd like to make you need to checkout to that branch:

.. code-block:: bash

    git checkout -b <branch name>

``<branch name>`` should be replaced with the name of the new branch. 

To make sure all dependencies are installed, run:

.. code-block:: bash

    poetry install

Next, start editing the articles you'd like to edit or copy the ``template.rst`` file
to a section inside ``\docs`` to create a new page. Make sure to follow the `Conventions`_. Next, the localization files need to be updated. First, build the current set of ``.rst`` files from the current directory [#f2]_:

.. code-block:: bash

    poetry run sphinx-build -b gettext . _build/gettext

Next, update the English and Dutch localization files:

.. code-block:: bash

    poetry run sphinx-intl update -p _build/gettext -l en
    poetry run sphinx-intl update -p _build/gettext -l nl

In order to keep the documentation nicely synced between English and Dutch it's recommended that you go into the ``locale\nl\LC_MESSAGES`` folder and translate the page you have edited.
Next, stage and commit all changes:

.. code-block:: bash

    git add -A
    # Stage all changes
    git commit 
    # Commit all changes to the directory

Next, you need to push the committed changes to the remote repository:

.. code-block:: bash

    git push --origin

If you don't use a GUI tool to manage your Git directory you'll probably run into a password prompt right about here. Though the commandline is a very useful and powerful feature, it's a lot easier to use *VS Code* or *Git GUI* to manage your commits.

Finally, create a pull request and assign a reviewer. If the reviewer accepts all changes, the website will automatically update the build.

.. note:: Because it is normal to not operate on the current stable release of anything, it is possible to see the final result in a working version. This version is nothing more than a branch in Github, but that 
            branch needs to be activated through `readthedocs.org <readthedocs.org>`_.

*******************************
Conventions
*******************************

The ``template.rst`` will allow you to follow the conventions as closely as possible, but here's a small list of things to think about when writing articles for the documentation:

- Always start the page with a title.
- A page should always end with a ``.. sectionauthor: Your Name`` directive to differentiate who has written what on the website.
- Use admonitions and other formatting tools often and precisely. It's better to be too explainfull than having a vague documentation.

.. rubric:: Footnotes

.. [#f1] Creating a new branch is only possible if the curator is added as a collaborator in GitHub or the project ownership is handed off to him/her.
.. [#f2] It is important that you have a basic knowledge of the command line and know how to change the current directory.

.. sectionauthor:: Bo Kamphues