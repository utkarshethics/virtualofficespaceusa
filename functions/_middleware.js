/**
 * Cloudflare Pages middleware: edge HTML enhancement for virtualofficespaceusa.online
 *
 * Only rewrites successful HTML responses:
 *  - loads /assets/enhance.js (smooth scroll, scroll reveal, microinteractions,
 *    exit-intent popup) with this site's settings
 *  - lazy-loads images below the first two, adds async decoding
 * Assets, redirects and everything else pass through untouched.
 */

const ENHANCE_SETTINGS = {
  exitIntent: {
    title: 'Get your US address today',
    text: 'Real commercial street address, registered agent and same-day mail scanning. Plans from $19/mo.',
    ctaText: 'Chat with us on WhatsApp',
    ctaHref: 'https://wa.me/919244240917?text=' + encodeURIComponent("Hi, I'm interested in a US virtual office")
  },
  language: { enabled: false }
};

const ENHANCE_TAGS =
  `<script>window.SITE_ENHANCE=${JSON.stringify(ENHANCE_SETTINGS)};</script>` +
  '<script src="/assets/enhance.js" defer></script>';

export async function onRequest(context) {
  const response = await context.next();
  const type = response.headers.get('content-type') || '';
  if (response.status !== 200 || !type.includes('text/html')) return response;

  let imgCount = 0;
  return new HTMLRewriter()
    .on('img', {
      element(el) {
        imgCount += 1;
        if (!el.getAttribute('decoding')) el.setAttribute('decoding', 'async');
        if (imgCount > 2 && !el.getAttribute('loading')) el.setAttribute('loading', 'lazy');
      }
    })
    .on('body', { element(el) { el.append(ENHANCE_TAGS, { html: true }); } })
    .transform(response);
}
