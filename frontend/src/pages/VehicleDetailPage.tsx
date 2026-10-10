import { useEffect, useMemo, useState } from 'react'
import { Link, useParams } from 'react-router'
import { FaArrowRight, FaBarcode, FaCheck, FaChair, FaCogs, FaCog, FaEnvelope, FaFileAlt, FaMapMarkerAlt, FaPhoneAlt, FaRoad, FaTachometerAlt, FaTint } from 'react-icons/fa'
import { getVehicle, listVehicles } from '../api/vehicles'
import { Button } from '../components/Button'
import { LeadForm } from '../components/LeadForm'
import { Seo } from '../components/Seo'
import { VehicleDetailSkeleton } from '../components/Skeletons'
import { VehicleGallery } from '../components/VehicleGallery'
import { VehicleCard } from '../components/VehicleCard'
import { business } from '../data/business'
import type { Vehicle } from '../types/vehicle'
import { trackContactCta } from '../utils/ctaTracking'
import { formatNumber, formatPrice } from '../utils/format'
import { trackViewContent } from '../utils/metaPixel'

const phoneHref = business.phoneHref || business.contactHref
const hasListingValue = (value: string | number) => String(value).trim() !== '' && !/^not listed$/i.test(String(value).trim())
const plainDescription = (value: string) => {
  if (/^\s*<(?:!doctype|html)\b/i.test(value)) return ''
  return new DOMParser().parseFromString(value, 'text/html').body.textContent?.replace(/\s+/g, ' ').trim() ?? ''
}

const featuresFromListingInfo = (content: string) => content
  .split('\n')
  .map((line) => line.trim())
  .filter((line) => line.startsWith('- '))
  .map((line) => line.slice(2).trim())
  .filter((item) => !/^(chassis:|vin:|\d+[\d,.]*k? miles$|.*\b(engine|transmission|dual-clutch|tiptronic|single-speed|v8|v6|v12|inline|turbodiesel|twin-turbocharged|supercharged)\b|.*\b(paint|metallic|upholstery|interior|leather)\b)/i.test(item))

const Feature = ({ feature }: { feature: string }) => (
  <p className="flex items-start gap-3 text-[15px] leading-6 text-[#4d4d4d] sm:text-base"><FaCheck aria-hidden="true" className="mt-1 shrink-0 text-[15px] text-[#4d4d4d] sm:text-base" />{feature}</p>
)

const SectionHeading = ({ children, id }: { children: string; id?: string }) => <div><h2 id={id} className="text-[27px] font-bold leading-tight text-[#171717] sm:text-[32px]">{children}</h2><span aria-hidden="true" className="mt-2 block h-[3px] w-[90px] bg-[#c9001b]" /></div>

const RelatedVehiclesCarousel = ({ vehicles }: { vehicles: Vehicle[] }) => {
  const [visibleCount, setVisibleCount] = useState(() => window.innerWidth >= 1024 ? 3 : window.innerWidth >= 640 ? 2 : 1)
  useEffect(() => {
    const resize = () => setVisibleCount(window.innerWidth >= 1024 ? 3 : window.innerWidth >= 640 ? 2 : 1)
    window.addEventListener('resize', resize)
    return () => window.removeEventListener('resize', resize)
  }, [])
  if (!vehicles.length) return null
  const visible = vehicles.slice(0, visibleCount)
  return <section aria-labelledby="related-vehicles-title" className="bg-white px-5 py-8 sm:px-7 lg:px-9 lg:py-8">
    <div className="mx-auto max-w-[1600px]">
      <div className="mb-5 flex items-end justify-between gap-4">
        <SectionHeading id="related-vehicles-title">Similar Vehicles</SectionHeading>
        <Link to="/inventory" className="inline-flex shrink-0 items-center gap-2 border-b border-[#c9001b] pb-1 text-[14px] font-semibold text-[#c9001b] sm:text-base">View All Inventory <FaArrowRight aria-hidden="true" className="text-base" /></Link>
      </div>
      <div className={`grid gap-4 ${visible.length >= 3 ? 'lg:grid-cols-3' : visible.length === 2 ? 'sm:grid-cols-2' : 'grid-cols-1'}`}>
        {visible.map((vehicle) => <VehicleCard key={vehicle.id} vehicle={vehicle} />)}
      </div>
    </div>
  </section>
}

