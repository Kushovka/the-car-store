import { useEffect, useRef, useState } from 'react'
import type { ReactNode } from 'react'
import { useSearchParams } from 'react-router'
import { FaChevronDown, FaChevronLeft, FaChevronRight, FaSearch, FaTimes } from 'react-icons/fa'
import { getVehicleFilters, listVehicles } from '../api/vehicles'
import { Seo } from '../components/Seo'
import { VehicleGridSkeleton } from '../components/Skeletons'
import { VehicleCard } from '../components/VehicleCard'
import type { Vehicle } from '../types/vehicle'

type SortKey = 'price-low' | 'price-high' | 'year' | 'mileage'
const PAGE_SIZE = 12
const queryNumber = (value: string | null) => {
  if (!value) return undefined
  const parsed = Number(value)
  return Number.isFinite(parsed) && parsed >= 0 ? parsed : undefined
}
const selectClass = 'mt-1 h-10 w-full appearance-none border border-[#d8d8d8] bg-white px-2.5 pr-9 text-[14px] text-[#333] outline-none transition focus:border-[#c9001b]'
const filterLabel = 'block text-[13px] font-semibold text-[#333]'

const InventoryVehicleCard = ({ vehicle }: { vehicle: Vehicle }) => {
  return <VehicleCard vehicle={vehicle} />
}

