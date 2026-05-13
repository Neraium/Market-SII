import { useEffect, useState } from 'react'

export function useMarketStream() {
  const [state, setState] = useState<any>(null)

  useEffect(() => {
    const socket = new WebSocket('ws://localhost:8000/stream/market-state')

    socket.onmessage = (event) => {
      setState(JSON.parse(event.data))
    }

    return () => socket.close()
  }, [])

  return state
}
