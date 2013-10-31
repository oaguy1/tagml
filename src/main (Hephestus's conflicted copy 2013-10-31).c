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
    MapNode *mn = createMapNode();
    mn->desc = "Welcome!";

    printf("%s\n", mn->desc);
    destroyMapNode(mn);

    return 0;
}
