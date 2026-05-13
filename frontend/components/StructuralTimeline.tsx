export default function StructuralTimeline() {
  const events = [
    {
      label: 'Compression',
      time: '09:30',
    },
    {
      label: 'Transition',
      time: '10:15',
    },
    {
      label: 'Elevated Drift',
      time: '11:40',
    },
  ]

  return (
    <div className="rounded-2xl border border-zinc-800 bg-zinc-950 p-6">
      <h2 className="text-xl font-semibold text-white">
        Structural Timeline
      </h2>

      <div className="mt-6 space-y-4">
        {events.map((event) => (
          <div
            key={event.time}
            className="flex items-center justify-between rounded-xl border border-zinc-800 bg-black px-4 py-3"
          >
            <div className="text-white font-medium">
              {event.label}
            </div>

            <div className="text-zinc-500 text-sm">
              {event.time}
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
