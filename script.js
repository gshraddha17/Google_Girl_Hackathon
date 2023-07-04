const dashboardIcon = document.querySelector('.dashboard-icon');
const dashboard = document.getElementById('dashboard');
dashboardIcon.addEventListener('click', () => {
  dashboard.classList.toggle('hide');
});
document.addEventListener('click', (event) => {
  const target = event.target;
  if (!dashboard.contains(target) && !dashboardIcon.contains(target)) {
    dashboard.classList.add('hide');
  }
});

