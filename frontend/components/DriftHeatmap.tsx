type Relationship = {
  relationship: string
  abs_change: number
}

type Props = {
  relationships?: Relationship[]
}

export default function DriftHeatmap({ relationships = [] }: Props) {
  return (
    <div className="rounded-2xl border border-zinc-800 bg-zinc-950 p-6">
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-xl font-semibold text-white">
            Drift Heatmap
          </h2>

          <p className="mt-2 text-zinc-400">
            Structural deterioration intensity across relationships.
          </p>
        </div>

        <div className="text-zinc-500 text-sm">
          Live drift matrix
        </div>
      </div>

      <div className="grid grid-cols-2 gap-3 mt-6">
        {relationships.slice(0, 12).map((relationship) => (
          <div
            key={relationship.relationship}
            className="rounded-xl border border-zinc-800 p-3 text-sm text-white"
            style={{
              background: `rgba(239, 68, 68, ${Math.min(relationship.abs_change, 1) * 0.4})`,
            }}
          >
            <div className="font-medium">
              {relationship.relationship}
            </div>

            <div className="text-zinc-300 mt-2">
              Drift: {relationship.abs_change.toFixed(3)}
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
