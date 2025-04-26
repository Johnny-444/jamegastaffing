// Initialize tooltips
document.addEventListener('DOMContentLoaded', function() {
  // Enable Bootstrap tooltips
  var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
  var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl)
  });

  // Smooth scrolling for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      
      const targetId = this.getAttribute('href');
      if (targetId === '#') return;
      
      const targetElement = document.querySelector(targetId);
      if (targetElement) {
        targetElement.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    });
  });

  // Add active class to nav items based on current page
  const currentLocation = window.location.pathname;
  const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
  
  navLinks.forEach(link => {
    const linkPath = link.getAttribute('href');
    if (linkPath === currentLocation) {
      link.classList.add('active');
    }
  });

  // Add animation class to elements when they come into view
  const animateFadeIn = () => {
    const elements = document.querySelectorAll('.feature-box, .industry-card, .value-card, .approach-card, .contact-info-card');
    
    elements.forEach(element => {
      const elementPosition = element.getBoundingClientRect().top;
      const windowHeight = window.innerHeight;
      
      if (elementPosition < windowHeight - 100) {
        element.classList.add('fadeIn');
      }
    });
  };

  // Run animation on page load and scroll
  animateFadeIn();
  window.addEventListener('scroll', animateFadeIn);

  // Form validation visual feedback
  const forms = document.querySelectorAll('form');
  
  forms.forEach(form => {
    const inputs = form.querySelectorAll('input, textarea, select');
    
    inputs.forEach(input => {
      input.addEventListener('blur', function() {
        if (this.value.trim() === '' && this.hasAttribute('required')) {
          this.classList.add('is-invalid');
        } else {
          this.classList.remove('is-invalid');
        }
        
        // Email validation
        if (this.type === 'email' && this.value.trim() !== '') {
          const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
          if (!emailRegex.test(this.value.trim())) {
            this.classList.add('is-invalid');
          } else {
            this.classList.remove('is-invalid');
          }
        }
      });
    });
  });
});
