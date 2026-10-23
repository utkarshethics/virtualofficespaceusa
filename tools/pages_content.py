# -*- coding: utf-8 -*-
"""Content for keyword landing pages. Edit copy here, then run: python3 tools/build_pages.py

Fact check date: 2026-10-23. State fees come from state fee schedules as summarised by
current 2026 guides; re-check each Secretary of State before changing figures.
"""

FACT_DATE = "October 2026"

# ---------------------------------------------------------------- service hubs
SERVICES = [
 {
  "slug": "virtual-business-address",
  "nav": "Virtual Business Address",
  "title": "Virtual Business Address for LLCs | Virtual Office Space USA",
  "desc": "A real US street address for your LLC, not a P.O. Box. Use it on state filings, IRS forms, invoices and bank applications. Same-day mail scanning from $19/mo.",
  "h1": "Virtual business address for your US LLC",
  "lead": "A real commercial street address with your own suite number, in Wyoming, Delaware, Florida, Texas, California or New York. Your mail is received by a USPS-registered mailroom and scanned the same day, so you can run a US company from anywhere.",
  "keywords": ["virtual business address", "virtual address for business", "virtual address for LLC", "business address for LLC"],
  "service_id": "service-commercial-address",
  "sections": [
   ("What a virtual business address is", [
    "p:A virtual business address is a street address at a commercial building that you can use as your company's official mailing and business address without renting desk space. The building is operated by a Commercial Mail Receiving Agency (CMRA) registered with the US Postal Service, and you get a unique suite or unit number that identifies your mail.",
    "p:Because it is a real street address, not a P.O. Box, it can be used in places where a P.O. Box is refused, such as many state business filings and bank account applications.",
   ]),
   ("Where you can use it", [
    "ul:State filings — the principal office or mailing address on your LLC's Articles of Organization and annual reports|IRS forms — the mailing address on Form SS-4 when you apply for an EIN, and on later tax filings|Banking and payments — the business address on applications to fintech banks and payment processors such as Mercury, Relay, Brex and Stripe (each provider makes its own approval decision)|Your website, invoices, contracts and marketplace seller accounts|Business cards, letterheads and email signatures",
    "p:One thing to know: Google Business Profile guidelines generally do not allow virtual offices or mailboxes to be listed as a storefront location unless the address is staffed during business hours. Use your virtual address for filings and correspondence, not as a Maps listing.",
   ]),
   ("Virtual address vs. P.O. Box vs. home address", [
    "table:|Virtual business address|P.O. Box|Home address\nReal street address|Yes|No|Yes\nAccepted on most state filings|Yes|Often refused|Yes\nKeeps your home address off public records|Yes|Yes|No\nReceives courier packages (FedEx, UPS, DHL)|Yes|USPS only|Yes\nMail scanned and viewable online|Yes|No|No\nWorks if you live outside the US|Yes|No|No",
   ]),
   ("Is a virtual address allowed for an LLC?", [
    "p:Yes. US states do not require an LLC to lease office space. What every state does require is a registered agent with a physical address in the state of formation, available during normal business hours to accept legal papers. That role is separate from your business address — see our <a href=\"/registered-agent/\">registered agent service</a>. Our Business Pro plan covers both, so your registered office and your business address can sit with the same provider.",
   ]),
   ("How it works", [
    "ol:Choose your state and plan — <a href=\"/#pricing\">plans start at $19/month</a>.|Complete USPS Form 1583, which authorises us to receive mail for you. We send it pre-filled and guide you through ID verification — read our <a href=\"/guides/usps-form-1583/\">Form 1583 guide</a>.|Start using your address. Every envelope is scanned on arrival; you decide whether to open and scan, forward or shred it.",
   ]),
  ],
  "faqs": [
   ("Can I use a virtual business address as my LLC's registered office?", "Your registered office must be the physical address of your registered agent in the state of formation, staffed during business hours. A plain mailbox address does not meet that rule on its own. Our Business Pro plan includes registered agent service, so we can act as your registered agent and give you a separate business address."),
   ("Will a bank accept a virtual business address?", "Many US fintech banks and payment processors accept a commercial street address with a suite number. We provide proof-of-address documentation for these applications, but each bank sets its own rules and makes the final decision."),
   ("Is a virtual business address the same as a P.O. Box?", "No. A virtual business address is a street address at a commercial building, with your own suite number. It can receive courier deliveries and is accepted in many places where a P.O. Box is not."),
   ("Do I need to live in the US to get one?", "No. Founders anywhere in the world can get a US virtual business address. You will need to complete USPS Form 1583 with two forms of identification."),
  ],
  "related": ["registered-agent", "virtual-mailbox", "guides/usps-form-1583", "wyoming", "delaware"],
 },
 {
  "slug": "registered-agent",
  "nav": "Registered Agent",
  "title": "Registered Agent Service for LLCs | Virtual Office Space USA",
  "desc": "Registered agent service for your LLC: we accept legal papers and state notices, scan them the same day and remind you of deadlines. Included in Business Pro.",
  "h1": "Registered agent service for your LLC",
  "lead": "Every US LLC and corporation must name a registered agent in its state of formation. We take that role, receive legal and state documents on your behalf, scan them the same day and keep your personal address off the public record.",
  "keywords": ["registered agent for LLC", "registered agent services", "registered agent service"],
  "service_id": "service-registered-agent",
  "sections": [
   ("What a registered agent does", [
    "p:A registered agent (called a resident agent or statutory agent in some states) is the person or company officially designated to receive service of process — lawsuits and subpoenas — and official notices from the Secretary of State, such as annual report reminders and franchise tax notices.",
    "p:The registered agent's name and address appear on public state records, so anyone who needs to formally contact your company knows where to send papers.",
    "p:For a full explanation, read <a href=\"/guides/what-is-a-registered-agent/\">What is a registered agent?</a>",
   ]),
   ("State requirements", [
    "ul:A physical street address in the state where the company is formed or registered — P.O. Boxes are not allowed|Availability during normal business hours to accept documents in person|Consent to act as the company's agent",
    "p:If you live outside that state — or outside the US — you cannot act as your own registered agent there, which is why most non-resident founders use a registered agent service.",
   ]),
   ("Why use a registered agent service", [
    "ul:Privacy — our address goes on the public record instead of your home address|Reliability — someone is always there to sign for documents during business hours|Speed — documents are scanned and sent to you the same day|Compliance — we remind you of annual report and franchise tax deadlines so you avoid late fees or administrative dissolution",
   ]),
   ("What is included", [
    "p:Registered agent service is included in our <a href=\"/#plan-business-pro\">Business Pro plan ($39/month)</a>, together with a commercial business address and digital mail scanning. It is available in all 50 states, with dedicated pages for the most popular formation states:",
    "states:",
   ]),
   ("Changing your registered agent", [
    "p:You can switch registered agents at any time by filing a change of registered agent form with the Secretary of State. Most states charge a small filing fee. We tell you which form your state uses and what to enter in the new agent fields.",
   ]),
  ],
  "faqs": [
   ("Do I need a registered agent for an LLC?", "Yes. Every state requires LLCs and corporations to maintain a registered agent with a physical address in the state for as long as the company exists."),
   ("Can I be my own registered agent?", "Only if you have a physical address in the state of formation and can be there during business hours. Non-residents and people who want privacy usually appoint a registered agent service."),
   ("Is the registered agent address public?", "Yes. The registered agent's name and address are listed on the state's public business records. Using a service keeps your personal address off those records."),
   ("Can my registered agent address also be my business address?", "They are two different roles. Some states let the principal office and registered office be the same, but many owners prefer a separate business address for mail and banking. Business Pro gives you both."),
  ],
  "related": ["guides/what-is-a-registered-agent", "virtual-business-address", "texas", "delaware", "florida"],
 },
 {
  "slug": "virtual-mailbox",
  "nav": "Virtual Mailbox",
  "title": "Virtual Mailbox for Business — Same-Day Mail Scanning",
  "desc": "A virtual mailbox for business at a real US street address. Every envelope scanned on arrival; open, forward worldwide or shred online. From $19/mo.",
  "h1": "Virtual mailbox for business with same-day scanning",
  "lead": "Your business mail goes to a real US street address and is scanned the moment it arrives. Read it online, request a full scan, have it forwarded anywhere in the world, or shred it — without visiting a post office.",
  "keywords": ["virtual mailbox for business", "virtual mailbox", "mail scanning service", "mail forwarding"],
  "service_id": "service-mail-scanning",
  "sections": [
   ("How mail scanning works", [
    "ol:Mail arrives at your US address and is logged against your suite number.|We scan the outside of the envelope and notify you by email.|You choose: open and scan the contents to PDF, forward the item, hold it, or securely shred it.",
    "p:Packages from USPS, FedEx, UPS and DHL are received too, and can be forwarded internationally.",
   ]),
   ("What a business mailbox handles well", [
    "ul:IRS letters, including your EIN confirmation and tax notices|Secretary of State and franchise tax notices|Bank and payment-processor correspondence|Checks and invoices from customers|Marketplace and platform verification letters",
   ]),
   ("Virtual mailbox vs. virtual office", [
    "p:A virtual mailbox is the mail-handling part of a virtual office. Our <a href=\"/#plan-digital-mail\">Digital Mail plan</a> gives you the address and mailbox. The <a href=\"/#plan-business-pro\">Business Pro plan</a> adds registered agent service and bank-ready proof of address, which most new LLCs need.",
   ]),
   ("USPS Form 1583", [
    "p:Federal rules require anyone receiving mail through a commercial mail receiving agency to file USPS Form 1583 and verify their identity. We send the form pre-filled and walk you through verification — see the <a href=\"/guides/usps-form-1583/\">Form 1583 guide</a>.",
   ]),
  ],
  "faqs": [
   ("Is a virtual mailbox a real street address?", "Yes. Your mail goes to a commercial building address with your own suite number, not a P.O. Box."),
   ("How fast is mail scanned?", "Envelopes are scanned on the day they arrive. Full-content scans are made when you request them."),
   ("Can you forward mail outside the US?", "Yes. Letters and packages can be forwarded worldwide; carrier postage is charged at cost."),
   ("Do I need Form 1583 for a virtual mailbox?", "Yes. USPS requires Form 1583 and identity verification before a commercial mail receiving agency can accept mail for you."),
  ],
  "related": ["virtual-business-address", "guides/usps-form-1583", "registered-agent", "new-york", "california"],
 },
 {
  "slug": "us-llc-for-non-residents",
  "nav": "US LLC for Non-Residents",
  "title": "US LLC for Non-Residents — Formation, EIN & Address",
  "desc": "Form a US LLC from outside the US: pick a state, appoint a registered agent, get an EIN without an SSN and set up a US address for banking. Step-by-step.",
  "h1": "How to form a US LLC as a non-resident",
  "lead": "You do not need to be a US citizen or resident to own a US LLC. Here is the full path — state, registered agent, filing, EIN without an SSN, US address and banking — and the ongoing filings to keep it in good standing.",
  "keywords": ["US LLC for non-residents", "LLC for non US residents", "form LLC from India", "EIN without SSN"],
  "service_id": "service-llc-ein",
  "sections": [
   ("1. Choose a state", [
    "p:Most non-resident founders choose <a href=\"/wyoming/\">Wyoming</a> for its low ongoing cost and privacy, or <a href=\"/delaware/\">Delaware</a> if they plan to raise venture capital. If you will have staff, an office or inventory in a particular state, you may also need to register there. Compare the two in <a href=\"/guides/wyoming-vs-delaware-llc/\">Wyoming vs. Delaware LLC</a>.",
   ]),
   ("2. Appoint a registered agent", [
    "p:Every LLC needs a <a href=\"/registered-agent/\">registered agent</a> with a physical address in the formation state. As a non-resident you cannot fill this role yourself.",
   ]),
   ("3. File the Articles of Organization", [
    "p:File with the Secretary of State and pay the state fee — for example $100 in Wyoming, $110 in Delaware, $125 in Florida (including the registered agent designation) or $300 in Texas. Then sign an Operating Agreement that sets out ownership and how the LLC is run.",
   ]),
   ("4. Get an EIN without an SSN", [
    "p:Apply to the IRS with Form SS-4. If the responsible party has no SSN or ITIN, the online application is not available; international applicants can apply by phone (+1 267-941-1099), by fax or by mail, writing \"Foreign\" on line 7b. Full steps are in <a href=\"/guides/how-to-get-an-ein-for-an-llc/\">How to get an EIN for an LLC</a>.",
   ]),
   ("5. Set up a US address and bank account", [
    "p:Banks and payment processors ask for a US business address. A <a href=\"/virtual-business-address/\">virtual business address</a> gives you a commercial street address and proof-of-address documents for your applications.",
   ]),
   ("6. Stay compliant every year", [
    "ul:File your state annual report or franchise tax report on time (see each state page for dates and fees)|Keep your registered agent active|For a single-member LLC owned by a foreign person: file IRS Form 5472 with a pro forma Form 1120 each year, even with no US income — the penalty for not filing starts at $25,000",
    "p:We are not a law firm or tax adviser; talk to a US tax professional about your situation, especially if you have US-source income.",
   ]),
   ("How we help", [
    "p:The <a href=\"/#plan-global-founder-suite\">Global Founder Suite ($79/month)</a> covers formation assistance, EIN filing support, registered agent service, a commercial US address with mail scanning, and a US business phone number.",
   ]),
  ],
  "faqs": [
   ("Can a non-US citizen own a US LLC?", "Yes. There is no citizenship or residency requirement to form or own an LLC in any US state."),
   ("Can I get an EIN without an SSN or ITIN?", "Yes. Use Form SS-4 and write \"Foreign\" on line 7b. International applicants can apply by phone, fax or mail; the online application is not available without an SSN or ITIN."),
   ("Which state is best for a non-resident LLC?", "Wyoming is popular for low annual cost and privacy; Delaware is the standard for venture-backed startups. If you operate physically in another state, you may need to register there as well."),
   ("Do foreign-owned LLCs file US tax forms?", "A single-member LLC owned by a foreign person generally must file Form 5472 with a pro forma Form 1120 every year, even without US income. Check with a US tax professional."),
  ],
  "related": ["guides/how-to-get-an-ein-for-an-llc", "guides/wyoming-vs-delaware-llc", "wyoming", "delaware", "virtual-business-address"],
 },
]

