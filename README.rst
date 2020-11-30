===============
ZIMA-Tables.org
===============

This repository contains the source codes of `ZIMA-Tables.org`_. It is a Django
project built on top of `ZIMA-WEB-Parts`_. The data of mechanical tables and
engineering calculations are in a `standalone repository <http://fixme>`_.

Requirements
============

* Python 3.4+
* Django 1.9+
* `ZIMA-WEB-Parts`_

Installation
============

Create ``zima_tables/local_settings.py`` and configure at least the following
settings:

* ``ALLOWED_HOSTS``
* ``SECRET_KEY``
* ``DATABASES``
* ``STATIC_ROOT``
* ``MEDIA_ROOT``
* ``ZWP_DATA_SOURCES``

For more configuration requirements, see the installation instructions of
`ZIMA-WEB-Parts`_.

Initialize the database::

    $ python manage.py migrate

.. _ZIMA-Tables.org: http://www.zima-tables.org
.. _ZIMA-WEB-Parts: https://github.com/ZIMA-Engineering/ZIMA-WEB-Parts
