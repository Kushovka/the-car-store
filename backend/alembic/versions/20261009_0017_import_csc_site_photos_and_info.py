"""Import CSC site photos and listing details.

Revision ID: 20261009_0017
Revises: 20261009_0016
Create Date: 2026-10-09
"""

import importlib.util
from pathlib import Path

from alembic import op
import sqlalchemy as sa

revision = "20261009_0017"
down_revision = "20261009_0016"
branch_labels = None
depends_on = None


VEHICLES = [
    {
        'slug': '2021-lexus-lx570-inspiration-series',
        'images': ['/media/vehicles/2021-lexus-lx570-inspiration-series/01.webp', '/media/vehicles/2021-lexus-lx570-inspiration-series/02.webp', '/media/vehicles/2021-lexus-lx570-inspiration-series/03.webp', '/media/vehicles/2021-lexus-lx570-inspiration-series/04.webp', '/media/vehicles/2021-lexus-lx570-inspiration-series/05.webp', '/media/vehicles/2021-lexus-lx570-inspiration-series/06.webp', '/media/vehicles/2021-lexus-lx570-inspiration-series/07.webp', '/media/vehicles/2021-lexus-lx570-inspiration-series/08.webp', '/media/vehicles/2021-lexus-lx570-inspiration-series/09.webp', '/media/vehicles/2021-lexus-lx570-inspiration-series/10.webp', '/media/vehicles/2021-lexus-lx570-inspiration-series/11.webp', '/media/vehicles/2021-lexus-lx570-inspiration-series/12.webp', '/media/vehicles/2021-lexus-lx570-inspiration-series/13.webp', '/media/vehicles/2021-lexus-lx570-inspiration-series/14.webp', '/media/vehicles/2021-lexus-lx570-inspiration-series/15.webp', '/media/vehicles/2021-lexus-lx570-inspiration-series/16.webp', '/media/vehicles/2021-lexus-lx570-inspiration-series/17.webp', '/media/vehicles/2021-lexus-lx570-inspiration-series/18.webp', '/media/vehicles/2021-lexus-lx570-inspiration-series/19.webp', '/media/vehicles/2021-lexus-lx570-inspiration-series/20.webp', '/media/vehicles/2021-lexus-lx570-inspiration-series/21.webp'],
        'price': 49999,
        'mileage': 42518,
        'transmission': 'Automatic',
        'drivetrain': 'All-Wheel Drive (AWD)',
        'engine': '5.7L Naturally Aspirated V8',
        'exterior_color': 'Black Onyx',
        'interior_color': 'Black/Red',
        'location': 'Virginia',
        'features': ['2021 Lexus LX 570 Inspiration Series', '5.7L Naturally Aspirated V8', '8-Speed Automatic', 'AWD', 'Black Onyx Exterior', 'Black/Red Semi-Aniline Leather Interior', 'Wireless Charger', 'Cool Box', 'Head-Up Display', 'Mark Levinson 19-Speaker, 450-Watt Reference Surround Sound System', 'Inspiration Series Package', 'Luxury Package', 'Heated Espresso Steering Wheel', 'Cargo Net', 'Alloy Wheel Locks', '1 of 500 Units Produced (1 of 250 In Black Onyx)'],
        'description': 'Finished in Black Onyx, this 2021 Lexus LX 570 Inspiration Series carries an unmistakably stealthy presence. The Inspiration Series package adds a host of exclusive black exterior details, including black 21-inch wheels, black grille accents, smoked lighting elements, black roof rails, black chrome trim, and exclusive badging that give the traditionally elegant LX a much more aggressive and contemporary personality. Despite its premium presentation, the LX remains highly functional, retaining its full-size SUV practicality, commanding ride height, and genuine off-road capability beneath the luxury veneer.\n\nInside, the cabin reflects Lexus’ signature approach to craftsmanship and comfort. The exclusive black and Rioja Red-accented semi-aniline leather interior immediately distinguishes this Inspiration Series from ordinary LX 570s, while the Luxury Package adds heated and ventilated front and second-row outboard seating, four-zone climate control, and premium trim materials throughout. Convenience and technology features include a head-up display, wireless charging, cool box, heated espresso wood-and-leather steering wheel, and the superb Mark Levinson 19-speaker, 450-watt Reference Surround Sound System. Even by modern standards, the cabin remains exceptionally comfortable, solidly built, and unmistakably upscale.\n\nEngine\nAt the heart of this 2021 Lexus LX 570 Inspiration Series sits Lexus’ venerable 5.7-liter naturally aspirated V8, producing smooth, effortless power delivery that prioritizes refinement and durability over forced-induction theatrics. Paired with an 8-speed automatic transmission and a full-time all-wheel-drive system, the LX delivers confident all-weather performance while retaining the serious off-road DNA inherited from its Land Cruiser platform sibling. Advanced systems such as adaptive variable suspension, active height control, crawl control, and multi-terrain select make this far more than just a luxury cruiser—it remains one of the most capable full-size SUVs ever engineered. What makes the LX 570 especially compelling today is its analog honesty: a naturally aspirated V8, body-on-frame construction, and proven mechanical engineering in a segment increasingly dominated by more complex alternatives.',
        'title': '2021 Lexus LX570 Inspiration Series',
        'lot_number': '260557794',
        'condition': None,
    },
    {
        'slug': '2025-mercedes-benz-gle63-s-amg-coupe',
        'images': ['/media/vehicles/2025-mercedes-benz-gle63-s-amg-coupe/01.webp', '/media/vehicles/2025-mercedes-benz-gle63-s-amg-coupe/02.webp', '/media/vehicles/2025-mercedes-benz-gle63-s-amg-coupe/03.webp', '/media/vehicles/2025-mercedes-benz-gle63-s-amg-coupe/04.webp', '/media/vehicles/2025-mercedes-benz-gle63-s-amg-coupe/05.webp', '/media/vehicles/2025-mercedes-benz-gle63-s-amg-coupe/06.webp', '/media/vehicles/2025-mercedes-benz-gle63-s-amg-coupe/07.webp', '/media/vehicles/2025-mercedes-benz-gle63-s-amg-coupe/08.webp', '/media/vehicles/2025-mercedes-benz-gle63-s-amg-coupe/09.webp', '/media/vehicles/2025-mercedes-benz-gle63-s-amg-coupe/10.webp', '/media/vehicles/2025-mercedes-benz-gle63-s-amg-coupe/11.webp', '/media/vehicles/2025-mercedes-benz-gle63-s-amg-coupe/12.webp', '/media/vehicles/2025-mercedes-benz-gle63-s-amg-coupe/13.webp', '/media/vehicles/2025-mercedes-benz-gle63-s-amg-coupe/14.webp', '/media/vehicles/2025-mercedes-benz-gle63-s-amg-coupe/15.webp', '/media/vehicles/2025-mercedes-benz-gle63-s-amg-coupe/16.webp', '/media/vehicles/2025-mercedes-benz-gle63-s-amg-coupe/17.webp', '/media/vehicles/2025-mercedes-benz-gle63-s-amg-coupe/18.webp', '/media/vehicles/2025-mercedes-benz-gle63-s-amg-coupe/19.webp', '/media/vehicles/2025-mercedes-benz-gle63-s-amg-coupe/20.webp', '/media/vehicles/2025-mercedes-benz-gle63-s-amg-coupe/21.webp', '/media/vehicles/2025-mercedes-benz-gle63-s-amg-coupe/22.webp', '/media/vehicles/2025-mercedes-benz-gle63-s-amg-coupe/23.webp'],
        'price': 78499,
        'mileage': 16737,
        'transmission': 'Automatic',
        'drivetrain': 'All-Wheel Drive (AWD)',
        'engine': '4.0L Twin-Turbocharged V8',
        'exterior_color': 'Cirrus Silver Metallic',
        'interior_color': 'Macchiato Beige/Black',
        'location': 'California',
        'features': ['2025 Mercedes-Benz AMG GLE 63 S 4MATIC+ Coupe', '4.0L Twin-Turbocharged V8', '9-Speed AMG SPEEDSHIFT Automatic', '4MATIC+ AWD', 'Cirrus Silver Metallic Exterior', 'AMG Macchiato Beige/Black Exclusive Nappa Leather Interior', '22” AMG Cross-Spoke Forged Matte Black Wheels', 'Natural Grain Brown Walnut Trim', 'Driver Assistance Package', 'AMG Night Package', 'Heated Rear Seats', '4-Zone Climate Control', 'Acoustic Comfort Package', 'Dashcam', 'Black Wheel Locking Bolts', 'Full Body STEK DYNOmatte Satin Paint Protection Film', 'Ceramic Coating', 'Tinted Windows', 'Larte Design Black Painted Carbon Fiber Front Lip', 'Larte Design Black Painted Carbon Fiber Rear Diffuser', 'Larte Design Black Painted Carbon Fiber Rear Spoiler'],
        'description': 'The exterior of this 2025 Mercedes-Benz AMG GLE 63 S 4MATIC+ Coupe is an impressive mix of aggression and sophistication. Finished in Cirrus Silver Metallic, the satin appearance created by the full STEK DYNOmatte paint protection film gives the SUV a far more bespoke visual character than standard gloss paint. The AMG Night Package adds blacked-out trim for sharper contrast, while the 22-inch AMG forged cross-spoke wheels in matte black reinforce the vehicle’s muscular stance. This example goes a step further with Larte Design black painted carbon fiber additions including the front lip, rear diffuser, and rear spoiler, creating a more exclusive and assertive look. Tinted windows, ceramic coating, and black wheel locking bolts further suggest an owner who paid close attention to both preservation and presentation.\n\nThe interior of this 2025 Mercedes-Benz AMG GLE 63 S 4MATIC+ Coupe delivers the sort of environment expected from a flagship AMG performance SUV. The AMG Macchiato Beige and Black Exclusive Nappa leather cabin offers a rich upscale contrast, while natural grain brown walnut trim brings warmth and traditional luxury to the otherwise high-tech cockpit. Comfort-focused features include heated rear seats, four-zone climate control, and the Acoustic Comfort Package, making this a genuinely refined grand tourer despite its performance credentials. The inclusion of the factory dashcam and Driver Assistance Package adds modern convenience and safety technology, making this AMG equally capable in stop-and-go city driving or long interstate journeys.\n\nEngine\nAt the heart of this 2025 Mercedes-Benz AMG GLE 63 S 4MATIC+ Coupe is AMG’s legendary hand-built 4.0-liter twin-turbocharged V8, an engine that has become one of the defining modern Mercedes-AMG powerplants. Producing exhilarating performance with immense low-end torque, this engine delivers the kind of acceleration that makes vehicles of this size feel genuinely improbable. Power is sent through AMG’s 9-speed SPEEDSHIFT automatic transmission and fully variable 4MATIC+ all-wheel-drive system, giving the GLE 63 S remarkable traction in all conditions. AMG-specific suspension tuning, adaptive chassis technologies, and performance braking all work together to ensure this is far more than just a fast luxury SUV—it is a true high-performance machine that can confidently challenge dedicated sports cars while still carrying passengers in comfort.',
        'title': '2025 Mercedes-Benz GLE63 S AMG Coupe',
        'lot_number': '260556906',
        'condition': None,
    },
    {
        'slug': '2025-bmw-m4-competition-xdrive',
        'images': ['/media/vehicles/2025-bmw-m4-competition-xdrive/01.webp', '/media/vehicles/2025-bmw-m4-competition-xdrive/02.webp', '/media/vehicles/2025-bmw-m4-competition-xdrive/03.webp', '/media/vehicles/2025-bmw-m4-competition-xdrive/04.webp', '/media/vehicles/2025-bmw-m4-competition-xdrive/05.webp', '/media/vehicles/2025-bmw-m4-competition-xdrive/06.webp', '/media/vehicles/2025-bmw-m4-competition-xdrive/07.webp', '/media/vehicles/2025-bmw-m4-competition-xdrive/08.webp', '/media/vehicles/2025-bmw-m4-competition-xdrive/09.webp', '/media/vehicles/2025-bmw-m4-competition-xdrive/10.webp', '/media/vehicles/2025-bmw-m4-competition-xdrive/11.webp', '/media/vehicles/2025-bmw-m4-competition-xdrive/12.webp', '/media/vehicles/2025-bmw-m4-competition-xdrive/13.webp', '/media/vehicles/2025-bmw-m4-competition-xdrive/14.webp', '/media/vehicles/2025-bmw-m4-competition-xdrive/15.webp', '/media/vehicles/2025-bmw-m4-competition-xdrive/16.webp', '/media/vehicles/2025-bmw-m4-competition-xdrive/17.webp', '/media/vehicles/2025-bmw-m4-competition-xdrive/18.webp', '/media/vehicles/2025-bmw-m4-competition-xdrive/19.webp', '/media/vehicles/2025-bmw-m4-competition-xdrive/20.webp', '/media/vehicles/2025-bmw-m4-competition-xdrive/21.webp', '/media/vehicles/2025-bmw-m4-competition-xdrive/22.webp', '/media/vehicles/2025-bmw-m4-competition-xdrive/23.webp'],
        'price': 63999,
        'mileage': 8173,
        'transmission': 'Automatic',
        'drivetrain': 'All-Wheel Drive (AWD)',
        'engine': '3.0L Twin-Turbocharged I6',
        'exterior_color': 'Tanzanite Blue II Metallic',
        'interior_color': 'Tartufo',
        'location': 'Nebraska',
        'features': ['2025 BMW M4 Competition xDrive', '3.0L Twin-Turbocharged I6', '8-Speed M Steptronic Automatic', 'AWD', 'Tanzanite Blue II Metallic Exterior', 'Tartufo Extended Merino Leather Interior', 'Driving Assistance Professional', 'Parking Assistance Package', 'Executive Package', '19” Front / 20” Rear Dual-Spoke Bi-Color Wheels', 'M Shadowline Lights', 'Carbon Fiber Trim', 'Front Ventilated Seats', 'BMW First Aid Kit', 'M Performance Floor Mats', 'Luggage Compartment Mat', 'Wheel Locks'],
        'description': 'Tanzanite Blue II Metallic is the color chosen for this 2025 BMW M4 Competition Coupe xDrive and it makes for a very stylish outlook. It’s close to a Midnight Blue, but adds some shimmer and glimmer as lighting dances off it at various angles. The car features M Shadowline lights, carbon-fiber trim and a set of dual-spoke bi-color wheels. These wheels are 19 inches at the front and 20 inches at the rear, and of course, they wear the correct high-performance tires as demanded for a vehicle of this ilk. Wheel locks help keep the wheels safe from thieves.\nThe Tartufo interior of this 2025 BMW M4 Competition Coupe xDrive includes the Extended Merino Leather option too. The car can easily take four adults, and comes with M Performance floor mats to keep the carpeting neat and tidy. There’s also the signature BMW First Aid Kit in case you need it, plus a luggage compartment mat for the roomy trunk. Meanwhile, the front seats are powered, heated and ventilated. There’s the Driving Assistance Professional Package, Parking Assistance Package and Executive Package. Dual-zone automatic climate control keeps you comfortable, while the Harman/Kardon sound system serenades you beautifully as you pair your smartphone with the car’s iDrive infotainment system.\n\nEngine\nBMW is known for their smooth straight sixes, and this 2025 BMW M4 Competition Coupe xDrive is no exception. Its 3.0-liter unit is twin turbocharged, tuned to make a reported 503hp and 479lb-ft for Competition variants. Power goes to all four wheels via an 8-speed M Steptronic automatic transmission and xDrive all-wheel drive system. Thanks to xDrive, you can see 0-60 in 3 seconds!',
        'title': '2025 BMW M4 Competition xDrive',
        'lot_number': '260353522',
        'condition': None,
    },
    {
        'slug': '2025-bmw-m3-competition-xdrive',
        'images': ['/media/vehicles/2025-bmw-m3-competition-xdrive/01.webp', '/media/vehicles/2025-bmw-m3-competition-xdrive/02.webp', '/media/vehicles/2025-bmw-m3-competition-xdrive/03.webp', '/media/vehicles/2025-bmw-m3-competition-xdrive/04.webp', '/media/vehicles/2025-bmw-m3-competition-xdrive/05.webp', '/media/vehicles/2025-bmw-m3-competition-xdrive/06.webp', '/media/vehicles/2025-bmw-m3-competition-xdrive/07.webp', '/media/vehicles/2025-bmw-m3-competition-xdrive/08.webp', '/media/vehicles/2025-bmw-m3-competition-xdrive/09.webp', '/media/vehicles/2025-bmw-m3-competition-xdrive/10.webp', '/media/vehicles/2025-bmw-m3-competition-xdrive/11.webp', '/media/vehicles/2025-bmw-m3-competition-xdrive/12.webp', '/media/vehicles/2025-bmw-m3-competition-xdrive/13.webp', '/media/vehicles/2025-bmw-m3-competition-xdrive/14.webp', '/media/vehicles/2025-bmw-m3-competition-xdrive/15.webp', '/media/vehicles/2025-bmw-m3-competition-xdrive/16.webp', '/media/vehicles/2025-bmw-m3-competition-xdrive/17.webp', '/media/vehicles/2025-bmw-m3-competition-xdrive/18.webp', '/media/vehicles/2025-bmw-m3-competition-xdrive/19.webp', '/media/vehicles/2025-bmw-m3-competition-xdrive/20.webp', '/media/vehicles/2025-bmw-m3-competition-xdrive/21.webp'],
        'price': 59999,
        'mileage': 18576,
        'transmission': 'Automatic',
        'drivetrain': 'All-Wheel Drive (AWD)',
        'engine': '3.0L Twin-Turbocharged I6',
        'exterior_color': 'Grey Black',
        'interior_color': 'Ivory White',
        'location': 'Florida',
        'features': ['2025 BMW M3 Competition xDrive', '3.0L Twin-Turbocharged I6', '8-Speed M Steptronic Automatic', 'xDrive AWD', 'Grey Black Exterior', 'Ivory White Full Merino Leather Interior', 'Driving Assistance Professional Package', 'Parking Assistance Package', 'Executive Package', 'M Drive Professional', 'Carbon Fiber Trim', 'Galvanic Controls', 'M Carbon Bucket Seats', 'M Carbon Exterior Package', 'Drive Recorder'],
        'description': 'This 2025 BMW M3 Competition xDrive comes in a gray and black exterior, which is pretty aggressive looking from the moment you set eyes upon it. At the rear, a prominent lower diffuser houses four tailpipes, while there’s a discrete but noticeable lip spoiler. Along the sides, you’ll see typical BMW performance cues such as M Performance disc brakes behind M multi-spoke alloy wheels that are staggered bicolor units. Meanwhile, the front sports BMW’s larger-than-life kidney grille that has heavily divided opinions, but at least provides abundant cooling air for the high-performance powertrain within. LED headlamps are also standard.\nThe Ivory White interior of this car comes with M Carbon Bucket Seats at the front, as well as Carbon Fiber interior trim. It’s got the Executive Package, M Drive Professional Package, Driver Recorder Package, Galvanic Controls Package and Driving Assistance Professional Package. There’s even the Parking Assistance Package and all the creature comforts and conveniences you’d expect. The car can seat five occupants, child seats can be strapped into the rear, and the trunk is your typical 3-Series affair. Yes, it’s pretty much as family friendly as you can get.\n\nEngine\nThis 2025 BMW M3 Competition xDrive is all-wheel drive hence the xDrive moniker. It’s got a fearsome 3.0-liter straight six under the hood. That doesn’t sound much initially, but let’s talk about the twin turbos that force copious amounts of air into it. Hence, it can reportedly develop 503hp and 479lb-ft, enough for 0-60 in less than 4 seconds. A smooth 8-speed ZF automatic gearbox handles shifting, and you can take control via the paddle shifters too.',
        'title': '2025 BMW M3 Competition xDrive',
        'lot_number': '260251832',
        'condition': None,
    },
    {
        'slug': '2025-bmw-x5-xdrive40i-silver-anniversary',
        'images': ['/media/vehicles/2025-bmw-x5-xdrive40i-silver-anniversary/01.webp', '/media/vehicles/2025-bmw-x5-xdrive40i-silver-anniversary/02.webp', '/media/vehicles/2025-bmw-x5-xdrive40i-silver-anniversary/03.webp', '/media/vehicles/2025-bmw-x5-xdrive40i-silver-anniversary/04.webp', '/media/vehicles/2025-bmw-x5-xdrive40i-silver-anniversary/05.webp', '/media/vehicles/2025-bmw-x5-xdrive40i-silver-anniversary/06.webp', '/media/vehicles/2025-bmw-x5-xdrive40i-silver-anniversary/07.webp', '/media/vehicles/2025-bmw-x5-xdrive40i-silver-anniversary/08.webp', '/media/vehicles/2025-bmw-x5-xdrive40i-silver-anniversary/09.webp', '/media/vehicles/2025-bmw-x5-xdrive40i-silver-anniversary/10.webp', '/media/vehicles/2025-bmw-x5-xdrive40i-silver-anniversary/11.webp', '/media/vehicles/2025-bmw-x5-xdrive40i-silver-anniversary/12.webp', '/media/vehicles/2025-bmw-x5-xdrive40i-silver-anniversary/13.webp', '/media/vehicles/2025-bmw-x5-xdrive40i-silver-anniversary/14.webp', '/media/vehicles/2025-bmw-x5-xdrive40i-silver-anniversary/15.webp', '/media/vehicles/2025-bmw-x5-xdrive40i-silver-anniversary/16.webp', '/media/vehicles/2025-bmw-x5-xdrive40i-silver-anniversary/17.webp', '/media/vehicles/2025-bmw-x5-xdrive40i-silver-anniversary/18.webp', '/media/vehicles/2025-bmw-x5-xdrive40i-silver-anniversary/19.webp', '/media/vehicles/2025-bmw-x5-xdrive40i-silver-anniversary/20.webp', '/media/vehicles/2025-bmw-x5-xdrive40i-silver-anniversary/21.webp'],
        'price': 42999,
        'mileage': 10019,
        'transmission': 'Automatic',
        'drivetrain': 'All-Wheel Drive (AWD)',
        'engine': '3.0L Twin-Turbocharged I6',
        'exterior_color': 'Lime Rock Grey Metallic',
        'interior_color': 'Cognac',
        'location': 'Florida',
        'features': ['2025 BMW X5 xDrive40i Silver Anniversary Edition', '3.0L Twin-Turbocharged I6 w/ 48V Mild-Hybrid Technology', '8-Speed Automatic', 'AWD', 'Lime Rock Grey Metallic Exterior', 'Cognac Sensafin Leather Interior', 'Off-Road Package:', 'Carbon Fiber Trim', 'Extended Shadowline Trim', 'Harman Kardon Surround Sound System', 'Heated Front Seats, Armrests & Steering Wheel', 'Illuminated Kidney Grille', 'Live Cockpit Pro (Including HUD)', 'M Shadowline Lights', 'M Sport Differential', 'Remote Engine Start', 'Roof Rails In High-Gloss Shadowline', 'Shadowline Exterior Trim', 'Trailer Hitch', '2-Axle Air Suspension', '20” M Star-Spoke Bicolor 740M Wheels', 'Parking Assistance Package:', 'Active Park Distance Control', 'Parking Assistant Professional', 'Parking View With 3D View (Surround View)', 'Special Edition'],
        'description': 'Lime Rock Gray Metallic is the color worn by this 2025 BMW X5 xDrive40i Silver Anniversary Edition and believe us, it looks suave. With its Extended Shadowline Exterior Trim, illuminated kidney grilles, M Shadowline lights and 20-inch M Star-Spoke Bicolor 740M wheels, this is definitely a head-turner to behold. You’ve also got 2-axle air suspension for excellent ride comfort, while a trailer hitch is present as well. Roof rails in High Gloss Shadowline complement this fine BMW’s exterior package.\nThe Cognac interior of this 2025 BMW X5 xDrive40i Silver Anniversary Edition features Sensafin leather upholstery and seats five adults in sheer comfort and luxury. There are many packages on board, including the Parking Assistant Professional, Parking View with 3D View, Active Park Distance Control, Carbon Fiber trim, Harman/Kardon surround sound system, and more. You’ve also got the BMW Live Cockpit Pro with heads-up display, heated and powered front seats with heating for the arm rests and steering wheel as well, multi-zone climate control, Apple CarPlay, Android Auto, a panoramic sunroof, and ample cargo space.\n\nEngine\nThis 2025 BMW X5 xDrive40i Silver Anniversary Edition comes with a 3.0-liter twin-turbo six under the hood. Aided by 48-volt mild-hybrid technology, the powerplant is reportedly rated at 329hp and 332lb-ft. All four wheels are driven via an 8-speed automatic transmission and an M Sport differential too. You’ll also find paddle shifters for manual gear shifting, and even a remote engine starter to pre-heat or pre-chill the interior.',
        'title': '2025 BMW X5 xDrive40i Silver Anniversary Edition',
        'lot_number': '250941883',
        'condition': None,
    },
    {
        'slug': '2020-bmw-m760i-xdrive',
        'images': ['/media/vehicles/2020-bmw-m760i-xdrive/01.webp', '/media/vehicles/2020-bmw-m760i-xdrive/02.webp', '/media/vehicles/2020-bmw-m760i-xdrive/03.webp', '/media/vehicles/2020-bmw-m760i-xdrive/04.webp', '/media/vehicles/2020-bmw-m760i-xdrive/05.webp', '/media/vehicles/2020-bmw-m760i-xdrive/06.webp', '/media/vehicles/2020-bmw-m760i-xdrive/07.webp', '/media/vehicles/2020-bmw-m760i-xdrive/08.webp', '/media/vehicles/2020-bmw-m760i-xdrive/09.webp', '/media/vehicles/2020-bmw-m760i-xdrive/10.webp', '/media/vehicles/2020-bmw-m760i-xdrive/11.webp', '/media/vehicles/2020-bmw-m760i-xdrive/12.webp', '/media/vehicles/2020-bmw-m760i-xdrive/13.webp', '/media/vehicles/2020-bmw-m760i-xdrive/14.webp', '/media/vehicles/2020-bmw-m760i-xdrive/15.webp', '/media/vehicles/2020-bmw-m760i-xdrive/16.webp', '/media/vehicles/2020-bmw-m760i-xdrive/17.webp', '/media/vehicles/2020-bmw-m760i-xdrive/18.webp', '/media/vehicles/2020-bmw-m760i-xdrive/19.webp', '/media/vehicles/2020-bmw-m760i-xdrive/20.webp', '/media/vehicles/2020-bmw-m760i-xdrive/21.webp', '/media/vehicles/2020-bmw-m760i-xdrive/22.webp', '/media/vehicles/2020-bmw-m760i-xdrive/23.webp', '/media/vehicles/2020-bmw-m760i-xdrive/24.webp', '/media/vehicles/2020-bmw-m760i-xdrive/25.webp'],
        'price': 40999,
        'mileage': 33002,
        'transmission': 'Automatic',
        'drivetrain': None,
        'engine': '6.6L V12',
        'exterior_color': 'Bernina Grey Amber Effect',
        'interior_color': 'Black Nappa',
        'location': 'Mississippi',
        'features': ['Bernina Grey Amber Effect Exterior', 'Black Nappa Leather Interior', 'Drivers Assistance Pro Package', 'Individual Piano Black Trim', 'Ambient Air Package', 'Panoramic Sky Lounge LED Roof', 'Icon Adaptive LED with Laserlight', 'Bowers and Wilkins Sound System', 'Extended Shadow Line Trim', 'Carbon Fiber Mirror Caps', 'Painted Rear Spoiler', 'Floating Hub Caps', 'LED Door Projector', 'M Performance Door Projector S', 'Load Sill Paint Protection', 'Original MSRP: $171,195'],
        'description': 'The 2020 BMW M760i drive is a perfect blend of fly-under-the-radar\nstealth along with its head-turning presence. This particular example\nis from the G11 generation of 7er and is an LCI, meaning it’s the\nfacelifted 7-Series with a more modern exterior and interior. With an\noriginal MSRP of over $170,000, this car is loaded with a myriad of\noptions. It features Icon Adaptive LEDs with Laser light, extended\nShadow Line trim, carbon fiber mirror caps, painted rear spoiler, and\nfloating hubcaps are all part of an extensive exterior options list.\nThis example is an M-Sport, which means aggressive bumpers and side\nsills along with upgraded brakes sitting behind 20-inch M-Sport\nwheels. The car is finished in a gorgeous deep Bernina grey amber\neffect paint with blacked-out accents.\nAs you step in, LED door projectors with the M Sport projection greet\nyou. The black Nappa leather interior offers electric seats all around\nto ensure all passengers ride in supreme comfort. The individual piano\nblack trim, along with a panoramic sky lounge LED roof, exudes\nsophistication and class. The Bowers and Wilkins sound system provides\nstate-of-the-art surround sound, giving an immersive audio experience.\n\nEngine\nThe best thing about BMW is even their luxury limousines are insanely\nfast and fun to drive. With the M-Sport tuning on top it is even more\naggressive. Powering the M760i is a 6.6-liter twin-turbocharged V12\nthat transfers 600 hp and 800 Nm of torque to all four wheels through\na smooth eight-speed automatic transmission. It sprints to 60 mph in\njust 3.5 seconds, which is impressive for a 6,000 lb luxury limousine.',
        'title': '2020 BMW M760i xDrive',
        'lot_number': '240516609',
        'condition': None,
    },
    {
        'slug': '2024-bmw-m4-competition-xdrive-convertible',
        'images': ['/media/vehicles/2024-bmw-m4-competition-xdrive-convertible/01.webp', '/media/vehicles/2024-bmw-m4-competition-xdrive-convertible/02.webp', '/media/vehicles/2024-bmw-m4-competition-xdrive-convertible/03.webp', '/media/vehicles/2024-bmw-m4-competition-xdrive-convertible/04.webp', '/media/vehicles/2024-bmw-m4-competition-xdrive-convertible/05.webp', '/media/vehicles/2024-bmw-m4-competition-xdrive-convertible/06.webp', '/media/vehicles/2024-bmw-m4-competition-xdrive-convertible/07.webp', '/media/vehicles/2024-bmw-m4-competition-xdrive-convertible/08.webp', '/media/vehicles/2024-bmw-m4-competition-xdrive-convertible/09.webp', '/media/vehicles/2024-bmw-m4-competition-xdrive-convertible/10.webp', '/media/vehicles/2024-bmw-m4-competition-xdrive-convertible/11.webp', '/media/vehicles/2024-bmw-m4-competition-xdrive-convertible/12.webp', '/media/vehicles/2024-bmw-m4-competition-xdrive-convertible/13.webp', '/media/vehicles/2024-bmw-m4-competition-xdrive-convertible/14.webp', '/media/vehicles/2024-bmw-m4-competition-xdrive-convertible/15.webp', '/media/vehicles/2024-bmw-m4-competition-xdrive-convertible/16.webp', '/media/vehicles/2024-bmw-m4-competition-xdrive-convertible/17.webp'],
        'price': 56999,
        'mileage': 14796,
        'transmission': 'Automatic',
        'drivetrain': 'All-Wheel Drive (AWD)',
        'engine': '3.0L Twin-Turbocharged I6',
        'exterior_color': 'Black Sapphire Metallic',
        'interior_color': 'Black',
        'location': 'Georgia',
        'features': ['2024 BMW M4 Competition xDrive Convertible', '3.0L Twin-Turbocharged I6', '8-Speed M Steptronic Automatic', 'xDrive AWD', 'Satin Black Vinyl Wrap', 'Black Sapphire Metallic Exterior', 'Black Extended Merino Leather Interior', 'Driving Assistance Professional Package', 'Parking Assistance Package', 'Executive Package', 'M Compound Brakes w/ Red Calipers', 'M Shadowline Lights', 'Icon Adaptive LED Headlights w/ Laserlight', 'Neck Warmer', 'Carbon Fiber Interior Trim', 'Drive Recorder'],
        'description': 'Originally, this 2024 BMW M4 Competition came in Black Sapphire Metallic. That paint job is still there, beneath the matte black vinyl wrap that this car currently wears. So, the choice is yours – metallic paint or matte effect. Regardless of your choice, the black powered soft top complements the car’s looks, as do the 826M Bi-Color wheels that are 19-inches at the front and 20-inches at the rear. You’ve also got M Shadowline lights, as well as the red calipers of those M Compound upgraded brakes. Quad tailpipes out back aren’t for show either, they really let out a spine-tingling soundtrack when you drive this car hard.\nThe black interior of this 2024 BMW M4 Competition can seat four occupants and comes with the Extended Merino Leather specification. It’s your typical BMW driver-focused cabin with a digital gauge cluster, BMW’s iDrive infotainment system, and paddle shifters on the multifunction steering wheel. You’ll also find a nice Harman/Kardon sound system that gels well with your choice of tunes, ideally piped via Apple CarPlay or Android Auto. Other features include climate control, powered and heated front seats, charging ports, cup holders and all the usual refinements you’d expect from a BMW. You’ve also got a Drive Recorder and M Performance floor mats.\n\nEngine\nThis 2024 BMW M4 Competition features a twin-turbocharged 3.0-liter straight six. The engine is tuned to deliver 503hp and 479lb-ft. It’s twinned with an ZF 8-speed automatic gearbox and drives all four wheels. Thanks to the all-wheel drive system, a low 3-second 0-60 time is very doable.',
        'title': '2024 BMW M4 Competition xDrive Convertible',
        'lot_number': '260252751',
        'condition': None,
    },
    {
        'slug': '2024-gmc-sierra-2500-at4',
        'images': ['/media/vehicles/2024-gmc-sierra-2500-at4/01.webp', '/media/vehicles/2024-gmc-sierra-2500-at4/02.webp', '/media/vehicles/2024-gmc-sierra-2500-at4/03.webp', '/media/vehicles/2024-gmc-sierra-2500-at4/04.webp', '/media/vehicles/2024-gmc-sierra-2500-at4/05.webp', '/media/vehicles/2024-gmc-sierra-2500-at4/06.webp', '/media/vehicles/2024-gmc-sierra-2500-at4/07.webp', '/media/vehicles/2024-gmc-sierra-2500-at4/08.webp', '/media/vehicles/2024-gmc-sierra-2500-at4/09.webp', '/media/vehicles/2024-gmc-sierra-2500-at4/10.webp', '/media/vehicles/2024-gmc-sierra-2500-at4/11.webp', '/media/vehicles/2024-gmc-sierra-2500-at4/12.webp', '/media/vehicles/2024-gmc-sierra-2500-at4/13.webp', '/media/vehicles/2024-gmc-sierra-2500-at4/14.webp', '/media/vehicles/2024-gmc-sierra-2500-at4/15.webp', '/media/vehicles/2024-gmc-sierra-2500-at4/16.webp', '/media/vehicles/2024-gmc-sierra-2500-at4/17.webp', '/media/vehicles/2024-gmc-sierra-2500-at4/18.webp', '/media/vehicles/2024-gmc-sierra-2500-at4/19.webp', '/media/vehicles/2024-gmc-sierra-2500-at4/20.webp', '/media/vehicles/2024-gmc-sierra-2500-at4/21.webp'],
        'price': 51999,
        'mileage': 14200,
        'transmission': 'Automatic',
        'drivetrain': 'Four-Wheel Drive (4WD)',
        'engine': '6.6L Turbo-Diesel V8',
        'exterior_color': 'Summit White',
        'interior_color': 'Jet Black',
        'location': 'California',
        'features': ['2024 GMC Sierra 2500HD Crew Cab AT4', 'Duramax 6.6L Turbo-Diesel V8', 'Allison 10-Speed Automatic', 'RWD w/ 4x4', 'Summit White Exterior', 'Jet Black Interior w/ Kalahari Accents', 'AT4 Premium Plus Preferred Package', 'Body Color Wheel Arch Moldings', 'Gooseneck/5th Wheel Package', 'All-Weather Floor Liners', 'Sport Pedal Cover Kit', 'GMC MultiPro Tailgate Step Lights', 'Cargo Tie-Downs', 'Heavy-Duty Front Springs / Camper Package', 'Rear Axle, 3.42 Ratio', 'GVWR, 11,350 Lbs', '6.5" Lift Kit w/ BDS Adjustable Coilovers', 'Front & Rear FOX Shocks', '22" Foreplay Wheels', '35" Toyo R/T Tires', 'Tinted Windows'],
        'description': 'Wearing a white coat, you’ll immediately notice that this 2024 GMC Sierra 2500 HD Crew Cab sits taller than stock. That’s because it’s got a 6.5-inch lift with BDS adjustable coilovers plus front and rear FOX shocks. Moreover, the lift is needed to amply accommodate the 35-inch Toyo R/T tires on 22-inch Foreplay aftermarket wheels. You’ve also got the AT4 Premium Plus Package, Preferred Package, a power-sliding rear window and even the Gooseneck and Fifth Wheel Package. The cargo bed features stamped holes with caps for better cargo securing, as well as a 7-pin trailer harness. Meanwhile, the passenger cabin enjoys tinted windows, and the cargo bed is protected via a tonneau cover. Yup, you can use this truck like an SUV if you desire.\nThe interior of this 2024 GMC Sierra 2500 HD Crew Cab comes with gray leather upholstery and can easily accommodate five full-sized adults. In fact, if we take the cabin’s interior volume in a purely academic sense, it’s roomier than many full-size luxury sedans! Plus, you’ve got features such as adaptive cruise control, the Technology Package, a multi-color heads-up display, dual-zone climate control and even a power sunroof. Apple CarPlay and Android Auto are standard, as is a Bose sound system too.\n\nEngine\nThis 2024 GMC Sierra 2500 HD Crew Cab packs a 6.6-liter Duramax turbodiesel V8 under the hood. It’s rated to reportedly make 470hp and 975lb-ft, which are staggering figures, to say the least. Power is sent to all four wheels through a 10-speed automatic gearbox from Allison.',
        'title': '2024 GMC Sierra 2500 AT4',
        'lot_number': '260149223',
        'condition': None,
    },
    {
        'slug': '2025-chevrolet-corvette-z06-convertible-2lz',
        'images': ['/media/vehicles/2025-chevrolet-corvette-z06-convertible-2lz/01.webp', '/media/vehicles/2025-chevrolet-corvette-z06-convertible-2lz/02.webp', '/media/vehicles/2025-chevrolet-corvette-z06-convertible-2lz/03.webp', '/media/vehicles/2025-chevrolet-corvette-z06-convertible-2lz/04.webp', '/media/vehicles/2025-chevrolet-corvette-z06-convertible-2lz/05.webp', '/media/vehicles/2025-chevrolet-corvette-z06-convertible-2lz/06.webp', '/media/vehicles/2025-chevrolet-corvette-z06-convertible-2lz/07.webp', '/media/vehicles/2025-chevrolet-corvette-z06-convertible-2lz/08.webp', '/media/vehicles/2025-chevrolet-corvette-z06-convertible-2lz/09.webp', '/media/vehicles/2025-chevrolet-corvette-z06-convertible-2lz/10.webp', '/media/vehicles/2025-chevrolet-corvette-z06-convertible-2lz/11.webp', '/media/vehicles/2025-chevrolet-corvette-z06-convertible-2lz/12.webp', '/media/vehicles/2025-chevrolet-corvette-z06-convertible-2lz/13.webp', '/media/vehicles/2025-chevrolet-corvette-z06-convertible-2lz/14.webp', '/media/vehicles/2025-chevrolet-corvette-z06-convertible-2lz/15.webp', '/media/vehicles/2025-chevrolet-corvette-z06-convertible-2lz/16.webp', '/media/vehicles/2025-chevrolet-corvette-z06-convertible-2lz/17.webp', '/media/vehicles/2025-chevrolet-corvette-z06-convertible-2lz/18.webp', '/media/vehicles/2025-chevrolet-corvette-z06-convertible-2lz/19.webp'],
        'price': 86999,
        'mileage': 5224,
        'transmission': 'Dual-clutch Transmission (DCT)',
        'drivetrain': 'Rear-Wheel Drive (RWD)',
        'engine': '5.5L Naturally Aspirated V8',
        'exterior_color': 'Red Mist Metallic',
        'interior_color': 'Jet Black',
        'location': 'Arizona',
        'features': ['2025 Chevrolet Corvette Z06 Convertible 2LZ', '5.5L Naturally Aspirated V8', '8-Speed Dual-Clutch Automatic', 'RWD', 'Red Mist Metallic Tintcoat Exterior', 'Jet Black Interior', 'Front Lift Adjustable Height Memory', 'GT2 Bucket Seats', 'Carbon Flash Painted Nacelles & Convertible Roof', 'Gloss Black Forged Aluminum Spider Design Wheels', 'Scrape Armor Grille', 'Edge Red-Painted Brake Calipers', 'Contoured Liner Protection Package', 'Black Exhaust Tips', 'Clear Spoiler Bridge', 'Black Lug Nuts', 'Carbon Flash Metallic Painted Outside Mirrors', 'Battery Protection Package', 'AutoNation Vehicle Protection Plan (VPP Standard Platinum)', 'Chevrolet Pre-Paid Maintenance (Premier Plan)', 'Ceramic Pro Ultimate Armor Exterior Coating', 'KAVACA Paint Protection Film', 'ClearPlex Windshield Protection Film', 'Ceramic IR Window Tint', 'Ceramic Pro Wheel-Off Wheel & Caliper Coating', 'Ceramic Pro Lux Interior Coating'],
        'description': 'Dressed in Red Mist Metallic Tintcoat, this 2025 Chevrolet Corvette Convertible Z06 2LZ comes with Carbon Flash painted rear-view mirrors, nacelles and convertible roof, which is a power-retracting metal panel in case you were wondering. Then, it’s got a Scrape Armor grille, and a set of gloss black forged aluminum spider-design wheels with black lug nuts. We’re told that there’s Ceramic IR window tint, Ceramic Pro Wheel-Off wheel and caliper coating, a ClearPlex windshield protection film, A KAVACA paint protection film and Ceramic Pro Ultimate Armor exterior coating. Furthermore, there’s a Chevy Pre-Paid Maintenance Premier Plan too.\nThe Jet Black interior comes with GT2 bucket seats that are heated, ventilated, power adjustable and have memory functionality as well. We’re told that the interior has received a Ceramic Pro Lux interior coating too. You’ve got Apple CarPlay, Android Auto, automatic climate control, a Bose Professional Series sound system, and so much more to enjoy.\n\nEngine\nThe 5.5-liter V8 that moves this 2025 Chevrolet Corvette Convertible Z06 2LZ is a high-rev screamer. It delivers 670hp at 8,400rpm with maximum torque of 460lb-ft coming in at 6,300rpm. Paired with an 8-speed dual-clutch automatic transmission and rear-wheel drive, this car is a beast to drive. Official figures place the 0-60 time at 2.6 seconds, with a 195mph top speed.',
        'title': '2025 Chevrolet Corvette Z06 Convertible 2LZ',
        'lot_number': '251247726',
        'condition': None,
    },
    {
        'slug': '2022-gmc-sierra-1500-elevation',
        'images': ['/media/vehicles/2022-gmc-sierra-1500-elevation/01.webp', '/media/vehicles/2022-gmc-sierra-1500-elevation/02.webp', '/media/vehicles/2022-gmc-sierra-1500-elevation/03.webp', '/media/vehicles/2022-gmc-sierra-1500-elevation/04.webp', '/media/vehicles/2022-gmc-sierra-1500-elevation/05.webp', '/media/vehicles/2022-gmc-sierra-1500-elevation/06.webp', '/media/vehicles/2022-gmc-sierra-1500-elevation/07.webp', '/media/vehicles/2022-gmc-sierra-1500-elevation/08.webp', '/media/vehicles/2022-gmc-sierra-1500-elevation/09.webp', '/media/vehicles/2022-gmc-sierra-1500-elevation/10.webp', '/media/vehicles/2022-gmc-sierra-1500-elevation/11.webp', '/media/vehicles/2022-gmc-sierra-1500-elevation/12.webp', '/media/vehicles/2022-gmc-sierra-1500-elevation/13.webp', '/media/vehicles/2022-gmc-sierra-1500-elevation/14.webp', '/media/vehicles/2022-gmc-sierra-1500-elevation/15.webp', '/media/vehicles/2022-gmc-sierra-1500-elevation/16.webp'],
        'price': 29999,
        'mileage': 33836,
        'transmission': 'Automatic',
        'drivetrain': 'Four-Wheel Drive (4WD)',
        'engine': '3.0L Turbo-Diesel I6',
        'exterior_color': 'Onyx Black',
        'interior_color': 'Jet Black',
        'location': 'Florida',
        'features': ['2022 GMC Sierra 1500 Elevation', 'Duramax 3.0L Turbo Diesel I6', '10-Speed Automatic', 'RWD w/ 4x4', 'Onyx Black Exterior', 'Jet Black Interior', 'Elevation Premium Package', 'X31 Off-Road & Protection Package', 'Elevation Black Package', 'Front Bucket Seats w/ Center Console', 'GVWR 7,200 lbs', 'Rear Axle 3.23 Ratio', '20” Painted High-Gloss Black Aluminum Wheels', 'Rear Park Assist'],
        'description': 'Finished in Onyx Black with matching blacked-out accents, this Sierra presents a clean and aggressive appearance. The 20-inch high-gloss black wheels, black assist steps, and black GMC badging give it a cohesive, sport-oriented look. Inside, the Jet Black cabin is equipped with leather-appointed seating, heated front seats, a heated steering wheel, and dual-zone climate control. The large 13.4-inch touchscreen and 12.3-inch digital driver display create a modern, driver-focused environment, while HD Surround Vision and advanced camera systems improve visibility and ease of use.\n\nEngine\nThe Duramax 3.0L turbo-diesel inline-six is known for its smooth power delivery, strong torque output, and long-range efficiency. Paired with a 10-speed automatic transmission and four-wheel drive, this Sierra handles highway cruising, trailering, and off-road conditions with confidence. The X31 Off-Road package adds additional capability through an off-road suspension, skid plates, and all-terrain tires, while integrated trailering technology and trailer brake control make this truck a highly capable and refined tow vehicle.',
        'title': '2022 GMC Sierra 1500 Elevation',
        'lot_number': '251247495',
        'condition': None,
    },
    {
        'slug': '2021-gmc-sierra-1500-denali',
        'images': ['/media/vehicles/2021-gmc-sierra-1500-denali/01.webp', '/media/vehicles/2021-gmc-sierra-1500-denali/02.webp', '/media/vehicles/2021-gmc-sierra-1500-denali/03.webp', '/media/vehicles/2021-gmc-sierra-1500-denali/04.webp', '/media/vehicles/2021-gmc-sierra-1500-denali/05.webp', '/media/vehicles/2021-gmc-sierra-1500-denali/06.webp', '/media/vehicles/2021-gmc-sierra-1500-denali/07.webp', '/media/vehicles/2021-gmc-sierra-1500-denali/08.webp', '/media/vehicles/2021-gmc-sierra-1500-denali/09.webp', '/media/vehicles/2021-gmc-sierra-1500-denali/10.webp', '/media/vehicles/2021-gmc-sierra-1500-denali/11.webp', '/media/vehicles/2021-gmc-sierra-1500-denali/12.webp', '/media/vehicles/2021-gmc-sierra-1500-denali/13.webp', '/media/vehicles/2021-gmc-sierra-1500-denali/14.webp', '/media/vehicles/2021-gmc-sierra-1500-denali/15.webp', '/media/vehicles/2021-gmc-sierra-1500-denali/16.webp', '/media/vehicles/2021-gmc-sierra-1500-denali/17.webp', '/media/vehicles/2021-gmc-sierra-1500-denali/18.webp', '/media/vehicles/2021-gmc-sierra-1500-denali/19.webp', '/media/vehicles/2021-gmc-sierra-1500-denali/20.webp'],
        'price': 26999,
        'mileage': 18802,
        'transmission': 'Automatic',
        'drivetrain': 'Four-Wheel Drive (4WD)',
        'engine': '5.3L V8',
        'exterior_color': 'Satin Steel Metallic',
        'interior_color': 'Jet Black',
        'location': 'Florida',
        'features': ['2021 GMC Sierra 1500 Crew Cab Denali', '5.3L EcoTec3 V8', '10-Speed Automatic', 'RWD w/ 4x4', 'Satin Steel Metallic Exterior', 'Jet Black Interior', 'Technology Package', 'Driver Alert Package II', 'Power Sunroof', 'Weather Tech Mats', 'Diamondback Bed Cover', 'Aftermarket Rhino Wheels', 'Aftermarket ARB Bumpers', 'Chrome Assist Steps', 'Aftermarket Remote Powered Warn Winch, 12k lbs', 'Up-To-Date Servicing'],
        'description': 'The color worn by this 2021 GMC Sierra 1500 Denali is called Satin Steel Metallic, and it’s a smooth shade of gray that will look equally good when caked with mud as it would when detailed and waxed. This truck also seems to ride higher than stock, and rolls on a set of aftermarket Rhino wheels with Toyo Open Country A/T tires for more off-road capability. Then, there’s a set of aftermarket ARB bumpers, and a remotely operated aftermarket Warn winch that can pull up to 12,000 pounds. Accessing the truck’s passenger cabin is made easier as well, by the presence of chrome assist steps. Meanwhile, a Diamond Back bed cover keeps your cargo safe and secure from the elements or opportunistic thieves.\nClimb into the cabin and you’ll discover it to be quite luxurious. Your feet will rest upon WeatherTech mats, while the seats are upholstered in supple black leather. The front and outboard rear seats have heating as well, and there’s dual-zone automatic climate control with air conditioning and rear air vents too. Moreover, the front seats have ventilation and power adjustment for even more comfort and ergonomic benefit. There’s a touchscreen infotainment system with Apple CarPlay and Android Auto, as well as a digital screen between the two major analog gauges in the instrument cluster. A Bose sound system takes care of your tunes, while front plus rear USB charging ports keeps everyone’s devices juiced up.\n\nEngine\nA gargantuan vehicle like this 2021 GMC Sierra 1500 Denali needs a suitably potent engine, and we’ve got a 5.3-liter V8 with 355hp and 383lb-ft on tap. The engine powers all four wheels through a 10-speed automatic transmission for effortless cruising abilities and off-road prowess.',
        'title': '2021 GMC Sierra 1500 Denali',
        'lot_number': '250331649',
        'condition': None,
    },
    {
        'slug': '2025-cadillac-ct5-v-blackwing',
        'images': ['/media/vehicles/2025-cadillac-ct5-v-blackwing/01.webp', '/media/vehicles/2025-cadillac-ct5-v-blackwing/02.webp', '/media/vehicles/2025-cadillac-ct5-v-blackwing/03.webp', '/media/vehicles/2025-cadillac-ct5-v-blackwing/04.webp', '/media/vehicles/2025-cadillac-ct5-v-blackwing/05.webp', '/media/vehicles/2025-cadillac-ct5-v-blackwing/06.webp', '/media/vehicles/2025-cadillac-ct5-v-blackwing/07.webp', '/media/vehicles/2025-cadillac-ct5-v-blackwing/08.webp', '/media/vehicles/2025-cadillac-ct5-v-blackwing/09.webp', '/media/vehicles/2025-cadillac-ct5-v-blackwing/10.webp', '/media/vehicles/2025-cadillac-ct5-v-blackwing/11.webp', '/media/vehicles/2025-cadillac-ct5-v-blackwing/12.webp', '/media/vehicles/2025-cadillac-ct5-v-blackwing/13.webp', '/media/vehicles/2025-cadillac-ct5-v-blackwing/14.webp', '/media/vehicles/2025-cadillac-ct5-v-blackwing/15.webp', '/media/vehicles/2025-cadillac-ct5-v-blackwing/16.webp', '/media/vehicles/2025-cadillac-ct5-v-blackwing/17.webp', '/media/vehicles/2025-cadillac-ct5-v-blackwing/18.webp', '/media/vehicles/2025-cadillac-ct5-v-blackwing/19.webp', '/media/vehicles/2025-cadillac-ct5-v-blackwing/20.webp', '/media/vehicles/2025-cadillac-ct5-v-blackwing/21.webp', '/media/vehicles/2025-cadillac-ct5-v-blackwing/22.webp', '/media/vehicles/2025-cadillac-ct5-v-blackwing/23.webp', '/media/vehicles/2025-cadillac-ct5-v-blackwing/24.webp', '/media/vehicles/2025-cadillac-ct5-v-blackwing/25.webp'],
        'price': 82999,
        'mileage': 4237,
        'transmission': 'Automatic',
        'drivetrain': 'Rear-Wheel Drive (RWD)',
        'engine': '6.2L Supercharged V8',
        'exterior_color': 'Typhoon Metallic',
        'interior_color': 'Natural Tan/Jet Black',
        'location': 'Florida',
        'features': ['2025 Cadillac CT5-V Blackwing', '6.2L Supercharged V8', '10-Speed Automatic', 'RWD', 'Typhoon Metallic Exterior', 'Natural Tan/Jet Black Interior', 'Precision Package', 'Natural Tan w/ Jet Black Accents w/ Full Semi-Aniline Leather Seats w/ Custom Quilting & Carbon fiber Front Seatbacks', 'Super Cruise 1 Package', 'Performance Data & Video Recorder', '19" Aluminum Alloy Wheels w/ Tech Bronze Finish', 'Ultra View Sunroof', 'Parking Package', 'Interior Protection Package'],
        'description': 'Bronze wheels don’t suit every car, but with the shade of green on this car (Typhoon Metallic) it is the perfect choice. The wheels on this car are 19” aluminum alloy wheels with a tech bronze finish. The CT5 got a facelift for 2025, and Cadillac somehow took an already good-looking car and made it even better. The interior is a combination of Natural Tan and Jet Black, and the leather seats have custom quilting and carbon fiber front seatbacks. The steering wheel is also leather wrapped and has alloy paddleshift controls. In terms of options, this vehicle has been equipped with the Precision Package, the Super Cruise 1 Package (giving it self-driving capabilities) and the parking package (which includes a rear camera mirror). The tech doesn’t stop there either; it has a sensor that indicates air quality, driver attention assist, a hands-free decklid release and a performance data and video recorder. It also has an ultra-view sunroof. In short, it is truly the Cadillac of muscle cars.\n\nEngine\nThe standard transmission on the Blackwing is a 6-speed manual, which is probably more fun-oriented. This particular car has been optioned with the 10-speed automatic, which is both more convenient and statistically faster. Regardless of the transmission chosen, the Blackwing will always be a fun car thanks to its 6.2L supercharged V8 and rear-wheel drive setup.',
        'title': '2025 Cadillac CT5-V Blackwing',
        'lot_number': '250839960',
        'condition': None,
    },
    {
        'slug': '2023-cadillac-ct5-v-blackwing-edition',
        'images': ['/media/vehicles/2023-cadillac-ct5-v-blackwing-edition/01.webp', '/media/vehicles/2023-cadillac-ct5-v-blackwing-edition/02.webp', '/media/vehicles/2023-cadillac-ct5-v-blackwing-edition/03.webp', '/media/vehicles/2023-cadillac-ct5-v-blackwing-edition/04.webp', '/media/vehicles/2023-cadillac-ct5-v-blackwing-edition/05.webp', '/media/vehicles/2023-cadillac-ct5-v-blackwing-edition/06.webp', '/media/vehicles/2023-cadillac-ct5-v-blackwing-edition/07.webp', '/media/vehicles/2023-cadillac-ct5-v-blackwing-edition/08.webp', '/media/vehicles/2023-cadillac-ct5-v-blackwing-edition/09.webp', '/media/vehicles/2023-cadillac-ct5-v-blackwing-edition/10.webp', '/media/vehicles/2023-cadillac-ct5-v-blackwing-edition/11.webp', '/media/vehicles/2023-cadillac-ct5-v-blackwing-edition/12.webp', '/media/vehicles/2023-cadillac-ct5-v-blackwing-edition/13.webp', '/media/vehicles/2023-cadillac-ct5-v-blackwing-edition/14.webp', '/media/vehicles/2023-cadillac-ct5-v-blackwing-edition/15.webp', '/media/vehicles/2023-cadillac-ct5-v-blackwing-edition/16.webp', '/media/vehicles/2023-cadillac-ct5-v-blackwing-edition/17.webp', '/media/vehicles/2023-cadillac-ct5-v-blackwing-edition/18.webp', '/media/vehicles/2023-cadillac-ct5-v-blackwing-edition/19.webp'],
        'price': 63999,
        'mileage': 12000,
        'transmission': 'Automatic',
        'drivetrain': None,
        'engine': '6.2L V8',
        'exterior_color': 'Summit White',
        'interior_color': 'Lightning Package',
        'location': 'Michigan',
        'features': ['2023 MY Cadillac CT5-V Blackwing Edition', '10-speed automatic transmission', 'Driver Assist Package', 'Enhanced automatic emergency braking', 'Reverse automatic braking', 'Red painted brake calipers', 'Torch Red seat belts', 'Heated & ventilated front seats', 'WiFi hotspot capability', 'BREMBO front & rear brakes', 'High performance mesh grille', 'Aero decklid spoiler', 'Adaptive suspension with magnetic ride control', 'Quad tipped exhaust', '19" alloy wheels with polished finish', 'High performance steering wheel with carbon fiber', 'Premium 16-speaker AKG premium audio system', 'V-Series floor mats', 'Head-up display', 'Wireless phone charging'],
        'description': 'Just as striking as its performance capabilities, the 2023 Cadillac CT5-V Blackwing Edition boasts a commanding visage highlighted by its high-performance mesh grille. The elegant Summit White paint gracefully contours the sedan\'s lines, while an Aero deck lid spoiler adds a subtle touch of aggression to the rear. Just below it, a Quad-tipped exhaust system serenades the symphony of its potent engine. The sedan elegantly rides on 19" polished alloy wheels enveloped by BREMBO front and rear brakes adorned with bold red calipers—Cadillac\'s largest factory-installed brakes to date.\nThe interior of this 2023 Cadillac CT5-V Blackwing Edition enjoys both the Lightning Package and Driver Assist Package, harmonizing perfectly. Torch Red seat belts contrast stylishly with the black Heated & Ventilated front seats featuring white piping. The multifunctional high-performance steering wheel incorporates carbon fiber trim, while V-Series floor mats embrace your feet. Noteworthy technological features encompass a Head-up display, a premium 16-speaker AKG audio system, and WiFi hotspot capability.\n\nEngine\nElevating the power of the CT5-V\'s supercharged 6.2-liter V-8 engine, this updated version reigns supreme in the heart of our 2023 Cadillac CT5-V Blackwing Edition. Unleashing an astonishing 668 horsepower and 659 lb-ft of torque, this juggernaut pairs with the optional 10-speed automatic transmission. As a result, our sedan can catapult from 0 to 60 in a mere 3.4 seconds. Safety and comfort seamlessly merge with performance, thanks to features like enhanced automatic emergency braking, reverse automatic braking, and an adaptive suspension with magnetic ride control.',
        'title': '2023 Cadillac CT5-V Blackwing Edition',
        'lot_number': '23106854',
        'condition': None,
    },
    {
        'slug': '2023-cadillac-escalade-sport-platinum-onyx',
        'images': ['/media/vehicles/2023-cadillac-escalade-sport-platinum-onyx/01.webp', '/media/vehicles/2023-cadillac-escalade-sport-platinum-onyx/02.webp', '/media/vehicles/2023-cadillac-escalade-sport-platinum-onyx/03.webp', '/media/vehicles/2023-cadillac-escalade-sport-platinum-onyx/04.webp', '/media/vehicles/2023-cadillac-escalade-sport-platinum-onyx/05.webp', '/media/vehicles/2023-cadillac-escalade-sport-platinum-onyx/06.webp', '/media/vehicles/2023-cadillac-escalade-sport-platinum-onyx/07.webp', '/media/vehicles/2023-cadillac-escalade-sport-platinum-onyx/08.webp', '/media/vehicles/2023-cadillac-escalade-sport-platinum-onyx/09.webp', '/media/vehicles/2023-cadillac-escalade-sport-platinum-onyx/10.webp', '/media/vehicles/2023-cadillac-escalade-sport-platinum-onyx/11.webp', '/media/vehicles/2023-cadillac-escalade-sport-platinum-onyx/12.webp', '/media/vehicles/2023-cadillac-escalade-sport-platinum-onyx/13.webp', '/media/vehicles/2023-cadillac-escalade-sport-platinum-onyx/14.webp', '/media/vehicles/2023-cadillac-escalade-sport-platinum-onyx/15.webp', '/media/vehicles/2023-cadillac-escalade-sport-platinum-onyx/16.webp', '/media/vehicles/2023-cadillac-escalade-sport-platinum-onyx/17.webp', '/media/vehicles/2023-cadillac-escalade-sport-platinum-onyx/18.webp', '/media/vehicles/2023-cadillac-escalade-sport-platinum-onyx/19.webp', '/media/vehicles/2023-cadillac-escalade-sport-platinum-onyx/20.webp', '/media/vehicles/2023-cadillac-escalade-sport-platinum-onyx/21.webp', '/media/vehicles/2023-cadillac-escalade-sport-platinum-onyx/22.webp'],
        'price': 64999,
        'mileage': 250,
        'transmission': 'Automatic',
        'drivetrain': None,
        'engine': '6.2L V8',
        'exterior_color': 'Black Raven',
        'interior_color': 'Dark Auburn/Black Accents',
        'location': 'Pennsylvania',
        'features': ['Black Raven exterior', 'Dark Auburn/Black accents interior', '4WD Sport Platinum', 'Onyx Package', 'Super Cruise - might require activation', 'Power retractable assist steps', '6.2L V8', '10 Speed automatic transmission'],
        'description': "A cursory examination of the 2023 Cadillac Escalade Sport Platinum 4WD reveals an understated yet commanding presence. Cloaked in a Black Raven paint finish, this exterior exudes an air of stealth and elegance. Key exterior elements, such as the front grille, harmoniously adopt the black theme, imparting a sense of unity to the design. The discerning owner has bestowed this modern American luxury SUV with the Onyx package, which introduces monochromatic Cadillac emblems and a gloss black Cadillac nameplate. The package further elevates the aesthetic appeal with 22-inch 12-spoke wheels finished in black, reinforcing the Escalade's contemporary and sophisticated character.\nStepping into the interior of the 2023 Cadillac Escalade Sport Platinum 4WD is an exercise in opulence. The power-retractable assist steps graciously facilitate entry into the luxurious two-tone dark Auburn and black cabin. This distinctive interior color scheme creates an ambiance that seamlessly marries technology and luxury. The auburn leather seats cocoon passengers in unparalleled comfort, a testament to Cadillac's unwavering commitment to providing a superior driving experience. The cabin is also home to a state-of-the-art AKG sound system, ensuring that every note of your chosen tunes resonates with exceptional clarity and fidelity.\n\nEngine\nThe 2023 Cadillac Escalade Sport Platinum 4WD perfectly exemplifies the fusion of luxury, performance, and sophistication that defines this iconic SUV. Nestled beneath the hood lies a commanding Ecotec 6.2L V8 powerplant, meticulously engineered to complement the sumptuous interior with a thrilling and effortless driving experience. Generating a robust 420 horsepower, this formidable powertrain distributes its ample might to all four wheels through a seamlessly responsive 10-speed automatic transmission. This harmonious integration ensures that each journey is marked by both power and poise, a testament to the artistry of modern American luxury motoring.",
        'title': '2023 Cadillac Escalade Sport Platinum 4WD Onyx Package',
        'lot_number': '23095427',
        'condition': None,
    },
    {
        'slug': '2024-cadillac-escalade-v',
        'images': ['/media/vehicles/2024-cadillac-escalade-v/01.webp', '/media/vehicles/2024-cadillac-escalade-v/02.webp', '/media/vehicles/2024-cadillac-escalade-v/03.webp', '/media/vehicles/2024-cadillac-escalade-v/04.webp', '/media/vehicles/2024-cadillac-escalade-v/05.webp', '/media/vehicles/2024-cadillac-escalade-v/06.webp', '/media/vehicles/2024-cadillac-escalade-v/07.webp', '/media/vehicles/2024-cadillac-escalade-v/08.webp', '/media/vehicles/2024-cadillac-escalade-v/09.webp', '/media/vehicles/2024-cadillac-escalade-v/10.webp', '/media/vehicles/2024-cadillac-escalade-v/11.webp', '/media/vehicles/2024-cadillac-escalade-v/12.webp', '/media/vehicles/2024-cadillac-escalade-v/13.webp', '/media/vehicles/2024-cadillac-escalade-v/14.webp', '/media/vehicles/2024-cadillac-escalade-v/15.webp', '/media/vehicles/2024-cadillac-escalade-v/16.webp', '/media/vehicles/2024-cadillac-escalade-v/17.webp', '/media/vehicles/2024-cadillac-escalade-v/18.webp', '/media/vehicles/2024-cadillac-escalade-v/19.webp', '/media/vehicles/2024-cadillac-escalade-v/20.webp', '/media/vehicles/2024-cadillac-escalade-v/21.webp', '/media/vehicles/2024-cadillac-escalade-v/22.webp', '/media/vehicles/2024-cadillac-escalade-v/23.webp', '/media/vehicles/2024-cadillac-escalade-v/24.webp', '/media/vehicles/2024-cadillac-escalade-v/25.webp', '/media/vehicles/2024-cadillac-escalade-v/26.webp'],
        'price': 94999,
        'mileage': 8800,
        'transmission': 'Automatic',
        'drivetrain': None,
        'engine': '6.2L V8',
        'exterior_color': 'Dark Emerald Metallic',
        'interior_color': 'Jet Black',
        'location': 'Iowa',
        'features': ['6.2L Supercharged V8 Engine', '10 Speed Automatic Transmission', 'REAR WHEEL DRIVE W/ 4X4', 'V-SERIES EXCLUSIVE:', 'SEMI-ANILINE LEATHER SEATS ALL THREE ROWS', 'LEATHER-WRAPPED INTERIOR TRIM', '20TH ANNIVERSARY V-SERIES PKG', 'ONYX PACKAGE (DLR INSTALLED)', 'GLOSS BLACK ESCALADE NAMEPLATE (DLR INSTALLED)', 'MONOCHROMATIC CADILLAC EMBLEM (DLR INSTALLED)', 'WHEELS, 22" FORGED MULTISPOKE W/ SATIN GRAPHITE FINISH &', 'CONSOLE REFRIGERATOR W/ FREEZER', 'Heated and Ventilated Seats', 'Head Up Display', 'Panoramic Roof'],
        'description': 'This 2024 Cadillac Escalade V is a fifth-generation example and wears a lovely Dark Emerald Metallic suit. The vehicle comes with the Onyx Package, which was dealer-installed, as well as a gloss black ESCALADE nameplate and a monochromatic Cadillac emblem, both of which are also dealer-installed items. Another eye-catching dealer-installed option that will definitely grab everyone’s attention is the set of 22-inch satin graphite multi-spoke forged alloy wheels with laser etching. That’s sure to make people take notice of this Escalade.\nThe interior of this 2024 Cadillac Escalade V is a luxurious three-row affair, and all three rows feature semi-aniline leather seating that’s superbly comfortable. Then, there’s leather-wrapped interior trim, multi-zone climate control, Apple CarPlay, Android Auto, a heads-up display, a panoramic sunroof, and heated plus ventilated seats. There are many more features that bear mentioning, including the slick digital gauge cluster, multifunction steering wheel, AKG premium sound system, and the switches in the trunk for power-folding the third row, should you need more luggage space. There’s even a console refrigerator with a freezer!\n\nEngine\nThis 2024 Cadillac Escalade V is a hulking beast of a full-size luxury SUV.  Under the hood lies a supercharged 6.2L V8 paired with a smooth-shifting 10-speed automatic gearbox. By default, this 2024 Cadillac Escalade V is rear-wheel drive, but you can switch it into four-wheel drive mode when you need more traction.',
        'title': '2024 Cadillac Escalade V',
        'lot_number': '240922939',
        'condition': None,
    },
    {
        'slug': '2020-mercedes-benz-g63-amg-4matic',
        'images': ['/media/vehicles/2020-mercedes-benz-g63-amg-4matic/01.webp', '/media/vehicles/2020-mercedes-benz-g63-amg-4matic/02.webp', '/media/vehicles/2020-mercedes-benz-g63-amg-4matic/03.webp', '/media/vehicles/2020-mercedes-benz-g63-amg-4matic/04.webp', '/media/vehicles/2020-mercedes-benz-g63-amg-4matic/05.webp', '/media/vehicles/2020-mercedes-benz-g63-amg-4matic/06.webp', '/media/vehicles/2020-mercedes-benz-g63-amg-4matic/07.webp', '/media/vehicles/2020-mercedes-benz-g63-amg-4matic/08.webp', '/media/vehicles/2020-mercedes-benz-g63-amg-4matic/09.webp', '/media/vehicles/2020-mercedes-benz-g63-amg-4matic/10.webp', '/media/vehicles/2020-mercedes-benz-g63-amg-4matic/11.webp', '/media/vehicles/2020-mercedes-benz-g63-amg-4matic/12.webp', '/media/vehicles/2020-mercedes-benz-g63-amg-4matic/13.webp', '/media/vehicles/2020-mercedes-benz-g63-amg-4matic/14.webp', '/media/vehicles/2020-mercedes-benz-g63-amg-4matic/15.webp', '/media/vehicles/2020-mercedes-benz-g63-amg-4matic/16.webp', '/media/vehicles/2020-mercedes-benz-g63-amg-4matic/17.webp'],
        'price': 94999,
        'mileage': 20000,
        'transmission': 'Automatic',
        'drivetrain': None,
        'engine': '4.0L V8',
        'exterior_color': 'G Manufaktur Monza Grey Magno',
        'interior_color': 'Designo Classic Red/Black',
        'location': 'Florida',
        'features': ['2020 Model Year Mercedes-benz G-class AMG G63 4MATIC', 'G Manufaktur Monza Grey Magno exterior', 'Designo Classic Red/Black Nappa leather interior', 'AMG front and rear red brake calipers', 'AMG Carbon fiber trim', 'Exclusive interior package', 'AMG Night Package', 'AMG performance steering wheel in Dinamica/Carbon FIber', '22" Forged AMG Cross spoke wheels in black', 'Seller reports aftermarket downpipes and tune', 'PPF and Ceramic coating on entire car reported'],
        'description': 'From this 2020 Mercedes-AMG G63 4MATIC, you get a G Manufaktur Monza\nGrey Magno exterior color. It’s nothing flashy but it sure does go\nwith its aggressive attitude and the gloss-black front bumper guard.\nThe AMG Night Package also helps matters. This imposing exterior is\nset down on 22" forged AMG cross spoke wheels in black and a splash of\ncolor is added thanks to the AMG front and rear red brake calipers.\nThis G-Wagen is reportedly treated to a fine PPF and ceramic coating\non the entire body.\nOpening the doors to this mighty AMG G63 reveals the Designo Classic\nRed/Black Nappa leather interior armed with the AMG Carbon fiber trim\nand Exclusive interior package. it offers a modern experience with the\n12-inch digital display, quality materials and the all-important cup\nholders and surround cameras. Even the steering wheel is an AMG\nperformance steering wheel in Dinamica and carbon fiber.\n\nEngine\nProviding a glut of power and torque from underneath the hood of this\n2020 Mercedes-AMG G63 4MATIC is a twin-turbocharged 4.0L V8\npowertrain. You can unlock 577 horsepower by pressing the gas pedal\nand 627 lb-ft of torque is available to go hand in hand with it. To\nadd to the bargain, its seller also reports that this G-Wagen received\naftermarket downpipes and tune.',
        'title': '2020 Mercedes-Benz G63 AMG 4MATIC',
        'lot_number': '22082855',
        'condition': None,
    },
    {
        'slug': '2026-tesla-model-y-launch-edition',
        'images': ['/media/vehicles/2026-tesla-model-y-launch-edition/01.webp', '/media/vehicles/2026-tesla-model-y-launch-edition/02.webp', '/media/vehicles/2026-tesla-model-y-launch-edition/03.webp', '/media/vehicles/2026-tesla-model-y-launch-edition/04.webp', '/media/vehicles/2026-tesla-model-y-launch-edition/05.webp', '/media/vehicles/2026-tesla-model-y-launch-edition/06.webp', '/media/vehicles/2026-tesla-model-y-launch-edition/07.webp', '/media/vehicles/2026-tesla-model-y-launch-edition/08.webp', '/media/vehicles/2026-tesla-model-y-launch-edition/09.webp', '/media/vehicles/2026-tesla-model-y-launch-edition/10.webp', '/media/vehicles/2026-tesla-model-y-launch-edition/11.webp', '/media/vehicles/2026-tesla-model-y-launch-edition/12.webp', '/media/vehicles/2026-tesla-model-y-launch-edition/13.webp', '/media/vehicles/2026-tesla-model-y-launch-edition/14.webp', '/media/vehicles/2026-tesla-model-y-launch-edition/15.webp', '/media/vehicles/2026-tesla-model-y-launch-edition/16.webp', '/media/vehicles/2026-tesla-model-y-launch-edition/17.webp', '/media/vehicles/2026-tesla-model-y-launch-edition/18.webp', '/media/vehicles/2026-tesla-model-y-launch-edition/19.webp', '/media/vehicles/2026-tesla-model-y-launch-edition/20.webp'],
        'price': None,
        'mileage': 17118,
        'transmission': 'Automatic',
        'drivetrain': 'All-Wheel Drive (AWD)',
        'engine': '75 kWh Lithium-Ion Battery',
        'exterior_color': 'Pearl White',
        'interior_color': 'White/Black',
        'location': 'Maryland',
        'features': ['2026 Tesla Model Y Launch Edition', '75 kWh Lithium-Ion Battery', 'Dual Electric Motors', 'Single-Speed Automatic', 'AWD', 'Pearl White Multi-Coat Exterior', 'White/Black Interior', '19’’ Crossflow Wheels', 'Towing Package'],
        'description': 'Exterior and Interior\nThis 2026 Tesla Model Y Launch Edition wears a Pearl White coat of paint and rolls on a set of 19-inch aerodynamically designed alloy wheels. These are shod in Continental ProContact tires for optimal grip and performance, given that performance is a key attribute of Tesla’s vehicles. In fact, the overall design of the Model Y, like other Teslas, screams effortless performance. The aerodynamic design, futuristic lines and overall space-age presence mean that you can never mistake a Tesla for anything else – be it American, European or Far Eastern.\nThe sleek black interior features white seats and can accommodate five adults with ease. It may look highly minimalistic at first glance but looks are indeed deceiving. There’s so much tech on board, backed by a ton of processing power. In fact, you can engage in console-level gaming via the car’s systems, such is the computing prowess available. OF course, you’ve got the usual dual-zone automatic climate control, power front seats, smartphone connectivity and the essentials of modern automotive amenities at your fingertips. Rear-seat passengers get their own touchscreen for adjusting settings too. And for cargo, there are two spaces! Yes, the regular trunk out back is there, plus a front trunk, or frunk for even more capacity.\n\nEngine\nThis 2026 Tesla Model Y Launch Edition comes with dual electric motors. Hence, it’s all-wheel drive. With a reported total of 384hp and 376lb-ft available, 0-60 takes just under 5 seconds on average. An 81 kilowatt-hour battery pack ensures ample range, and of course, Tesla’s famed Supercharger network is available for you to use.',
        'title': '2026 Tesla Model Y Launch Edition',
        'lot_number': '260251552',
        'condition': 'Used',
    },
    {
        'slug': '2025-tesla-model-y-performance',
        'images': ['/media/vehicles/2025-tesla-model-y-performance/01.webp', '/media/vehicles/2025-tesla-model-y-performance/02.webp', '/media/vehicles/2025-tesla-model-y-performance/03.webp', '/media/vehicles/2025-tesla-model-y-performance/04.webp', '/media/vehicles/2025-tesla-model-y-performance/05.webp', '/media/vehicles/2025-tesla-model-y-performance/06.webp', '/media/vehicles/2025-tesla-model-y-performance/07.webp', '/media/vehicles/2025-tesla-model-y-performance/08.webp', '/media/vehicles/2025-tesla-model-y-performance/09.webp', '/media/vehicles/2025-tesla-model-y-performance/10.webp', '/media/vehicles/2025-tesla-model-y-performance/11.webp', '/media/vehicles/2025-tesla-model-y-performance/12.webp', '/media/vehicles/2025-tesla-model-y-performance/13.webp', '/media/vehicles/2025-tesla-model-y-performance/14.webp'],
        'price': None,
        'mileage': 7200,
        'transmission': 'Automatic',
        'drivetrain': 'All-Wheel Drive (AWD)',
        'engine': 'Dual Electric Motors',
        'exterior_color': 'Deep Blue Metallic',
        'interior_color': 'Black',
        'location': 'North Carolina',
        'features': ['2025 Tesla Model Y Performance', 'Dual Electric Motors', 'Single-Speed Automatic', 'AWD', 'Deep Blue Metallic Exterior', 'Black Interior', 'Performance Upgrade', '21" Uberturbine Wheels', 'All Black Premium Interior', 'Five Seat Interior Layout', 'Autopilot'],
        'description': 'Exterior and Interior\nThe Model Y is a compact-class crossover SUV, and is heavily based on the Model 3 compact car. This particular 2025 Tesla Model Y Performance wears a Deep Blue Metallic paint job, and rides on a suitably alluring set of 21-inch Uberturbine wheels. Red brake calipers lie behind each wheel, peeking out behind the spokes. Then, the vehicle’s exterior LED lighting shines bright when called upon, while its sleek, coupe-like stance gives it a real performance-car vibe. The interior of this 2025 Tesla Model Y Performance is minimalistic in form, comprehensive in function. You’ve got Apple CarPlay and Android Auto, as well as a super-powerful infotainment system that can easily run a myriad of video games. Then, there’s powered and heated seats, climate control with air conditioning, a decent speaker system, and even Tesla’s famed Autopilot autonomous driving system. Now we must tell you that this is to be used responsibly; don’t engage it and climb into the passenger or rear seats. Instead, consider it an advanced form of cruise control, meant to relax you as much as possible on long drives – but you must remain at the wheel, and alert at all times. As for trunk space, you’ve got the usual rear trunk behind the rear seats, plus a front storage compartment, called a Frunk. When the rear seat backs are dropped and both compartments are combined, you’ll have over 75 cubic feet of total cargo capacity.\n\nEngine\nPowering this 2025 Tesla Model Y Performance is a duo of electric motors that drive all four wheels and make up to a reported 456hp and 497lb-ft of torque. The vehicle’s long-range battery can be charged at a regular home charger, or a fast charging facility such as Tesla’s Supercharger network."',
        'title': '2025 Tesla Model Y Performance',
        'lot_number': '250129375',
        'condition': 'Used',
    },
    {
        'slug': '2024-tesla-cybertruck-cyberbeast-foundation',
        'images': ['/media/vehicles/2024-tesla-cybertruck-cyberbeast-foundation/01.webp', '/media/vehicles/2024-tesla-cybertruck-cyberbeast-foundation/02.webp', '/media/vehicles/2024-tesla-cybertruck-cyberbeast-foundation/03.webp', '/media/vehicles/2024-tesla-cybertruck-cyberbeast-foundation/04.webp', '/media/vehicles/2024-tesla-cybertruck-cyberbeast-foundation/05.webp', '/media/vehicles/2024-tesla-cybertruck-cyberbeast-foundation/06.webp', '/media/vehicles/2024-tesla-cybertruck-cyberbeast-foundation/07.webp', '/media/vehicles/2024-tesla-cybertruck-cyberbeast-foundation/08.webp', '/media/vehicles/2024-tesla-cybertruck-cyberbeast-foundation/09.webp', '/media/vehicles/2024-tesla-cybertruck-cyberbeast-foundation/10.webp', '/media/vehicles/2024-tesla-cybertruck-cyberbeast-foundation/11.webp', '/media/vehicles/2024-tesla-cybertruck-cyberbeast-foundation/12.webp', '/media/vehicles/2024-tesla-cybertruck-cyberbeast-foundation/13.webp', '/media/vehicles/2024-tesla-cybertruck-cyberbeast-foundation/14.webp', '/media/vehicles/2024-tesla-cybertruck-cyberbeast-foundation/15.webp', '/media/vehicles/2024-tesla-cybertruck-cyberbeast-foundation/16.webp', '/media/vehicles/2024-tesla-cybertruck-cyberbeast-foundation/17.webp', '/media/vehicles/2024-tesla-cybertruck-cyberbeast-foundation/18.webp', '/media/vehicles/2024-tesla-cybertruck-cyberbeast-foundation/19.webp', '/media/vehicles/2024-tesla-cybertruck-cyberbeast-foundation/20.webp'],
        'price': None,
        'mileage': 600,
        'transmission': 'Automatic',
        'drivetrain': None,
        'engine': 'EV',
        'exterior_color': 'Silver',
        'interior_color': 'Black/White',
        'location': 'Florida',
        'features': [],
        'description': 'Exterior and Interior\nThe 2024 Tesla Cybertruck Cyberbeast Foundation Series is nothing like\nany other pickup truck, even the most modern electric ones from other\nbrands. The ultra-hard stainless steel exoskeleton of the Cybertruck\nis unpainted and finished in a Silver/Steel finish. The windshield and\nwindows of the truck comprise armored shatter-resistant glass,\nensuring superior protection and enhanced noise isolation. Adding to\nthe rugged appeal of the Cyberbeast is a set of 20-inch Cyber wheels\nencircled by 35-inch Goodyear Wrangler Territory RT tires. At the rear\nend, there is a 6x4 feet lockable cargo bed, whereas there is a frunk\nupfront offering extra storage space. However, it is to be noted that\nthe standard light bar and rear tow hooks of this particular truck\nhave not arrived yet. On the inside, there is ample space for five\noccupants and the cabin is specced in a simple and minimalistic Black\nand White color combo. Technology is abundant inside this 2024 Tesla\nCybertruck Cyberbeast Foundation Series. There is a massive,\ndashboard-mounted 8.5-inch central touchscreen display, a 9.4-inch\ntouchscreen at the rear, and a 15-speaker audio system.\n\nEngine\nPropelling the 2024 Tesla Cybertruck Cyberbeast Foundation Series is a\ntri-motor electric powertrain, comprising one 276 hp motor on the\nfront axle and two 284 hp rear-axle-mounted motors. Powering these\nmotors is a 123 kWh liquid-cooled lithium-ion battery pack, capable of\na peak charging rate of 250 kW. The combined output generated by this\nsetup is a whopping 845 horsepower and 740 lb-ft, sent to all four\nwheels via a direct-drive transmission. The 6,843 lbs Cyberbeast can\ngallop to 60 mph in just 2.6 seconds and is rated to tow up to 11,000\nlbs. Tesla promises an estimated range of 320 miles and has included\nan 11.5 kW charger onboard. Furthermore, being the Foundation Series\nedition, the truck is also equipped with Tesla’s Powershare home\nbackup hardware and full self-driving capability. Overall, this\noutlandish badass electric pickup truck is supersonic on the road and\nimpressively competent off it. It is also exceptionally tech-loaded,\nwith plenty of space for people and luggage.',
        'title': '2024 Tesla Cybertruck Cyberbeast Foundation',
        'lot_number': '240517552',
        'condition': 'Used',
    },
    {
        'slug': '2024-tesla-cybertruck-foundation-series',
        'images': ['/media/vehicles/2024-tesla-cybertruck-foundation-series/01.webp', '/media/vehicles/2024-tesla-cybertruck-foundation-series/02.webp', '/media/vehicles/2024-tesla-cybertruck-foundation-series/03.webp', '/media/vehicles/2024-tesla-cybertruck-foundation-series/04.webp', '/media/vehicles/2024-tesla-cybertruck-foundation-series/05.webp', '/media/vehicles/2024-tesla-cybertruck-foundation-series/06.webp', '/media/vehicles/2024-tesla-cybertruck-foundation-series/07.webp', '/media/vehicles/2024-tesla-cybertruck-foundation-series/08.webp', '/media/vehicles/2024-tesla-cybertruck-foundation-series/09.webp', '/media/vehicles/2024-tesla-cybertruck-foundation-series/10.webp', '/media/vehicles/2024-tesla-cybertruck-foundation-series/11.webp', '/media/vehicles/2024-tesla-cybertruck-foundation-series/12.webp', '/media/vehicles/2024-tesla-cybertruck-foundation-series/13.webp', '/media/vehicles/2024-tesla-cybertruck-foundation-series/14.webp', '/media/vehicles/2024-tesla-cybertruck-foundation-series/15.webp'],
        'price': None,
        'mileage': 461,
        'transmission': 'Automatic',
        'drivetrain': 'Front-Wheel Drive (FWD)',
        'engine': 'Dual Motor',
        'exterior_color': 'Stainless Silver',
        'interior_color': 'Black',
        'location': 'California',
        'features': ['Dual Motor', 'AWD', 'Foundation Series', 'Full Self Drive', 'Wrapped Army Green', 'Stainless Steel Exterior', 'Black Leather Interior', '2,500 lbs Payload Capacity', '11,000 lbs Towing Capacity', 'Laser-Etched Foundation Series Badges And Cabin Graphics', '3D All-Weather Interior Liners', 'Original Mileage', '1 Owner'],
        'description': 'Exterior and Interior\nThe Cybertruck is renowned for its 300-series shiny silver stainless steel body panels, much like another car from a few decades back, the iconic DeLorean. While stainless steel is a notoriously difficult color to paint, you’ve now got the option of wraps. That’s what this 2024 Tesla Cybertruck Foundation Series wears: an Army Green wrap, giving it a distinctive appearance from the majority of others on the road. But if Army Green isn’t your thing, you can wrap it in another color of choice or remove the wrap and showcase the truck’s stainless steel bodywork. Either way, its futuristic, angular design and distinctive wheel caps make for a stunning machine.\nThe interior of this 2024 Tesla Cybertruck Foundation Series features a simplistic dashboard dominated by a single screen. However, don’t be fooled into thinking that simple means spartan. Nope, the truck has all the tech features you’d expect from a Tesla. It’s just controlled from this screen. Take a closer look, and you’ll see items such as power-adjustable and heated front seats, dual-zone automatic climate control, a full infotainment system, and more. Plus, you’ve got some cool 3D all-weather liners, plus special laser-etched Foundation Series badges and cabin graphics. As for cargo capacity, there’s a fully enclosed truck bed plus a front trunk. With a 2,500lb payload capacity, you’ve got something akin to a full-size pickup truck right here, replete with a motorized roller tonneau for safety and security. Furthermore, the towing capacity is an impressive 11,000lbs.\n\nEngine\nThis 2024 Tesla Cybertruck Foundation Series comes with, as you’d expect, electric propulsion. With a dual-motor configuration, you’ll enjoy 600hp and 743lb-ft at your disposal. Furthermore, the truck comes with full Tesla Self-Drive capabilities.',
        'title': '2024 Tesla Cybertruck Foundation Series',
        'lot_number': '241024920',
        'condition': 'Used',
    },
]

