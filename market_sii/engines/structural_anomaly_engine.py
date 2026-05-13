from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler


class StructuralAnomalyEngine:
    def detect(self, feature_frame):
        scaled = StandardScaler().fit_transform(feature_frame)

        model = DBSCAN(eps=0.8, min_samples=5)
        labels = model.fit_predict(scaled)

        anomalies = (labels == -1).sum()

        return {
            "clusters": int(len(set(labels)) - (1 if -1 in labels else 0)),
            "anomalies": int(anomalies),
            "labels": labels.tolist(),
        }
