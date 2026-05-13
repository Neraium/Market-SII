export default function SubsystemPressureCard() {
  const systems = [
    {
      name: 'Growth Tech',
      pressure: 'High',
    },
    {
      name: 'Macro Fear',
      pressure: 'Elevated',
    },
    {
      name: 'Crypto',
      pressure: 'Moderate',
    },
  ]

  return (
    <div className="rounded-2xl border border-zinc-800 bg-zinc-950 p-6">
      <h2 className="text-xl font-semibold text-white">
        Subsystem Pressure
      </h2>

      <div className="mt-6 space-y-3">
        {systems.map((system) => (
          <div
            key={system.name}
            className="flex items-center justify-between rounded-xl border border-zinc-800 bg-black px-4 py-3"
          >
            <div className="text-white">
              {system.name}
            </div>

            <div className="text-orange-300 text-sm font-medium">
              {system.pressure}
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
