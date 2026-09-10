/* ==========================================================================
   EventCraft - Client & Admin Dashboard Logic
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  initPreloader();
  initSidebarToggle();
  displayUserSessionInfo();
  initLogoutHandler();
  initAdminRevenueChart();
  initAdminTableActions();
  initClientInteractions();
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

/* Dashboard Mobile Sidebar Navigation Toggle */
function initSidebarToggle() {
  const sidebar = document.getElementById('sidebar');
  const toggleBtns = document.querySelectorAll('.sidebar-toggle');

  toggleBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.stopPropagation();
      sidebar?.classList.toggle('active');
    });
  });

  // Close sidebar when clicking links inside sidebar on mobile
  sidebar?.querySelectorAll('.sidebar-link').forEach(link => {
    link.addEventListener('click', () => {
      if (window.innerWidth <= 1024) {
        sidebar.classList.remove('active');
      }
    });
  });

  // Close sidebar when clicking outside on mobile
  document.addEventListener('click', (e) => {
    if (window.innerWidth <= 1024 && sidebar?.classList.contains('active')) {
      if (!sidebar.contains(e.target) && !e.target.closest('.sidebar-toggle')) {
        sidebar.classList.remove('active');
      }
    }
  });
}

/* Retrieve and Render Current Email ID in Dashboards */
function displayUserSessionInfo() {
  const currentEmail = localStorage.getItem('currentUserEmail') || 'client@eventcraft.com';
  const currentRole = localStorage.getItem('currentUserRole') || 'client';

  const userEmailBadges = document.querySelectorAll('.display-user-email');
  userEmailBadges.forEach(badge => {
    badge.innerText = currentEmail;
  });

  const userRoleBadges = document.querySelectorAll('.display-user-role');
  userRoleBadges.forEach(badge => {
    badge.innerText = currentRole.toUpperCase();
  });
}

/* Logout functionality */
function initLogoutHandler() {
  const logoutBtns = document.querySelectorAll('.logout-btn');
  logoutBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      localStorage.removeItem('currentUserEmail');
      localStorage.removeItem('currentUserRole');
      window.location.href = 'auth.html';
    });
  });
}

/* Admin Revenue Analytics Canvas Chart */
function initAdminRevenueChart() {
  const canvas = document.getElementById('revenueChart');
  if (!canvas) return;

  const ctx = canvas.getContext('2d');
  if (!ctx) return;

  // Simple, elegant HTML5 canvas bar/line graph
  const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug'];
  const revenues = [45, 62, 85, 95, 110, 140, 165, 190]; // in thousands $

  const width = canvas.width = canvas.parentElement.clientWidth;
  const height = canvas.height = 240;

  ctx.clearRect(0, 0, width, height);

  const padding = 40;
  const graphWidth = width - (padding * 2);
  const graphHeight = height - (padding * 2);

  const maxVal = 220;

  // Draw Grid Lines
  ctx.strokeStyle = 'rgba(255, 255, 255, 0.08)';
  ctx.lineWidth = 1;
  for (let i = 0; i <= 4; i++) {
    const y = padding + (graphHeight / 4) * i;
    ctx.beginPath();
    ctx.moveTo(padding, y);
    ctx.lineTo(width - padding, y);
    ctx.stroke();
  }

  // Draw Gradient Bars & Trend Line
  const barWidth = graphWidth / months.length - 20;

  months.forEach((month, index) => {
    const x = padding + index * (graphWidth / months.length) + 10;
    const barH = (revenues[index] / maxVal) * graphHeight;
    const y = height - padding - barH;

    // Bar gradient
    const grad = ctx.createLinearGradient(0, y, 0, height - padding);
    grad.addColorStop(0, '#6366f1');
    grad.addColorStop(1, 'rgba(99, 102, 241, 0.1)');

    ctx.fillStyle = grad;
    ctx.beginPath();
    ctx.roundRect(x, y, barWidth, barH, [6, 6, 0, 0]);
    ctx.fill();

    // Month Label
    ctx.fillStyle = '#94a3b8';
    ctx.font = '12px "Plus Jakarta Sans", sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText(month, x + barWidth / 2, height - 15);

    // Value Label
    ctx.fillStyle = '#d4af37';
    ctx.fillText(`$${revenues[index]}k`, x + barWidth / 2, y - 8);
  });

  window.addEventListener('resize', () => {
    clearTimeout(window.chartResizeTimer);
    window.chartResizeTimer = setTimeout(initAdminRevenueChart, 200);
  });
}

/* Admin Event Approval & Rejection Handlers */
function initAdminTableActions() {
  const table = document.querySelector('.data-table');
  if (!table) return;

  table.addEventListener('click', (e) => {
    const target = e.target;
    if (target.classList.contains('action-approve')) {
      const row = target.closest('tr');
      const statusBadge = row.querySelector('.status-tag');
      if (statusBadge) {
        statusBadge.className = 'status-tag status-confirmed';
        statusBadge.innerText = 'APPROVED';
      }
    } else if (target.classList.contains('action-reject')) {
      const row = target.closest('tr');
      const statusBadge = row.querySelector('.status-tag');
      if (statusBadge) {
        statusBadge.className = 'status-tag status-pending';
        statusBadge.innerText = 'REJECTED';
      }
    }
  });
}

/* Client Dashboard Dynamic Tools */
function initClientInteractions() {
  const rsvpBtn = document.getElementById('btn-add-rsvp');
  const rsvpCountEl = document.getElementById('client-rsvp-count');

  if (rsvpBtn && rsvpCountEl) {
    rsvpBtn.addEventListener('click', () => {
      let count = parseInt(rsvpCountEl.innerText || '120', 10);
      count += 1;
      rsvpCountEl.innerText = count;
    });
  }
}
