from client import NlpToGeojsonSpatialFeatureCompilerClient

def main():
    client = NlpToGeojsonSpatialFeatureCompilerClient()
    res = client.compile_spatial_query('Central Park Walking Zone', 40.785091, -73.968285)
    print('GeoJSON Feature Compiler: ' + res['compiler_job_id'] + ' (' + res['parsed_spatial_intent'] + ')')
    print('Valid: ' + str(res['geojson_schema_valid']) + ' | Coordinates: ' + str(res['geojson_feature']['geometry']['coordinates']))
    print('Feature URL: ' + res['feature_collection_url'])

if __name__ == '__main__':
    main()
