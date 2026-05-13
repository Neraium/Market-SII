export default function TopologyGraph() {
  const nodes = ['SPY', 'QQQ', 'XLK', 'SMH', 'NVDA', 'BTC']

  return (
    <div className="rounded-2xl border border-zinc-800 bg-zinc-950 p-6 overflow-hidden">
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-xl font-semibold text-white">
            Market Topology Graph
          </h2>

          <p className="mt-2 text-zinc-400">
            Structural relationship network across major subsystems.
          </p>
        </div>

        <div className="text-sm text-zinc-500">
          Live topology
        </div>
      </div>

      <div className="relative h-[420px] mt-6 rounded-xl border border-zinc-800 bg-black">
        <svg className="absolute inset-0 w-full h-full">
          <line x1="120" y1="120" x2="300" y2="100" stroke="#3f3f46" />
          <line x1="300" y1="100" x2="500" y2="160" stroke="#3f3f46" />
          <line x1="500" y1="160" x2="380" y2="300" stroke="#3f3f46" />
          <line x1="380" y1="300" x2="180" y2="260" stroke="#3f3f46" />
        </svg>

        <div className="absolute inset-0 flex items-center justify-center">
          <div className="grid grid-cols-3 gap-10">
            {nodes.map((node) => (
              <div
                key={node}
                className="h-20 w-20 rounded-full border border-emerald-500/20 bg-emerald-500/10 flex items-center justify-center text-sm font-semibold text-emerald-300 shadow-lg shadow-emerald-500/10"
              >
                {node}
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  )
}