const PriceCard = ({ vehicle }: { vehicle: Vehicle }) => <aside className="flex min-w-0 flex-col bg-white px-1 py-1 sm:px-3 lg:px-0">
  <span className="mb-3 w-fit bg-[#f0f0f0] px-3 py-1.5 text-sm font-medium text-[#444]">Used</span>
  <h1 className="text-[clamp(28px,2.4vw,40px)] font-bold leading-[1.1] tracking-[-0.025em] text-[#171717]">{vehicle.year} {vehicle.make} {vehicle.model} {vehicle.trim}</h1>
  <p className="mt-4 text-[clamp(40px,3vw,48px)] font-bold leading-none tracking-[-0.025em] text-[#c9001b]">{formatPrice(vehicle.price)}</p>
  <VehicleQuickFacts vehicle={vehicle} />
  <a href={phoneHref} className="site-button vehicle-detail-contact mt-4 flex min-h-[62px] items-center justify-center gap-3 rounded-[3px] bg-[#c9001b] px-4 text-base font-bold text-white transition hover:bg-[#a90017]" onClick={() => trackContactCta('phone_click', 'Vehicle Price Card Phone')}><FaPhoneAlt aria-hidden="true" className="text-xl" /><span className="leading-tight">Call Now<small className="mt-1 block text-sm font-medium">{business.phone}</small></span></a>
  <a href="#request-info" className="site-button vehicle-detail-contact mt-3 flex min-h-[52px] items-center justify-center gap-2 rounded-[3px] border border-[#c9001b] bg-white text-base font-semibold text-[#c9001b] transition hover:bg-[#fff4f5]" onClick={() => trackContactCta('contact_form_click', 'Vehicle Price Card Request Info')}><FaEnvelope aria-hidden="true" className="text-lg" /> Get Quote</a>
  <a href={business.mapsUrl} target="_blank" rel="noreferrer" className="site-button vehicle-detail-contact mt-3 flex min-h-[52px] items-center justify-center gap-2 rounded-[3px] border border-[#c9001b] bg-white text-base font-semibold text-[#c9001b] transition hover:bg-[#fff4f5]" onClick={() => trackContactCta('directions_click', 'Vehicle Price Card Get Directions')}><FaMapMarkerAlt aria-hidden="true" className="text-lg" /> Get Directions</a>
</aside>

const VehicleQuickFacts = ({ vehicle }: { vehicle: Vehicle }) => {
  const facts = [
    { label: 'Mileage', value: vehicle.mileage > 0 ? `${formatNumber(vehicle.mileage)} miles` : 'Mileage not listed', icon: FaTachometerAlt },
    { label: 'Engine', value: vehicle.engine, icon: FaCogs },
    { label: 'Transmission', value: vehicle.transmission, icon: FaCog },
    { label: 'Drivetrain', value: vehicle.drivetrain, icon: FaRoad },
    { label: 'Exterior', value: hasListingValue(vehicle.exteriorColor) ? `Exterior: ${vehicle.exteriorColor}` : '', icon: FaTint },
    { label: 'Interior', value: hasListingValue(vehicle.interiorColor) ? `Interior: ${vehicle.interiorColor}` : '', icon: FaChair },
    { label: 'Stock', value: vehicle.stockNumber ? `Stock: ${vehicle.stockNumber}` : '', icon: FaFileAlt },
    { label: 'VIN', value: hasListingValue(vehicle.vin) ? `VIN: ${vehicle.vin}` : '', icon: FaBarcode },
  ].filter((fact) => hasListingValue(fact.value))
  return <dl className="mt-5 grid grid-cols-1 gap-x-4 gap-y-3 border-y border-[#ddd] py-4 sm:grid-cols-2">{facts.map(({ label, value, icon: Icon }) => <div key={label} className="flex min-w-0 items-start gap-3 text-sm leading-5 text-[#444] sm:text-[15px]"><Icon aria-hidden="true" className="mt-0.5 shrink-0 text-base text-[#555]" /><dt className="sr-only">{label}</dt><dd className="min-w-0 whitespace-normal break-words" title={value}>{value}</dd></div>)}</dl>
}

