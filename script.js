document.addEventListener('DOMContentLoaded', function() {
  console.log('Script loaded!');
  
  // Fetch products from backend
  fetch('/api/products')
    .then(response => response.json())
    .then(products => {
      const productsContainer = document.getElementById('products');
      products.forEach(product => {
        const productElement = document.createElement('div');
        productElement.textContent = `Product: ${product.name}, Manufacturer: ${product.manufacturer}`;
        productsContainer.appendChild(productElement);
      });
    })
    .catch(error => console.error('Error fetching products:', error));
});
