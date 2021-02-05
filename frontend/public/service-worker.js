
workbox.setConfig({ debug: false });
workbox.precaching.precacheAndRoute([]);

// CSS
workbox.routing.registerRoute(
    new RegExp('\.css$'),
    workbox.strategies.cacheFirst({
        cacheName: 'style',
        plugins: [
            new workbox.expiration.Plugin({
                maxAgeSeconds: 60 * 60 * 24,
                maxEntries: 20,
                purgeOnQuotaError: true
            })
        ]
    })
);

workbox.routing.registerRoute(
  /\.(?:png|gif|jpg|jpeg|svg)$/,
  workbox.strategies.staleWhileRevalidate({
    cacheName: 'images',
    plugins: [
      new workbox.expiration.Plugin({
        maxEntries: 60,
        maxAgeSeconds: 30 * 24,
      }),
    ],
  }),
);

workbox.routing.registerRoute(
    new RegExp('/v1/origins/'),
    workbox.strategies.staleWhileRevalidate({
        cacheName: 'origins',
        cacheExpiration: {
            maxAgeSeconds: 60 * 30
        }
    })
);

workbox.routing.registerRoute(
  new RegExp('https://fonts.(?:googleapis|gstatic).com/(.*)'),
  workbox.strategies.cacheFirst({
    cacheName: 'google_fonts',
    plugins: [
      new workbox.expiration.Plugin({
        maxEntries: 30,
      }),
    ],
  }),
);
