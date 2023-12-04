from imports import go, opencage, pd


def geocode_city(city, geocoder):
    try:
        result = geocoder.geocode(city)
        return result[0]['geometry']['lat'], result[0]['geometry']['lng']
    except (IndexError, TypeError):
        return None, None


def aggregate_and_plot(data, api_key, sample_batch=10):
    # Create an OpenCage geocoder instance
    geocoder = opencage.geocoder.OpenCageGeocode(api_key)

    # Sample the data if sample_batch is provided
    if sample_batch:
        data = data.sample(n=sample_batch, random_state=42)

    # Geocode origin and destination cities
    data[['Origin Latitude', 'Origin Longitude']] = (
        data['Origin City'].apply(lambda x: geocode_city(x, geocoder)).apply(pd.Series)
    )

    data[['Destination Latitude', 'Destination Longitude']] = (
        data['Destination City'].apply(lambda x: geocode_city(x, geocoder)).apply(pd.Series)
    )

    # Aggregate data based on 'Origin City'
    origin_agg = data.groupby('Origin City').agg({
        'Origin Latitude': 'mean',
        'Origin Longitude': 'mean',
        'Distance (km)': 'sum'
    }).reset_index()

    # Aggregate data based on 'Destination City'
    destination_agg = data.groupby('Destination City').agg({
        'Destination Latitude': 'mean',
        'Destination Longitude': 'mean',
        'Distance (km)': 'sum'
    }).reset_index()

    # Combine aggregated data
    agg_df = pd.concat([origin_agg, destination_agg])

    # Create a scatter plot on a map using Mapbox with custom layers
    fig = go.Figure()

    # Add scatter mapbox traces
    fig.add_trace(go.Scattermapbox(
        lon=agg_df['Origin Longitude'],
        lat=agg_df['Origin Latitude'],
        text=agg_df['Origin City'],
        mode='markers',
        marker=dict(
            size=agg_df['Distance (km)'] * 0.5,
            color=agg_df['Distance (km)'],
            colorscale='Turbo_r',
            colorbar_title='Distance (km)'
        ),
        name='Origin Cities'
    ))

    # Add custom Mapbox raster layer
    fig.update_layout(
        mapbox=dict(
            style="white-bg",
            layers=[
                {
                    "below": 'traces',
                    "sourcetype": "raster",
                    "sourceattribution": "United States Geological Survey",
                    "source": [
                        "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
                    ]
                }
            ],
            zoom=5,
            center=dict(lat=46, lon=2),
        )
    )

    fig.update_layout(
        paper_bgcolor='#262626',
        margin=dict(l=0, r=0, b=0, t=0),
        font=dict(color='#ffffff'),
        legend=dict(font=dict(color='#f2f5f5'))
    )

    fig.show()
