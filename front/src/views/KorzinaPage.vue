<template>
      <div class="cart-container">
        <h1 class="po"> Ваша корзина</h1>

        <div class="cart-item">
            <img src="@/assets/215.jpg" alt="Ноутбук">
            <div class="item-info">
                <h2>BMW X5 40d IV (G05/G18) Рестайлинг</h2>
                <p>Цена: 50 000 000 ₽</p>
                <div class="quantity-controls">
                    <button>-</button>
                    <span class="rad">1</span>
                    <button>+</button>
                </div>
                <button class="remove-btn"> Удалить</button>
            </div>
        </div>

        <div class="cart-item">
            <img src="@/assets/27.webp" alt="Смартфон">
            <div class="item-info">
                <h2>Mercedes-Benz G-Класс AMG 63 AMG II (W465) Рестайлинг</h2>
                <p>Цена: 60 000 000 ₽</p>
                <div class="quantity-controls">
                    <button>-</button>
                    <span class="rad">2</span>
                    <button>+</button>
                </div>
                <button class="remove-btn"> Удалить</button>
            </div>
        </div>

        <div class="cart-summary">
            <h2 class="po">Итого: 110 000 000 ₽</h2>
            <router-link to="/pokypka" class="checkout-btn">Оформить заказ</router-link>
        </div>
    </div>
</template>
<script>
export default {
    name: 'KorzinaPage',
};

</script>
<style>
.rad{
    font-size: 19px;
    margin: 0 5px;
}

.cart-container {
    max-width: 800px;
    margin: 30px auto;
    padding: 20px;
    background: white;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    text-align: center;
}

.po {
    margin-bottom: 20px;
}

.cart-item {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px;
    border-bottom: 1px solid #ddd;
}

.cart-item img {
    width: 200px;
    height: 200px;
    border-radius: 5px;
}

.item-info {
    flex: 1;
    margin-left: 15px;
    text-align: left;
}

.quantity-controls {
    display: flex;
    align-items: center;
    margin-top: 5px;
}

.quantity-controls button {
    background: #007bff;
    color: white;
    border: none;
    padding: 5px 10px;
    cursor: pointer;
    border-radius: 20px;
}

.quantity-controls button:hover {
    background: #0056b3;
}

.remove-btn {
    background: red;
    color: white;
    border: none;
    padding: 5px 10px;
    cursor: pointer;
    margin-top: 5px;
    border-radius: 25px;
}

.remove-btn:hover {
    background: darkred;
}

.cart-summary {
    margin-top: 20px;
}

.checkout-btn {
    padding: 10px 15px;
    background: #28a745;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;
}

.checkout-btn:hover {
    background: #218838;
}
</style>