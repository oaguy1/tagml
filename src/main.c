/******************************************************************************
 * FILE: main.c
 * ------------
 *  Main execution file for TagML.
 */

#include <config.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "map.h"

int main(void) {
    int i, j;
    Map *map;

    map = createMap(2, 2);

    for(i = 0; i < map->rows; i++) {
        for(j = 0; j < map->cols; j++) {
        map->data[i+j] = createMapNode();
        sprintf(map->data[i+j]->desc,"%d:%d", i, j);
        }
    }

    return 0;
}
