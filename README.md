# Pokemongo-bot-scripts
Various scripts and Dockerfile to automatize pokemon go botting

# PokemonGoMap-Snipe

This script aims at automating sniping for https://github.com/PokemonGoMap/PokemonGo-Map

## Prerequisites

You must have a Docker container of https://github.com/PokemonGoMap/PokemonGo-Map working and running. Please refer to https://pgm.readthedocs.io/en/develop/advanced-install/docker.html on how to get it running.

## How to setup

Go into the pokemongomap-snipe folder, and edit the the `snipe.py` file. Replace the `YOUR-MAP-CONTAINER-NAME` by the name of the container running your PokemonGo-Map. If you followed the docs to create the container, it should be `pogomap`.

Then build the container by running `docker build -t pogomap-snipe .`

Then, to run the container and link it to the map container, run this command :

`docker run --name pogomap-snipe-live -d -t --link MAP-CONTAINER-NAME:MAP-CONTAINER-NAME pogomap-snipe`

If you followed the docs to create the container, you should replace `MAP-CONTAINER-NAME` with `pogomap`. If not, just replace with the `MAP-CONTAINER-NAME` with the name of your map container.

You are now automaticaly going to rare pokemon locations, well done.

If you whish to see the log of the sniping script, just run `docker logs -f pogomap-snipe-live`

# PokemonGoBot-multi

This script aims at automating the launching of multiple session of https://github.com/PokemonGoF/PokemonGo-Bot/

## Prerequisites

You will need to have build the docker image for https://github.com/PokemonGoF/PokemonGo-Bot/. If you didn't please refer to https://github.com/PokemonGoF/PokemonGo-Bot/wiki/How-to-run-with-Docker.

## How to setup

Go into the pokemongobot-multi folder. Open the docker_creation.py file, and edit the following things :

### Run with pokemongo-map linked

If you want to run those container linked to a pokemongo-map for sniping, replace `YOUR-MAP-CONTAINER-NAME` with the name of the container running your pokemongo-map (if you followed the docs when building the image, it should be `pogomap`). Then replace the `YOUR-IMAGE-NAME` by the name of the pokemongo-bot image name (if you have followed the docs when building the image, it should be `pokemongo-bot`).

Then open the config.json.templ.map file. This is template config file, that I use to run my bots, and you can adjust it as your liking as long as you keep the `TEMPL_USERNAME` and `TEMPL_PASSWORD` required for the script to work. Put your GMap api key in here at the same time. Replace the `YOUR-MAP-CONTAINER-NAME` line 63 by the name of the container running your pokemongo-map. Then copy this file to config.json.templ (`cp config.json.templ.map config.json.templ`).

### Run without the pokemongo-map linked

If you do not wish to link those containers to a map container, comment the before last line, and uncomment the last one. Then replace the `YOUR-IMAGE-NAME` by the name of the pokemongo-bot image name (if you have followed the docs when building the image, it should be `pokemongo-bot`).

Then open the config.json.templ.no_map file. This is template config file, that I use to run my bots, and you can adjust it as your liking as long as you keep the `TEMPL_USERNAME` and `TEMPL_PASSWORD` required for the script to work. Put your GMap api key in here at the same time. Then copy this file to confing.json.templ (`cp config.json.templ.no_map config.json.templ`)

Edit the accounts file to add your accounts in this format :

```
ACCOUNT_NAME PASSWORD\n
ACCOUNT_NAME PASSWORD\n
...
```

Then all you have to do is `python docker_creation.py` and you should be all set.

To print the log of a container, just do `docker logs -f YOUR-CONTAINER-NAME`
