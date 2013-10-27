/******************************************************************************
 * FILE: parse.h
 * -------------
 *  The header file for the parsing module for TagML. 
 *
 *  AUTHOR: David N. Robinson
 *  DATE:   10.23.2013
 *  VER:    0.11
 */

#include <libxml/xmlmemory.h>
#include <libxml/parser.h>

#ifndef PARSE
#define PARSE

/******************************************************************************
 * FUNCTION: parseDoc(char *docname)
 * ---------------------------------
 *  Given a character array containing a file name, this function will begin
 *  a recursive decent parse of an TagXML file. An integer will be returned
 *  signifying success (0) or failure (1) to parse the TagML document.
 */
int parseDoc(char *docname);

#endif
