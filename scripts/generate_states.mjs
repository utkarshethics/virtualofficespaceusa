import { readFileSync, writeFileSync, mkdirSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = join(dirname(fileURLToPath(import.meta.url)), '..');
const baseHtml = readFileSync(join(root, 'index.html'), 'utf8');

const STATES = [
  {
    slug: 'wyoming',
    name: 'Wyoming',
    city: 'Sheridan / Cheyenne',
    taxRate: '0% Corporate & Personal State Tax',
    privacy: 'Maximum Anonymous LLC Ownership',
    bestFor: 'E-commerce, Asset Protection & Privacy-Focused Founders',
    tag: 'Top Choice for Non-US Residents',
    heroH1: 'Wyoming Virtual Office & Registered Agent',
    heroSub: 'Get a verified commercial street address in Sheridan or Cheyenne, Wyoming. 0% state tax, full member privacy protection, and bank-ready verification for Mercury & Stripe.',
    keywords: 'wyoming virtual office, wyoming registered agent, wyoming commercial address, wyoming llc address mercury bank'
  },
  {
    slug: 'delaware',
    name: 'Delaware',
    city: 'Wilmington / Dover',
    taxRate: 'Chancery Court Prestige & Pro-Business Law',
    privacy: 'Global Investor & VC Standard',
    bestFor: 'VC-Backed Tech Startups & Raising Venture Capital',
    tag: 'Preferred by 68% of Fortune 500',
    heroH1: 'Delaware Virtual Office & Registered Agent',
    heroSub: 'Establish your Delaware commercial business address in Wilmington or Dover. Perfect for C-Corps, investor due diligence, and official registered agent representation.',
    keywords: 'delaware virtual office, delaware registered agent, delaware commercial street address, delaware c corp address stripe'
  },
  {
    slug: 'florida',
    name: 'Florida',
    city: 'Miami / Orlando',
    taxRate: '0% State Personal Income Tax',
    privacy: 'Strong Asset Shield & Pro-Growth',
    bestFor: 'Global Trade, Real Estate & Latin America Commercial Gateway',
    tag: 'Fastest Growing US Business Hub',
    heroH1: 'Florida Virtual Office & Registered Agent',
    heroSub: 'Secure an iconic commercial street address in Miami or Orlando, Florida. Zero personal income tax, instant mail scanning, and compliant CMRA verification.',
    keywords: 'florida virtual office, miami virtual address, florida registered agent, orlando business address'
  },
  {
    slug: 'texas',
    name: 'Texas',
    city: 'Austin / Dallas',
    taxRate: '0% Individual State Income Tax',
    privacy: 'Pro-Business Legal Infrastructure',
    bestFor: 'Tech Companies, High-Scale Operations & Manufacturing',
    tag: 'Booming Enterprise Tech Destination',
    heroH1: 'Texas Virtual Office & Registered Agent',
    heroSub: 'Get an official commercial street address in Austin or Dallas, Texas. High-growth business corridor, bank-compliant mail forwarding, and registered agent coverage.',
    keywords: 'texas virtual office, austin commercial address, dallas registered agent, texas llc business address'
  },
  {
    slug: 'california',
    name: 'California',
    city: 'San Francisco / Silicon Valley',
    taxRate: 'Silicon Valley Venture Benchmark',
    privacy: 'Global Tech & AI Authority',
    bestFor: 'AI Startups, SaaS Companies & Global Media Brands',
    tag: 'Global Innovation & Capital Center',
    heroH1: 'California Virtual Office & Registered Agent',
    heroSub: 'Position your company with a prestigious Silicon Valley or San Francisco commercial address. Instant digital mail scanning, bank verification, and registered agent service.',
    keywords: 'california virtual office, silicon valley business address, san francisco registered agent, california llc address'
  },
  {
    slug: 'new-york',
    name: 'New York',
    city: 'Manhattan, NYC',
    taxRate: 'Iconic Wall Street Presence & Global Credibility',
    privacy: 'Tier-1 International Authority',
    bestFor: 'Finance, Consulting, Fashion & Media Brands',
    tag: 'World Financial & Business Capital',
    heroH1: 'New York Virtual Office & Registered Agent',
    heroSub: 'Command global respect with an authentic Manhattan, New York commercial street address. Bank-ready verification, daily mail scans, and professional registered agent support.',
    keywords: 'new york virtual office, nyc commercial address, manhattan virtual business address, new york registered agent'
  },
  {
  "slug": "nevada",
  "name": "Nevada",
  "city": "Las Vegas / Reno",
  "taxRate": "0% Corporate & Personal Income Tax",
  "privacy": "Strong Corporate Veil & Privacy",
  "bestFor": "Entertainment, Gaming, Asset Protection",
  "tag": "Tax-Free Western Corridor",
  "heroH1": "Nevada Virtual Office & Registered Agent",
  "heroSub": "Real commercial street address in Las Vegas or Reno, Nevada. Zero state personal and corporate income tax, bank-compliant CMRA verification, and official registered agent.",
  "keywords": "nevada virtual office, las vegas virtual address, nevada registered agent, reno business address"
},
  {
  "slug": "washington",
  "name": "Washington",
  "city": "Seattle / Bellevue",
  "taxRate": "0% Personal State Income Tax",
  "privacy": "Pacific Northwest Tech Hub",
  "bestFor": "Cloud, SaaS, AI & Global E-Commerce",
  "tag": "Tech Titan Gateway (Amazon/Microsoft)",
  "heroH1": "Washington Virtual Office & Registered Agent",
  "heroSub": "Establish your corporate presence in Seattle or Bellevue, Washington. Zero personal income tax, same-day mail scans, and bank-compliant registered agent services.",
  "keywords": "washington virtual office, seattle commercial address, bellevue registered agent, washington llc address"
},
  {
  "slug": "illinois",
  "name": "Illinois",
  "city": "Chicago",
  "taxRate": "Midwest Financial Capital",
  "privacy": "Commercial Banking Anchor",
  "bestFor": "Fintech, Trading, Logistics & B2B SaaS",
  "tag": "Midwest Commercial Center",
  "heroH1": "Illinois Virtual Office & Registered Agent",
  "heroSub": "Command executive prestige with a commercial street address in Chicago, Illinois. Bank-compliant CMRA verification, registered agent coverage, and instant mail forwarding.",
  "keywords": "illinois virtual office, chicago virtual address, illinois registered agent, chicago commercial address"
},
  {
  "slug": "georgia",
  "name": "Georgia",
  "city": "Atlanta",
  "taxRate": "Southeast Fintech Hub",
  "privacy": "Pro-Business Transaction Corridor",
  "bestFor": "Fintech, Payments, Logistics & Media",
  "tag": "Top Tier Southeast Hub",
  "heroH1": "Georgia Virtual Office & Registered Agent",
  "heroSub": "Official commercial street address in Atlanta, Georgia. Premier fintech hub, Mercury and Stripe bank-approved, with complete registered agent representation.",
  "keywords": "georgia virtual office, atlanta virtual address, georgia registered agent, atlanta business address"
},
  {
  "slug": "massachusetts",
  "name": "Massachusetts",
  "city": "Boston / Cambridge",
  "taxRate": "Global Biotech & Academic Capital",
  "privacy": "Premier Institutional Trust",
  "bestFor": "Biotech, DeepTech, AI & Robotics",
  "tag": "World Biotech & MIT/Harvard Hub",
  "heroH1": "Massachusetts Virtual Office & Registered Agent",
  "heroSub": "Prestigious commercial business address in Boston or Cambridge, Massachusetts. Perfect for institutional due diligence, federal grant compliance, and registered agent support.",
  "keywords": "massachusetts virtual office, boston commercial address, cambridge registered agent, massachusetts business address"
},
  {
  "slug": "north-carolina",
  "name": "North Carolina",
  "city": "Raleigh / Charlotte",
  "taxRate": "2.5% Lowest Corporate Income Tax",
  "privacy": "Research Triangle Moat",
  "bestFor": "Banking, Life Sciences & Enterprise Tech",
  "tag": "Fastest-Growing East Coast Hub",
  "heroH1": "North Carolina Virtual Office & Registered Agent",
  "heroSub": "Get a verified commercial address in Charlotte or Raleigh, North Carolina. Sub-3% corporate tax rate, Research Triangle innovation ecosystem, and bank-ready verification.",
  "keywords": "north carolina virtual office, raleigh commercial address, charlotte registered agent, nc business address"
},
  {
  "slug": "colorado",
  "name": "Colorado",
  "city": "Denver / Boulder",
  "taxRate": "4.4% Flat Corporate Income Tax",
  "privacy": "Mountain Tech Hub",
  "bestFor": "Aerospace, CleanTech, Web3 & Outdoor Brands",
  "tag": "Mountain Region Capital",
  "heroH1": "Colorado Virtual Office & Registered Agent",
  "heroSub": "Real commercial street address in Denver or Boulder, Colorado. Highly rated registered agent coverage, same-day envelope scanning, and compliant LLC verification.",
  "keywords": "colorado virtual office, denver business address, boulder registered agent, colorado commercial address"
},
  {
  "slug": "arizona",
  "name": "Arizona",
  "city": "Phoenix / Scottsdale",
  "taxRate": "2.5% Flat Corporate Income Tax",
  "privacy": "Desert Silicon Corridor",
  "bestFor": "Semiconductors, Healthcare, Real Estate & SaaS",
  "tag": "Sunbelt Innovation Hub",
  "heroH1": "Arizona Virtual Office & Registered Agent",
  "heroSub": "Secure a commercial street address in Phoenix or Scottsdale, Arizona. Low 2.5% flat tax, fast KYC turnaround, bank verification, and registered agent representation.",
  "keywords": "arizona virtual office, phoenix virtual address, scottsdale registered agent, arizona business address"
},
  {
  "slug": "ohio",
  "name": "Ohio",
  "city": "Columbus / Cleveland",
  "taxRate": "Commercial Activity Tax (CAT) Only",
  "privacy": "Midwest Industrial & Healthcare",
  "bestFor": "Manufacturing, HealthTech, Retail & B2B",
  "tag": "Heartland Commerce Corridor",
  "heroH1": "Ohio Virtual Office & Registered Agent",
  "heroSub": "Official commercial address in Columbus or Cleveland, Ohio. No traditional corporate income tax, bank-compliant CMRA verification, and registered agent services.",
  "keywords": "ohio virtual office, columbus business address, cleveland registered agent, ohio commercial address"
},
  {
  "slug": "pennsylvania",
  "name": "Pennsylvania",
  "city": "Philadelphia / Pittsburgh",
  "taxRate": "Mid-Atlantic Innovation Corridor",
  "privacy": "Historic Commercial Capital",
  "bestFor": "Healthcare, Robotics, EdTech & Commerce",
  "tag": "Historic Business Foundation",
  "heroH1": "Pennsylvania Virtual Office & Registered Agent",
  "heroSub": "Command trust with a commercial street address in Philadelphia or Pittsburgh, Pennsylvania. Bank verification for Mercury/Relay, same-day mail scans, and registered agent.",
  "keywords": "pennsylvania virtual office, philadelphia virtual address, pittsburgh registered agent, pa commercial address"
},
  {
  "slug": "michigan",
  "name": "Michigan",
  "city": "Detroit / Ann Arbor",
  "taxRate": "6% Flat Corporate Tax",
  "privacy": "Mobility & Automotive Tech",
  "bestFor": "Mobility, Robotics, Manufacturing & AI",
  "tag": "Great Lakes Innovation Hub",
  "heroH1": "Michigan Virtual Office & Registered Agent",
  "heroSub": "Real commercial street address in Detroit or Ann Arbor, Michigan. Registered agent support, digital mail forwarding, and compliant business presence.",
  "keywords": "michigan virtual office, detroit business address, ann arbor registered agent, michigan commercial address"
},
  {
  "slug": "virginia",
  "name": "Virginia",
  "city": "Tysons / Richmond",
  "taxRate": "6% Corporate Income Tax",
  "privacy": "Defense & Federal Cloud Hub",
  "bestFor": "GovTech, Cybersecurity, Cloud Infrastructure",
  "tag": "Federal Tech & Cloud Capital",
  "heroH1": "Virginia Virtual Office & Registered Agent",
  "heroSub": "Establish your commercial address in Northern Virginia / Tysons or Richmond. Strategic proximity to federal agencies, registered agent coverage, and instant mail forwarding.",
  "keywords": "virginia virtual office, tysons business address, richmond registered agent, virginia commercial address"
},
  {
  "slug": "new-jersey",
  "name": "New Jersey",
  "city": "Jersey City / Newark",
  "taxRate": "Metro NYC Commercial Gateway",
  "privacy": "Pharma & Financial Infrastructure",
  "bestFor": "Pharma, Life Sciences, Logistics & Finance",
  "tag": "New York Metro Gateway",
  "heroH1": "New Jersey Virtual Office & Registered Agent",
  "heroSub": "Commercial street address in Jersey City or Newark, New Jersey. Proximity to Manhattan, bank verification, digital mail scans, and compliant registered agent support.",
  "keywords": "new jersey virtual office, jersey city commercial address, newark registered agent, nj business address"
},
  {
  "slug": "utah",
  "name": "Utah",
  "city": "Salt Lake City / Provo",
  "taxRate": "4.85% Flat Corporate Income Tax",
  "privacy": "Silicon Slopes SaaS Center",
  "bestFor": "Enterprise SaaS, Cloud, Fintech & Hardware",
  "tag": "Silicon Slopes Hub",
  "heroH1": "Utah Virtual Office & Registered Agent",
  "heroSub": "Prime commercial address in Salt Lake City or Provo (Silicon Slopes), Utah. Fast-growing tech ecosystem, bank verification, and registered agent coverage.",
  "keywords": "utah virtual office, salt lake city virtual address, provo registered agent, silicon slopes business address"
},
  {
  "slug": "oregon",
  "name": "Oregon",
  "city": "Portland",
  "taxRate": "0% General Sales Tax",
  "privacy": "Silicon Forest Corridor",
  "bestFor": "Apparel, Clean Energy, Semiconductor & Design",
  "tag": "Pacific Northwest Creative Hub",
  "heroH1": "Oregon Virtual Office & Registered Agent",
  "heroSub": "Establish your commercial street address in Portland, Oregon. Zero sales tax, compliant registered agent services, and digital mail scans.",
  "keywords": "oregon virtual office, portland business address, oregon registered agent, portland commercial address"
},
  {
  "slug": "tennessee",
  "name": "Tennessee",
  "city": "Nashville / Memphis",
  "taxRate": "0% Personal State Income Tax",
  "privacy": "Healthcare & Music Industry Capital",
  "bestFor": "Healthcare, Music, Logistics & E-Commerce",
  "tag": "No State Income Tax Hub",
  "heroH1": "Tennessee Virtual Office & Registered Agent",
  "heroSub": "Real commercial address in Nashville or Memphis, Tennessee. Zero personal income tax, compliant registered agent coverage, and same-day mail forwarding.",
  "keywords": "tennessee virtual office, nashville commercial address, memphis registered agent, tennessee business address"
},
  {
  "slug": "maryland",
  "name": "Maryland",
  "city": "Bethesda / Baltimore",
  "taxRate": "Federal Health & Cyber Corridor",
  "privacy": "Life Sciences & Biotech",
  "bestFor": "BioHealth, Federal Contracting & Research",
  "tag": "Capital Health Corridor",
  "heroH1": "Maryland Virtual Office & Registered Agent",
  "heroSub": "Commercial street address in Bethesda or Baltimore, Maryland. Close to NIH and federal institutes, compliant registered agent, and instant mail forwarding.",
  "keywords": "maryland virtual office, bethesda business address, baltimore registered agent, maryland commercial address"
},
  {
  "slug": "indiana",
  "name": "Indiana",
  "city": "Indianapolis",
  "taxRate": "4.9% Flat Corporate Tax",
  "privacy": "Crossroads Logistics Capital",
  "bestFor": "Logistics, Agriculture Tech & Manufacturing",
  "tag": "Crossroads of America",
  "heroH1": "Indiana Virtual Office & Registered Agent",
  "heroSub": "Verified commercial address in Indianapolis, Indiana. Central logistics hub, bank-compliant CMRA verification, and official registered agent representation.",
  "keywords": "indiana virtual office, indianapolis business address, indiana registered agent, indy commercial address"
},
  {
  "slug": "missouri",
  "name": "Missouri",
  "city": "St. Louis / Kansas City",
  "taxRate": "4.0% Low Corporate Income Tax",
  "privacy": "Bio-Ag & Financial Services",
  "bestFor": "AgTech, BioSciences & Financial Tech",
  "tag": "Central Midwest Gateway",
  "heroH1": "Missouri Virtual Office & Registered Agent",
  "heroSub": "Get a verified commercial street address in St. Louis or Kansas City, Missouri. Low 4.0% corporate tax, bank verification, and registered agent services.",
  "keywords": "missouri virtual office, st louis business address, kansas city registered agent, missouri commercial address"
},
  {
  "slug": "wisconsin",
  "name": "Wisconsin",
  "city": "Milwaukee / Madison",
  "taxRate": "Great Lakes Water & BioTech",
  "privacy": "Manufacturing & Academic Tech",
  "bestFor": "WaterTech, BioTech, Dairy Tech & Manufacturing",
  "tag": "Great Lakes Corridor",
  "heroH1": "Wisconsin Virtual Office & Registered Agent",
  "heroSub": "Commercial address in Milwaukee or Madison, Wisconsin. Bank verification, digital mail scans, and reliable registered agent coverage.",
  "keywords": "wisconsin virtual office, milwaukee commercial address, madison registered agent, wisconsin business address"
},
  {
  "slug": "connecticut",
  "name": "Connecticut",
  "city": "Stamford / Hartford",
  "taxRate": "Insurance & Hedge Fund Capital",
  "privacy": "Institutional Private Equity",
  "bestFor": "Hedge Funds, Insurance & Private Wealth",
  "tag": "Tri-State Financial Haven",
  "heroH1": "Connecticut Virtual Office & Registered Agent",
  "heroSub": "Commercial street address in Stamford or Hartford, Connecticut. Elite financial center, bank verification for Stripe/Mercury, and registered agent services.",
  "keywords": "connecticut virtual office, stamford commercial address, hartford registered agent, ct business address"
},
  {
  "slug": "minnesota",
  "name": "Minnesota",
  "city": "Minneapolis / St. Paul",
  "taxRate": "Twin Cities Fortune 500 Density",
  "privacy": "MedTech & HealthTech Capital",
  "bestFor": "Medical Devices, Retail & Enterprise SaaS",
  "tag": "Twin Cities Commercial Hub",
  "heroH1": "Minnesota Virtual Office & Registered Agent",
  "heroSub": "Secure a commercial address in Minneapolis or St. Paul, Minnesota. MedTech capital presence, registered agent coverage, and same-day mail scans.",
  "keywords": "minnesota virtual office, minneapolis business address, st paul registered agent, mn commercial address"
},
  {
  "slug": "south-carolina",
  "name": "South Carolina",
  "city": "Charleston / Greenville",
  "taxRate": "5% Corporate Income Tax",
  "privacy": "Port Commerce & Advanced Auto",
  "bestFor": "Advanced Manufacturing, Aerospace & Port Logistics",
  "tag": "East Coast Deepwater Port Hub",
  "heroH1": "South Carolina Virtual Office & Registered Agent",
  "heroSub": "Commercial business address in Charleston or Greenville, South Carolina. Boom corridor, registered agent representation, and bank verification.",
  "keywords": "south carolina virtual office, charleston commercial address, greenville registered agent, sc business address"
},
  {
  "slug": "alabama",
  "name": "Alabama",
  "city": "Huntsville / Birmingham",
  "taxRate": "Aerospace & Defense Rocket City",
  "privacy": "Defense & BioTech Infrastructure",
  "bestFor": "Aerospace, Defense, BioTech & Engineering",
  "tag": "Rocket City Tech Capital",
  "heroH1": "Alabama Virtual Office & Registered Agent",
  "heroSub": "Commercial address in Huntsville or Birmingham, Alabama. Defense and aerospace hub, registered agent coverage, and instant mail scanning.",
  "keywords": "alabama virtual office, huntsville business address, birmingham registered agent, alabama commercial address"
},
  {
  "slug": "louisiana",
  "name": "Louisiana",
  "city": "New Orleans / Baton Rouge",
  "taxRate": "Gulf Coast Maritime Gateway",
  "privacy": "Energy, Chemicals & Culture",
  "bestFor": "Logistics, Maritime Trade & Energy Tech",
  "tag": "Gulf Coast Port Corridor",
  "heroH1": "Louisiana Virtual Office & Registered Agent",
  "heroSub": "Commercial street address in New Orleans or Baton Rouge, Louisiana. Bank-ready CMRA verification, registered agent, and digital mail forwarding.",
  "keywords": "louisiana virtual office, new orleans commercial address, baton rouge registered agent, la business address"
}
];

const TODAY = new Date().toISOString().slice(0, 10);

console.log('Generating state landing pages for virtualofficespaceusa.online...');

const sitemapUrls = [
  { loc: 'https://virtualofficespaceusa.online/', priority: '1.0' }
];

for (const state of STATES) {
  const dir = join(root, state.slug);
  mkdirSync(dir, { recursive: true });

  let html = baseHtml;

  // 1. Replace title & descriptions
  html = html.replace(
    /<title>.*?<\/title>/s,
    `<title>${state.name} Virtual Office &amp; Registered Agent | Virtual Office Space USA</title>`
  );
  html = html.replace(
    /<meta name="description" content=".*?" \/>/s,
    `<meta name="description" content="Real US commercial street address in ${state.city}, ${state.name}. CMRA compliant, same-day mail scanning, registered agent &amp; bank-ready proof. From $19/mo." />`
  );

  // 2. Canonical & Alternates
  const stateUrl = `https://virtualofficespaceusa.online/${state.slug}/`;
  html = html.replace(
    /<link rel="canonical" href=".*?" \/>/s,
    `<link rel="canonical" href="${stateUrl}" />`
  );
  html = html.replace(
    /<link rel="alternate" hreflang="en-us" href=".*?" \/>/s,
    `<link rel="alternate" hreflang="en-us" href="${stateUrl}" />`
  );

  // 3. OpenGraph & Twitter
  html = html.replace(
    /<meta property="og:title" content=".*?" \/>/s,
    `<meta property="og:title" content="${state.name} Virtual Office &amp; Registered Agent — from $19/mo" />`
  );
  html = html.replace(
    /<meta property="og:url" content=".*?" \/>/s,
    `<meta property="og:url" content="${stateUrl}" />`
  );
  html = html.replace(
    /<meta property="og:description" content=".*?" \/>/s,
    `<meta property="og:description" content="Commercial street address in ${state.city}, ${state.name}. Official registered agent and same-day mail scanning." />`
  );

  // 4. Update asset paths from root so they load properly in subfolder
  html = html.replace(/href="styles\.css"/g, 'href="/styles.css"');
  html = html.replace(/src="script\.js"/g, 'src="/script.js"');
  html = html.replace(/src="site\.config\.js"/g, 'src="/site.config.js"');

  // 5. Hero H1 and Subtitle customization
  html = html.replace(
    /<h1 class="hero-title">[\s\S]*?<\/h1>/,
    `<h1 class="hero-title">${state.heroH1}</h1>`
  );
  html = html.replace(
    /<p class="hero-subtitle">[\s\S]*?<\/p>/,
    `<p class="hero-subtitle">${state.heroSub}</p>`
  );

  writeFileSync(join(dir, 'index.html'), html, 'utf8');
  console.log(`[Created State Page] /${state.slug}/index.html`);

  sitemapUrls.push({
    loc: stateUrl,
    priority: '0.85'
  });
}

// 6. Generate Updated Sitemap
const sitemapXml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">
${sitemapUrls.map(u => `  <url>
    <loc>${u.loc}</loc>
    <lastmod>${TODAY}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>${u.priority}</priority>
    <image:image>
      <image:loc>https://virtualofficespaceusa.online/assets/og-image.png</image:loc>
    </image:image>
  </url>`).join('\n')}
</urlset>
`;

writeFileSync(join(root, 'sitemap.xml'), sitemapXml, 'utf8');
console.log(`[Updated Sitemap] sitemap.xml now contains ${sitemapUrls.length} indexable URLs!`);