# ---------------------------------------------------------------- state pages
STATES = [
 {
  "slug": "wyoming", "name": "Wyoming", "abbr": "WY", "cities": "Sheridan & Cheyenne", "wikidata": "Q1214",
  "title": "Wyoming Registered Agent & Virtual Office Address",
  "desc": "Wyoming registered agent and a Sheridan or Cheyenne business address. $100 LLC filing, $60 minimum annual report, no state income tax. From $19/mo.",
  "h1": "Wyoming registered agent & virtual office",
  "lead": "Wyoming is the most popular state for non-resident founders: low fees, no state income tax and strong owner privacy. Get a Wyoming registered agent and a commercial address in Sheridan or Cheyenne.",
  "facts": [("LLC formation fee", "$100"), ("Annual report", "Due the first day of your formation anniversary month"), ("Annual fee", "$60 minimum, or $0.0002 per dollar of Wyoming assets if higher"), ("State income tax", "None — no corporate or personal income tax"), ("Owner privacy", "Members are not listed in the Articles of Organization")],
  "body": [
   ("Why founders choose Wyoming", [
    "p:Wyoming charges $100 to form an LLC and a $60 minimum annual fee, one of the lowest ongoing costs of any state. It has no state corporate or personal income tax, and the names of members do not have to appear in the public formation documents.",
    "p:That combination makes it the default for e-commerce sellers, SaaS founders and consultants who live outside the US and want a simple holding or operating LLC.",
   ]),
   ("Wyoming registered agent", [
    "p:Every Wyoming LLC must keep a registered agent with a physical Wyoming address. We act as your Wyoming registered agent, receive service of process and Secretary of State notices, scan them the same day and remind you before your annual report falls due on the first day of your anniversary month. If the annual fee is not paid within 60 days of the due date, the state can dissolve the LLC, so reminders matter.",
   ]),
   ("Virtual office address in Wyoming", [
    "p:Pair your registered agent with a commercial street address in Sheridan or Cheyenne for your business mail, bank applications and invoices. Mail is scanned on arrival and can be forwarded worldwide.",
   ]),
  ],
  "faqs": [
   ("How much does a Wyoming LLC cost per year?", "The state annual report fee is $60 minimum (or $0.0002 per dollar of Wyoming-based assets if that is higher), plus your registered agent fee. Online filing may add a small processing fee."),
   ("When is the Wyoming annual report due?", "On the first day of the month in which the LLC was formed, every year. You can file up to 120 days early."),
   ("Does Wyoming have a state income tax?", "No. Wyoming has no state corporate income tax and no personal income tax."),
   ("Do I need a Wyoming registered agent if I live abroad?", "Yes. Every Wyoming LLC needs a registered agent with a physical Wyoming address, so non-residents appoint a registered agent service."),
  ],
  "related": ["guides/wyoming-vs-delaware-llc", "us-llc-for-non-residents", "registered-agent", "delaware"],
 },
 {
  "slug": "delaware", "name": "Delaware", "abbr": "DE", "cities": "Wilmington & Dover", "wikidata": "Q1393",
  "title": "Delaware Registered Agent & Virtual Office Address",
  "desc": "Delaware registered agent and a Wilmington or Dover business address. The Delaware LLC annual tax is $400 from the 2026 tax year. Same-day mail scanning.",
  "h1": "Delaware registered agent & virtual office",
  "lead": "Delaware is the standard for venture-backed startups thanks to its Court of Chancery and well-tested corporate law. Get a Delaware registered agent and a business address in Wilmington or Dover.",
  "facts": [("LLC formation fee", "$110 (Delaware changed several filing fees on August 1, 2026 — confirm the current schedule)"), ("LLC annual tax", "$400 from the 2026 tax year (was $300), due June 1 of the following year"), ("Corporation annual report", "Due March 1, with franchise tax — minimum $175 (authorized shares method) or $400 (assumed par value capital method)"), ("Business court", "Court of Chancery — specialist business court"), ("Best for", "C-corporations raising venture capital")],
  "body": [
   ("Why founders choose Delaware", [
    "p:Investors and their lawyers know Delaware law, and the Court of Chancery has decades of business case law. If you plan to raise venture capital, issue stock options or sell the company one day, a Delaware C-corporation is usually expected.",
    "p:For a small LLC without investors, Delaware costs more each year than Wyoming — compare them in <a href=\"/guides/wyoming-vs-delaware-llc/\">Wyoming vs. Delaware LLC</a>.",
   ]),
   ("New: Delaware LLC tax rises to $400", [
    "p:Delaware raised the flat annual tax for LLCs and partnerships from $300 to $400, effective for the 2026 tax year. Because the tax is paid in arrears, the first $400 payment is due by June 1, 2027. Corporations are unaffected: their annual report and franchise tax remain due March 1.",
   ]),
   ("Delaware registered agent", [
    "p:Every Delaware entity must keep a registered agent with a physical Delaware address. We receive service of process and state notices, scan them the same day, and remind you before the March 1 (corporations) or June 1 (LLCs) deadline. Delaware charges a penalty for late payment, so reminders save money.",
   ]),
   ("Virtual office address in Delaware", [
    "p:Add a commercial street address in Wilmington or Dover for correspondence, invoices and bank applications, with same-day scanning and worldwide forwarding.",
   ]),
  ],
  "faqs": [
   ("How much is the Delaware LLC annual tax?", "$400 per year starting with the 2026 tax year (previously $300). It is due by June 1 of the following year."),
   ("When is the Delaware franchise tax due for corporations?", "Corporations file their annual report and pay franchise tax by March 1 each year."),
   ("Do I need a Delaware registered agent?", "Yes. Every Delaware LLC and corporation must maintain a registered agent with a physical address in Delaware."),
   ("Is Delaware better than Wyoming for an LLC?", "Delaware is better if you plan to raise venture capital or convert to a C-corporation. For a small LLC, Wyoming usually costs less each year."),
  ],
  "related": ["guides/wyoming-vs-delaware-llc", "registered-agent", "us-llc-for-non-residents", "wyoming"],
 },
 {
  "slug": "florida", "name": "Florida", "abbr": "FL", "cities": "Miami & Orlando", "wikidata": "Q812",
  "title": "Florida Registered Agent & Virtual Office Address",
  "desc": "Florida registered agent and a Miami or Orlando business address. $125 LLC filing, $138.75 annual report due May 1, no personal income tax. Same-day scanning.",
  "h1": "Florida registered agent & virtual office",
  "lead": "Florida is a gateway for trade with Latin America and Europe, with no personal state income tax. Get a Florida registered agent and a commercial address in Miami or Orlando.",
  "facts": [("LLC formation fee", "$125 ($100 filing + $25 registered agent designation)"), ("Annual report", "$138.75, due by May 1 every year"), ("Late fee", "$400 if the annual report is filed after May 1"), ("Personal income tax", "None"), ("Best for", "Trade, e-commerce, real estate and Latin America-facing businesses")],
  "body": [
   ("Why founders choose Florida", [
    "p:Florida has no personal state income tax, a large consumer market and strong links to Latin America. Miami in particular is home to many international trade, logistics and fintech companies.",
   ]),
   ("Florida registered agent", [
    "p:Florida requires a registered agent with a physical Florida street address; the $25 designation fee is part of the formation cost. We act as your Florida registered agent and remind you well before May 1 — Florida's $400 late fee is one of the highest in the country.",
   ]),
   ("Virtual office address in Florida", [
    "p:Get a commercial street address in Miami or Orlando for your business mail, bank applications and invoices, with same-day scanning and international forwarding.",
   ]),
  ],
  "faqs": [
   ("How much does it cost to form a Florida LLC?", "$125: a $100 filing fee for the Articles of Organization plus a $25 registered agent designation fee."),
   ("When is the Florida annual report due?", "By May 1 every year. The fee is $138.75, and a $400 late fee applies after the deadline."),
   ("Does Florida have a state income tax?", "Florida has no personal income tax. C-corporations do pay Florida corporate income tax."),
   ("Do I need a Florida registered agent?", "Yes. Every Florida LLC must name a registered agent with a physical Florida address."),
  ],
  "related": ["registered-agent", "virtual-business-address", "texas", "us-llc-for-non-residents"],
 },
 {
  "slug": "texas", "name": "Texas", "abbr": "TX", "cities": "Austin & Dallas", "wikidata": "Q1439",
  "title": "Texas Registered Agent & Virtual Office Address",
  "desc": "Texas registered agent and an Austin or Dallas address. $300 LLC filing; no franchise tax under $2.65M revenue (2026), but the May 15 report is still required.",
  "h1": "Texas registered agent & virtual office",
  "lead": "Texas has no personal income tax and one of the fastest-growing tech and manufacturing economies in the US. Get a Texas registered agent and a commercial address in Austin or Dallas.",
  "facts": [("LLC formation fee", "$300 (Certificate of Formation, Form 205)"), ("Franchise tax", "No tax due if annualized revenue is $2.65 million or less (2026 reports)"), ("Annual filing", "Franchise tax report and Public Information Report due May 15 — still required when no tax is due"), ("Personal income tax", "None"), ("Best for", "Tech, SaaS, manufacturing and companies selling into Texas")],
  "body": [
   ("Why founders choose Texas", [
    "p:Texas has no personal income tax, a large and growing economy, and major tech hubs in Austin and Dallas. If you have customers, staff or inventory in Texas, forming there can be simpler than forming elsewhere and registering in Texas as a foreign LLC.",
   ]),
   ("Texas franchise tax, explained", [
    "p:Texas LLCs are subject to franchise tax, but businesses with annualized total revenue of $2.65 million or less owe no tax for 2026 reports. That does not remove the filing: you still need to file by May 15 — including a Public Information Report — or face penalties and, eventually, forfeiture of the LLC's right to do business.",
   ]),
   ("Texas registered agent", [
    "p:Texas requires a registered agent with a physical Texas address. We act as your Texas registered agent, scan service of process and Comptroller notices the same day, and remind you before the May 15 deadline.",
   ]),
   ("Virtual office address in Texas", [
    "p:Add a commercial street address in Austin or Dallas for your mail, contracts and bank applications.",
   ]),
  ],
  "faqs": [
   ("How much does a Texas LLC cost?", "The Certificate of Formation filing fee is $300. There is no separate annual report fee, but a franchise tax report is due every May 15."),
   ("Do Texas LLCs pay franchise tax?", "Only if annualized revenue exceeds the no-tax-due threshold, which is $2.65 million for 2026 reports. All LLCs must still file their report on time."),
   ("Does Texas have a state income tax?", "Texas has no personal income tax. Businesses are taxed through the franchise (margin) tax instead."),
   ("Do I need a Texas registered agent?", "Yes. Every Texas LLC must maintain a registered agent with a physical address in Texas."),
  ],
  "related": ["registered-agent", "guides/what-is-a-registered-agent", "florida", "virtual-business-address"],
 },
 {
  "slug": "california", "name": "California", "abbr": "CA", "cities": "San Francisco & Silicon Valley", "wikidata": "Q99",
  "title": "California Registered Agent & Virtual Office Address",
  "desc": "California registered agent and a San Francisco or Silicon Valley address. Know the costs: $70 LLC filing, $800 yearly franchise tax, $20 biennial statement.",
  "h1": "California registered agent & virtual office",
  "lead": "A San Francisco or Silicon Valley address signals credibility with tech clients and investors. Get a California registered agent and a commercial business address — and know the state's costs before you form there.",
  "facts": [("LLC formation fee", "$70"), ("Annual franchise tax", "$800 minimum every year; first payment due by the 15th day of the 4th month after formation"), ("Statement of Information", "$20, within 90 days of formation, then every two years"), ("Additional LLC fee", "Applies when California gross receipts exceed the state threshold"), ("Best for", "Businesses operating in California or selling to Bay Area tech companies")],
  "body": [
   ("Should you form in California?", [
    "p:California is one of the more expensive states to keep an LLC in: the $800 minimum franchise tax applies every year until the LLC is cancelled, whether or not it makes money. If you do business in California — staff, an office or significant sales there — you generally have to pay it anyway, even if you form elsewhere.",
    "p:If you only want Silicon Valley credibility, you can form in another state and use a California <a href=\"/virtual-business-address/\">business address</a>. Get advice if you are unsure whether you are \"doing business\" in California.",
   ]),
   ("California registered agent", [
    "p:California calls the registered agent an \"agent for service of process\". It must have a physical California address. We fill that role, scan documents the same day and remind you of franchise tax and Statement of Information deadlines.",
   ]),
   ("Virtual office address in California", [
    "p:Get a commercial street address in San Francisco or Silicon Valley for business mail, contracts and bank applications.",
   ]),
  ],
  "faqs": [
   ("How much does a California LLC cost per year?", "At least $800 a year in franchise tax, plus $20 for the Statement of Information every two years. Larger LLCs also pay an additional fee based on gross receipts."),
   ("When is the first $800 California payment due?", "Generally by the 15th day of the fourth month after the LLC is filed with the Secretary of State."),
   ("Can I use a California address without forming a California LLC?", "Yes. You can form in another state and use a California business address. If you actually do business in California, you may still need to register there and pay California taxes."),
   ("What is an agent for service of process?", "It is California's term for a registered agent: the person or company with a California address that receives legal papers and state notices for your business."),
  ],
  "related": ["virtual-business-address", "registered-agent", "new-york", "guides/what-is-a-registered-agent"],
 },
 {
  "slug": "new-york", "name": "New York", "abbr": "NY", "cities": "Manhattan, NYC", "wikidata": "Q1384",
  "title": "New York Registered Agent & Manhattan Virtual Office",
  "desc": "Manhattan virtual office address and New York registered agent. Know the rules: $200 LLC filing, newspaper publication within 120 days, $9 biennial statement.",
  "h1": "New York registered agent & Manhattan virtual office",
  "lead": "A Manhattan street address carries weight with finance, fashion, media and consulting clients. Get a commercial New York address and a registered agent — and understand New York's publication rule before you form.",
  "facts": [("LLC formation fee", "$200"), ("Publication requirement", "Publish a notice in two newspapers for six consecutive weeks within 120 days of formation"), ("Certificate of Publication", "$50 state filing fee, plus newspaper costs that vary by county"), ("Biennial statement", "$9 every two years"), ("Best for", "Finance, consulting, fashion and media businesses that want a Manhattan presence")],
  "body": [
   ("New York's publication requirement", [
    "p:New York is one of the few states that requires new LLCs to publish a notice of formation. Within 120 days, you must run it in two newspapers chosen by the county clerk for six consecutive weeks, then file a Certificate of Publication ($50). Newspaper costs depend on the county and are much higher in Manhattan. If you skip it, the LLC's authority to do business in New York can be suspended.",
   ]),
   ("New York registered agent", [
    "p:In New York the Secretary of State is the default agent for service of process, and it forwards papers to the address you list. Many companies also appoint a registered agent so documents reach a staffed address and are scanned the same day. We can fill that role and remind you of your biennial statement.",
   ]),
   ("Manhattan virtual office address", [
    "p:Get a commercial street address in Manhattan for client correspondence, contracts and bank applications, with same-day scanning and worldwide forwarding. You can use a New York address with an LLC formed in another state.",
   ]),
  ],
  "faqs": [
   ("How much does a New York LLC cost?", "$200 to file the Articles of Organization, $50 for the Certificate of Publication, plus newspaper publication costs that vary by county, and $9 every two years for the biennial statement."),
   ("What happens if I don't publish my New York LLC?", "The LLC's authority to carry on business in New York can be suspended until publication is completed."),
   ("Do I need a registered agent in New York?", "New York designates the Secretary of State to receive service of process, but you can also appoint a registered agent so documents go to a staffed address."),
   ("Can I get a Manhattan address without a New York LLC?", "Yes. You can form your LLC in another state and use a Manhattan business address for mail and correspondence."),
  ],
  "related": ["virtual-business-address", "virtual-mailbox", "california", "registered-agent"],
 },
]

