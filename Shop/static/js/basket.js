document.addEventListener('DOMContentLoaded', function() {
    const basketIcon = document.getElementById('basket-icon');
    const dropdown = document.getElementById('basket-dropdown');
    if (basketIcon && dropdown) {
        basketIcon.addEventListener('click', function(e) {
            e.stopPropagation();
            dropdown.style.display = dropdown.style.display === 'none' ? 'block' : 'none';
        });
        document.addEventListener('click', function() {
            dropdown.style.display = 'none';
        });
    }
});