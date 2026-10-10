import { useState } from 'react'
import { FaArrowRight, FaCalendarAlt, FaCar, FaUsers, FaShieldAlt } from 'react-icons/fa'
import { Link } from 'react-router'
import { LeadForm } from '../components/LeadForm'
import { Seo } from '../components/Seo'

const process = [
  ['Choose Your Vehicle', 'Browse our inventory and find the car, truck, SUV, or van you want. Our team is here to answer any questions about the vehicle.'],
  ['Request a Delivery Quote', 'Let us know where you need the vehicle delivered. We’ll provide a custom quote based on your location and the vehicle.'],
  ['Schedule Your Delivery', 'Once you’re ready, we’ll coordinate timing with our trusted transport partners and keep you updated every step of the way.'],
]

const benefits = [
  { icon: FaCar, title: 'Save Time', text: 'Have your vehicle delivered directly to your home or office and skip the long drive.' },
  { icon: FaShieldAlt, title: 'Convenient Process', text: 'We handle the logistics and work with trusted transport carriers.' },
  { icon: FaCalendarAlt, title: 'Flexible Scheduling', text: 'We’ll work with you to find a delivery time that fits your schedule.' },
  { icon: FaUsers, title: 'We Coordinate the Details', text: 'From pickup to delivery, our team stays in touch to make sure everything goes smoothly.' },
]

const questions = [
  ['How much does delivery cost?', 'Delivery pricing depends on your location, the vehicle, and current carrier availability. Request a quote with your delivery ZIP code and we’ll provide a custom estimate.'],
  ['How long does delivery take?', 'Timing varies by route and carrier availability. We’ll share an estimated delivery timeframe when we prepare your quote.'],
  ['Do you deliver out of state?', 'Yes. We can help coordinate vehicle delivery throughout North Carolina and across the country. Contact us with your destination for a quote.'],
  ['Can I buy a vehicle remotely?', 'Yes. Our team can help you with the vehicle details and coordinate delivery to your location. Browse our inventory and get in touch to get started.'],
]

export const DeliveryPage = () => {
  const [openQuestion, setOpenQuestion] = useState<number | null>(null)
  const scrollToQuote = () => document.getElementById('delivery-quote')?.scrollIntoView({ behavior: 'smooth', block: 'start' })

  return <>
    <Seo title="Nationwide Vehicle Delivery" description="The Car Store of Cherryville can help arrange vehicle delivery throughout North Carolina and across the country." />
    <main className="delivery-page">
      <section className="delivery-hero">
        <div className="delivery-hero-copy">
          <h1>Nationwide Vehicle Delivery</h1>
          <p className="delivery-hero-description">The Car Store of Cherryville, Inc. can help arrange vehicle delivery for customers throughout North Carolina and across the country. Whether you’re nearby or hundreds of miles away, we’ll work with you to get your next vehicle delivered safely and conveniently.</p>
          <div className="delivery-actions">
            <Link className="delivery-button delivery-button--red" to="/inventory">Browse Inventory <FaArrowRight aria-hidden="true" /></Link>
            <Link className="delivery-button delivery-button--light" to="/contact">Contact Us</Link>
          </div>
        </div>
        <img className="delivery-hero-image" src="/images/delivery-car-carrier.webp" alt="Car carrier transporting vehicles on a North Carolina highway" />
      </section>

      <section className="delivery-process delivery-wrap" aria-labelledby="delivery-process-title">
        <h2 id="delivery-process-title">How Delivery Works</h2>
        <div className="delivery-process-grid">{process.map(([title, text], i) => <article key={title}><span>{i + 1}</span><div><h3>{title}</h3><p>{text}</p></div></article>)}</div>
      </section>

      <section className="delivery-details">
        <div className="delivery-details-inner">
          <div className="delivery-copy">
            <h2>What to Expect with Vehicle Delivery</h2>
            <p>We work with experienced, insured auto transport carriers to deliver vehicles safely to customers in North Carolina and nationwide. Delivery pricing varies based on distance, vehicle type, and current transport rates, and we’re happy to provide a custom quote for your specific location.</p>
            <p>Our team will help coordinate the entire process, from scheduling to final delivery, and keep you informed along the way. In most cases, delivery can be arranged within a few days, depending on location and carrier availability.</p>
            <p>Whether you’re buying a vehicle from Cherryville, NC or from out of state, we’ll make the delivery process as smooth and straightforward as possible.</p>
          </div>
          <div className="delivery-form-wrap" id="delivery-quote">
            <h2>Request Delivery Quote</h2>
            <LeadForm title="Request Delivery Quote" messagePlaceholder="Tell us where you need the vehicle delivered and any other questions you have..." showVehicleInterest phonePlaceholder="(704) 555-0123" className="delivery-quote-form" />
          </div>
        </div>
      </section>

      <section className="delivery-lower delivery-wrap">
        <div className="delivery-benefits" aria-labelledby="delivery-benefits-title">
          <h2 id="delivery-benefits-title">Why Customers Use Our Delivery Service</h2>
          <div className="delivery-benefits-grid">{benefits.map(({ icon: Icon, title, text }) => <article key={title}><Icon aria-hidden="true"/><div><h3>{title}</h3><p>{text}</p></div></article>)}</div>
        </div>
        <div className="delivery-faq" aria-labelledby="delivery-faq-title">
          <h2 id="delivery-faq-title">Frequently Asked Questions</h2>
          {questions.map(([question, answer], i) => <div className="delivery-faq-item" key={question}><button type="button" aria-expanded={openQuestion === i} onClick={() => setOpenQuestion(openQuestion === i ? null : i)}><span>{question}</span><span aria-hidden="true">{openQuestion === i ? '−' : '+'}</span></button>{openQuestion === i ? <p>{answer}</p> : null}</div>)}
        </div>
      </section>

      <section className="delivery-final-cta">
        <div><h2>Found the Right Vehicle? Let’s Help Get It to You.</h2><p>Browse our inventory or contact our team to get a delivery quote and learn more about the process.</p><div className="delivery-actions"><Link className="delivery-button delivery-button--red" to="/inventory">Browse Inventory <FaArrowRight aria-hidden="true" /></Link><a className="delivery-button delivery-button--dark" href="#delivery-quote" onClick={(event) => { event.preventDefault(); scrollToQuote() }}>Contact Us</a></div></div>
      </section>
    </main>
  </>
}
