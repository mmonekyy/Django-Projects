document.addEventListener('DOMContentLoaded', function() {
    const p = document.querySelector('p#text-muted');
    if (p) {
        const year = new Date().getFullYear();
        p.innerHTML = `&copy; ${year}. All rights reserved.`;
    }
});