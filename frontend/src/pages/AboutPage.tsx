import { FaArrowRight, FaCar, FaClock, FaFileAlt, FaHandshake, FaMapMarkerAlt, FaPhoneAlt, FaUsers } from 'react-icons/fa'
import { Link } from 'react-router'
import { Button } from '../components/Button'
import { Seo } from '../components/Seo'
import { business } from '../data/business'

const reasons = [
  { icon: FaUsers, title: 'Locally Owned', text: "We're part of the Cherryville community and proud to serve our neighbors." },
  { icon: FaCar, title: 'Quality Pre-Owned Vehicles', text: 'We carefully select our inventory of dependable cars, trucks, SUVs and vans.' },
  { icon: FaHandshake, title: 'Straightforward Service', text: 'No high-pressure sales tactics. Just honest answers and friendly help.' },
  { icon: FaFileAlt, title: 'Convenient Buying Process', text: 'We make it easy to find, finance and drive home the right vehicle for your needs.' },
]

const expectations = [
  { image: '/images/cherryville-dealership-hero.webp', title: 'Carefully Selected Inventory', text: 'We hand-pick our vehicles from trusted sources and inspect them for quality and reliability, so you can shop with confidence.' },
  { image: '/images/cherryville-dealership-exterior.webp', title: 'Honest Communication', text: 'We believe in clear, upfront information and straight answers. Our team will always be honest about our vehicles and the buying process.' },
  { image: '/images/cherryville-lot-closeup.webp', title: 'Help Every Step of the Way', text: "From browsing and test drives to financing and after your purchase, we're here to answer your questions and make the process as easy as possible." },
]

export const AboutPage = () => (
  <main className="about-page">
    <Seo title="About The Car Store of Cherryville, Inc" description="Meet The Car Store of Cherryville, Inc, located in Cherryville, North Carolina." />

    <section className="about-hero">
      <div className="about-hero-copy">
        <h1>About The Car Store<br />of Cherryville</h1>
        <span className="about-rule" />
        <p>The Car Store of Cherryville, Inc. is a local, independent used car dealership committed to providing quality pre-owned vehicles and straightforward, no-pressure service. We’re proud to serve Cherryville and the surrounding communities with reliable vehicles, fair pricing, and a friendly, helpful team.</p>
        <div className="about-actions">
          <Link className="about-button about-button--red" to="/inventory">Browse Inventory <FaArrowRight /></Link>
          <a className="about-button about-button--outline-red" href={business.mapsUrl} target="_blank" rel="noreferrer"><FaMapMarkerAlt /> Get Directions</a>
        </div>
      </div>
      <img className="about-hero-image" src="/images/cherryville-dealership-hero.webp" alt="The Car Store dealership and vehicle lot in Cherryville" />
    </section>

    <section className="about-reasons">
      <div className="about-section-inner">
        <h2>Why Drivers Choose Us</h2><span className="about-rule" />
        <div className="about-reasons-grid">
          {reasons.map(({ icon: Icon, title, text }) => <article key={title}><span className="about-icon"><Icon aria-hidden="true" /></span><div><h3>{title}</h3><p>{text}</p></div></article>)}
        </div>
      </div>
    </section>

    <section className="about-story">
      <img src="/images/cherryville-dealership-exterior.webp" alt="Vehicles outside The Car Store of Cherryville" />
      <div className="about-story-copy">
        <h2>A Local Dealership<br />You Can Count On</h2><span className="about-rule" />
        <p>For years, The Car Store of Cherryville, Inc. has been helping drivers in Cherryville, Lincolnton, Gastonia, Shelby and the surrounding areas find quality, dependable used vehicles. As a locally owned and operated dealership, we take pride in building long-term relationships with our customers.</p>
        <p>Our team is here to make your car buying experience simple, straightforward and stress-free. Whether you’re shopping for a car, truck, SUV or van, we’ll take the time to understand your needs and help you find the right vehicle at a fair price.</p>
        <div className="about-contact-strip">
          <div><FaMapMarkerAlt /><span>Our Location<strong>{business.address}<br />{business.cityState} {business.postalCode}</strong></span></div>
          <a href={business.phoneHref}><FaPhoneAlt /><span>Give Us a Call<strong>{business.phone}</strong></span></a>
          <div><FaClock /><span>Hours<strong>Mon–Fri: 8:30 AM – 5:30 PM<br />Saturday: 9:00 AM – 2:00 PM<br />Sunday: Closed</strong></span></div>
        </div>
      </div>
    </section>

    <section className="about-expectations">
      <div className="about-section-inner">
        <h2>What You Can Expect</h2><span className="about-rule" />
        <div className="about-expectations-grid">
          {expectations.map(({ image, title, text }) => <article key={title}><img src={image} alt="" /><div><h3>{title}</h3><p>{text}</p></div></article>)}
        </div>
      </div>
    </section>

    <section className="about-visit">
      <div className="about-section-inner about-visit-grid">
        <div className="about-visit-copy"><h2>Visit Our Dealership</h2><span className="about-rule" />
          <p><FaMapMarkerAlt /><span><strong>{business.address}</strong>{business.cityState} {business.postalCode}</span></p>
          <p><FaPhoneAlt /><a href={business.phoneHref}><strong>{business.phone}</strong></a></p>
          <p><FaClock /><span>Mon–Fri: 8:30 AM – 5:30 PM<br />Saturday: 9:00 AM – 2:00 PM<br />Sunday: Closed</span></p>
          <div className="about-actions"><Button className="about-visit-button" href={business.mapsUrl}><FaMapMarkerAlt /> Get Directions</Button><Button className="about-visit-button about-visit-button--secondary" href="/contact" variant="secondary">Contact Us</Button></div>
        </div>
        <a className="about-map" href={business.mapsUrl} target="_blank" rel="noreferrer" aria-label="Open map directions to The Car Store"><iframe title="Map to The Car Store of Cherryville" src={business.mapEmbedUrl} loading="lazy" referrerPolicy="no-referrer-when-downgrade" /></a>
      </div>
    </section>

    <section className="about-cta"><div><h2>Ready to Find Your Next Vehicle?</h2><p>Browse our current inventory of quality used cars, trucks &amp; SUVs.</p><div className="about-actions"><Button className="about-visit-button" href="/inventory">View Inventory</Button><Button className="about-visit-button about-visit-button--light" href="/contact" variant="secondary">Contact Us</Button></div></div></section>
  </main>
)
