CSV-based workflow
==================

This channel uses the Studio API to export exercises from an existing Studio channel 
  - no content files
  - topic structure from the filesystem hierarchy (empty folders)
  - metadata from 4 CSV files:
      - Channel metadata provided in Chaannel.csv
      - Files metadata provided in Content.csv
      - Exercises.csv to store exercise metadata and master model
      - ExerciseQuestions.csv to store individual questions



Use case
--------
  - Manually edit exercises and question--> exercise associations




Usage
-----

1. Import from Studio

    ./linecook.py -v  --importstudioid=58c962a919cd4bb2854e230ca4d07ea1 \
                      --token=<TOKENVALUE> \
                      --channeldir=VGISrestore

2. Manually edit adjust CSV files

3. Upload to Studio

    ./linecook.py -v --reset --token=/Users/ivan/.studiotoken --channeldir=VGISrestore

