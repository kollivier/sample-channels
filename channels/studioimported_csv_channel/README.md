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

    rm -rf VGISrestore/* ExerciseQuestions.csv Exercises.csv Content.csv
    ./linecook.py -v  --importstudioid=58c962a919cd4bb2854e230ca4d07ea1 \
                      --token=<TOKENVALUE> \
                      --channeldir=VGISrestore

2. Manually edit adjust CSV files

3. Upload to Studio

    ./linecook.py -v --reset --token=/Users/ivan/.studiotoken --channeldir=VGISrestore



More info
---------

Original channel API result (sample Exercise)
https://studio.learningequality.org/api/get_nodes_by_ids_complete/8c3cfa8ec9e34d3f878b16291392e631

Restored channel API result showing identical info:
http://develop.studio.learningequality.org/api/get_nodes_by_ids_complete/0a6c6429f91c4325a3b567da8fc5b242



Note the all-the-questions-still-in-the-last exercise is still present, but 
after modifying the first column in `ExerciseQuestions.csv` this won't be the case anymore.


Restored channel [WIP]: https://studio.learningequality.org/channels/094097ce6f395ec0b50aabd04943c6b3/view/6ff33f3

Issue ticket: https://github.com/learningequality/studio/issues/1047#issuecomment-435458297


TODO
----

If used in the future --- have to watch out for string "=" which Spreasheet software interpets as bad formula, and shows up as `#ERROR` in CSV.
Can manually change `=` to `'=` when this occurs.


