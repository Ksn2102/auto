<template>
    <header class="header">
      <div class="header__logo">Автопродажи</div>
      <router-link :to="`/adminkat`" class="pp">Просмотр заказов</router-link>
      <router-link :to="`/adminkateg`" class="pp">Добавление категории</router-link>
      <button class="header__logout" @click="logout">Выход</button>
    </header>
  
    <main class="content">
      <h1 class="content__title">Управление автомобилями</h1>

      <section class="add-car">
        <h2>Добавить автомобиль</h2>
        <form @submit.prevent="addCar">

          <label for="image">Изображение:</label>
          <input type="file" ref="fileInput" @change="handleFileUpload" />
          <img v-if="newCar.image" :src="`http://localhost:5000/uploads/${newCar.image}`" />

          <label for="brand">Марка:</label>
          <input type="text" v-model="newCar.brand" id="brand" name="brand" required />
          <span class="error" v-if="errors.brand">{{ errors.brand }}</span>

          <label for="color">Цвет:</label>
          <input type="text" v-model="newCar.color" id="color" name="color" required />
          <span class="error" v-if="errors.color">{{ errors.color }}</span>

          <label for="height">Габариты:</label>
          <input type="number" v-model="newCar.height" id="height" name="height" required />
          <span class="error" v-if="errors.height">{{ errors.height }}</span>

          <label for="weight">Масса:</label>
          <input type="number" v-model="newCar.weight" id="weight" name="weight" required />
          <span class="error" v-if="errors.weight">{{ errors.weight }}</span>
  
          <label for="price">Цена:</label>
          <input type="number" v-model="newCar.price" id="price" name="price" required />
          <span class="error" v-if="errors.price">{{ errors.price }}</span>

          <label for="availability">Наличие:</label>
          <input type="text" v-model="newCar.availability" id="availability" name="availability" required />
          <span class="error" v-if="errors.availability">{{ errors.availability }}</span>

          <label for="opic">Описание:</label>
          <input type="text" v-model="newCar.opic" id="opic" name="opic" required />
          <span class="error" v-if="errors.opic">{{ errors.opic }}</span>
  
  
          <button type="submit">Добавить</button>
        </form>
      </section>
      <section class="car-list">
        <h2>Список автомобилей</h2>
        <table>
          <thead>
            <tr>
              <th>#</th>
              <th>Изображение</th>
              <th>Марка</th>
              <th>Цвет</th>
              <th>Габариты</th>
              <th>Масса</th>
              <th>Цена</th>
              <th>Наличие</th>
              <th>Описание</th>
              <th>Действия</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(car, index) in cars" :key="car.id">
              <td>{{ index + 1 }}</td>
              <td>{{ car.photo }}</td>
              <td>{{ car.brand }}</td>
              <td>{{ car.color }}</td>
              <td>{{ car.height }}</td>
              <td>{{ car.weight }}</td>
              <td>{{ car.price }}</td>
              <td>{{ car.availability }}</td>
              <td>{{ car.opic }}</td>
              <td>
                <button @click="editCar(car)">Редактировать</button>
                <button @click="deleteCar(car.id)">Удалить</button>
              </td>
            </tr>
          </tbody>
        </table>
      </section>
      <section class="edit-car" v-if="editingCar">
        <h2>Редактировать автомобиль</h2>
        <form @submit.prevent="saveEditedCar">

          <label for="image">Изображение:</label>
          <input type="file" ref="fileInput" @change="handleFileChange" />

          <label for="editBrand">Марка:</label>
          <input type="text" v-model="editingCar.brand" id="editBrand" name="editBrand" required />
          <span class="error" v-if="errors.brand">{{ errors.brand }}</span>
  
          <label for="editColor">Цвет:</label>
          <input type="text" v-model="editingCar.color" id="editColor" name="editColor" required />
          <span class="error" v-if="errors.color">{{ errors.color }}</span>
  
          <label for="editHeight">Габариты:</label>
          <input type="number" v-model="newCar.height" id="editHeight" name="editHeight" required />
          <span class="error" v-if="errors.height">{{ errors.height }}</span>

          <label for="editWeight">Масса:</label>
          <input type="number" v-model="newCar.weight" id="editWeight" name="editWeight" required />
          <span class="error" v-if="errors.weight">{{ errors.weight }}</span>
  
          <label for="editPrice">Цена:</label>
          <input type="number" v-model="newCar.price" id="editPrice" name="editPrice" required />
          <span class="error" v-if="errors.price">{{ errors.price }}</span>

          <label for="editAvailability">Наличие:</label>
          <input type="text" v-model="newCar.availability" id="editAvailability" name="editAvailability" required />
          <span class="error" v-if="errors.availability">{{ errors.availability }}</span>

          <label for="editOpic">Описание:</label>
          <input type="text" v-model="newCar.opic" id="editOpic" name="editOpic" required />
          <span class="error" v-if="errors.opic">{{ errors.opic }}</span>
  
          <button type="submit">Сохранить</button>
          <button @click="cancelEdit">Отмена</button>
        </form>
      </section>
 
    </main>
  </template>
