/* ==========================================================================
   Gemalyn Cabanos — Personal Portfolio Website
   Main JavaScript
   ========================================================================== */

(function() {
  'use strict';

  // --------------------------------------------------------------------------
  // DOM Elements
  // --------------------------------------------------------------------------
  const navToggle = document.querySelector('.nav__toggle');
  const navList = document.querySelector('.nav__list');
  const navLinks = document.querySelectorAll('.nav__link');
  const header = document.querySelector('.header');
  const yearEl = document.getElementById('year');

  // --------------------------------------------------------------------------
  // Initialize
  // --------------------------------------------------------------------------
  function init() {
    setCurrentYear();
    initMobileNav();
    initScrollHeader();
    initSmoothScroll();
    initScrollAnimations();
  }

  // --------------------------------------------------------------------------
  // Set current year in footer
  // --------------------------------------------------------------------------
  function setCurrentYear() {
    if (yearEl) {
      yearEl.textContent = new Date().getFullYear();
    }
  }

  // --------------------------------------------------------------------------
  // Mobile Navigation Toggle
  // --------------------------------------------------------------------------
  function initMobileNav() {
    if (!navToggle || !navList) return;

    navToggle.addEventListener('click', toggleMobileNav);

    // Close mobile nav when clicking a link
    navLinks.forEach(link => {
      link.addEventListener('click', closeMobileNav);
    });

    // Close mobile nav when clicking outside
    document.addEventListener('click', (e) => {
      if (navList.classList.contains('nav__list--open') &&
          !navList.contains(e.target) &&
          !navToggle.contains(e.target)) {
        closeMobileNav();
      }
    });

    // Close mobile nav on Escape key
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && navList.classList.contains('nav__list--open')) {
        closeMobileNav();
        navToggle.focus();
      }
    });
  }

  function toggleMobileNav() {
    const isOpen = navList.classList.toggle('nav__list--open');
    navToggle.setAttribute('aria-expanded', isOpen);
    // Allow page scroll even when menu is open (better UX)
  }

  function closeMobileNav() {
    navList.classList.remove('nav__list--open');
    navToggle.setAttribute('aria-expanded', 'false');
  }

  // --------------------------------------------------------------------------
  // Header scroll effect
  // --------------------------------------------------------------------------
  function initScrollHeader() {
    if (!header) return;

    let lastScrollY = window.scrollY;
    let ticking = false;

    function updateHeader() {
      const scrollY = window.scrollY;

      if (scrollY > 100) {
        header.classList.add('header--scrolled');
      } else {
        header.classList.remove('header--scrolled');
      }

      // Hide/show header on scroll (optional)
      // if (scrollY > lastScrollY && scrollY > 200) {
      //   header.classList.add('header--hidden');
      // } else {
      //   header.classList.remove('header--hidden');
      // }

      lastScrollY = scrollY;
      ticking = false;
    }

    window.addEventListener('scroll', () => {
      if (!ticking) {
        window.requestAnimationFrame(updateHeader);
        ticking = true;
      }
    }, { passive: true });
  }

  // --------------------------------------------------------------------------
  // Smooth scroll for anchor links (fallback for browsers without CSS scroll-behavior)
  // --------------------------------------------------------------------------
  function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function(e) {
        const targetId = this.getAttribute('href');
        if (targetId === '#') return;

        const target = document.querySelector(targetId);
        if (target) {
          e.preventDefault();
          const headerHeight = header ? header.offsetHeight : 0;
          const targetPosition = target.getBoundingClientRect().top + window.scrollY - headerHeight;

          window.scrollTo({
            top: targetPosition,
            behavior: 'smooth'
          });

          // Update URL without jumping
          history.pushState(null, '', targetId);
        }
      });
    });
  }

  // --------------------------------------------------------------------------
  // Scroll-triggered animations (Intersection Observer)
  // --------------------------------------------------------------------------
  function initScrollAnimations() {
    // Check if user prefers reduced motion
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (prefersReducedMotion) {
      // Show all animated elements immediately
      document.querySelectorAll('.animate-fade-in-up').forEach(el => {
        el.style.opacity = '1';
        el.style.transform = 'none';
      });
      return;
    }

    const animatedElements = document.querySelectorAll(
      '.section__header, .about__text, .card, .skills__group, .timeline__item, .education__column, .contact__link'
    );

    if (!animatedElements.length) return;

    const observerOptions = {
      root: null,
      rootMargin: '0px 0px -10% 0px',
      threshold: 0.1
    };

    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry, index) => {
        if (entry.isIntersecting) {
          // Add staggered animation delay
          entry.target.style.animationDelay = `${index * 100}ms`;
          entry.target.classList.add('animate-fade-in-up');
          observer.unobserve(entry.target);
        }
      });
    }, observerOptions);

    animatedElements.forEach(el => observer.observe(el));
  }

  // --------------------------------------------------------------------------
  // Initialize when DOM is ready
  // --------------------------------------------------------------------------
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();