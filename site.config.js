/**
 * SITE CONFIGURATION: Virtual Office Space USA
 */
const SITE_CONFIG = {
  business: {
    name: "Virtual Office Space USA",
    legalName: "STAGE-X Virtual Office Space USA",
    tagline: "Prestigious US Commercial Business Address, Registered Agent & Mail Forwarding",
    description: "Get a verified, commercial US street address in Wyoming, Delaware, Florida, Texas, or California. Bank-ready for Mercury, Relay & Stripe with official registered agent service and same-day digital mail scanning.",
    domain: "virtualofficespaceusa.online",
    url: "https://virtualofficespaceusa.online",
    
    // Communication
    whatsappNumber: "919244240917", // International format without '+'
    phoneDisplay: "+1 (331) 328-7053",
    contactEmail: "connect@virtualofficespaceusa.online",
    
    // Key Stats & Trust Badges
    turnaroundTime: "Instant 24/7 Address Issuance",
    priceStartingAt: "$19/mo",
    ratingScore: "4.95",
    reviewCount: "2,480+ Founders",
    cmraCompliant: true
  },
  
  states: [
    {
      name: "Wyoming",
      city: "Sheridan / Cheyenne",
      taxRate: "0% Corporate / 0% Personal",
      privacy: "Maximum Anonymous Ownership",
      bestFor: "E-commerce, Asset Protection & Privacy",
      tag: "Top Choice for Non-US Residents"
    },
    {
      name: "Delaware",
      city: "Wilmington / Dover",
      taxRate: "Chancery Court Prestige",
      privacy: "Global Investor Standard",
      bestFor: "VC-Backed Tech Startups & Raising Capital",
      tag: "Preferred by 68% of Fortune 500"
    },
    {
      name: "Florida",
      city: "Miami / Orlando",
      taxRate: "0% Personal Income Tax",
      privacy: "High Asset Shield",
      bestFor: "Global Trade, Real Estate & Latin America Gateway",
      tag: "Fastest Growing Business Hub"
    },
    {
      name: "Texas",
      city: "Austin / Dallas",
      taxRate: "0% Individual State Tax",
      privacy: "Pro-Business Infrastructure",
      bestFor: "Tech, Manufacturing & High-Scale Operations",
      tag: "Booming Enterprise Destination"
    },
    {
      name: "California",
      city: "San Francisco / Silicon Valley",
      taxRate: "Venture Benchmark",
      privacy: "Global Tech Authority",
      bestFor: "AI Startups, SaaS & Media Brands",
      tag: "Global Innovation Center"
    },
    {
      name: "New York",
      city: "Manhattan, NYC",
      taxRate: "Iconic Wall Street Presence",
      privacy: "Global Credibility",
      bestFor: "Finance, Consulting, Fashion & Media",
      tag: "World Business Capital"
    }
  ],

  services: [
    {
      id: "commercial-address",
      title: "Commercial Street Address",
      icon: "🏢",
      desc: "Real physical commercial building address (never a P.O. Box). Approved for USPS Form 1583, Google Business, and state business registrations.",
      intent: "Inquiry: US Commercial Address"
    },
    {
      id: "registered-agent",
      title: "Certified Registered Agent",
      icon: "⚖️",
      desc: "State-licensed registered agent representation across all 50 US states. Receives legal service of process and state compliance notices with same-day digital delivery.",
      intent: "Inquiry: Registered Agent Service"
    },
    {
      id: "digital-mailroom",
      title: "Same-Day Digital Mailroom",
      icon: "📨",
      desc: "High-resolution envelope & document scanning. Preview mail online, request secure shredding, or forward physical packages globally via FedEx, DHL, or USPS.",
      intent: "Inquiry: Digital Mailroom & Scanning"
    },
    {
      id: "us-banking",
      title: "Bank & Fintech Readiness",
      icon: "💳",
      desc: "Address documentation pre-verified for US fintech business checking accounts including Mercury Bank, Relay Financial, Brex, Stripe, and PayPal.",
      intent: "Inquiry: US Banking & Mercury Account"
    },
    {
      id: "llc-ein",
      title: "US LLC & EIN Support",
      icon: "📑",
      desc: "Step-by-step guidance for non-resident LLC formation, Articles of Organization, Operating Agreement, and IRS Form SS-4 EIN acquisition without an SSN/ITIN.",
      intent: "Inquiry: US LLC & EIN Setup"
    },
    {
      id: "corporate-phone",
      title: "US Business Phone & VoIP",
      icon: "📱",
      desc: "Dedicated US phone number with SMS verification, call forwarding, and custom voicemail greeting to maintain a 100% professional US presence.",
      intent: "Inquiry: US Business Phone Number"
    }
  ],

  pricing: [
    {
      plan: "Digital Mail",
      price: "$19",
      period: "/ month",
      billing: "or $199 billed annually (save 15%)",
      featured: false,
      features: [
        "Prestigious US Commercial Street Address",
        "Unique Suite / Unit Number",
        "Digital Envelope Scanning & Email Alerts",
        "Secure Online Mail Portal",
        "International Package Forwarding Access",
        "USPS Form 1583 Verification Support"
      ],
      intent: "Order Plan: Digital Mail ($19/mo)"
    },
    {
      plan: "Business Pro",
      price: "$39",
      period: "/ month",
      billing: "or $389 billed annually (save 20%)",
      featured: true,
      badge: "Most Popular for US LLCs",
      features: [
        "Everything in Digital Mail Plan",
        "State Registered Agent Service Included",
        "Annual State Report Compliance Reminders",
        "Unlimited Open & Scan of Official Documents",
        "Bank-Ready Address Proof for Mercury & Relay",
        "Priority Customer Support via WhatsApp & Email"
      ],
      intent: "Order Plan: Business Pro ($39/mo)"
    },
    {
      plan: "Global Founder Suite",
      price: "$79",
      period: "/ month",
      billing: "or $749 billed annually",
      featured: false,
      features: [
        "Everything in Business Pro Plan",
        "US LLC Formation Guidance (WY / DE / FL)",
        "IRS Federal EIN (Tax ID) Support",
        "Free US Virtual Business Phone Number",
        "Dedicated Account Specialist",
        "Notarized Proof of Address Support"
      ],
      intent: "Order Plan: Global Founder Suite ($79/mo)"
    }
  ],

  faqs: [
    {
      q: "Is this a real physical street address or a P.O. Box?",
      a: "Every address we provide is a genuine, verified commercial office building address with a dedicated suite number. We never use P.O. Boxes. It is fully compliant with USPS CMRA guidelines and accepted by the IRS, state governments, and banks."
    },
    {
      q: "Can I use this address to open a US bank account like Mercury or Relay?",
      a: "Yes. Our commercial street addresses and lease documentation meet the physical address requirements enforced by US fintech banking partners including Mercury Bank, Relay Financial, Brex, and Stripe."
    },
    {
      q: "Do I need to be a US citizen or have an SSN/ITIN?",
      a: "No! International entrepreneurs from anywhere in the world can legally own a US virtual office, form a US company, and obtain an IRS EIN without requiring a US Social Security Number (SSN) or ITIN."
    },
    {
      q: "What is USPS Form 1583 and how do I complete it?",
      a: "USPS Form 1583 is the legal US Postal Service authorization permitting a Commercial Mail Receiving Agency (CMRA) to handle mail on your behalf. We provide pre-filled forms and guide you through fast online notarization in minutes."
    },
    {
      q: "How does same-day mail scanning work?",
      a: "When mail arrives for your business, our secure mailroom scans the outside envelope and uploads it to your notification feed. You can click to request an interior scan, forward the item anywhere globally, or securely shred it."
    },
    {
      q: "What is a Registered Agent and do I need one?",
      a: "A Registered Agent is legally required by every US state to accept official government notices, franchise tax forms, and legal service of process during business hours. Our Business Pro plan includes full Registered Agent service."
    }
  ]
};

if (typeof module !== 'undefined' && module.exports) {
  module.exports = SITE_CONFIG;
}
