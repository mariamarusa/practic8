const API_URL = 'http://localhost:8000';

// Загрузка при открытии страницы
window.onload = function() {
    loadAllProducts();
    loadCategories();
};

// Загрузить все товары
async function loadAllProducts() {
    showLoading();
    hideError();
    
    try {
        const res = await fetch(`${API_URL}/products/all`);
        const products = await res.json();
        showProducts(products);
        
        document.querySelectorAll('.cat-btn').forEach(b => b.classList.remove('active'));
        document.querySelector('button[onclick="loadAllProducts()"]').classList.add('active');
    } catch(e) {
        showError('Ошибка загрузки');
    } finally {
        hideLoading();
    }
}

// Загрузить категории
async function loadCategories() {
    try {
        const res = await fetch(`${API_URL}/categories`);
        const categories = await res.json();
        
        const container = document.getElementById('categories');
        
        categories.forEach(cat => {
            const btn = document.createElement('button');
            btn.className = 'cat-btn';
            btn.textContent = cat.name;
            btn.onclick = () => loadByCategory(cat.id);
            container.appendChild(btn);
        });
    } catch(e) {
        console.log('Ошибка загрузки категорий');
    }
}

// Загрузить товары по категории
async function loadByCategory(categoryId) {
    showLoading();
    hideError();
    
    try {
        const res = await fetch(`${API_URL}/products/category/${categoryId}`);
        const products = await res.json();
        showProducts(products);
        
        document.querySelectorAll('.cat-btn').forEach(b => b.classList.remove('active'));
        event.target.classList.add('active');
    } catch(e) {
        showError('Ошибка загрузки');
    } finally {
        hideLoading();
    }
}

// Показать товары
function showProducts(products) {
    const container = document.getElementById('products');
    
    if(products.length === 0) {
        container.innerHTML = '<p style="text-align: center;">Товары не найдены</p>';
        return;
    }
    
    let html = '';
    products.forEach(p => {
        html += `
            <div class="product-card" onclick="showProductDetail(${p.id})">
                <div class="product-name">${p.name}</div>
                <div class="product-category">${p.category?.name || 'Без категории'}</div>
                <div class="product-description">${p.description || 'Нет описания'}</div>
                <div class="product-price">${p.price.toLocaleString()} ₽</div>
                <div class="product-stock">В наличии: ${p.stock} шт.</div>
            </div>
        `;
    });
    
    container.innerHTML = html;
}

// Показать детали товара
async function showProductDetail(id) {
    try {
        const res = await fetch(`${API_URL}/products/get/${id}`);
        const p = await res.json();
        
        alert(`
${p.name}
Категория: ${p.category?.name || 'Без категории'}
Цена: ${p.price} ₽
В наличии: ${p.stock} шт.
Описание: ${p.description || 'Нет описания'}
        `);
    } catch(e) {
        alert('Ошибка загрузки товара');
    }
}

function showLoading() {
    document.getElementById('loading').classList.remove('hidden');
}

function hideLoading() {
    document.getElementById('loading').classList.add('hidden');
}

function showError(msg) {
    const err = document.getElementById('error');
    err.textContent = msg;
    err.classList.remove('hidden');
    setTimeout(() => err.classList.add('hidden'), 3000);
}

function hideError() {
    document.getElementById('error').classList.add('hidden');
}