# open cius

time series [crime in the us reports]() from the [fbi's ucr]() program.

## installation

0. `$ git clone open-cius && cd open-cius`
0. `$ mkdir data`
0. `$ docker build -t cius .`
0. `$ docker run -v $PWD/data:/data -it cius scripts/clean.sh`

## development

run the container with the scripts directory mounted as well as the data directory

0. `$ docker run -v $PWD/data:/data -v $PWD/scripts:/src/scripts -it cius bash`