import { Seo } from '../components/Seo'
import { HeaderSearch } from '../components/Header'
import { autoDealerSchema } from '../utils/schema'
import { Link, useLocation } from 'react-router'
import { useEffect, useState } from 'react'
import { FaArrowRight } from 'react-icons/fa'
import { FaClock, FaMapMarkerAlt, FaPhoneAlt } from 'react-icons/fa'
import { FaStar, FaUsers } from 'react-icons/fa'
import { listVehicles } from '../api/vehicles'
import type { Vehicle } from '../types/vehicle'
import { business } from '../data/business'
import { trackContactCta } from '../utils/ctaTracking'
import { reviews } from '../data/reviews'
import { VehicleCard } from '../components/VehicleCard'

const vehicleStyles = [
  { label: 'SUVs', filter: 'SUV', image: '/images/vehicle-types/suv.webp' },
  { label: 'Trucks', filter: 'Truck', image: '/images/vehicle-types/truck.webp' },
  { label: 'Sedans', filter: 'Sedan', image: '/images/vehicle-types/sedan.webp' },
  { label: 'Cars', filter: 'Coupe', image: '/images/vehicle-types/coupe.webp' },
  { label: 'Vans', filter: 'Van', image: '/images/vehicle-types/van.webp' },
  { label: 'Hybrid', filter: 'Hybrid', image: '/images/vehicle-types/hybrid.webp' },
]

export const HomePage = () => {
  const { hash } = useLocation()

  useEffect(() => {
    if (hash !== '#hero-search') return
    requestAnimationFrame(() => {
      const search = document.getElementById('hero-search')
      search?.scrollIntoView({ behavior: 'smooth', block: 'center' })
      search?.querySelector('input')?.focus({ preventScroll: true })
    })
  }, [hash])

  return (
  <>
    <Seo
      title="Used Cars in Cherryville, NC"
      description="Shop quality pre-owned cars, trucks, and SUVs at The Car Store of Cherryville."
      schema={autoDealerSchema}
    />
    <section className="reference-home-hero" aria-labelledby="home-title">
      <img
        className="reference-home-hero__image"
        src="/images/cherryville-lot-closeup.png"
        alt=""
        fetchPriority="high"
      />
      <div className="reference-home-hero__shade" aria-hidden="true" />
      <div className="reference-home-hero__panel">
        <h1 id="home-title">Quality used cars, trucks &amp; SUVs in Cherryville, NC</h1>
        <p>Local deals. Straightforward service. Browse dependable pre-owned vehicles.</p>
        <HeaderSearch variant="hero" />
      </div>
    </section>
    <section className="browse-styles" aria-labelledby="browse-styles-title">
      <div className="browse-styles__inner">
        <h2 id="browse-styles-title">Browse by Style</h2>
        <div className="browse-styles__grid">
          {vehicleStyles.map(({ label, filter, image }) => (
            <Link className="browse-styles__card" key={label} to={`/inventory?${label === 'Hybrid' ? 'q' : 'bodyType'}=${encodeURIComponent(filter)}`}>
              <img className="browse-styles__image" src={image} alt="" loading="lazy" />
              <span>{label}</span>
            </Link>
          ))}
        </div>
      </div>
    </section>
    <FeaturedVehicles />
    <DealershipIntro />
    <CustomerReviews />
  </>
  )
}

const FeaturedVehicles = () => {
  const [vehicles, setVehicles] = useState<Vehicle[]>([])

  useEffect(() => {
    let active = true
    listVehicles({ featured: true, pageSize: 4, sort: 'year_desc' })
      .then(({ items }) => { if (active) setVehicles(items) })
      .catch(() => { if (active) setVehicles([]) })
    return () => { active = false }
  }, [])

  if (!vehicles.length) return null

  return (
    <section className="featured-stock" aria-labelledby="featured-stock-title">
      <div className="featured-stock__inner">
        <div className="featured-stock__heading">
          <h2 id="featured-stock-title">Featured Vehicles</h2>
          <Link to="/inventory">View All Inventory <FaArrowRight aria-hidden="true" /></Link>
        </div>
        <div className="featured-stock__grid">
          {vehicles.slice(0, 4).map((vehicle) => <VehicleCard key={vehicle.id} vehicle={vehicle} />)}
        </div>
      </div>
    </section>
  )
}