<script>

// export default {
//    data() {
//        return {
//             car: {
//                 brand: null,
//                 model: null,
//                 price: null, 
//                 year: null
//             },
//             cars: [
//                { id: 1, brand: "Toyota", model: "Corolla", price: 20000, year: 2020 },
//                { id: 2, brand: "Honda", model: "Civic", price: 22000, year: 2019 }
//            ]
//        }
//    },
//    mounted() {
//     console.log('car admin mounted')
//    }
// }

import api from '@/utils';

export default {
  data() {
    return {
      newCar: { image: null, brand: null, color: null, height: null, weight: null, price: null, availability: null, opic: null }, 
      editingCar: null, 
      cars: [],
      errors: {}, 
    };
  },
  methods: {
    async fetchCars() {
        const response = await api.get('/api/cars')
        console.log(response)
        this.cars = response.data
    },

    addCar() {
      if (this.validateCar(this.newCar)) {
        try {
        api.post('/api/cars', this.newCar)
        this.newCar = { image: null, brand: null, color: null, height: null, weight: null, price: null, availability: null, opic: null }; 
        this.fetchCars()
      } catch {
          console.log('error create user')
        }
      }
    },

    editCar(car) {
      this.editingCar = { ...car };
    },

    saveEditedCar() {
      if (this.validateCar(this.editingCar)) {
        const index = this.cars.findIndex((c) => c.id === this.editingCar.id);
        if (index !== -1) {
          this.cars.splice(index, 1, { ...this.editingCar }); 
        }
        this.cancelEdit(); 
      }
    },

    cancelEdit() {
      this.editingCar = null;
    },

    deleteCar(id) {
      if (confirm("Вы уверены, что хотите удалить этот автомобиль?")) {
        this.cars = this.cars.filter((car) => car.id !== id);
      }
    },

    validateCar(car) {
      this.errors = {}; 

      if (!car.image) this.errors.image = "Фото обязательно";
      if (!car.brand) this.errors.brand = "Марка обязательна";
      if (!car.color) this.errors.brand = "Цвет обязательно";
      if (!car.height || car.height <= 0) this.errors.height = "Габариты должны быть положительным числом";
      if (!car.weight || car.weight <= 0) this.errors.weight = "Масса должна быть положительным числом";
      if (!car.price || car.price <= 0) this.errors.price = "Цена должна быть положительным числом";
      if (!car.availability) this.errors.availability = "Наличие обязательно";
      if (!car.opic) this.errors.opic = "Описание обязательно";

      return Object.keys(this.errors).length === 0; 
    },


    logout() {
      alert("Выполнен выход из системы");
    },

    async handleFileUpload(e) {
      console.log(e.target.value)
      // this.newCar.image = e.target.files[0]
      const payload = new FormData();
      payload.append('file', e.target.files[0]);
      const response = await api.post('/api/cars/upload-image', payload);
      console.log(response.data)
      this.newCar.image = response.data.filename;
    }
  },

  mounted() {
    this.fetchCars()
  }
};
// document.getElementById('carForm').addEventListener('submit', function(event) {
//     event.preventDefault(); // Предотвращаем стандартную отправку формы

//     const car = {
//         brand: document.getElementById('brand').value.trim(),
//         model: document.getElementById('model').value.trim(),
//         price: document.getElementById('price').value.trim(),
//         year: document.getElementById('year').value.trim()
//     };

//     // Сброс ошибок
//     resetErrors();

//     // Валидация полей
//     if (!validateCar(car)) {
//         return; // Если есть ошибки, не отправляем форму
//     }

//     // Отправка данных на сервер
//     fetch('http://127.0.0.1:8080/api/cars', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//             'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6Z…1MDZ9.WI3v4HrOgYW0mAfeB1LY6h9I19hBSUR9aE-GAXb2li0' // Замените на реальный токен
//         },
//         body: JSON.stringify(car)
//     })
//     .then(response => {
//         if (!response.ok) {
//             throw new Error('Ошибка при добавлении автомобиля');
//         }
//         return response.json();
//     })
//     .then(data => {
//         alert('Автомобиль успешно добавлен!');
//         console.log(data);
//         resetForm(); // Очистка формы после успешной отправки
//     })
//     .catch(error => {
//         alert('Произошла ошибка: ' + error.message);
//     });
// });

// // Функция валидации
// function validateCar(car) {
//     let isValid = true;

//     if (!car.brand) {
//         showError('brandError', 'Поле "Марка" обязательно');
//         isValid = false;
//     }

//     if (!car.model) {
//         showError('modelError', 'Поле "Модель" обязательно');
//         isValid = false;
//     }

//     if (!car.price || isNaN(car.price) || car.price <= 0) {
//         showError('priceError', 'Введите корректную цену');
//         isValid = false;
//     }

//     if (!car.year || isNaN(car.year) || car.year < 1900 || car.year > new Date().getFullYear()) {
//         showError('yearError', 'Введите корректный год выпуска');
//         isValid = false;
//     }

//     return isValid;
// }

