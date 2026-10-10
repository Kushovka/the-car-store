import { FaArrowRight, FaUsers } from 'react-icons/fa'
import { Link } from 'react-router'
import { Seo } from '../components/Seo'
import { teamPortraits } from '../data/team'

export const TeamPage = () => (
  <main className="team-page">
    <Seo title="Our Team" description="Meet the people who make The Car Store of Cherryville, Inc a friendly place to find and service a vehicle." />
    <section className="team-section" aria-labelledby="team-title">
      <div className="team-intro">
        <div className="team-intro-copy">
          <h1 id="team-title">Meet the Team Behind The Car Store</h1>
          <p className="team-intro-description">Our experienced and friendly team is here to help with all of your automotive needs. From sales and financing to service, warranty, delivery, and inventory questions, we’re committed to making your experience at The Car Store of Cherryville, Inc. a great one.</p>
        </div>
        <aside className="team-help-panel">
          <div className="team-help-icon"><FaUsers aria-hidden="true" /></div>
          <div className="team-help-copy">
            <h2>Friendly, knowledgeable staff ready to help.</h2>
            <p>Have a question? Our team is here to guide you every step of the way — whether you’re buying, selling, or just exploring your options.</p>
          </div>
        </aside>
      </div>
      <div className="team-gallery">
        <div className="mx-auto grid max-w-[1400px] grid-cols-2 gap-x-4 gap-y-7 sm:gap-x-6 sm:gap-y-10 lg:grid-cols-4 lg:gap-x-8 lg:gap-y-12">
          {teamPortraits.map((member, index) => (
            <article key={member.src} className="team-member-card group overflow-hidden">
              <div className="team-member-photo team-portrait relative aspect-[4/5] overflow-hidden">
                <img src={member.src} alt={member.alt} loading={index > 3 ? 'lazy' : 'eager'} className="team-member-portrait absolute inset-0 h-full w-full object-cover object-center" />
              </div>
              <div className="team-member-caption">
                <h2>{member.name}</h2>
                <p>{member.title}</p>
              </div>
            </article>
          ))}
        </div>
      </div>
      <div className="team-cta-row">
        <Link to="/contact" className="team-cta team-cta-primary">Contact Our Team <FaArrowRight aria-hidden="true" /></Link>
        <Link to="/inventory" className="team-cta team-cta-secondary">View Inventory <FaArrowRight aria-hidden="true" /></Link>
      </div>
    </section>
  </main>
)
