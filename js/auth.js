/* ==========================================================================
   EventCraft - Client & Admin Authentication Flow
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  initAuthTabs();
  initAuthForms();
  initDemoAccountFillers();
});

/* Tab Switching (Sign In / Sign Up) */
function initAuthTabs() {
  const tabBtns = document.querySelectorAll('.auth-tab-btn');
  const forms = document.querySelectorAll('.auth-form');

  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const targetTab = btn.getAttribute('data-tab');

      tabBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      forms.forEach(form => {
        if (form.id === `${targetTab}-form`) {
          form.style.display = 'block';
          gsap.fromTo(form, { opacity: 0, y: 15 }, { opacity: 1, y: 0, duration: 0.4 });
        } else {
          form.style.display = 'none';
        }
      });
    });
  });
}

/* Auth Forms Submission Handler */
function initAuthForms() {
  const signupForm = document.getElementById('signup-form');
  const signinForm = document.getElementById('signin-form');

  // Sign Up Logic
  signupForm?.addEventListener('submit', (e) => {
    e.preventDefault();
    const name = document.getElementById('signup-name')?.value || 'Guest User';
    const email = document.getElementById('signup-email')?.value || 'client@eventcraft.com';
    const role = document.getElementById('signup-role')?.value || 'client';

    // Store user data in localStorage
    const users = JSON.parse(localStorage.getItem('eventcraft_users') || '[]');
    users.push({ name, email, role });
    localStorage.setItem('eventcraft_users', JSON.stringify(users));

    // Auto fill sign in email & switch tab to Sign In
    const signinEmailInput = document.getElementById('signin-email');
    if (signinEmailInput) {
      signinEmailInput.value = email;
    }

    const signinTabBtn = document.querySelector('[data-tab="signin"]');
    signinTabBtn?.click();
  });

  // Sign In Logic
  signinForm?.addEventListener('submit', (e) => {
    e.preventDefault();
    const email = document.getElementById('signin-email')?.value || 'user@stackly.com';
    const selectedRole = document.getElementById('signin-role')?.value || 'client';

    let role = selectedRole;

    localStorage.setItem('currentUserEmail', email);
    localStorage.setItem('currentUserRole', role);

    if (role === 'admin') {
      window.location.href = 'admin-dashboard.html';
    } else {
      window.location.href = 'client-dashboard.html';
    }
  });
}

function initDemoAccountFillers() {
  // Demo fillers retired in favor of Role select dropdown
}
