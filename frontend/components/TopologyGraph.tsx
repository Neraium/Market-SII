type Node = {
  id: string
}

type Edge = {
  source: string
  target: string
  weight: number
}

type Props = {
  graph?: {
    nodes: Node[]
    edges: Edge[]
  }
}

export default function TopologyGraph({ graph }: Props) {
  const nodes = graph?.nodes || []
  const edges = graph?.edges || []

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
          {nodes.length} nodes · {edges.length} edges
        </div>
      </div>

      <div className="relative h-[420px] mt-6 rounded-xl border border-zinc-800 bg-black overflow-hidden">
        <svg className="absolute inset-0 w-full h-full">
          {edges.slice(0, 24).map((edge, idx) => {
            const x1 = 80 + ((idx * 71) % 500)
            const y1 = 60 + ((idx * 47) % 280)
            const x2 = 180 + ((idx * 37) % 420)
            const y2 = 120 + ((idx * 61) % 240)

            return (
              <line
                key={`${edge.source}-${edge.target}`}
                x1={x1}
                y1={y1}
                x2={x2}
                y2={y2}
                stroke="rgba(239,68,68,0.35)"
                strokeWidth={Math.max(edge.weight * 6, 1)}
              />
            )
          })}
        </svg>

        <div className="absolute inset-0 flex flex-wrap items-center justify-center gap-8 p-10">
          {nodes.map((node, idx) => (
            <div
              key={node.id}
              className="h-20 w-20 rounded-full border border-emerald-500/20 bg-emerald-500/10 flex items-center justify-center text-sm font-semibold text-emerald-300 shadow-lg shadow-emerald-500/10"
              style={{
                transform: `translateY(${(idx % 3) * 8}px)`,
              }}
            >
              {node.id}
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}
