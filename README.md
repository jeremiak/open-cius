# open cius

easy to use (hopefully), time series [crime in the us reports](https://ucr.fbi.gov/crime-in-the-u.s) from the [fbi's ucr](https://ucr.fbi.gov/) program.

[sample of cleaned output for table 1 and table 8](https://gist.github.com/jeremiak/d9a2c9e4d03b6dcedbcbf91c8e32cdcb)

## installation

0. `$ git clone open-cius && cd open-cius`
0. `$ mkdir data`
0. `$ docker build -t cius .`
0. `$ docker run -v $PWD/data:/data -it cius`

## development

run the container with the scripts directory mounted as well as the data directory

0. `$ docker run -v $PWD/data:/data -v $PWD/scripts:/app/scripts -it cius bash`