export const InventoryPage = () => {
  const [searchParams] = useSearchParams()
  const resultsRef = useRef<HTMLDivElement | null>(null)
  const [make, setMake] = useState(() => searchParams.get('make') ?? '')
  const [model, setModel] = useState(() => searchParams.get('model') ?? '')
  const [yearFrom, setYearFrom] = useState<number | undefined>(() => queryNumber(searchParams.get('yearFrom')))
  const [priceMin, setPriceMin] = useState<number | undefined>(() => queryNumber(searchParams.get('priceMin')))
  const [priceMax, setPriceMax] = useState<number | undefined>(() => queryNumber(searchParams.get('priceMax')))
  const [mileageMin, setMileageMin] = useState<number | undefined>()
  const [mileageMax, setMileageMax] = useState<number | undefined>()
  const [bodyType, setBodyType] = useState(() => searchParams.get('bodyType') ?? '')
  const [color, setColor] = useState('')
  const [transmission, setTransmission] = useState('')
  const [drivetrain, setDrivetrain] = useState('')
  const [search, setSearch] = useState('')
  const [sort, setSort] = useState<SortKey>('year')
  const [page, setPage] = useState(1)
  const [items, setItems] = useState<Vehicle[]>([])
  const [total, setTotal] = useState(0)
  const [filterCounts, setFilterCounts] = useState<Record<string, number>>({})
  const [loading, setLoading] = useState(true)
  const [inventoryError, setInventoryError] = useState(false)
  const [makes, setMakes] = useState<string[]>([])
  const [models, setModels] = useState<string[]>([])
  const [years, setYears] = useState<number[]>([])
  const [bodyTypes, setBodyTypes] = useState<string[]>([])
  const [transmissions, setTransmissions] = useState<string[]>([])
  const [drivetrains, setDrivetrains] = useState<string[]>([])
  const [colors, setColors] = useState<string[]>([])
  const [filtersOpen, setFiltersOpen] = useState(false)

  useEffect(() => {
    setSearch(searchParams.get('q') ?? '')
    setBodyType(searchParams.get('bodyType') ?? '')
    setPage(1)
  }, [searchParams])

  useEffect(() => {
    let cancelled = false
    getVehicleFilters().then((filters) => { if (!cancelled) { setMakes(filters.makes); setModels(filters.models); setYears(filters.years); setBodyTypes(filters.bodyTypes); setTransmissions(filters.transmissions); setDrivetrains(filters.drivetrains); setColors(filters.colors) } }).catch(() => undefined)
    return () => { cancelled = true }
  }, [])
  useEffect(() => {
    let cancelled = false
    const loadCounts = async () => {
      const firstPage = await listVehicles({ page: 1, pageSize: 50 })
      const extraPages = await Promise.all(Array.from({ length: Math.max(0, Math.ceil(firstPage.total / firstPage.pageSize) - 1) }, (_, index) => listVehicles({ page: index + 2, pageSize: firstPage.pageSize })))
      if (cancelled) return
      const vehicles = [...firstPage.items, ...extraPages.flatMap((response) => response.items)]
      const counts: Record<string, number> = {}
      const add = (key: string, matches: boolean) => { if (matches) counts[key] = (counts[key] ?? 0) + 1 }
      const ranges = [
        { key: 'price:under', matches: (value: number) => value > 0 && value < 20000 },
        { key: 'price:20-40', matches: (value: number) => value >= 20000 && value <= 40000 },
        { key: 'price:40-60', matches: (value: number) => value > 40000 && value <= 60000 },
        { key: 'price:over', matches: (value: number) => value > 60000 },
        { key: 'miles:under', matches: (value: number) => value > 0 && value < 25000 },
        { key: 'miles:25-50', matches: (value: number) => value >= 25000 && value <= 50000 },
        { key: 'miles:50-100', matches: (value: number) => value > 50000 && value <= 100000 },
        { key: 'miles:over', matches: (value: number) => value > 100000 },
      ]
      vehicles.forEach((vehicle) => {
        add(`body:${vehicle.bodyType}`, true)
        add(`make:${vehicle.make}`, true)
        add(`year:${vehicle.year}`, true)
        add(`drive:${vehicle.drivetrain}`, true)
        add(`transmission:${vehicle.transmission}`, true)
        add('color:White', /white/i.test(vehicle.exteriorColor))
        add('color:Black', /black/i.test(vehicle.exteriorColor))
        add('color:Silver', /silver/i.test(vehicle.exteriorColor))
        add('color:Gray', /gr[ae]y/i.test(vehicle.exteriorColor))
        add('color:Blue', /blue/i.test(vehicle.exteriorColor))
        add('color:Red', /red/i.test(vehicle.exteriorColor))
        ranges.forEach(({ key, matches }) => add(key, matches(key.startsWith('price:') ? vehicle.price : vehicle.mileage)))
      })
      setFilterCounts(counts)
    }
    loadCounts().catch(() => undefined)
    return () => { cancelled = true }
  }, [])
  useEffect(() => {
    let cancelled = false
    getVehicleFilters(make).then((filters) => { if (!cancelled) setModels(filters.models) }).catch(() => { if (!cancelled) setModels([]) })
    return () => { cancelled = true }
  }, [make])
  useEffect(() => {
    let cancelled = false
    Promise.resolve().then(() => { if (!cancelled) setLoading(true) })
    listVehicles({ make, model, q: search, yearFrom, bodyType, transmission, drivetrain, color, priceMin, priceMax, mileageMin, mileageMax, page, pageSize: PAGE_SIZE, sort: sort === 'price-low' ? 'price_asc' : sort === 'price-high' ? 'price_desc' : sort === 'mileage' ? 'mileage_asc' : 'year_desc' })
      .then((response) => { if (!cancelled) { setItems(response.items); setTotal(response.total); setInventoryError(false) } })
      .catch(() => { if (!cancelled) { setItems([]); setTotal(0); setInventoryError(true) } })
      .finally(() => { if (!cancelled) setLoading(false) })
    return () => { cancelled = true }
  }, [bodyType, color, drivetrain, make, mileageMax, mileageMin, model, page, priceMax, priceMin, search, sort, transmission, yearFrom])

  const resetFilters = () => { setPage(1); setMake(''); setModel(''); setSearch(''); setYearFrom(undefined); setPriceMin(undefined); setPriceMax(undefined); setMileageMin(undefined); setMileageMax(undefined); setBodyType(''); setColor(''); setTransmission(''); setDrivetrain('') }
  const totalPages = Math.max(1, Math.ceil(total / PAGE_SIZE))
  const pageNumbers = Array.from({ length: totalPages }, (_, index) => index + 1)
  const goToPage = (nextPage: number) => { setPage(Math.min(totalPages, Math.max(1, nextPage))); window.setTimeout(() => resultsRef.current?.scrollIntoView({ behavior: 'smooth', block: 'start' }), 0) }
  const filterChange = <T,>(setter: (value: T) => void, value: T) => { setPage(1); setter(value) }
  const filterSection = (title: string, content: ReactNode) => <details key={title} open className="group rounded-[3px] border border-[#e0e0e0] bg-white px-3 py-2.5"><summary className="flex cursor-pointer list-none items-center justify-between text-[14px] font-bold text-[#222]"><span>{title}</span><FaChevronDown className="text-[11px] transition-transform group-open:rotate-180" /></summary><div className="mt-2 border-t border-[#eee] pt-2">{content}</div></details>
  const checkOption = (label: string, checked: boolean, onChange: () => void, count?: number, colorDot?: string) => <label key={label} className="flex min-h-[22px] cursor-pointer items-center gap-2 text-[12px] leading-tight text-[#555]"><input type="checkbox" checked={checked} onChange={onChange} className="h-4 w-4 shrink-0 accent-[#c9001b]" />{colorDot ? <span aria-hidden="true" className="h-4 w-4 shrink-0 rounded-full border border-black/10" style={{ backgroundColor: colorDot }} /> : null}<span className="min-w-0 flex-1">{label}</span>{count !== undefined ? <span className="shrink-0 text-[12px] text-[#888]">({count})</span> : null}</label>
  const filters = <aside className="inventory-filters-scroll h-fit min-w-0 lg:h-full lg:overflow-y-auto lg:overscroll-contain lg:pr-2">
    <div id="inventory-filters" className={`${filtersOpen ? 'block' : 'hidden'} space-y-1.5 lg:block`}>
      <div className="mb-2 hidden h-10 items-center justify-between rounded-[3px] border border-[#e0e0e0] bg-white px-3 lg:flex">
        <h2 className="text-[15px] font-bold text-[#222]">Filter Vehicles</h2>
        <button id="inventory-clear-filters" type="button" onClick={resetFilters} className="inventory-clear-filters">Clear All</button>
      </div>
      {filterSection('Body Style', <div className="space-y-0.5">{bodyTypes.map((item) => checkOption(item, bodyType === item, () => filterChange(setBodyType, bodyType === item ? '' : item), filterCounts[`body:${item}`] ?? 0))}</div>)}
      {filterSection('Make', <><div className="space-y-0.5">{makes.slice(0, 8).map((item) => checkOption(item, make === item, () => { filterChange(setMake, make === item ? '' : item); setModel('') }, filterCounts[`make:${item}`] ?? 0))}{makes.length > 8 ? <details className="pt-1"><summary className="cursor-pointer text-[12px] font-semibold text-[#c9001b]">Show More <span aria-hidden="true">⌄</span></summary><div className="mt-1 space-y-0.5">{makes.slice(8).map((item) => checkOption(item, make === item, () => { filterChange(setMake, make === item ? '' : item); setModel('') }, filterCounts[`make:${item}`] ?? 0))}</div></details> : null}</div>{make ? <label className={`${filterLabel} relative mt-2`}>Model<select className={selectClass} value={model} onChange={(event) => filterChange(setModel, event.target.value)}><option value="">All models</option>{models.map((item) => <option key={item}>{item}</option>)}</select><FaChevronDown aria-hidden="true" className="pointer-events-none absolute bottom-[14px] right-3 text-[12px] text-[#333]" /></label> : null}</>)}
      {filterSection('Price Range', <div className="space-y-0.5">{[
        { label: 'Under $20,000', min: undefined, max: 19999 },
        { label: '$20,000 - $40,000', min: 20000, max: 40000 },
        { label: '$40,000 - $60,000', min: 40001, max: 60000 },
        { label: 'Over $60,000', min: 60001, max: undefined },
      ].map(({ label, min, max }, index) => checkOption(label, priceMin === min && priceMax === max, () => { const selected = priceMin === min && priceMax === max; filterChange(setPriceMin, selected ? undefined : min); filterChange(setPriceMax, selected ? undefined : max) }, filterCounts[['price:under', 'price:20-40', 'price:40-60', 'price:over'][index]] ?? 0))}</div>)}
      {filterSection('Mileage', <div className="space-y-0.5">{[
        { label: 'Under 25,000', min: undefined, max: 24999 },
        { label: '25,000 - 50,000', min: 25000, max: 50000 },
        { label: '50,000 - 100,000', min: 50001, max: 100000 },
        { label: 'Over 100,000', min: 100001, max: undefined },
      ].map(({ label, min, max }, index) => checkOption(label, mileageMin === min && mileageMax === max, () => { const selected = mileageMin === min && mileageMax === max; filterChange(setMileageMin, selected ? undefined : min); filterChange(setMileageMax, selected ? undefined : max) }, filterCounts[['miles:under', 'miles:25-50', 'miles:50-100', 'miles:over'][index]] ?? 0))}</div>)}
      {filterSection('Year', <div className="space-y-0.5">{years.slice(0, 5).map((item) => checkOption(String(item), yearFrom === item, () => filterChange(setYearFrom, yearFrom === item ? undefined : item), filterCounts[`year:${item}`] ?? 0))}{years.length > 5 ? <details className="pt-1"><summary className="cursor-pointer text-[12px] font-semibold text-[#c9001b]">Show More</summary><div className="mt-1 space-y-0.5">{years.slice(5).map((item) => checkOption(String(item), yearFrom === item, () => filterChange(setYearFrom, yearFrom === item ? undefined : item), filterCounts[`year:${item}`] ?? 0))}</div></details> : null}</div>)}
      {filterSection('Drivetrain', <div className="space-y-0.5">{drivetrains.map((item) => checkOption(item, drivetrain === item, () => filterChange(setDrivetrain, drivetrain === item ? '' : item), filterCounts[`drive:${item}`] ?? 0))}</div>)}
      {filterSection('Transmission', <div className="space-y-0.5">{transmissions.map((item) => checkOption(item, transmission === item, () => filterChange(setTransmission, transmission === item ? '' : item), filterCounts[`transmission:${item}`] ?? 0))}</div>)}
      {filterSection('Exterior Color', <div className="space-y-0.5">{['White', 'Black', 'Silver', 'Gray', 'Blue', 'Red', 'Other'].map((item) => { const colorMap: Record<string, string> = { White: '#fff', Black: '#111', Silver: '#b8b8b8', Gray: '#858585', Blue: '#1455a5', Red: '#d71920' }; const needle = item === 'Gray' ? 'grey' : item.toLowerCase(); const vehicleColor = colors.find((available) => available.toLowerCase().includes(needle)) ?? item; return checkOption(item, color === vehicleColor, () => filterChange(setColor, color === vehicleColor ? '' : vehicleColor), filterCounts[`color:${item}`] ?? 0, colorMap[item]) })}</div>)}
    </div>
  </aside>

  return <>
    <Seo title="Used Car Inventory" description="Browse used cars, SUVs, trucks, and crossovers at The Car Store of Cherryville, Inc in Cherryville, NC." />
    <section className="inventory-page bg-[#f7f7f7] px-[clamp(20px,6.8vw,96px)] pb-2 pt-8 sm:pt-8"><div className="mx-auto w-full max-w-[1440px]">
      <header className="mb-4"><h1 className="text-[clamp(36px,3.7vw,58px)] font-bold leading-[1.12] text-[#222]">Used Cars, Trucks &amp; SUVs for Sale</h1><p className="mt-2 max-w-[1200px] text-[clamp(16px,1.25vw,21px)] leading-[1.48] text-[#626262]">Browse our selection of quality pre-owned vehicles in Cherryville, NC. We carry a wide variety of cars, trucks, SUVs and vans from trusted brands, all inspected and ready for the road. Use the filters to find the right vehicle for your needs.</p></header>
      <div className="mb-4 flex gap-2">
        <label className="relative block min-w-0 flex-1"><span className="sr-only">Search make, model, or keyword</span><FaSearch aria-hidden="true" className="pointer-events-none absolute left-3.5 top-1/2 -translate-y-1/2 text-[15px] text-[#777]" /><input className="h-11 w-full rounded-[3px] border border-[#ddd] bg-white pl-11 pr-10 text-[14px] text-[#222] outline-none placeholder:text-[#888] focus:border-[#c9001b]" value={search} onChange={(event) => filterChange(setSearch, event.target.value)} placeholder="Search by make, model, or keyword..." />{search ? <button type="button" aria-label="Clear vehicle search" onClick={() => filterChange(setSearch, '')} className="absolute right-0 top-0 grid h-11 w-10 place-items-center text-[#777]"><FaTimes /></button> : null}</label>
        <button className="h-11 shrink-0 rounded-[3px] bg-[#c9001b] px-5 text-[14px] font-bold !normal-case text-white transition hover:bg-[#a90017] sm:px-7" type="button" onClick={() => resultsRef.current?.scrollIntoView({ behavior: 'smooth', block: 'start' })}>Search Inventory</button>
      </div>
      <div className="grid items-start gap-4 lg:grid-cols-[272px_minmax(0,1fr)] xl:gap-5">
        <div className="lg:sticky lg:top-[calc(var(--header-height)_+_74px)] lg:h-[calc(100vh-var(--header-height)-74px)]"><button type="button" aria-expanded={filtersOpen} onClick={() => setFiltersOpen((open) => !open)} className="mb-2 flex h-10 w-full items-center justify-between rounded-[3px] border border-[#e0e0e0] bg-white px-3 text-left text-[14px] font-bold !normal-case text-[#222] lg:hidden"><span>Filter Vehicles</span><FaChevronDown className={`text-[11px] transition-transform ${filtersOpen ? 'rotate-180' : ''}`} /></button>{filters}</div>
        <div ref={resultsRef} className="min-w-0 scroll-mt-4">
          <div className="mb-2 flex min-h-10 flex-wrap items-center justify-between gap-2">
            <h2 className="text-[18px] font-bold text-[#222]">{loading ? 'Loading vehicles…' : `${total} Vehicles Found`}</h2>
            <div className="flex items-center gap-2">
              <label className="relative flex items-center gap-2 text-[12px] text-[#444]">Sort By:<select className="h-10 max-w-[160px] appearance-none rounded-[3px] border border-[#ddd] bg-white px-2 pr-9 text-[13px] text-[#333] outline-none focus:border-[#c9001b] sm:max-w-none" value={sort} onChange={(event) => filterChange(setSort, event.target.value as SortKey)}><option value="year">Newest Arrivals</option><option value="price-low">Price low-high</option><option value="price-high">Price high-low</option><option value="mileage">Lowest mileage</option></select><FaChevronDown aria-hidden="true" className="pointer-events-none absolute right-3 top-1/2 -translate-y-1/2 text-[12px] text-[#333]" /></label>
            </div>
          </div>
        <div className="grid items-stretch gap-2.5 sm:grid-cols-2 lg:grid-cols-3">{loading ? <VehicleGridSkeleton count={PAGE_SIZE} /> : inventoryError ? <div className="border border-[var(--color-border)] bg-[var(--color-surface)] p-7 text-center text-sm text-[var(--color-muted)]">Inventory is temporarily unavailable. Please try again later or call us for current vehicles.</div> : items.length ? items.map((vehicle) => <InventoryVehicleCard key={vehicle.id} vehicle={vehicle} />) : <div className="border border-[var(--color-border)] bg-[var(--color-surface)] p-7 text-center text-sm text-[var(--color-muted)]">No vehicles match these filters right now.</div>}</div>
        {!loading && totalPages > 1 ? <div className="relative mt-7 flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-center"><div className="flex items-center justify-center gap-1.5"><button aria-label="Previous page" className="grid h-9 w-9 place-items-center border border-[var(--color-border)] transition hover:bg-[var(--color-section)] disabled:opacity-35" disabled={page === 1} onClick={() => goToPage(page - 1)} type="button"><FaChevronLeft /></button>{pageNumbers.map((pageNumber) => <button key={pageNumber} aria-label={`Page ${pageNumber}`} className={`grid h-9 min-w-9 place-items-center px-2 text-[13px] ${pageNumber === page ? 'bg-[var(--color-primary)] text-white' : 'hover:bg-[var(--color-section)]'}`} onClick={() => goToPage(pageNumber)} type="button">{pageNumber}</button>)}<button aria-label="Next page" className="grid h-9 w-9 place-items-center border border-[var(--color-border)] transition hover:bg-[var(--color-section)] disabled:opacity-35" disabled={page === totalPages} onClick={() => goToPage(page + 1)} type="button"><FaChevronRight /></button></div><p className="text-center text-[12px] text-[var(--color-muted)] sm:absolute sm:right-0">Showing {((page - 1) * PAGE_SIZE) + 1}-{Math.min(page * PAGE_SIZE, total)} of {total} vehicles</p></div> : null}
        </div>
      </div></div>
    </section>
  </>
}