export const VehicleDetailPage = () => {
  const { slug } = useParams()
  const [vehicle, setVehicle] = useState<Vehicle | null>(null)
  const [recommendations, setRecommendations] = useState<Vehicle[]>([])
  const [loaded, setLoaded] = useState(false)
  const [loadError, setLoadError] = useState(false)
  const [detailView, setDetailView] = useState<'overview' | 'photos'>(() => window.location.hash === '#photos' ? 'photos' : 'overview')
  const showPhotos = () => {
    setDetailView('photos')
    window.history.replaceState(null, '', '#photos')
    window.setTimeout(() => document.getElementById('photos')?.scrollIntoView({ behavior: 'smooth', block: 'start' }), 0)
  }
  useEffect(() => {
    let cancelled = false
    getVehicle(slug ?? '')
      .then(async (item) => {
        const [listingDescription, listingInfo] = await Promise.all([
          fetch(`/listing-descriptions/${item.slug}.txt`).then((response) => response.ok ? response.text() : '').catch(() => ''),
          fetch(`/listing-info/${item.slug}.txt`).then((response) => response.ok ? response.text() : '').catch(() => ''),
        ])
        if (!cancelled) {
          const sourceFeatures = featuresFromListingInfo(listingInfo)
          const description = [listingDescription, item.shortDescription ?? '', item.description].map(plainDescription).find(Boolean)
          setVehicle({
            ...item,
            description: description || `${item.year} ${item.make} ${item.model} ${item.trim} is listed with a ${item.engine}, ${item.transmission}, and ${item.drivetrain}.`,
            features: sourceFeatures.length ? sourceFeatures : item.features,
          })
          setLoadError(false)
          trackViewContent(item.id, `${item.year} ${item.make} ${item.model} ${item.trim}`, item.price)
        }
      })
      .catch(() => { if (!cancelled) { setVehicle(null); setLoadError(true) } })
      .finally(() => { if (!cancelled) setLoaded(true) })
    return () => { cancelled = true }
  }, [slug])
  useEffect(() => {
    if (!vehicle || vehicle.slug !== slug) return
    let cancelled = false
    listVehicles({ pageSize: 8, sort: 'year_desc' })
      .then(({ items }) => {
        const candidates = items.filter((item) => item.id !== vehicle.id && item.slug !== vehicle.slug)
        const score = (item: Vehicle) =>
          (item.bodyType.toLowerCase() === vehicle.bodyType.toLowerCase() ? 3 : 0)
          + (item.make.toLowerCase() === vehicle.make.toLowerCase() ? 2 : 0)
          + (vehicle.price > 0 && Math.abs(item.price - vehicle.price) / vehicle.price < 0.3 ? 1 : 0)
        candidates.sort((a, b) => score(b) - score(a))
        if (!cancelled) setRecommendations(candidates.slice(0, 6))
      })
      .catch(() => { if (!cancelled) setRecommendations([]) })
    return () => { cancelled = true }
  }, [slug, vehicle])
  const title = useMemo(() => vehicle ? `${vehicle.year} ${vehicle.make} ${vehicle.model} ${vehicle.trim}` : '', [vehicle])
  if (!vehicle && loaded && loadError) return <section className="section soft-band"><div className="mx-auto max-w-3xl px-4 text-center sm:px-6 lg:px-8"><div className="surface-card p-8"><h1 className="text-3xl text-[var(--color-text)]">Vehicle details are temporarily unavailable</h1><p className="mt-3 text-[var(--color-muted)]">Please try again later or call us for current vehicle information.</p><div className="mt-6 flex flex-col justify-center gap-3 sm:flex-row"><Button href="/inventory" variant="secondary">Back to Inventory</Button><Button href={phoneHref}><FaPhoneAlt /> Contact</Button></div></div></div></section>
  if (!vehicle) return <VehicleDetailSkeleton />
  const baseSpecs: [string, string][] = [
    ['Body Style', vehicle.bodyType], ['Doors', vehicle.specs?.doors ?? ''], ['Engine', vehicle.engine],
    ['Transmission', vehicle.transmission], ['Drivetrain', vehicle.drivetrain], ['Fuel Type', vehicle.specs?.fuel_type ?? ''],
    ['Exterior Color', vehicle.exteriorColor], ['Interior Color', vehicle.interiorColor],
    ['Mileage', vehicle.mileage > 0 ? `${formatNumber(vehicle.mileage)} miles` : ''], ['Stock', vehicle.stockNumber],
    ['VIN', hasListingValue(vehicle.vin) ? vehicle.vin : ''], ['City MPG', vehicle.specs?.city_mpg ?? ''], ['Highway MPG', vehicle.specs?.highway_mpg ?? ''],
  ]
  const detailSpecs: [string, string][] = (vehicle.details?.info ?? [])
    .filter(({ label }) => !/^(listing|vehicle history|lot(?:\s+number)?)$/i.test(label.replace(/\s+/g, ' ').trim()))
    .map(({ label, value }) => [label, value])
  const specMap = new Map<string, [string, string]>()
  for (const [label, value] of [...baseSpecs, ...detailSpecs]) if (hasListingValue(value)) specMap.set(label.toLowerCase(), [label, value])
  const specs = [...specMap.values()]
  const specColumns = [specs.slice(0, Math.ceil(specs.length / 2)), specs.slice(Math.ceil(specs.length / 2))]
  return <><Seo title={title} description={`${title} for sale at The Car Store of Cherryville in Cherryville, NC. Call or request info today.`} noIndex schema={{ '@context': 'https://schema.org', '@type': 'Vehicle', name: title, brand: vehicle.make, model: vehicle.model, vehicleModelDate: vehicle.year, ...(vehicle.mileage > 0 ? { mileageFromOdometer: `${vehicle.mileage} MI` } : {}), ...(vehicle.price > 0 ? { offers: { '@type': 'Offer', price: vehicle.price, priceCurrency: 'USD' } } : {}) }} /><main className="bg-white text-[#202124]">
    <section className="mx-auto grid w-full max-w-[1600px] items-start gap-6 px-4 pb-6 pt-8 sm:px-7 2xl:grid-cols-[minmax(0,1.65fr)_minmax(350px,.9fr)] 2xl:gap-7 lg:px-9 lg:pb-7">
      <div id="vehicle-gallery" className="min-w-0"><VehicleGallery images={vehicle.images} imagesTotal={vehicle.imagesTotal} slug={vehicle.slug} title={title} onShowPhotos={showPhotos} showAllPhotos={detailView === 'photos'} /></div>
      <PriceCard vehicle={vehicle} />
    </section>
    {detailView === 'photos' ? <section id="photos" className="mx-auto max-w-[1600px] scroll-mt-24 px-5 pb-8 sm:px-7 lg:px-9"><SectionHeading>Photos</SectionHeading><div id="vehicle-photos-grid" className="mt-4" /></section> : null}
    <section className="mx-auto grid max-w-[1600px] gap-7 px-5 pb-6 pt-4 sm:px-7 lg:grid-cols-[minmax(0,1.15fr)_minmax(0,.9fr)] lg:gap-12 lg:px-9 lg:pb-7">
      <article id="overview" className="min-w-0 scroll-mt-24"><SectionHeading>Vehicle Overview</SectionHeading><p id="description" className="mt-4 whitespace-pre-line text-base leading-7 text-[#555]">{vehicle.description}</p></article>
      <section id="features" className="min-w-0 scroll-mt-24"><SectionHeading>Vehicle Features</SectionHeading><div className="mt-4 grid gap-x-8 gap-y-3 sm:grid-cols-2">{vehicle.features.map((feature) => <Feature key={feature} feature={feature} />)}</div></section>
    </section>
    <section id="specifications" className="mx-auto max-w-[1600px] scroll-mt-24 px-5 pb-8 sm:px-7 lg:px-9"><SectionHeading>Vehicle Specs</SectionHeading><div className="mt-4 grid gap-x-5 lg:grid-cols-2">{specColumns.map((column, columnIndex) => <dl key={columnIndex} className="min-w-0">{column.map(([label, value], rowIndex) => <div key={label} className={`grid min-h-[44px] grid-cols-[minmax(110px,.72fr)_minmax(0,1fr)] items-center border-x border-b border-[#dedede] px-3 py-2 text-sm leading-5 first:border-t sm:text-[15px] ${rowIndex % 2 === 0 ? 'bg-[#f4f5f6]' : 'bg-white'}`}><dt className="text-[#363636]">{label}</dt><dd className="min-w-0 truncate text-[#555]" title={value}>{value}</dd></div>)}</dl>)}</div></section>
    <RelatedVehiclesCarousel vehicles={recommendations} />
    <section id="request-info" className="scroll-mt-24 bg-[#f5f5f5] px-5 py-12 sm:px-7 lg:px-9"><div className="mx-auto grid max-w-[1120px] gap-6 lg:grid-cols-[.7fr_1.3fr] lg:gap-10"><div><SectionHeading>Get a Quote</SectionHeading><p className="mt-4 text-base leading-7 text-[#555]">Send us a message about this vehicle and our team will be in touch.</p></div><LeadForm title="Send Inquiry" vehicleId={vehicle.id} vehicleName={title} vehicleValue={vehicle.price} variant="vehicle" className="vehicle-inquiry-form" messageDefaultValue={`I'm interested in the ${title}. Please contact me with more information.`} /></div></section>
  </main><div className="fixed inset-x-0 bottom-0 z-50 border-t border-[var(--color-border)] bg-[var(--color-background)] px-4 py-3 shadow-sm lg:hidden"><div className="mx-auto flex max-w-7xl items-center gap-3"><div className="min-w-0 flex-1"><p className="truncate text-base text-[var(--color-text)]">{title}</p><p className="text-base font-semibold text-[var(--color-primary)]">{formatPrice(vehicle.price)}</p></div><a href={phoneHref} className="site-button inline-flex h-14 w-14 shrink-0 items-center justify-center bg-[var(--color-primary)] text-2xl text-white" aria-label="Contact about this vehicle" onClick={() => trackContactCta('phone_click', 'Vehicle Sticky Contact')}><FaPhoneAlt /></a><a href="#request-info" className="site-button inline-flex h-14 w-14 shrink-0 items-center justify-center bg-[var(--color-button)] text-2xl text-white" aria-label="Request info about this vehicle" onClick={() => trackContactCta('contact_form_click', 'Vehicle Sticky Request Info')}><FaArrowRight /></a></div></div></>
}
