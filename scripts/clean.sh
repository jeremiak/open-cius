#/bin/bash

ls ./scripts/cleaners/*.py | xargs -n 1 -P 3 python
