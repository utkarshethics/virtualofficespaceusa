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
