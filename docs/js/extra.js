// Function to make embedded links open new tab when clicked
document.addEventListener('DOMContentLoaded', function() {
    // Select all anchor tags with href starting with "http"
    const externalLinks = document.querySelectorAll('a[href^="http"]:not([target="_blank"])');
    
    externalLinks.forEach(function(link) {
        link.setAttribute('target', '_blank'); 
        link.setAttribute('rel', 'noopener noreferrer');
    });
});