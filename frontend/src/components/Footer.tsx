import { Link } from 'react-router'
import { FaArrowRight, FaClock, FaMapMarkerAlt, FaPhoneAlt } from 'react-icons/fa'

import { business } from '../data/business'
import { trackContactCta } from '../utils/ctaTracking'

const quickLinks = [
  ['Home', '/'],
  ['Inventory', '/inventory'],
  ['Financing', '/contact'],
  ['Trade-In', '/contact'],
  ['About Us', '/about'],
  ['Contact', '/contact'],
]

const vehicleLinks = [
  ['SUVs', '/inventory?bodyType=SUV'],
  ['Trucks', '/inventory?bodyType=Truck'],
  ['Sedans', '/inventory?bodyType=Sedan'],
  ['Cars', '/inventory?bodyType=Coupe'],
  ['Vans', '/inventory?bodyType=Van'],
  ['Hybrid', '/inventory?q=Hybrid'],
]

export const Footer = () => (
  <footer className="home-footer">
    <div className="home-footer-container">
      <div className="home-footer-main">
        <section className="home-footer-intro" aria-label="The Car Store of Cherryville, Inc">
          <Link to="/" className="home-footer-logo" aria-label="The Car Store of Cherryville home">
            <img src="/images/car-store-logo-hq.webp" alt="The Car Store of Cherryville, Inc." />
          </Link>
          <p>Locally owned and operated, The Car Store of Cherryville, Inc. is a trusted used car dealership serving Cherryville and the surrounding area with quality pre-owned vehicles and straightforward service.</p>
          <Link to="/inventory" className="home-footer-cta-button" onClick={() => trackContactCta('inventory_click', 'Footer Browse Inventory')}>
            Browse Inventory <FaArrowRight aria-hidden="true" />
          </Link>
          <a href={business.mapsUrl} target="_blank" rel="noreferrer" className="home-footer-directions" onClick={() => trackContactCta('directions_click', 'Footer Get Directions')}>
            <FaMapMarkerAlt aria-hidden="true" /> Get Directions
          </a>
        </section>

        <nav className="home-footer-column home-footer-nav" aria-label="Quick links">
          <h2>Quick Links</h2><i aria-hidden="true" />
          {quickLinks.map(([label, href]) => <Link to={href} key={label}>{label}</Link>)}
        </nav>

        <nav className="home-footer-column home-footer-shop" aria-label="Shop by vehicle">
          <h2>Shop by Vehicle</h2><i aria-hidden="true" />
          {vehicleLinks.map(([label, href]) => <Link to={href} key={label}>{label}</Link>)}
        </nav>

        <section className="home-footer-contact" aria-label="Contact and visit us">
          <h2>Contact / Visit Us</h2><i aria-hidden="true" />
          <a className="home-footer-contact-line" href={business.mapsUrl} target="_blank" rel="noreferrer" onClick={() => trackContactCta('directions_click', 'Footer Address')}>
            <FaMapMarkerAlt aria-hidden="true" /><span>{business.address}<br />{business.cityState} {business.postalCode}</span>
          </a>
          <a className="home-footer-contact-line" href={business.phoneHref} onClick={() => trackContactCta('phone_click', 'Footer Call')}>
            <FaPhoneAlt aria-hidden="true" /><span>(704) 435-1988</span>
          </a>
          <div className="home-footer-contact-line">
            <FaClock aria-hidden="true" /><span>Mon - Fri: 8:30 AM - 5:30 PM<br />Saturday: 9:00 AM - 2:00 PM<br />Sunday: Closed</span>
          </div>
        </section>
      </div>
      <div className="home-footer-bottom">
        <span>© 2026 The Car Store of Cherryville, Inc. All rights reserved.</span>
        <div><Link to="/privacy-policy">Privacy Policy</Link><Link to="/terms">Terms of Use</Link></div>
      </div>
    </div>
  </footer>
)
