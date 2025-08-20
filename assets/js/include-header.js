// Lightweight header include for static GitHub Pages
// Usage in HTML: <div data-include-header></div>
(function () {
  function setActiveLink(container) {
    try {
      var path = window.location.pathname.replace(/index\.html$/, '/');
      var links = container.querySelectorAll('#nav a');
      links.forEach(function (a) {
        var href = a.getAttribute('href');
        // Normalize to leading slash for site-relative links
        if (href && href.startsWith('http')) return;
        var normalized = href.startsWith('/') ? href : '/' + href;
        if (normalized === '/' && (path === '/' || path === '')) {
          a.classList.add('active');
        } else if (normalized !== '/' && path.startsWith(normalized)) {
          a.classList.add('active');
        }
      });
    } catch (e) {}
  }

  function includeHeader() {
    var target = document.querySelector('[data-include-header]');
    if (!target) return;
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/partials/header.html');
    xhr.onload = function () {
      if (xhr.status >= 200 && xhr.status < 300) {
        target.outerHTML = xhr.responseText;
        // After inject, set active state
        var header = document.getElementById('header');
        if (header) setActiveLink(header);
      }
    };
    xhr.send();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', includeHeader);
  } else {
    includeHeader();
  }
})();


