/* 星洲药业 — interactions */
(function () {
  'use strict';

  var header = document.getElementById('header');
  var burger = document.getElementById('burger');
  var nav = document.getElementById('nav');
  var form = document.getElementById('inquiry');
  var success = document.getElementById('formSuccess');
  var year = document.getElementById('year');

  /* ---------- sticky header ---------- */
  var onScroll = function () {
    if (window.scrollY > 16) { header.classList.add('is-scrolled'); }
    else { header.classList.remove('is-scrolled'); }
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* ---------- mobile nav ---------- */
  var setMenu = function (open) {
    if (!burger || !nav) return;
    nav.classList.toggle('is-open', open);
    burger.classList.toggle('is-open', open);
    burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    burger.setAttribute('aria-label', open ? '关闭菜单' : '打开菜单');
    document.body.style.overflow = open ? 'hidden' : '';
  };

  if (burger && nav) {
    burger.addEventListener('click', function () {
      setMenu(!nav.classList.contains('is-open'));
    });
    nav.addEventListener('click', function (e) {
      if (e.target.closest('a')) setMenu(false);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') setMenu(false);
    });
    window.addEventListener('resize', function () {
      if (window.innerWidth > 900) setMenu(false);
    });
  }

  /* ---------- reveal on scroll ---------- */
  var items = document.querySelectorAll('[data-reveal]');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-in');
          io.unobserve(entry.target);
        }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.12 });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add('is-in'); });
  }

  /* ---------- inquiry form ---------- */
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.checkValidity()) {
        form.reportValidity();
        return;
      }
      var btn = form.querySelector('button[type="submit"]');
      if (btn) {
        btn.textContent = '提交中…';
        btn.disabled = true;
      }
      window.setTimeout(function () {
        form.classList.add('is-sent');
        if (success) {
          success.hidden = false;
          success.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
        }
      }, 420);
    });
  }

  /* ---------- footer year ---------- */
  if (year) { year.textContent = String(new Date().getFullYear()); }
})();
