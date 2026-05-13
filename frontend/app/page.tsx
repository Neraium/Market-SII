export default function HomePage() {
  return (
    <main className="min-h-screen bg-black text-white p-8">
      <div className="max-w-7xl mx-auto">
        <h1 className="text-5xl font-bold tracking-tight">
          Market-SII
        </h1>

        <p className="mt-4 text-zinc-400 text-lg">
          Structural Market Intelligence Dashboard
        </p>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-10">
          <div className="rounded-2xl border border-zinc-800 bg-zinc-950 p-6">
            <h2 className="text-xl font-semibold">Market Health</h2>
            <p className="text-zinc-400 mt-2">Topology drift and regime state.</p>
          </div>

          <div className="rounded-2xl border border-zinc-800 bg-zinc-950 p-6">
            <h2 className="text-xl font-semibold">Subsystem Pressure</h2>
            <p className="text-zinc-400 mt-2">Structural stress by subsystem.</p>
          </div>

          <div className="rounded-2xl border border-zinc-800 bg-zinc-950 p-6">
            <h2 className="text-xl font-semibold">Relationship Drift</h2>
            <p className="text-zinc-400 mt-2">Topology deterioration timeline.</p>
          </div>
        </div>
      </div>
    </main>
  )
}
