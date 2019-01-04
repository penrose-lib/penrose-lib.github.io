#!/usr/bin/env python

from glob import glob
import os
import sys

here = sys.argv[1]

# A quick script to fix urls for circle
baseurl="https://6-163772993-gh.circle-artifacts.com/0/_site"

print('Working directory is %s' % here)

files = (glob('%s/_layouts/*.html' % here) +
         glob('%s/_includes/*.html' % here) +
         glob('%s/pages/*.md' % here))

# https://circleci.com/docs/2.0/env-vars/#built-in-environment-variables
running_ci = os.environ.get('CI', False)

if running_ci in ['true', True]:
    print('Detected running on CircleCi, fixing static files')
    # Only run if we are in CI environment

    for file_name in files:

        print('Fixing URLs in %s' % file_name)
        # 1. Read in the file
        with open(file_name, 'r') as filey:
            content = filey.read()

        # 2. Replace with the actual baseurl
        content = content.replace('{{ site.url }}', baseurl)

        # 3. Save the file
        with open(file_name, 'w') as filey:
            filey.writelines(content)
