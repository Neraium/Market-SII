export default function DriftHeatmap() {
  const cells = Array.from({ length: 30 }).map((_, idx) => ({
    id: idx,
    intensity: (idx % 5) + 1,
  }))

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

      <div className="grid grid-cols-6 gap-3 mt-6">
        {cells.map((cell) => (
          <div
            key={cell.id}
            className="aspect-square rounded-xl border border-zinc-800 flex items-center justify-center text-xs text-white"
            style={{
              background: `rgba(239, 68, 68, ${cell.intensity * 0.12})`,
            }}
          >
            {cell.intensity}
          </div>
        ))}
      </div>
    </div>
  )
}
