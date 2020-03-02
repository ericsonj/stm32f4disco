/*
 * cJSON_test.c
 *
 *  Created on: Feb 12, 2020
 *      Author: Ericson Joseph
 */

#include "main.h"
#include "stm32f4_discovery.h"
#include "cJSON_Utils.h"
#include "cJSON.h"
#include <string.h>
#include <stdlib.h>


uint32_t memoryCount = 0;

#if 0
static int supports_full_hd( const char * const monitor ) {

	const cJSON *resolution = NULL;
	const cJSON *resolutions = NULL;
	const cJSON *name = NULL;
	int status = 0;
	cJSON *monitor_json = cJSON_Parse(monitor);
	if ( monitor_json == NULL ) {
		const char *error_ptr = cJSON_GetErrorPtr();
		if ( error_ptr != NULL ) {
//			fprintf(stderr, "Error before: %s\n", error_ptr);
		}
		status = 0;
		goto end;
	}

	name = cJSON_GetObjectItemCaseSensitive(monitor_json, "name");
	if ( cJSON_IsString(name) && (name->valuestring != NULL) ) {
//		printf("Checking monitor \"%s\"\n", name->valuestring);
	}

	resolutions = cJSON_GetObjectItemCaseSensitive(monitor_json, "resolutions");
	cJSON_ArrayForEach(resolution, resolutions)
	{
		cJSON *width = cJSON_GetObjectItemCaseSensitive(resolution, "width");
		cJSON *height = cJSON_GetObjectItemCaseSensitive(resolution, "height");

		if ( !cJSON_IsNumber(width) || !cJSON_IsNumber(height) ) {
			status = 0;
			goto end;
		}

		if ( (width->valuedouble == 1920) && (height->valuedouble == 1080) ) {
			status = 1;
			goto end;
		}
	}

	end: cJSON_Delete(monitor_json);
	return status;

}
#endif

static void *testMalloc(size_t sz){
	memoryCount += sz;
	return malloc(sz);
}

static void testFree(void *ptr){
	return free(ptr);
}

static cJSON_Hooks hooks;


void cJSON_test( void ) {

	hooks.malloc_fn = testMalloc;
	hooks.free_fn = testFree;

	cJSON_InitHooks(&hooks);

	/**
	 * JSON-RPC
	 */
	char *msg = "{\"jsonrpc\": \"2.0\", \"method\": \"subtract\", \"params\": {\"minuend\": 42, \"subtrahend\": 23}, \"id\": 3}";


	const cJSON *method = NULL;
	const cJSON *id  = NULL;

	/**
	 * Parse data
	 */
	cJSON *monitor_json = cJSON_Parse(msg);
	method = cJSON_GetObjectItemCaseSensitive(monitor_json, "method");
	id = cJSON_GetObjectItemCaseSensitive(monitor_json, "id");

	/**
	 * Check method = subtract
	 */
	if (cJSON_IsString(method)){
		if(strcmp(method->valuestring, "subtract") == 0){
			BSP_LED_On(LED3);
		}
	}

	/**
	 * Check id
	 */
	if(cJSON_IsNumber(id)){
		BSP_LED_On(LED4);
	}

	/**
	 * Free memory
	 */
	cJSON_Delete(monitor_json);

}


