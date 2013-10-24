/******************************************************************************
 * FILE: map.h
 * -----------
 *  Header file for map module of TagML. This module contains the definition
 *  for the Map struct. It also includes functions required to properly
 *  allocate and deallocate memory for the Map struct.
 *
 *  AUTHOR: David N. Robinson
 *  DATE:   10.23.2013
 *  VER:    0.1
 */

#ifndef MAP
#define MAP
#define MAX_DESC_LENGTH 255

/******************************************************************************
 * DATA STRUCTURES
 * ---------------
 *  MapNode - All relavent information for a particular node of the map
 *  Map - Game map containing the entire game world
 */

struct map_node {
    char *description;
}

typedef map_node MapNode;

struct map {
    int rows;
    int columns;
    MapNode **data;
}

typedef map Map;

/******************************************************************************
 * FUNCTION: createMapNode()
 * -------------------------
 *  Function to properly allocate memory for a MapNode struct
 */
*MapNode createMapNode();

/******************************************************************************
 * FUNCTION: destroyMapNode(MapNode *node)
 * ---------------------------------------
 *  Function to properly deallocate memory for a MapNode struct
 */
void destroyMapNode(MapNode *node);

/******************************************************************************
 * FUNCTION: destroyMapNode(MapNode *node)
 * ---------------------------------------
 *  Function to properly allocate memory for a Map struct
 */
*Map createMap();

/******************************************************************************
 * FUNCTION: destroyMapNode(MapNode *node)
 * ---------------------------------------
 *  Function to properly deallocate memory for a Map struct
 */
void destroyMap(Map map);

#endif
