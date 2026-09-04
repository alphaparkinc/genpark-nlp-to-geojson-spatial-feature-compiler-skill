class NlpToGeojsonSpatialFeatureCompilerClient:
    def compile_spatial_query(self, query_text='San Francisco Downtown 1km Radius Circular Buffer', center_lat=37.7749, center_lng=-122.4194, radius_km=1.0):
        return {
            'compiler_job_id': 'geo_cmp_9918',
            'parsed_spatial_intent': 'BUFFER_POLYGON_GENERATION',
            'geojson_feature': {
                'type': 'Feature',
                'geometry': {'type': 'Point', 'coordinates': [center_lng, center_lat]},
                'properties': {'name': query_text, 'radius_km': radius_km, 'buffer_unit': 'KILOMETER'}
            },
            'geojson_schema_valid': True,
            'feature_collection_url': 'https://atlas.geojson.genpark.ai/features/9918.json'
        }
