========================
Onsite Python3 Interview
========================

.. contents:: Table of Contents

---------------
Getting Started
---------------

These instructions will get you a copy of the project up and running on
your local machine for development and testing purposes.

Prerequisites
=============

* git_ for source version control
* `GNU make`_ to organize and manage project lifecycle
* pyenv_ to manage multiple installs of different Python versions
* pyenv-virtualenv_ to manage auto-activated virtual environments

.. _git: https://git-scm.com/
.. _GNU make: https://www.gnu.org/software/make/
.. _pyenv: https://github.com/pyenv/pyenv
.. _pyenv-virtualenv: https://github.com/pyenv/pyenv-virtualenv

Installing
==========

#. Be sure all Prerequisites_ are installed.
#. Clone the repository with ``git``.
#. Run ``make init`` within the project to setup your Python virtual
   environment and Git hooks.


Installed
---------

Development Dependencies
""""""""""""""""""""""""

* pip-tools_ to manage locked dependencies

.. _pip-tools: https://github.com/jazzband/pip-tools

Static Checker Dependencies
"""""""""""""""""""""""""""

* bandit_ is a security linter
* flake8_ is the minimum required linter
* pre-commit_ to run checks in Git hooks
* safety_ checks dependencies for known security vulnerabilities
* pylint_ is a more strict linter than flake8_

.. _bandit: https://github.com/PyCQA/bandit
.. _flake8: https://flake8.pycqa.org/en/latest/index.html
.. _pre-commit: https://pre-commit.com/
.. _pylint: https://www.pylint.org/
.. _safety: https://pyup.io/safety/

Testing Dependencies
""""""""""""""""""""

* pytest_ is our preferred testing framework

.. _pytest: https://pytest.org/en/latest/

Runtime Dependencies
""""""""""""""""""""

* flask_ is a WSGI-based, microframework for web applications

.. _flask: https://palletsprojects.com/p/flask/
