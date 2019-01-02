---
path: '/contribute'
title: 'Contribute'

layout: none
---

If you are looking to contribute to the Penrose Library, you've come to the right
place!

### 1. What do you want to contribute?

The Penrose Library has style, dsl (domain specific language), and substance files.
Each of these types is considered a package, and each package is maintained 
in modular Github repositories. You can look at examples provided in the 
[Penrose Library](https://www.github.com/penrose-lib) Organization on Github.

 - DSL packages start with prefix "dsl"
 - Style packages start with prefix "sub"
 - Substance packages start with prefix "sub"

You can use these repositories as examples to design your own modular package
repository. We will be providing cookie cutter templates to make this easier for you.

### 2. Add to the library

When you use one of the package templates, you should turn on Github pages
so that the template renders the package metadata on Github pages. The repository
here will use that metadata to test your package.

> TODO: how do we test a contribution? Ask for examples?

See [this issue](https://github.com/penrose-lib/penrose-lib.github.io/issues/2).

What does it mean to add your package to the library?

**Package Type**

Under the _library folder, find your package type, one of dsl, sty, or sub.

**Package Folder**

In that folder create a folder that corresponds to your Github organization (if it doesn't exist) and using any of the existing markdown files as a template, create a new markdown file in that folder that corresponds to the repository name that serves the package. For example, a "dsl" package served from [https://github.com/penrose-lib/dsl-linear-algebra](https://github.com/penrose-lib/dsl-linear-algebra) would have the following structure:

```bash
_library/
├── dsl
│   └── penrose-lib
│       └── linear-algebra.md
``` 

This structure ensures that the package files have an organized and consistent namespace.
If another individual also creates a "linear-algebra" dsl package, it will belong
to a different folder and the two can exist in harmony.

**Package Metadata**

The purpose of this markdown file is to serve the minimal metadata to point to your
package, and help users to find it easily in the table. This primarily means that
you need to provide the Github repository, and relevant tags. Here is an example:

```yaml
layout: package
name:  "linear-algebra"
type: "dsl"
maintainer: "@vsoch"
github: "https://www.github.com/penrose-lib/dsl-linear-algebra"
endpoint: "https://penrose-lib.github.io/dsl-linear-algebra/api.json"
tags:
- dsl
```

 - name: should correspond to your repository name
 - type: is one of dsl, sub, or sty.
 - maintainer: refers to your Github username
 - layout: is a package, you don't need to change this
 - github: is the full Github URL
 - endpoint: is the API metadata endpoint, which should be the Github pages api.json of the repository, given that you've used a template.
 - tags: can be any relevant tags to help the user with search. They will appear in the main table.

### 3. Open a Pull Request

Once you've created your metadata file, assuming you are working on your forked
version of [https://github.com/penrose-lib/penrose-lib.github.io](https://github.com/penrose-lib/penrose-lib.github.io),
you can open a pull request to the master branch. The pull request will test your
contribution, and on approval and merge, your package will be deployed as part 
of the API and Penrose Library.
