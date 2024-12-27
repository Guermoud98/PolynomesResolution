const { createProxyMiddleware } = require('http-proxy-middleware');

const BASE_URL = 'http://localhost:8081';

module.exports = function(app) {
  app.use(
    '/polynomes',
    createProxyMiddleware({
      target: BASE_URL,
      changeOrigin: true,
    })
  );

  app.use(
    '/racines',
    createProxyMiddleware({
      target: BASE_URL,
      changeOrigin: true,
    })
  );

  app.use(
    '/api/factorisation',
    createProxyMiddleware({
      target: BASE_URL,
      changeOrigin: true,
    })
  );
};