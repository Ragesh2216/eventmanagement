/* ==========================================================================
   EventCraft - Main Client JavaScript & GSAP Animations
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  initPreloader();
  initNavbar();
  initGSAPAnimations();
  initCostCalculator();
  initFilterTabs();
  initAccordions();
  initModals();
});

/* Preloader Hide Timer (1.5 Seconds) */
function initPreloader() {
  const preloader = document.getElementById('preloader');
  if (preloader) {
    setTimeout(() => {
      preloader.classList.add('fade-out');
    }, 1500);
  }
}

/* Navbar Scroll & Mobile Toggle */
function initNavbar() {
  const navbar = document.querySelector('.navbar');
  const toggle = document.querySelector('.mobile-toggle');
  const navLinks = document.querySelector('.nav-links');

  window.addEventListener('scroll', () => {
    if (window.scrollY > 40) {
      navbar?.classList.add('scrolled');
    } else {
      navbar?.classList.remove('scrolled');
    }
  });

  if (toggle && navLinks) {
    toggle.addEventListener('click', () => {
      navLinks.classList.toggle('active');
      const icon = toggle.querySelector('i');
      if (icon) {
        icon.className = navLinks.classList.contains('active') ? 'fas fa-times' : 'fas fa-bars';
      }
    });

    // Close menu when clicking links or buttons inside nav drawer
    navLinks.querySelectorAll('a, button').forEach(clickable => {
      clickable.addEventListener('click', () => {
        navLinks.classList.remove('active');
        const icon = toggle.querySelector('i');
        if (icon) icon.className = 'fas fa-bars';
      });
    });
  }
}

/* GSAP Animations & ScrollTrigger */
function initGSAPAnimations() {
  if (typeof gsap === 'undefined') return;

  // Hero animations
  gsap.from('.hero-content h1', {
    duration: 1,
    y: 50,
    opacity: 0,
    ease: 'power3.out',
    delay: 0.2
  });

  gsap.from('.hero-content p', {
    duration: 1,
    y: 30,
    opacity: 0,
    ease: 'power3.out',
    delay: 0.4
  });

  gsap.from('.hero-btns', {
    duration: 1,
    y: 30,
    opacity: 0,
    ease: 'power3.out',
    delay: 0.6
  });

  gsap.from('.hero-media', {
    duration: 1.2,
    scale: 0.9,
    opacity: 0,
    ease: 'power2.out',
    delay: 0.5
  });

  // Floating badges continuous hover animation
  gsap.to('.floating-badge', {
    y: -10,
    duration: 2.5,
    repeat: -1,
    yoyo: true,
    ease: 'sine.inOut',
    stagger: 0.5
  });

  // Animated Numbers Counter Trigger
  const statNumbers = document.querySelectorAll('.stat-number');
  if (statNumbers.length > 0 && typeof ScrollTrigger !== 'undefined') {
    statNumbers.forEach(stat => {
      const targetVal = parseFloat(stat.getAttribute('data-target') || '0');
      const suffix = stat.getAttribute('data-suffix') || '';
      const prefix = stat.getAttribute('data-prefix') || '';

      gsap.to(stat, {
        scrollTrigger: {
          trigger: stat,
          start: 'top 85%'
        },
        duration: 2,
        innerText: targetVal,
        snap: { innerText: 1 },
        onUpdate: function () {
          stat.innerText = prefix + Math.ceil(this.targets()[0].innerText) + suffix;
        }
      });
    });
  }

  // ScrollReveal Cards Stagger
  if (typeof ScrollTrigger !== 'undefined') {
    gsap.utils.toArray('.glass-card, .event-card, .timeline-item').forEach(el => {
      gsap.from(el, {
        scrollTrigger: {
          trigger: el,
          start: 'top 88%',
          toggleActions: 'play none none none'
        },
        y: 40,
        opacity: 0,
        duration: 0.8,
        ease: 'power2.out'
      });
    });
  }
}