const DealershipIntro = () => (
  <section className="dealership-intro" aria-labelledby="dealership-intro-title">
    <div className="dealership-intro__inner">
      <div className="dealership-intro__copy">
        <p className="dealership-intro__eyebrow">About the Dealership</p>
        <h2 id="dealership-intro-title">Serving Cherryville and the Surrounding Area</h2>
        <p className="dealership-intro__text">The Car Store of Cherryville, Inc. is a local, independent used car dealership committed to providing quality pre-owned vehicles and straightforward, no-pressure service. We take pride in helping our neighbors in Cherryville and nearby communities find the right car, truck, or SUV.</p>
        <p className="dealership-intro__text">Whether you&apos;re shopping for your next vehicle or have a question, our team is here to help. Stop by the lot and see what&apos;s available.</p>
        <div className="dealership-intro__actions">
          <Link to="/about" onClick={() => trackContactCta('about_click', 'Homepage About Dealership')}>Learn More About Us</Link>
          <a href={business.mapsUrl} target="_blank" rel="noreferrer" onClick={() => trackContactCta('directions_click', 'Homepage Dealership Directions')}>Get Directions</a>
        </div>
        <div className="dealership-intro__details">
          <a href={business.mapsUrl} target="_blank" rel="noreferrer" onClick={() => trackContactCta('directions_click', 'Homepage Dealership Address')}>
            <FaMapMarkerAlt aria-hidden="true" /><span><small>Our Location</small><strong>{business.address}<br />{business.cityState} {business.postalCode}</strong></span>
          </a>
          <a href={business.phoneHref} onClick={() => trackContactCta('phone_click', 'Homepage Dealership Phone')}>
            <FaPhoneAlt aria-hidden="true" /><span><small>Give Us a Call</small><strong>{business.phone.replace('+1 ', '')}</strong></span>
          </a>
          <div>
            <FaClock aria-hidden="true" /><span><small>Hours</small><strong>Mon–Fri: 8:30 AM – 5:30 PM<br />Sat: 9:00 AM – 2:00 PM<br />Sunday: Closed</strong></span>
          </div>
        </div>
      </div>
      <div className="dealership-intro__gallery" aria-label="The Car Store dealership and vehicle lot">
        <img className="dealership-intro__main-photo" src="/images/cherryville-dealership-hero.png" alt="The Car Store dealership and vehicle lot in Cherryville" loading="lazy" />
        <div className="dealership-intro__small-photos">
          <img className="dealership-intro__lot-photo" src="/images/cherryville-lot-closeup.png" alt="Trucks and SUVs parked at The Car Store" loading="lazy" />
          <img className="dealership-intro__store-photo" src="/images/cherryville-dealership-exterior.png" alt="The dealership building in Cherryville" loading="lazy" />
        </div>
      </div>
    </div>
  </section>
)

const CustomerReviews = () => (
  <section className="customer-reviews" aria-labelledby="customer-reviews-title">
    <div className="customer-reviews__inner">
      <div className="customer-reviews__topline">
        <div>
          <p className="customer-reviews__eyebrow">Customer Reviews</p>
          <h2 id="customer-reviews-title">What Drivers Are Saying</h2>
        </div>
        <a href={business.reviewsUrl} target="_blank" rel="noreferrer" onClick={() => trackContactCta('review_click', 'Homepage View All Reviews')}>View All Reviews <FaArrowRight aria-hidden="true" /></a>
      </div>
      <p className="customer-reviews__intro">We’re proud to have earned the trust of local drivers. Our customers appreciate honest service, helpful people, and a straightforward experience. Here are a few of their Google reviews.</p>
      <div className="customer-reviews__grid">
        {reviews.slice(0, 3).map((review) => (
          <article className="customer-review-card" key={review.author}>
            <div className="customer-review-card__stars" aria-label={`${review.rating} out of 5 stars`}>
              {Array.from({ length: review.rating }, (_, index) => <FaStar key={index} aria-hidden="true" />)}
            </div>
            <h3>{review.author}</h3>
            <p className="customer-review-card__source">Google Review · {review.date}</p>
            <p className="customer-review-card__quote">{review.text}</p>
          </article>
        ))}
      </div>
      <div className="customer-reviews__trust">
        <div className="customer-reviews__rating">
          <div className="customer-reviews__rating-stars" aria-label="Five stars"><FaStar /><FaStar /><FaStar /><FaStar /><FaStar /></div>
          <strong>5-star reviews</strong>
          <span>Shared by our customers</span>
        </div>
        <div className="customer-reviews__message">
          <FaUsers aria-hidden="true" />
          <p><strong>Trusted by drivers in Cherryville and the surrounding area.</strong><span>Honest service and a straightforward experience matter to our team.</span></p>
        </div>
      </div>
    </div>
  </section>
)
