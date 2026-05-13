import { useEffect, useState } from 'react'

export function useSnapshot() {
  const [snapshot, setSnapshot] = useState<any>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    async function load() {
      try {
        const response = await fetch('http://localhost:8000/snapshot/current')
        const data = await response.json()
        setSnapshot(data)
      } finally {
        setLoading(false)
      }
    }

    load()
  }, [])

  return {
    snapshot,
    loading,
  }
}
