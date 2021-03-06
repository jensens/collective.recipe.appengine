Versions
========

Version 1.0
-----------

- cleanup, added integrated buildout and tests, depend on 
  hexagonit.recipe.download and removed copied code,
  make it work with zc.buildout >=2.0.1,
  create target-directory for applib if not exist.
  default under parts to appengine_sdk.
  Forked from appfy.recipe.gae
  [jensens, 2013-03-09]

Version 0.9.1 - November 27, 2010
---------------------------------
- Readded option 'clear-destination' to the dowanlod recipe, true by default.
  It was causing an error when the files existed, and 'ignore-existing' wasn't
  avoiding it.


Version 0.9 - November 23, 2010
-------------------------------
- Scripts now extends z3c.recipe.scripts.scripts.Scripts, for better
  compatibility with buildout 1.5.2.
- collective.recipe.appengine.sdk accepts a sha1sum option, to check the SDK checksum as
  provided by Google.
- removed hexagonit.recipe.download as it was not flexible enough to allow
  the sha1 checksum check.


Version 0.8 - July 27, 2010
---------------------------
- Do not raise IOError when egg info is not found, and let installation
  proceed only emitting a warning.


Version 0.7.2 - June 18, 2010
-----------------------------
- os.makedirs(), not os.mkdirs(). Ooops.


Version 0.7.1 - June 18, 2010
-----------------------------
- Minor enhancement: use os.mkdirs() instead of os.mkdir() when creating the
  backup for app_libs (Tom Lynn).


Version 0.7 - June 17, 2010
---------------------------
- Added multi-line top_level support. Now it can handle eggs with multiple
  lines in top_level.txt. Thanks to Benjamin Kampmann for this (Issue #3).

- Added ignore-packages option, useful to ignore setuptools, distribute and
  other dependency packages not useful on App Engine.

- Single modules are now also matched by ignore-globs.

- ignore-globs now removes the non-related path prefix for better matching.

- Documented extra-paths, useful to add libraries directories to sys.path in
  scripts.

- Several refactorings and cleanups.


Version 0.6.1 - June 3, 2010
----------------------------
- Don't install package if egg info is not found, instead of breaking. This
  was causing a problem when setuptools is declared as dependency.


Version 0.6 - June 1, 2010
--------------------------
- app_lib can now also install develop eggs.


Version 0.5.2 - May 27, 2010
----------------------------
- Single files are correctly installed.
- Namespaced packages are put in the same directory structure. This was causing
  an error when trying to create a directory for the second time.


Version 0.5.1 - May 17, 2010
----------------------------
- collective.recipe.appengine:app_lib now extends zc.recipe.egg.Scripts, so that scripts
  from packages are installed, as before.


Version 0.5 - May 5, 2010
---------------------------
- Dropped checksum checking, and now move files to a backup directory if
  delete-safe is `true` (which is the default). This makes the build faster
  and avoids the annoying invalid checksum errors.


Version 0.4.5 - May 5, 2010
---------------------------
- Use tempfile.gettempdir() to save temporary files. Thanks, tlynn.


Version 0.4.4 - May 3, 2010
---------------------------
- Unzip eggs by default in app_lib or we can't use some.


Version 0.4.3 - May 3, 2010
---------------------------
- Only accepts multi-line configuration for appenginetools.

- Fixed tmpdir in app_lib.


Version 0.4.2 - May 1st, 2010
-----------------------------
- app_lib now extends zc.recipe.egg.Eggs and sets default eggs to an empty
  string, just to avoid errors.

- More small refactorings.


Version 0.4.1 - May 1st, 2010
-----------------------------
- Removed `primary-lib-directory` option from app_lib.

- Code cleanup and refactoring.


Version 0.4 - April 30, 2010
----------------------------
- Fixed script path problem when buildout is configured to use absolute paths.
  Fixes issue #1. Thanks Lacrima.Maxim for the report.

- Scripts now run using alter_sys=True, so that help messages that use __doc__
  are displayed correctly.


Version 0.3 - April 29, 2010
----------------------------
- Added `config-file` option to collective.recipe.appengine:tools, to define the
  configuration file used to set default arguments for the scripts.


Version 0.2 - April 29, 2010
----------------------------
- Added bulkload_client, bulkloader and remote_api_shell scripts.

- Fixed script entry-points: they were breaking on Windows; now they work.

- All recipes are also tested and working on Windows now.


Version 0.1 - April 28, 2010
----------------------------
Initial release
