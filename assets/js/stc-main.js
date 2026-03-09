/**
 * Sahiwal Tech Community - Main JavaScript
 * Version: 1.0
 */

(function($) {
  'use strict';

  const STC = {
    // Initialize all functions
    init: function() {
      this.preloader();
      this.scrollTop();
      this.mobileMenu();
      this.smoothScroll();
      this.dynamicYear();
      this.animationOnScroll();
      this.enhancedAnimations();
      this.statCounters();
      this.intersectionObserver();
    },

    // Preloader
    preloader: function() {
      const preloader = $('#stc__preloader');
      if (preloader.length) {
        $(window).on('load', function() {
          preloader.addClass('hide');
          setTimeout(function() {
            preloader.remove();
          }, 300);
        });
      }
    },

    // Scroll To Top
    scrollTop: function() {
      const scrollTopBtn = $('.stc__scroll-top');

      if (scrollTopBtn.length) {
        $(window).on('scroll', function() {
          if ($(this).scrollTop() > 300) {
            scrollTopBtn.addClass('show');
          } else {
            scrollTopBtn.removeClass('show');
          }
        });

        scrollTopBtn.on('click', function(e) {
          e.preventDefault();
          $('html, body').animate({
            scrollTop: 0
          }, 600);
        });
      }
    },

    // Mobile Menu
    mobileMenu: function() {
      const menuToggle = $('.stc__mobile-menu-toggle');
      const mobileMenu = $('.stc__mobile-menu');
      const body = $('body');

      if (menuToggle.length) {
        menuToggle.on('click', function(e) {
          e.preventDefault();
          mobileMenu.toggleClass('active');
          body.toggleClass('stc__menu-open');
          $(this).toggleClass('active');
        });

        // Close menu on link click
        $('.stc__mobile-menu a').on('click', function() {
          mobileMenu.removeClass('active');
          body.removeClass('stc__menu-open');
          menuToggle.removeClass('active');
        });

        // Close menu on outside click
        $(document).on('click', function(e) {
          if (!$(e.target).closest('.stc__mobile-menu, .stc__mobile-menu-toggle').length) {
            mobileMenu.removeClass('active');
            body.removeClass('stc__menu-open');
            menuToggle.removeClass('active');
          }
        });
      }
    },

    // Smooth Scroll
    smoothScroll: function() {
      $('a[href*="#"]:not([href="#"])').on('click', function() {
        const target = $(this.hash);
        if (target.length) {
          $('html, body').animate({
            scrollTop: target.offset().top - 80
          }, 800);
          return false;
        }
      });
    },

    // Dynamic Year for Copyright
    dynamicYear: function() {
      const yearElements = $('#current-year, .stc__current-year, #stc__year');
      if (yearElements.length) {
        yearElements.text(new Date().getFullYear());
      }
    },

    // Animation on Scroll (using WOW.js if available)
    animationOnScroll: function() {
      if (typeof WOW !== 'undefined') {
        new WOW().init();
      }
    },

    // Enhanced Animations
    enhancedAnimations: function() {
      // Add fade-in animation to pillar cards on scroll
      const pillarCards = $('.stc__pillar-enhanced');
      if (pillarCards.length) {
        pillarCards.each(function(index) {
          $(this).css('animation-delay', (index * 0.1) + 's');
        });
      }

      // Add hover effect for benefit cards
      const benefitCards = $('.stc__benefit-enhanced');
      if (benefitCards.length) {
        benefitCards.on('mouseenter', function() {
          $(this).find('.stc__benefit-icon').css('transform', 'scale(1.1) rotate(5deg)');
        }).on('mouseleave', function() {
          $(this).find('.stc__benefit-icon').css('transform', 'scale(1) rotate(0deg)');
        });
      }
    },

    // Animated Stat Counters
    statCounters: function() {
      const stats = $('.stc__stat-animated, .stc__impact-stat-animated');
      let counted = false;

      const startCounting = function() {
        stats.each(function() {
          const $this = $(this);
          const target = $this.data('count') || 0;
          const $numberEl = $this.find('.stc__stat-number, .stc__impact-number');

          if ($numberEl.length && target > 0) {
            $({ countNum: 0 }).animate({
              countNum: target
            }, {
              duration: 2000,
              easing: 'swing',
              step: function() {
                $numberEl.text(Math.floor(this.countNum).toLocaleString() + '+');
              },
              complete: function() {
                $numberEl.text(target.toLocaleString() + '+');
              }
            });
          }
        });
      };

      // Start counting when impact section is visible
      const impactSection = $('.stc__impact');
      if (impactSection.length) {
        $(window).on('scroll', function() {
          if (!counted && $(window).scrollTop() > impactSection.offset().top - $(window).height() + 100) {
            startCounting();
            counted = true;
          }
        });
      }
    },

    // Intersection Observer for scroll animations
    intersectionObserver: function() {
      // Check if IntersectionObserver is supported
      if (!('IntersectionObserver' in window)) {
        return;
      }

      const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
      };

      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('stc__animate-fadeInUp');
            observer.unobserve(entry.target);
          }
        });
      }, observerOptions);

      // Observe elements
      $('.stc__pillar-card, .stc__benefit-card, .stc__impact-stat, .stc__partner-item').each(function() {
        observer.observe(this);
      });
    }
  };

  // Document Ready
  $(document).ready(function() {
    STC.init();
  });

})(jQuery);
