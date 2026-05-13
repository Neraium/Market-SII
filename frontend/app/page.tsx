'use client'

import MarketHealthCard from '../components/MarketHealthCard'
import RegimePanel from '../components/RegimePanel'
import TopologyGraph from '../components/TopologyGraph'
import DriftHeatmap from '../components/DriftHeatmap'
import StructuralTimeline from '../components/StructuralTimeline'
import SubsystemPressureCard from '../components/SubsystemPressureCard'
import { useMarketStream } from '../hooks/useMarketStream'
import { useSnapshot } from '../hooks/useSnapshot'

export default function HomePage() {
  const state = useMarketStream()
  const { snapshot } = useSnapshot()

  return (
    <main className="min-h-screen bg-black text-white p-8">
      <div className="max-w-7xl mx-auto">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-5xl font-bold tracking-tight">
              Market-SII
            </h1>

            <p className="mt-4 text-zinc-400 text-lg">
              Structural Market Intelligence Dashboard
            </p>
          </div>

          <div className="rounded-full border border-emerald-500/20 bg-emerald-500/10 px-4 py-2 text-emerald-300">
            {state?.status || 'connected'}
          </div>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-4 gap-6 mt-10">
          <MarketHealthCard forecast={snapshot?.forecast} />

          <RegimePanel
            forecast={snapshot?.forecast}
            explanation={snapshot?.explanation}
          />

          <DriftHeatmap
            relationships={snapshot?.topology?.relationship_changes}
          />

          <SubsystemPressureCard
            nodes={snapshot?.topology?.dominant_nodes}
          />
        </div>

        <div className="grid grid-cols-1 xl:grid-cols-3 gap-6 mt-8">
          <div className="xl:col-span-2">
            <TopologyGraph graph={snapshot?.graph} />
          </div>

          <StructuralTimeline />
        </div>
      </div>
    </main>
  )
}
