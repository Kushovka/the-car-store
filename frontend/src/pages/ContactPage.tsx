import { FaArrowRight, FaCheck, FaClock, FaHandshake, FaMapMarkerAlt, FaPhoneAlt, FaUsers, FaComments } from 'react-icons/fa'
import { Link } from 'react-router'
import { LeadForm } from '../components/LeadForm'
import { Seo } from '../components/Seo'
import { business } from '../data/business'
import { trackContactCta } from '../utils/ctaTracking'

const phoneHref = business.phoneHref || business.contactHref

const contactTopics = [
  'Questions about our current inventory',
  'Schedule a test drive',
  'Get more information about a vehicle',
  'General dealership information',
  'Financing and trade-in questions',
]

const benefits = [
  { icon: FaUsers, title: 'Friendly Local Team', text: "We're a local, independent dealership committed to honest, helpful service." },
  { icon: FaHandshake, title: 'Straightforward Service', text: 'No-pressure, transparent answers to your questions.' },
  { icon: FaMapMarkerAlt, title: 'Convenient Location', text: 'Easy to find on Lincolnton Hwy in Cherryville, NC.' },
  { icon: FaComments, title: 'Quick Responses', text: 'We strive to respond to all inquiries as quickly as possible.' },
]

export const ContactPage = () => (
  <main className="contact-page">
    <Seo title="Contact" description="Call, visit, or send a message to The Car Store of Cherryville, Inc in Cherryville, NC." />

    <section className="contact-hero" aria-labelledby="contact-title">
      <div className="contact-container contact-hero-grid">
        <div className="contact-hero-copy">
          <h1 id="contact-title">Contact The Car Store<br className="contact-desktop-break" /> of Cherryville</h1>
          <p>Have questions about our inventory? Want to schedule a test drive or get help finding the right vehicle? Our friendly team is here to help. Reach out by phone, email, or stop by our dealership in Cherryville, NC. We look forward to hearing from you!</p>
          <div className="contact-hero-actions">
            <a href={phoneHref} className="contact-action contact-action-primary" onClick={() => trackContactCta('phone_click', 'Contact Page Call Us')}><FaPhoneAlt aria-hidden="true" /> Call Us</a>
            <a href={business.mapsUrl} target="_blank" rel="noreferrer" className="contact-action contact-action-secondary" onClick={() => trackContactCta('directions_click', 'Contact Page Directions')}><FaMapMarkerAlt aria-hidden="true" /> Get Directions</a>
          </div>
        </div>
        <img className="contact-hero-image" src="/images/cherryville-dealership-hero.png" alt="The Car Store of Cherryville dealership and vehicle lot" />
      </div>
    </section>

    <section className="contact-main-section" aria-label="Contact our team">
      <div className="contact-container contact-main-grid">
        <div className="contact-card contact-message-card">
          <h2>Send Us a Message</h2>
          <p className="contact-form-intro">Fill out the form below and a member of our team will get back to you as soon as possible.</p>
          <LeadForm title="Send Message" variant="contact" phonePlaceholder="(704) 555-0123" messagePlaceholder="Tell us how we can help you. You can ask about a specific vehicle, schedule a test drive, or any other questions you have..." showVehicleInterest inquiryOptions={undefined} />
        </div>

        <aside className="contact-card contact-info-card">
          <h2>Dealership Information</h2>
          <div className="contact-info-list">
            <a href={business.mapsUrl} target="_blank" rel="noreferrer" className="contact-info-row" onClick={() => trackContactCta('directions_click', 'Contact Page Address')}>
              <span className="contact-info-icon"><FaMapMarkerAlt aria-hidden="true" /></span><span><strong>Our Location</strong>{business.address}<br />{business.cityState} {business.postalCode}</span>
            </a>
            <a href={phoneHref} className="contact-info-row" onClick={() => trackContactCta('phone_click', 'Contact Page Phone')}>
              <span className="contact-info-icon"><FaPhoneAlt aria-hidden="true" /></span><span><strong>Give Us a Call</strong>(704) 435-1988</span>
            </a>
            <div className="contact-info-row">
              <span className="contact-info-icon"><FaClock aria-hidden="true" /></span><span><strong>Hours of Operation</strong>Mon - Fri: 8:30 AM - 5:30 PM<br />Saturday: 9:00 AM - 2:00 PM<br />Sunday: Closed</span>
            </div>
          </div>
          <div className="contact-help-box"><h3>We're Here to Help With:</h3><ul>{contactTopics.map((topic) => <li key={topic}><FaCheck aria-hidden="true" />{topic}</li>)}</ul></div>
        </aside>
      </div>
    </section>

    <section className="contact-visit-section" aria-labelledby="location-heading">
      <div className="contact-container">
        <h2 id="location-heading" className="contact-section-title">Visit Us in Cherryville</h2>
        <div className="contact-visit-grid">
          <iframe title="The Car Store of Cherryville, Inc map" className="contact-map" loading="lazy" referrerPolicy="no-referrer-when-downgrade" src={business.mapEmbedUrl.replace('&t=k', '&t=m')} />
          <aside className="contact-card contact-plan-card">
            <h3>Plan Your Visit</h3>
            <p>We're conveniently located on Lincolnton Hwy (US-321) in Cherryville, NC. Stop by to browse our inventory in person, take a test drive, or speak with our team about your next vehicle. We're easy to find and always happy to help.</p>
            <div className="contact-plan-line"><FaMapMarkerAlt aria-hidden="true" /><span>{business.address}<br />{business.cityState} {business.postalCode}</span></div>
            <a className="contact-plan-line" href={phoneHref} onClick={() => trackContactCta('phone_click', 'Contact Page Visit Phone')}><FaPhoneAlt aria-hidden="true" /><span>(704) 435-1988</span></a>
            <div className="contact-plan-line"><FaClock aria-hidden="true" /><span>Mon - Fri: 8:30 AM - 5:30 PM<br />Saturday: 9:00 AM - 2:00 PM<br />Sunday: Closed</span></div>
            <div className="contact-plan-actions"><a href={business.mapsUrl} target="_blank" rel="noreferrer" className="contact-action contact-action-primary" onClick={() => trackContactCta('directions_click', 'Contact Page Map Directions')}><FaMapMarkerAlt aria-hidden="true" /> Get Directions</a><Link to="/inventory" className="contact-action contact-action-secondary" onClick={() => trackContactCta('inventory_click', 'Contact Page Browse Inventory')}>Browse Inventory</Link></div>
          </aside>
        </div>
      </div>
    </section>

    <section className="contact-benefits-section" aria-labelledby="contact-benefits-title">
      <div className="contact-container">
        <h2 id="contact-benefits-title" className="contact-section-title">Why Get in Touch With Us?</h2>
        <div className="contact-benefits-grid">{benefits.map(({ icon: Icon, title, text }) => <article className="contact-benefit" key={title}><Icon aria-hidden="true" /><div><h3>{title}</h3><p>{text}</p></div></article>)}</div>
      </div>
    </section>

    <section className="contact-bottom-cta">
      <div className="contact-bottom-cta-content"><h2>Ready to Find Your Next Vehicle?</h2><p>Browse our inventory online or give us a call. Our team is here to help you find the right car, truck, SUV, or van for your needs.</p><div><Link to="/inventory" className="contact-action contact-action-primary" onClick={() => trackContactCta('inventory_click', 'Contact Page Final Browse Inventory')}>Browse Inventory <FaArrowRight aria-hidden="true" /></Link><a href={phoneHref} className="contact-action contact-cta-call" onClick={() => trackContactCta('phone_click', 'Contact Page Final Call')}><FaPhoneAlt aria-hidden="true" /> Call Us</a></div></div>
    </section>
  </main>
)
