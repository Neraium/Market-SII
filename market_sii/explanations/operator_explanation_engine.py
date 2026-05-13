class OperatorExplanationEngine:
    def explain(
        self,
        regime,
        topology_drift,
        drift_velocity,
        drift_acceleration,
        dominant_nodes,
    ):
        explanation = []

        explanation.append(f'Regime detected: {regime}')

        if topology_drift > 2:
            explanation.append('Structural relationships are deteriorating.')

        if drift_velocity > 0:
            explanation.append('Instability progression is accelerating.')

        if drift_acceleration > 0:
            explanation.append('Structural deterioration momentum is increasing.')

        if dominant_nodes:
            names = ', '.join([node['symbol'] for node in dominant_nodes[:3]])
            explanation.append(f'Dominant structural pressure concentrated in: {names}.')

        return {
            'summary': ' '.join(explanation),
            'regime': regime,
            'topology_drift': topology_drift,
            'drift_velocity': drift_velocity,
            'drift_acceleration': drift_acceleration,
        }
