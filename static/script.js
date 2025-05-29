/* static/script.js */

// Create Dark Mode button and add to page
const toggleBtn = document.createElement('button');
toggleBtn.className = 'toggle-theme';
toggleBtn.innerText = 'Toggle Dark Mode 🌙';
document.body.appendChild(toggleBtn);

// Apply dark mode from local storage
if (localStorage.getItem('theme') === 'dark') {
    document.body.classList.add('dark-mode');
    toggleBtn.innerText = 'Toggle Light Mode ☀️'
}

// Toggle light/dark mode when clicked
toggleBtn.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
    localStorage.setItem('theme', document.body.classList.contains('dark-mode') ? 'dark' : 'light');
    if (localStorage.getItem('theme') === 'dark') { toggleBtn.innerText = 'Toggle Light Mode ☀️' } else { toggleBtn.innerText = 'Toggle Dark Mode 🌙' }
});

// Manage main product image when another image is clicked
const thumbnails = document.querySelectorAll('.thumbnail');
const mainImage = document.getElementById('main-image');

thumbnails.forEach(thumb => {
    thumb.addEventListener('click', () => {
        mainImage.src = thumb.src;
    });
});


// Add to Cart functionality
// Get all buttons on the page with same class
btns = document.getElementsByClassName("add-to-cart");

for (i of btns) {
    i.addEventListener('click', function(e) {
        const button = e.currentTarget;
        //const productId = e.target.closest('.product-card').querySelector('#product-id').innerText;
        const productId = button.dataset.productId;
        const variant = e.target.closest('.product-card').querySelector('select')?.value || '';

        fetch('/add-to-cart', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ product_id: productId, variant })
        })
        .then(res => res.json())
        .then(data => {
            console.log(data.message);
            location.reload();
        })
        .catch(err => {
            alert('Error adding to cart');
            console.error(err);
        });

    });
}