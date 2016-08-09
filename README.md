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
