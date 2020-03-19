/*
 * gtypes.h
 *
 *  Created on: Mar 9, 2020
 *      Author: ericson
 */

#ifndef GSTRING_GTYPES_H_
#define GSTRING_GTYPES_H_

#include <stdint.h>

#define MIN(a, b) \
    ((a < b) ? a : b)

#define MALLOC_BLOCK(l) \
    (((((l) / 32) + 1) * 32))


typedef char     gchar;
typedef uint32_t gsize;
typedef uint32_t gint;


#endif /* GSTRING_GTYPES_H_ */
