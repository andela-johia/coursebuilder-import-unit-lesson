# coursebuilder-import-unit-lesson

## Introduction
This module was designed for copying lessons from one unit or course to another. This is a standalone module and can be attached to any GCB application.

## Requirements

You'll need a system with current versions of `bash` and `git`, as well as
`python` 2.7.

## Getting started

First, clone the Code for Africa Course Builder Repository and change directory to the Course Builder root:

```sh
git clone https://github.com/CodeForAfricaLabs/coursebuilder-core
```

Course Builder provides a management script for fetching standalone modules, you can grab the Course Builder, then using it to fetch this module`coursebuilder-unit-lesson-copy`.

### Installation
In order to grab and add this module to your coursebuilder directory, use the following steps:

- Make sure you have your `bash` window opened.
- Next step is to cd into the coursebuilder directory like so
```sh
cd coursebuilder-core/coursebuilder
```
- Once you are in the coursebuilder directory, run the script below to fetch this module
```sh
sh scripts/modules.sh \
  --targets=coursebuilder-unit-lesson-copy@https://github.com/andela-johia/coursebuilder-import-unit-lesson
```

- This will both download the module and link it to Course Builder. Now you can start up Course Builder with this module installed:
```sh
sh scripts/start_in_shell.sh
```

In order to view this module in action, visit `localhost:8081/import`.

## Module contents

The structure of this module is

```sh
module.yaml            # Module definition file.
scripts/
  setup.sh             # configuration script for the import module.
src/                   # source files of the import module.
  _static/             # Folder holding the client side integration
      importLesson.js  # Javascript file for handling the module client side
  templates/           # HTML templates .
  unit_lesson_copy.py  # Module handler definition.
  lessons.py           # Source code handling the copying of lessonsa
tests/                 # Module tests.
  functional_tests.py  # Example test file.
```

### `module.yaml`

This file defines this module. Here's the `module.yaml` for this module, annotated:

```yaml
# The dotted name of the module used for imports within CB.
module_name: modules.coursebuilder-unit-lesson-copy.unit_lesson_copy
# The public URI where this module may be found.
module_uri: https://github.com/andela-johia/coursebuilder-import-unit-lesson.git
# The module's version.
module_version: 1.0.0
# The version of CB this module works with. This is pinned
# to a specific revsion. Format: <cb_version>-<git_revision_number>
container_version: 1.8.0-d2467e99e5a4
# Natural language description of the module.
description: Coursebuilder module for import lesson contents to another course
# License your make your module available under.
license: Apache 2.0
# List of tests in the module; see tests/ below.
tests:
  tests.ext.coursebuilder-unit-lesson-copy.functional_tests.GlobalHandlerTest: 2
  tests.ext.coursebuilder-unit-lesson-copy.functional_tests.NamespacedHandlerTest: 2
```

### `scripts/setup.sh`

When you run `modules.sh` from Course Builder, it fetches this module  and then invokes this script. This script is responsible for linking the module's
`src` and `tests` directories into the right places in your local Course Builder
filesystem (`coursebuilder/modules/coursebuilder-unit-lesson-copy` and
`coursebuilder/tests/ext/coursebuilder-unit-lesson-copy`, respectively).


## Working with this module

After you've downloaded and installed this module, start Course Builder normally
to use it:

```sh
sh scripts/start_in_shell.sh
```
### Steps to working effectively with this module

After starting starting the Coursebuilder and navigating to `localhost:8081/import`, use the following steps to ensure maximum usage:
 - There are two input fields present. The first one is the `from-lesson` input field and the second is the `to-lesson` input field.
 - Go to the admin dashboard and create an empty lesson.
 - Open a second tab on your browser and navigate to the `URLs` of the lesson you want copied and copied to.
 - Ensure to copy its full URL. The URL path is like so `<your-server>/<course>/unit?unit=<number>&lesson=<number>`
 - Add the  copied URLs to their respective input fields in the import page
 - Click the import button.
 - Navigate to the lesson that was copied to.

### Running tests

You can run specific tests with `test.sh`, which is in `coursebuilder/scripts`.
For example, after you've installed this module, you can run all its tests from
the Course Builder root with:

```sh
sh scripts/test.sh tests.ext.coursebuilder-unit-lesson-copy.functional_tests
```

To run all tests in Course Builder as well as your module, run

```sh
sh scripts/run_all_tests.sh
```
## Contribution
Contributions are always welcomed to this module. If you are interested in enhancing the functionalities of this module follow these simple steps:
- Fork the module to your repository then clone it to your local machine.
- Create a new branch and make the necessary enhancement to the features.
- If the you wish to update an existing enhancement submit a pull request.
- If you are unsure about certain areas in the module feel to ask for assistance.

