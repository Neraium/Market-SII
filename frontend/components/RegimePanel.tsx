type Props = {
  forecast?: {
    forecast_outlook?: string
  }
  explanation?: {
    summary?: string
  }
}

export default function RegimePanel({ forecast, explanation }: Props) {
  const outlook = forecast?.forecast_outlook || 'loading'
  const summary = explanation?.summary || 'Loading structural explanation...'

  return (
    <div className="rounded-2xl border border-zinc-800 bg-zinc-950 p-6">
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-xl font-semibold text-white">
            Structural Regime
          </h2>

          <p className="mt-2 text-zinc-400 text-sm leading-relaxed">
            {summary}
          </p>
        </div>

        <div className="rounded-full border border-yellow-500/20 bg-yellow-500/10 px-4 py-2 text-yellow-300 capitalize">
          {outlook.replaceAll('_', ' ')}
        </div>
      </div>
    </div>
  )
}
