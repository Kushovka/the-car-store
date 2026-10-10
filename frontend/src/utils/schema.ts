import { business } from '../data/business'

export const autoDealerSchema = {
  '@context': 'https://schema.org',
  '@type': 'AutoDealer',
  name: business.name,
  address: {
    '@type': 'PostalAddress',
    streetAddress: business.address,
    addressLocality: 'Cherryville',
    addressRegion: 'NC',
    postalCode: business.postalCode,
    addressCountry: 'US',
  },
  geo: {
    '@type': 'GeoCoordinates',
    latitude: business.latitude,
    longitude: business.longitude,
  },
  url: business.website || business.mapsUrl,
  openingHours: ['Mo-Fr 08:30-17:30', 'Sa 09:00-14:00'],
}
