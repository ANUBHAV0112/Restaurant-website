// aos.js
document.addEventListener('DOMContentLoaded', function () {
  AOS.init({
    duration: 1000,         // Animation duration in ms
    easing: 'ease-in-out',  // Easing function
    offset: 150,            // Offset from the original trigger point
    once: true,             // Whether animation should happen only once
    mirror: false           // Whether elements should animate out while scrolling past them
  });
});
