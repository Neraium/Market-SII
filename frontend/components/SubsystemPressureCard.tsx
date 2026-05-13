type Node = {
  symbol: string
  relationship_pressure: number
}

type Props = {
  nodes?: Node[]
}

export default function SubsystemPressureCard({ nodes = [] }: Props) {
  return (
    <div className="rounded-2xl border border-zinc-800 bg-zinc-950 p-6">
      <h2 className="text-xl font-semibold text-white">
        Subsystem Pressure
      </h2>

      <div className="mt-6 space-y-3">
        {nodes.slice(0, 5).map((node) => (
          <div
            key={node.symbol}
            className="flex items-center justify-between rounded-xl border border-zinc-800 bg-black px-4 py-3"
          >
            <div className="text-white">
              {node.symbol}
            </div>

            <div className="text-orange-300 text-sm font-medium">
              {node.relationship_pressure.toFixed(2)}
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