/* Event Cost Calculator Widget */
function initCostCalculator() {
  const eventTypeSelect = document.getElementById('calc-event-type');
  const guestsInput = document.getElementById('calc-guests');
  const venueTierSelect = document.getElementById('calc-venue');
  const cateringSelect = document.getElementById('calc-catering');
  const resultDisplay = document.getElementById('calc-total-price');

  if (!resultDisplay) return;

  function calculateCost() {
    const baseRates = {
      corporate: 5000,
      wedding: 8000,
      concert: 12000,
      gala: 7000,
      launch: 6000
    };

    const venueMultipliers = {
      standard: 1.0,
      premium: 1.5,
      luxury: 2.2
    };

    const cateringPerHead = {
      standard: 45,
      gourmet: 95,
      michelin: 185
    };

    const type = eventTypeSelect?.value || 'corporate';
    const guests = parseInt(guestsInput?.value || '100', 10);
    const venue = venueTierSelect?.value || 'standard';
    const catering = cateringSelect?.value || 'standard';

    const base = baseRates[type] || 5000;
    const venueMult = venueMultipliers[venue] || 1.0;
    const cateringTotal = (cateringPerHead[catering] || 45) * guests;

    const total = Math.round((base * venueMult) + cateringTotal);

    // Animate price count up
    let currentVal = parseInt(resultDisplay.innerText.replace(/[^0-9]/g, '') || '0', 10);
    gsap.to({ val: currentVal }, {
      val: total,
      duration: 0.8,
      onUpdate: function () {
        resultDisplay.innerText = '$' + Math.ceil(this.targets()[0].val).toLocaleString();
      }
    });
  }

  [eventTypeSelect, guestsInput, venueTierSelect, cateringSelect].forEach(element => {
    element?.addEventListener('change', calculateCost);
    element?.addEventListener('input', calculateCost);
  });

  calculateCost();
}

/* Filter Cards Grid */
function initFilterTabs() {
  const filterBtns = document.querySelectorAll('.filter-btn');
  const filterCards = document.querySelectorAll('[data-category]');

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const cat = btn.getAttribute('data-filter');

      filterCards.forEach(card => {
        const cardCat = card.getAttribute('data-category');
        if (cat === 'all' || cardCat === cat) {
          card.style.display = 'block';
          gsap.fromTo(card, { opacity: 0, scale: 0.95 }, { opacity: 1, scale: 1, duration: 0.4 });
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
}

/* Accordion Component */
function initAccordions() {
  const accordionHeaders = document.querySelectorAll('.accordion-header');
  accordionHeaders.forEach(header => {
    header.addEventListener('click', () => {
      const item = header.parentElement;
      const isOpen = item.classList.contains('active');

      document.querySelectorAll('.accordion-item').forEach(i => i.classList.remove('active'));

      if (!isOpen) {
        item.classList.add('active');
      }
    });
  });
}

/* Modal Windows & Quick Toast Alerts */
function initModals() {
  const modalOverlays = document.querySelectorAll('.modal-overlay');
  const modalCloses = document.querySelectorAll('.modal-close');
  const modalTriggers = document.querySelectorAll('[data-modal-target]');

  modalTriggers.forEach(trigger => {
    trigger.addEventListener('click', (e) => {
      e.preventDefault();
      const targetId = trigger.getAttribute('data-modal-target');
      const targetModal = document.getElementById(targetId);
      if (targetModal) {
        targetModal.classList.add('active');
      }
    });
  });

  modalCloses.forEach(closeBtn => {
    closeBtn.addEventListener('click', () => {
      closeBtn.closest('.modal-overlay')?.classList.remove('active');
    });
  });

  modalOverlays.forEach(overlay => {
    overlay.addEventListener('click', (e) => {
      if (e.target === overlay) {
        overlay.classList.remove('active');
      }
    });
  });
}

/* Global Form Validation & Redirection to 404 Page (Except Auth Forms) */
function initGlobalFormValidation() {
  document.querySelectorAll('form').forEach(form => {
    if (form.id === 'signin-form' || form.id === 'signup-form') return;

    form.addEventListener('submit', (e) => {
      e.preventDefault();
      if (form.checkValidity()) {
        window.location.href = '404.html';
      } else {
        form.reportValidity();
      }
    });
  });
}

// Ensure initGlobalFormValidation runs on load
document.addEventListener('DOMContentLoaded', () => {
  initGlobalFormValidation();
});

// Toast disabled - popups removed
window.showToast = function () {
  // Pop-up messages removed as requested
};
