/******************************************************************************
 * FILE: map.c
 * -----------
 *  Implementation of map module for TagML
 *
 *  AUTHOR: David N. Robinson
 *  DATE:   10.23.2013
 *  VER:    0.1
 */

#include <config.h>
#include <stdlib.h>
#include <string.h>

#include "map.h"

#define MAX_STRING 255

MapNode* createMapNode() {
    MapNode *mn;
    mn = malloc(sizeof(struct map_node *));

    mn->desc = malloc(sizeof(char) * MAX_STRING);
    mn->desc = "/0";

    return mn;
}

void destroyMapNode(MapNode *mn) {
    free(&mn->desc);
    free(&mn);
}

Map* createMap(int rows, int cols) {
    int i;
    Map *map;
    map = (Map *) malloc(sizeof(struct map *));

    map->rows = rows;
    map->cols = cols;

    map->data = (MapNode **) malloc(sizeof(struct map_node *)*rows*cols);

    return map;
}

void destroyMap(Map *map) {
    int i;
    int j;

    for(i = 0; i < map->rows; i++) {
        for(j = 0; j < map->cols; j++) {
            free(&map->data[i][j]);
        }
    }

    free(&map);
}
