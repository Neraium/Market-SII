export default function MarketHealthCard() {
  return (
    <div className="rounded-2xl border border-zinc-800 bg-zinc-950 p-6">
      <h2 className="text-xl font-semibold text-white">
        Market Health
      </h2>

      <div className="mt-6 space-y-4">
        <div>
          <div className="text-zinc-500 text-sm">Topology Drift</div>
          <div className="text-3xl font-bold text-white">2.14</div>
        </div>

        <div>
          <div className="text-zinc-500 text-sm">Drift Velocity</div>
          <div className="text-2xl font-semibold text-orange-300">Increasing</div>
        </div>

        <div>
          <div className="text-zinc-500 text-sm">Structural Outlook</div>
          <div className="text-xl font-semibold text-yellow-300">Elevated Instability</div>
        </div>
      </div>
    </div>
  )
}
