===============
ZIMA-Tables.org
===============

This repository contains the source codes of `ZIMA-Tables.org`_. It is a Django
project built on top of `ZIMA-WEB-Parts`_. The mechanical tables and engineering calculations are included in ``data/mechanical-tables``.

See `data library documentation <docs/MECHANICAL_TABLES.md>`_ and the
`thread validation report <docs/validation/threads-2026-09-09.md>`_.
The imported tables have known defects; the report records proposed corrections.
The original data values have not been changed.

Requirements
============

* Python 3.6+
* Django 3.0+
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