def vehicles_table():
    return sa.table(
        "vehicles",
        sa.column("slug", sa.String), sa.column("title", sa.String),
        sa.column("price", sa.Integer), sa.column("mileage", sa.Integer),
        sa.column("transmission", sa.String), sa.column("drivetrain", sa.String),
        sa.column("engine", sa.String), sa.column("exterior_color", sa.String),
        sa.column("interior_color", sa.String), sa.column("location", sa.String),
        sa.column("short_description", sa.String), sa.column("description", sa.Text),
        sa.column("images", sa.JSON), sa.column("features", sa.JSON),
        sa.column("specs", sa.JSON), sa.column("details", sa.JSON),
    )


def _previous_vehicles(filename):
    path = Path(__file__).with_name(filename)
    spec = importlib.util.spec_from_file_location(f"prior_{path.stem}", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {filename} for downgrade")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.VEHICLES


def _apply_values(connection, table, slug, values):
    connection.execute(table.update().where(table.c.slug == slug).values(**values))


def upgrade():
    connection = op.get_bind()
    table = vehicles_table()
    for item in VEHICLES:
        description = item["description"].removeprefix("Exterior and Interior\n").strip()
        first = description.split("\n", 1)[0].strip()
        if first == "Engine":
            first = description.split("\n", 2)[1].strip()
        first = first[:252].rsplit(" ", 1)[0] + "..." if len(first) > 255 else first
        current = connection.execute(
            sa.select(table.c.specs, table.c.details).where(table.c.slug == item["slug"])
        ).mappings().first()
        current_specs = dict(current["specs"] or {}) if current else {}
        current_details = dict(current["details"] or {}) if current else {}
        preserved_info = [
            detail for detail in current_details.get("info", [])
            if str(detail.get("label", "")).strip().lower() in {"listing", "vehicle history"}
        ]
        imported_info = [
            {"label": label, "value": value}
            for label, value in (("Lot Number", item["lot_number"]), ("Condition", item["condition"]))
            if value is not None
        ]
        current_specs.update({
            key: value for key, value in (("lot_number", item["lot_number"]), ("condition", item["condition"]))
            if value is not None
        })
        current_details["info"] = preserved_info + imported_info
        current_details["raw_description"] = description
        values = {
            "title": item["title"],
            "images": item["images"],
            "features": item["features"],
            "description": description,
            "short_description": first,
            "specs": current_specs,
            "details": current_details,
        }
        for field in ("price", "mileage", "transmission", "drivetrain", "engine", "exterior_color", "interior_color", "location"):
            if item[field] is not None:
                values[field] = item[field]
        _apply_values(connection, table, item["slug"], values)


def downgrade():
    connection = op.get_bind()
    table = vehicles_table()
    previous = []
    previous.extend(_previous_vehicles("20261008_0015_inventory_from_exotic_car_trader.py"))
    previous.extend(_previous_vehicles("20261009_0016_add_tesla_inventory_without_prices.py"))
    for item in previous:
        _apply_values(connection, table, item["slug"], {
            field: item[field] for field in table.c.keys() if field in item and field != "slug"
        })
