import { useMemo, useState } from 'react'
import './App.css'

const API_BASE_URL = (import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:8000').replace(/\/$/, '')

function App() {
  const [query, setQuery] = useState('')
  const [topK, setTopK] = useState(5)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')
  const [response, setResponse] = useState(null)

  const canSubmit = useMemo(() => query.trim().length > 0 && !loading, [query, loading])

  async function onSubmit(event) {
    event.preventDefault()
    if (!canSubmit) {
      return
    }

    setLoading(true)
    setError('')

    try {
      const res = await fetch(`${API_BASE_URL}/chat`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          query: query.trim(),
          top_k: topK,
        }),
      })

      if (!res.ok) {
        throw new Error(`Request failed with status ${res.status}`)
      }

      const payload = await res.json()
      setResponse(payload)
    } catch (err) {
      setError(err.message || 'Unable to reach the API service.')
      setResponse(null)
    } finally {
      setLoading(false)
    }
  }

  return (
    <main className="page-shell">
      <section className="hero">
        <p className="eyebrow">Ethiopian Bible Guardian</p>
        <h1>Seek Witness Before Interpretation</h1>
        <p className="hero-copy">
          Ask a question and receive a four-part response in a solemn voice:
          Invocation, Witness, Exhortation, and Reflection.
        </p>
      </section>

      <section className="panel">
        <form className="ask-form" onSubmit={onSubmit}>
          <label htmlFor="query">Question</label>
          <textarea
            id="query"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="What witness speaks to steadfast faith in trial?"
            rows={5}
          />

          <div className="form-row">
            <label htmlFor="topk">Top K</label>
            <input
              id="topk"
              type="number"
              value={topK}
              min={1}
              max={20}
              onChange={(e) => setTopK(Number(e.target.value))}
            />
          </div>

          <button type="submit" disabled={!canSubmit}>
            {loading ? 'Gathering witness...' : 'Ask Guardian'}
          </button>
        </form>

        <div className="api-note">
          <strong>API:</strong> {API_BASE_URL}
        </div>

        {error ? <p className="error">{error}</p> : null}
      </section>

      <section className="panel response-panel">
        <h2>Response</h2>
        {!response ? (
          <p className="placeholder">Awaiting a question to render witness.</p>
        ) : (
          <div className="response-grid">
            <article>
              <h3>Invocation</h3>
              <p>{response.invocation}</p>
            </article>
            <article>
              <h3>Witness</h3>
              <p>{response.witness}</p>
            </article>
            <article>
              <h3>Exhortation</h3>
              <p>{response.exhortation}</p>
            </article>
            <article>
              <h3>Reflection</h3>
              <p>{response.reflection}</p>
            </article>
          </div>
        )}
      </section>

      <section className="panel citations-panel">
        <h2>Citations</h2>
        {!response?.citations?.length ? (
          <p className="placeholder">No citation lines yet.</p>
        ) : (
          <ul>
            {response.citations.map((c) => (
              <li key={`${c.source_file}-${c.page_number}`}>
                <span>{c.book_title}</span>
                <span>{c.source_file}</span>
                <span>{c.page_number ? `p.${c.page_number}` : 'page unknown'}</span>
              </li>
            ))}
          </ul>
        )}
      </section>
    </main>
  )
}

export default App
