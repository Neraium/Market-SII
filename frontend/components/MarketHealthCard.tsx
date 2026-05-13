type Props = {
  forecast?: {
    forecast_score?: number
    forecast_outlook?: string
    topology_drift?: number
    propagation_score?: number
  }
}

export default function MarketHealthCard({ forecast }: Props) {
  const topologyDrift = forecast?.topology_drift ?? 0
  const propagationScore = forecast?.propagation_score ?? 0
  const outlook = forecast?.forecast_outlook || 'loading'

  return (
    <div className="rounded-2xl border border-zinc-800 bg-zinc-950 p-6">
      <h2 className="text-xl font-semibold text-white">
        Market Health
      </h2>

      <div className="mt-6 space-y-4">
        <div>
          <div className="text-zinc-500 text-sm">Topology Drift</div>
          <div className="text-3xl font-bold text-white">
            {topologyDrift.toFixed(3)}
          </div>
        </div>

        <div>
          <div className="text-zinc-500 text-sm">Propagation Score</div>
          <div className="text-2xl font-semibold text-orange-300">
            {propagationScore.toFixed(1)}
          </div>
        </div>

        <div>
          <div className="text-zinc-500 text-sm">Structural Outlook</div>
          <div className="text-xl font-semibold text-yellow-300 capitalize">
            {outlook.replaceAll('_', ' ')}
          </div>
        </div>
      </div>
    </div>
  )
}
