#!/bin/bash
heroku container:push web -a dinoiasuadente
heroku container:release web -a dinoiasuadente
aplay /usr/share/sounds/purple/alert.wav
