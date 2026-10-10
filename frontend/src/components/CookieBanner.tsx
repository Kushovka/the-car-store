import { useState } from 'react'
import { Link } from 'react-router'

const storageKey = 'the-car-store-cherryville-cookie-consent'

export const CookieBanner = () => {
  const [visible, setVisible] = useState(() => !window.localStorage.getItem(storageKey))

  const choose = (value: 'accepted' | 'declined') => {
    window.localStorage.setItem(storageKey, value)
    setVisible(false)
  }

  if (!visible) return null

  return (
    <div className="pointer-events-none fixed inset-x-0 bottom-0 z-[60] flex justify-center p-3 sm:p-5 lg:pb-7">
      <section
        aria-label="Cookie preferences"
        className="pointer-events-auto grid w-full max-w-4xl gap-5 rounded-lg border border-[var(--color-border)] border-t-[3px] border-t-[var(--color-button)] bg-[var(--color-surface)] p-5 shadow-[0_12px_40px_rgba(25,20,18,0.2)] sm:p-6 md:grid-cols-[minmax(0,1fr)_auto] md:items-center md:gap-8 md:p-7"
      >
        <div className="min-w-0">
          <h2 className="m-0 font-[var(--font-heading)] text-xl font-bold leading-tight text-[var(--color-text)] sm:text-2xl">
            Your privacy matters
          </h2>
          <p className="mt-2 max-w-[68ch] text-sm leading-6 text-[var(--color-muted)] sm:text-base">
            We use cookies to understand site traffic and measure advertising. Choose whether to allow optional cookies.{' '}
            <Link to="/privacy-policy" className="font-semibold text-[var(--color-link)] underline decoration-[var(--color-accent)] underline-offset-4 transition-colors hover:text-[var(--color-link-hover)]">Privacy Policy</Link>
          </p>
        </div>
        <div className="grid grid-cols-2 gap-3 md:min-w-[340px]">
            <button
              type="button"
              className="min-h-12 rounded-md border border-[var(--color-border)] bg-[var(--color-background)] px-3 py-3 text-xs font-semibold uppercase tracking-[0.04em] text-[var(--color-link)] transition hover:border-[var(--color-primary)] hover:bg-[var(--color-hover)] focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[var(--color-accent)] sm:text-sm"
              onClick={() => choose('declined')}
            >
              Decline optional
            </button>
            <button
              type="button"
              className="min-h-12 rounded-md bg-[var(--color-button)] px-4 py-3 text-xs font-semibold uppercase tracking-[0.06em] text-white transition hover:bg-[var(--color-button-hover)] focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[var(--color-accent)] sm:text-sm"
              onClick={() => choose('accepted')}
            >
              Accept all
            </button>
        </div>
      </section>
    </div>
  )
}