# ---------------------------------------------------------------- guides
GUIDES = [
 {
  "slug": "guides/what-is-a-registered-agent",
  "nav": "What is a registered agent?",
  "title": "What Is a Registered Agent for an LLC? (Plain-English Guide)",
  "desc": "What a registered agent is, what it does, the legal requirements in every state, whether you can be your own, and what happens if your LLC doesn't have one.",
  "h1": "What is a registered agent?",
  "lead": "A registered agent is the person or company your LLC or corporation names to receive lawsuits and official state mail. Every state requires one. Here is what the role involves and how to choose one.",
  "sections": [
   ("The short answer", [
    "p:A registered agent is your company's official point of contact with the state. They accept service of process (notice of a lawsuit), subpoenas and official notices from the Secretary of State and state tax authorities, then pass them to you. Some states call it a resident agent, statutory agent or agent for service of process — it is the same role.",
   ]),
   ("What the law requires", [
    "ul:A physical street address in the state where your company is formed or registered — no P.O. Boxes|Someone available at that address during normal business hours|The agent's consent to serve|An agent for as long as the company exists, and in every state where it is registered",
   ]),
   ("Can you be your own registered agent?", [
    "p:Yes, if you live or have an office in the state and can be there during business hours. The trade-offs: your address goes on the public record, you have to be available every business day, and you cannot serve as agent in a state where you have no address. That is why non-residents, remote founders and anyone who values privacy use a <a href=\"/registered-agent/\">registered agent service</a>.",
   ]),
   ("What happens without a registered agent", [
    "ul:You can miss a lawsuit and have a default judgment entered against your company|You can miss state notices and annual report deadlines|The state can mark the company as not in good standing and eventually dissolve it",
   ]),
   ("Registered agent vs. business address", [
    "p:The registered agent receives legal papers. Your <a href=\"/virtual-business-address/\">business address</a> receives everything else — customer mail, bank letters and IRS correspondence — and is what you put on your website and invoices. Many companies use one provider for both.",
   ]),
   ("Registered agents by state", ["states:"]),
  ],
  "faqs": [
   ("What is a registered agent for an LLC?", "The person or company your LLC officially appoints to receive legal papers and state notices at a physical address in the state of formation during business hours."),
   ("Is a registered agent required?", "Yes. Every US state requires LLCs and corporations to maintain a registered agent."),
   ("Can I use my home address as the registered agent address?", "You can if you are your own agent and live in the state, but it becomes public record. A registered agent service keeps your home address private."),
   ("Is a registered agent the same as an owner?", "No. The registered agent only receives documents; it has no ownership or management rights in your company."),
  ],
  "related": ["registered-agent", "texas", "delaware", "florida", "wyoming"],
 },
 {
  "slug": "guides/usps-form-1583",
  "nav": "USPS Form 1583 guide",
  "title": "USPS Form 1583: How to Fill It Out & Verify Your ID",
  "desc": "What USPS Form 1583 is, who signs it, the two IDs you need, and how to verify in person, by live video or with a notary under the May 2024 rules.",
  "h1": "USPS Form 1583: how to complete it",
  "lead": "Before a virtual mailbox or virtual office can receive your mail, USPS requires Form 1583. It takes about ten minutes once you know what to prepare.",
  "sections": [
   ("What Form 1583 is", [
    "p:PS Form 1583, Application for Delivery of Mail Through Agent, authorises a Commercial Mail Receiving Agency (CMRA) — the company running your virtual address — to receive mail on your behalf. The CMRA keeps the signed form and files it with the Postal Service.",
   ]),
   ("Who needs to sign", [
    "ul:Every individual who will receive mail at the address|For a business, an authorised officer signs on behalf of the company and lists the business name|Each additional person receiving mail needs their own form",
   ]),
   ("Identification you need", [
    "p:You must present two acceptable forms of identification: a primary photo ID, such as a passport or driving licence, and a secondary ID such as a lease, insurance policy or vehicle registration. Use current documents that show exactly the same name as the form.",
   ]),
   ("How verification works (2024 rules)", [
    "p:Since USPS rules changed on May 1, 2024, you can confirm your signature and identity in one of these ways:",
    "ul:In person with your CMRA|Over a live audio-and-video call with an authorised CMRA employee|In front of a US notary public — including a remote online notary",
    "p:We prepare the form for you and arrange verification online, so you can complete it from anywhere in the world.",
   ]),
   ("Common mistakes", [
    "ul:Names that do not match exactly between the form and the IDs|Expired identification|Leaving out the business name when the mail is for a company|Forgetting a separate form for each additional recipient",
   ]),
  ],
  "faqs": [
   ("What is USPS Form 1583?", "It is the Postal Service form that authorises a commercial mail receiving agency, such as a virtual mailbox provider, to receive mail for you."),
   ("Does Form 1583 need to be notarized?", "Not necessarily. Since May 2024 you can verify in person or by live video with your provider, or have it notarized by a US notary, including online."),
   ("What ID do I need for Form 1583?", "Two acceptable forms of identification: a primary photo ID such as a passport, plus a secondary ID such as a lease or insurance policy."),
   ("Can I complete Form 1583 from outside the US?", "Yes. Verification by live video with the provider or by an online US notary works from anywhere."),
  ],
  "related": ["virtual-mailbox", "virtual-business-address", "us-llc-for-non-residents"],
 },
 {
  "slug": "guides/how-to-get-an-ein-for-an-llc",
  "nav": "How to get an EIN for an LLC",
  "title": "How to Get an EIN for an LLC (Including Without an SSN)",
  "desc": "How to apply for an EIN for your LLC: online with an SSN or ITIN, or by phone, fax or mail as a non-resident without one. IRS numbers, Form SS-4 tips and timelines.",
  "h1": "How to get an EIN for an LLC",
  "lead": "An Employer Identification Number (EIN) is your LLC's federal tax ID. You need it to open a US bank account, hire staff and file tax returns. Here is how to get one — with or without a Social Security Number.",
  "sections": [
   ("What you need first", [
    "ul:Your LLC must already be formed with the state|The legal name and address of the LLC — a <a href=\"/virtual-business-address/\">US business address</a> works for mailing|The responsible party: the owner who controls the LLC|An SSN or ITIN for the responsible party, if they have one",
   ]),
   ("If you have an SSN or ITIN: apply online", [
    "p:Use the IRS online EIN application. It is free and gives you the number immediately at the end of the session.",
   ]),
   ("If you have no SSN or ITIN: phone, fax or mail", [
    "p:The online application is not available if the responsible party has no SSN or ITIN, or if the business has no US principal office. Complete Form SS-4 and write \"Foreign\" on line 7b, then apply one of three ways:",
    "table:Method|Details|Typical time\nPhone (international applicants only)|+1 267-941-1099, Monday–Friday, 6 a.m.–11 p.m. Eastern (not toll-free)|EIN issued during the call\nFax|+1 304-707-9471 from outside the US, or 855-215-1627 from within the US; include your fax number|About 4 business days\nMail|Internal Revenue Service, Attn: EIN International Operation, Cincinnati, OH 45999|About 4 weeks",
   ]),
   ("Tips for Form SS-4", [
    "ul:Use the exact LLC name from your Articles of Organization|Line 7b: \"Foreign\" if the responsible party has no SSN/ITIN and is not eligible for one|Line 9a: a single-member LLC wholly owned by a foreign person that needs the EIN for Form 5472 ticks \"Other\" and writes \"Foreign-owned U.S. disregarded entity-Form 5472\"|Use a mailing address where you can reliably receive IRS letters",
   ]),
   ("After you get your EIN", [
    "p:Keep the IRS confirmation letter (CP 575): banks often ask for it. If it is mailed, a virtual mailbox lets you read it the day it arrives. Foreign-owned single-member LLCs should also plan for the annual Form 5472 filing — see <a href=\"/us-llc-for-non-residents/\">US LLC for non-residents</a>.",
   ]),
  ],
  "faqs": [
   ("Can I get an EIN without an SSN?", "Yes. Complete Form SS-4 with \"Foreign\" on line 7b and apply by phone (international applicants), fax or mail."),
   ("How long does it take to get an EIN as a non-resident?", "By phone you get it during the call; by fax in about four business days; by mail in about four weeks."),
   ("Is getting an EIN free?", "Yes. The IRS does not charge for an EIN."),
   ("Do I need an EIN for a single-member LLC?", "You need one to open a US bank account, hire employees or file Form 5472, so in practice almost every LLC gets one."),
  ],
  "related": ["us-llc-for-non-residents", "virtual-business-address", "guides/wyoming-vs-delaware-llc"],
 },
 {
  "slug": "guides/wyoming-vs-delaware-llc",
  "nav": "Wyoming vs. Delaware LLC",
  "title": "Wyoming vs. Delaware LLC: Costs, Privacy & Which to Choose",
  "desc": "Wyoming vs. Delaware LLC side by side: formation fees, annual cost ($60 vs. $400 from 2026), privacy, courts and which suits non-resident founders.",
  "h1": "Wyoming vs. Delaware LLC: which should you choose?",
  "lead": "Wyoming and Delaware are the two most popular states for founders who don't need to form where they live. The right choice depends mostly on whether you plan to raise venture capital.",
  "sections": [
   ("Side-by-side comparison", [
    "table:|Wyoming|Delaware\nLLC formation fee|$100|$110 (fees changed August 2026 — check the current schedule)\nAnnual LLC fee or tax|$60 minimum annual report fee|$400 annual tax from the 2026 tax year (was $300)\nAnnual deadline|First day of your anniversary month|June 1\nState income tax|None|No Delaware tax on income earned outside Delaware\nOwner names in public filings|Not required|Not required\nBusiness courts|Chancery Court for business cases since late 2021|Court of Chancery, long case-law history\nInvestor familiarity|Low|Very high",
   ]),
   ("Choose Wyoming if…", [
    "ul:You are a solo founder or small team without outside investors|You want the lowest ongoing cost|You run e-commerce, consulting, agency or SaaS revenue through the LLC",
    "p:<a href=\"/wyoming/\">Wyoming registered agent & address →</a>",
   ]),
   ("Choose Delaware if…", [
    "ul:You plan to raise venture capital or issue stock options (usually as a C-corporation)|Investors or an accelerator ask for Delaware|You expect complex ownership arrangements where predictable case law matters",
    "p:<a href=\"/delaware/\">Delaware registered agent & address →</a>",
   ]),
   ("Where you actually operate matters too", [
    "p:If you have staff, an office or inventory in another state, you will usually have to register there as a foreign LLC and pay that state's fees as well. For founders living outside the US with no US operations, that usually does not apply.",
   ]),
  ],
  "faqs": [
   ("Is Wyoming or Delaware cheaper for an LLC?", "Wyoming. Its annual fee starts at $60, while Delaware's LLC annual tax is $400 from the 2026 tax year."),
   ("Which state is better for raising venture capital?", "Delaware. Most venture investors expect a Delaware C-corporation."),
   ("Do Wyoming and Delaware publish LLC owners' names?", "Neither state requires member names in the public formation filing."),
   ("Can I switch from Wyoming to Delaware later?", "Yes. Both states allow domestication or conversion, so you can move the company if you later raise investment."),
  ],
  "related": ["wyoming", "delaware", "us-llc-for-non-residents", "guides/how-to-get-an-ein-for-an-llc"],
 },
]

