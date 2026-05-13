import numpy as np


class CovarianceTensorEngine:
    def evaluate(self, returns, windows=(5, 20, 60)):
        tensors = {}

        for window in windows:
            covariance = returns.iloc[-window:].cov()

            eigenvalues = np.linalg.eigvals(covariance.values)

            tensors[str(window)] = {
                "covariance_trace": float(np.trace(covariance.values)),
                "dominant_eigenvalue": float(np.max(eigenvalues.real)),
                "dispersion": float(np.std(eigenvalues.real)),
            }

        return tensors