// // Показать ошибку
// function showError(elementId, message) {
//     const errorElement = document.getElementById(elementId);
//     errorElement.textContent = message;
//     errorElement.style.color = 'red';
// }

// // Сброс ошибок
// function resetErrors() {
//     document.querySelectorAll('.error').forEach(error => {
//         error.textContent = '';
//     });
// }

// // Сброс формы
// function resetForm() {
//     document.getElementById('carForm').reset();
// }

// let cars = [
//             { id: 1, brand: "Toyota", model: "Corolla", price: 20000, year: 2020 },
//             { id: 2, brand: "Honda", model: "Civic", price: 22000, year: 2019 }
//         ];

//         function renderCarList() {
//             const carTableBody = document.getElementById("carTableBody");
//             carTableBody.innerHTML = "";
       
//             cars.forEach((car) => {
//                 const row = document.createElement("tr");
       
//                 row.innerHTML = `
//                     <td>${car.id}</td>
//                     <td>${car.brand}</td>
//                     <td>${car.model}</td>
//                     <td>$${car.price}</td>
//                     <td>${car.year}</td>
//                     <td>
//                         <button class="edit" onclick="editCar(${car.id})">Редактировать</button>
//                         <button class="delete" onclick="deleteCar(${car.id})">Удалить</button>
//                     </td>
//                 `;
       
//                 carTableBody.appendChild(row);
//             });
//         }

//         document.getElementById("carForm").addEventListener("submit", function (e) {
//             e.preventDefault();
       
//             const brand = document.getElementById("brand").value;
//             const model = document.getElementById("model").value;
//             const price = document.getElementById("price").value;
//             const year = document.getElementById("year").value;
       
//             if (!brand || !model || !price || !year) return;
       
//             const newCar = {
//                 id: cars.length + 1,
//                 brand,
//                 model,
//                 price: parseInt(price),
//                 year: parseInt(year)
//             };
       
//             cars.push(newCar);
//             renderCarList();
//             document.getElementById("carForm").reset();
//         });

//         function deleteCar(id) {
//             cars = cars.filter(car => car.id !== id);
//             renderCarList();
//         }

//         function editCar(id) {
//             const car = cars.find(car => car.id === id);
       
//             if (car) {
//                 document.getElementById("brand").value = car.brand;
//                 document.getElementById("model").value = car.model;
//                 document.getElementById("price").value = car.price;
//                 document.getElementById("year").value = car.year;
       
//                 deleteCar(id);
//             }
//         }
       
       
//         // function logout() {
//         //     alert("Вы вышли из системы.");
//         //     window.location.href = "/login"; 
//         // }
       
//         renderCarList();
</script>
<style>
* {
   margin: 0;
   padding: 0;
   box-sizing: border-box;
}

body {
   height: 100vh;
}

.header {
   background-color: #4CAF50;
   color: white;
   padding: 10px 20px;
   display: flex;
   justify-content: space-between;
   align-items: center;
   gap: 10px;
}

.header__logo {
   font-size: 24px;
   font-weight: bold;
}

.header__logout {
   background-color: #ff4d4d;
   color: white;
   border: none;
   padding: 8px 16px;
   cursor: pointer;
   border-radius: 4px;
}

.header__logout:hover {
   background-color: #ff7575;
}

.sidebar {
   background-color: #f4f4f4;
   width: 200px;
   height: 100%;
   padding: 20px;
}

.sidebar__menu {
   list-style: none;
}

.sidebar__menu li a {
   display: block;
   padding: 10px;
   text-decoration: none;
   color: #333;
   border-radius: 4px;
}

.sidebar__menu li a.active,
.sidebar__menu li a:hover {
   background-color: #e0e0e0;
   color: #000;
}

.content {
   flex-grow: 1;
   padding: 20px;
   overflow-y: auto;
}

.content__title {
   margin-bottom: 20px;
}

.add-car form {
   margin-bottom: 20px;
}

.add-car label {
   display: block;
   margin-bottom: 5px;
}

.add-car input {
   width: 100%;
   padding: 8px;
   margin-bottom: 10px;
   border: 1px solid #ccc;
   border-radius: 4px;
}

.add-car button {
   background-color: #4CAF50;
   color: white;
   border: none;
   padding: 10px 20px;
   cursor: pointer;
   border-radius: 4px;
}

.add-car button:hover {
   background-color: #45a049;
}

.car-list table {
   width: 100%;
   border-collapse: collapse;
}

.car-list th,
.car-list td {
   padding: 10px;
   border: 1px solid #ddd;
   text-align: left;
}

.car-list th {
   background-color: #f4f4f4;
}

.car-list button {
   background-color: #ff4d4d;
   color: white;
   border: none;
   padding: 5px 10px;
   cursor: pointer;
   border-radius: 4px;
   margin:5px;
}

.car-list button.edit {
   background-color: #2196F3;
   margin-right: 5px;
}

.car-list button.edit:hover {
   background-color: #1e88e5;
}

.car-list button.delete:hover {
   background-color: #ff7575;
}
</style>