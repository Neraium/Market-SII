import numpy as np


def compute_topology_drift(baseline_corr, recent_corr):
    diff = recent_corr - baseline_corr
    return np.linalg.norm(diff.values), diff


def compute_drift_velocity(current_drift, previous_drift):
    return current_drift - previous_drift


def compute_drift_acceleration(current_velocity, previous_velocity):
    return current_velocity - previous_velocity
