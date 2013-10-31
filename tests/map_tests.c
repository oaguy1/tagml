/******************************************************************************
 * FILE: map_tests.c
 * -----------------
 *  Unit tests for the map module, written using the Check Unit Test fraemwork.
 *
 *  AUTHOR: David N. Robinson
 *  DATE:   10/27/2013
 *  VER:    0.1
 */

#include <config.h>
#include <check.h>

START_TEST (map_node_create) {
    MapNode *mn;
    mn = createMapNode();
    mn->desc = "This is a test";
    ck_assert_str_eq (desc (mn), "This is a test");
    deleteMapNode(mn);
} END_TEST

int main(void) {
    return 0;
}
