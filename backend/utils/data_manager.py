from utils.time_utils import get_time_features

def prepare_features(lat, lon):
    features = {
        "lat": lat,
        "lon": lon
    }
    features.update(get_time_features())
    return features