# Homepage "Popular searches" hub — label: url
POPULAR = [
 ("Virtual office address", [
  ("Virtual business address for LLC", "/virtual-business-address/"),
  ("Virtual mailbox for business", "/virtual-mailbox/"),
  ("Virtual office in Wyoming", "/wyoming/"),
  ("Virtual office in Delaware", "/delaware/"),
  ("Virtual office in Miami, Florida", "/florida/"),
  ("Virtual office in Austin & Dallas, Texas", "/texas/"),
  ("Virtual office in San Francisco, California", "/california/"),
  ("Manhattan virtual office, New York", "/new-york/"),
 ]),
 ("Registered agent", [
  ("Registered agent for LLC", "/registered-agent/"),
  ("What is a registered agent?", "/guides/what-is-a-registered-agent/"),
  ("Wyoming registered agent", "/wyoming/"),
  ("Delaware registered agent", "/delaware/"),
  ("Texas registered agent", "/texas/"),
  ("Florida registered agent", "/florida/"),
  ("California registered agent", "/california/"),
  ("New York registered agent", "/new-york/"),
 ]),
 ("Company setup guides", [
  ("US LLC for non-residents", "/us-llc-for-non-residents/"),
  ("How to get an EIN for an LLC", "/guides/how-to-get-an-ein-for-an-llc/"),
  ("EIN without an SSN", "/guides/how-to-get-an-ein-for-an-llc/"),
  ("USPS Form 1583 guide", "/guides/usps-form-1583/"),
  ("Wyoming vs. Delaware LLC", "/guides/wyoming-vs-delaware-llc/"),
  ("Delaware LLC tax $400 (2026)", "/delaware/"),
  ("Texas franchise tax threshold", "/texas/"),
  ("New York LLC publication requirement", "/new-york/"),
 ]),
]
