export type Review = {
  author: string
  rating: number
  date: string
  text: string
}

export const reviews: Review[] = [
  {
    author: 'Mike Rinaldi',
    rating: 5,
    date: '4 years ago',
    text: '5 stars for these guys. They could’ve had me waiting all day, or all weekend for that matter. Had trailer tire troubles and I was in and out in less than an hour. Thank you for being fair, reasonable, and most of all, honest. If I’m ever in Cherryville again, I will make sure to stop and say hi.',
  },
  {
    author: 'Sunflower',
    rating: 5,
    date: '6 years ago',
    text: 'Super friendly people! Rick and Justin worked extra hard to get me financed with a reasonable down payment. They were super helpful and helped me find a great car in my price range. Great honest family!',
  },
  {
    author: 'matthew olszewski',
    rating: 5,
    date: '4 years ago',
    text: 'Had a check engine light on our way to visiting family in the Charlotte / Gastonia area. Car was running rough. Was told to call Justin at the car store from a neighbor. Great service he fixed the problem in a professional way. I would give six stars if I could!',
  },
]
