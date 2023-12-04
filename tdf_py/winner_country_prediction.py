from imports import accuracy_score, classification_report, LabelEncoder, pd, RandomForestClassifier


def winner_country_prediction(data):
    # Feature Engineering (create relevant features)
    # Convert 'Year' to numeric format
    data['Year'] = pd.to_datetime(data['Year']).dt.year

    # Ensure 'Country' is of type string and convert to uppercase
    data['Country'] = data['Country'].astype(str).apply(lambda x: x.upper() if isinstance(x, str) else x)

    # Label encode 'Stage Type'
    label_encoder = LabelEncoder()
    data['Stage Type'] = label_encoder.fit_transform(data['Stage Type'])

    # Extract relevant columns
    features = data[['Year', 'Distance (km)', 'Stage Type']]
    target = data['Country']

    # Create and train the model
    model = RandomForestClassifier(n_estimators=100, random_state=42)

    model.fit(features, target)

    # Make predictions on the entire dataset
    y_pred = model.predict(features)

    # Evaluate the model
    accuracy = accuracy_score(target, y_pred)

    # Preprocess labels to remove prefixes like 'C('
    target_processed = [label.split('(')[-1].rstrip() if '(' in label else label for label in target]
    y_pred_processed = [label.split('(')[-1].rstrip() if '(' in label else label for label in y_pred]

    report = classification_report(target_processed, y_pred_processed, zero_division=1)

    print(f"Accuracy: {accuracy:.2f}")
    print("Classification Report:\n", report)
    print("Class Distribution:\n", target.value_counts())

    # Return info
    return {
        'model': model,
        'y_pred': y_pred,
        'accuracy': accuracy,
        'classification_report': report
    }
