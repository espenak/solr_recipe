
=========================
solr_recipe
=========================

Buildout recipe that installs and configures Apache Solr. The recipe was made to
make it easy to setup Solr for Haystack. It has only been tested with
Haystack 1.2.3 and Solr 3.6.2.


Requirements
############

- Java 1.5 or greater from Oracle, OpenJDK or IMB. Gnu GCJ does not work. Run
  ``java -version`` to see what version you have installed if any.


Usage
#####

Add something like this to your ``buildout.cfg``::

    [buildout]
    ...
    parts = 
        ...
        solr
    ...

    [solr]
    recipe = solr_recipe
    solr_version = 3.6.2
    loglevel = INFO

The configuration above will work with Haystack. It installs a ``run_solr.sh``
script in ``bin/``, and stores data in ``var/solrdata/``.


Options
#############

``mirror``
    The Apache mirror to download from. Defaults to
    http://archive.apache.org/dist/lucene/solr/.
``solr_version``
    The solr version to download from the ``mirror``.
``java_executable``
    The Java executable to use in ``run_solr.sh``. Defaults to ``java``.
``solr_logconfig_tplfile``
    A Jinja2 template used to generate the solr ``logging.properties`` file.
    It gets all options added to the section as template variables, so
    ``loglevel`` and any other options you add will be available in the
    template. If no template file is specified, we use this template::

        .level = {{ loglevel }}

        # Write to the console:
        handlers = java.util.logging.ConsoleHandler

``solr_datadir``
    The directory where solr should store data. This is forwarded to
    solr via ``-Dsolr.data.dir`` in ``run_solr.sh``. Defaults to
    ``var/solrdata/``. The directory is created (recursively) if it does not
    exist.
``solr_home``
    Instead of using our example config-directory, you can configure your own
    using this option.
