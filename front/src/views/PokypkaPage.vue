<template>
    <div class="order-form">
        <h1>Формирование нового заказа</h1>
        <form id="newOrderForm">
            <label for="service">Выберите услугу:</label>
            <select id="service" name="service">
                <option value="cleaning">Автомобиль</option>
                <option value="delivery">Электромобиль</option>
            </select>
    
            <label for="address">Адрес:</label>
            <input type="text" id="address" name="address" placeholder="Введите адрес" required>
    
            <label for="date">Дата предоставления услуги:</label>
            <input type="date" id="date" name="date" required>
    
            <label for="time">Время предоставления услуги:</label>
            <input type="time" id="time" name="time" required>
    
            <label for="name">Имя клиента:</label>
            <input type="text" id="name" name="name" placeholder="Введите имя">
    
            <label for="phone">Телефон:</label>
            <input type="tel" id="phone" name="phone" placeholder="+7 (900) 123-45-67">
    
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" placeholder="example@example.com">
    
            <label for="description">Описание услуги:</label>
            <textarea id="description" name="description" rows="4" placeholder="Введите описание услуги"></textarea>
    
            <label for="price">Ожидаемая сумма (₽):</label>
            <input type="number" id="price" name="price" placeholder="Введите сумму">
    
            <label for="urgency">Срочность:</label>
            <select id="urgency" name="urgency">
                <option value="low">Низкая</option>
                <option value="medium">Средняя</option>
                <option value="high">Высокая</option>
            </select>
    
            <label for="paymentMethod">Способ оплаты:</label>
            <select id="paymentMethod" name="paymentMethod">
                <option value="cash">Наличные</option>
                <option value="card">Банковская карта</option>
                <option value="online">Онлайн-оплата</option>
            </select>
    
            <label for="comments">Дополнительные комментарии:</label>
            <textarea id="comments" name="comments" rows="4" placeholder="Введите комментарии"></textarea>
    
            <div class="buttons">
                <button type="button" class="cancel" onclick="window.location.href='lk.html'">Отмена</button>
                <button type="reset">Очистить</button>
                <button type="submit">Подтвердить</button>
            </div>
        </form>
    </div>
    
</template>
<script>
export default {
    name: 'PokypkaPage',
};

</script>
<style>
.order-form {
  max-width: 600px;
  margin: 0 auto;
  border-radius: 10px;
  padding: 20px;
}
.order-form h1 {
  text-align: center;
  margin-bottom: 20px;
}
.order-form label {
  display: block;
  font-weight: bold;
  margin-top: 10px;
  font-size: 1rem;
}
.order-form input,
.order-form select,
.order-form textarea {
  width: 100%;
  padding: 10px;
  margin: 5px 0 15px;
  border: 1px solid #ddd;
  border-radius: 5px;
  font-size: 1rem;
}

.buttons {
  text-align: center;
}
.buttons button {
  padding: 10px 15px;
  margin-right: 10px;
  border: none;
  background-color: #007BFF;
  color: white;
  cursor: pointer;
  border-radius: 5px;
  transition: background-color 0.3s ease;
}
.buttons button:hover {
  background-color: #0056b3;
}
.buttons button.cancel {
  background-color: #dc3545;
}
.buttons button.cancel:hover {
  background-color: #a71d2a;
}

@media (max-width: 768px) {
  .order-form {
    padding: 15px;
  }
  .order-form h1 {
    font-size: 1.5rem;
  }
  .order-form label {
    font-size: 0.9rem;
  }
  .order-form input,
  .order-form select,
  .order-form textarea {
    padding: 8px;
    font-size: 0.9rem;
  }
  .order-form .buttons button {
    padding: 8px 12px;
    font-size: 0.9rem;
  }
}
@media (max-width: 480px) {
  .buttons button {
    display: block;
    margin: 10px auto;
    width: 100%;
  }
}
</style>