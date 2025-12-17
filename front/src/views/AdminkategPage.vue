<template>
    <div class="category-management">
      <h1>Управление категориями</h1>
      <button @click="showAddCategoryForm = true" class="add-category-btn">Добавить категорию</button>
      <ul class="category-list">
        <li v-for="category in categories" :key="category.id" class="category-item">
          {{ category.name }}
          <button @click="confirmDelete(category.id)" class="delete-btn">Удалить</button>
        </li>
      </ul>
      <div v-if="showAddCategoryForm" class="add-category-form">
        <h2>Добавить категорию</h2>
        <form @submit.prevent="addCategory">
          <label for="name">Название:</label>
          <input type="text" id="name" v-model="newCategory.name" placeholder="Введите название категории" />
          <span v-if="errors.name" class="error">{{ errors.name }}</span>
          <div class="form-actions">
            <button type="submit" class="submit-btn">Добавить</button>
            <button type="button" @click="cancelAddCategory" class="cancel-btn">Отмена</button>
          </div>
        </form>
      </div>

      <div v-if="showDeleteConfirmation" class="delete-confirmation">
        <p>Вы уверены, что хотите удалить категорию "{{ categoryToDelete.name }}"?</p>
        <button @click="confirmDeleteCategory" class="confirm-delete-btn">Подтвердить</button>
        <button @click="cancelDelete" class="cancel-delete-btn">Отмена</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        categories: [
          { id: 1, name: 'Автомобили' },
          { id: 2, name: 'Электромобили' }
        ],
        showAddCategoryForm: false,
        newCategory: { name: '' },
        errors: { name: '' },
        showDeleteConfirmation: false,
        categoryToDelete: null
      };
    },
    methods: {
      addCategory() {
        if (!this.newCategory.name.trim()) {
          this.errors.name = 'Поле "Название" не может быть пустым';
          return;
        }
  
        this.categories.push({ ...this.newCategory, id: Date.now() });
        this.newCategory = { name: '' };
        this.errors.name = '';
        this.showAddCategoryForm = false;
      },
      cancelAddCategory() {
        this.newCategory = { name: '' };
        this.errors.name = '';
        this.showAddCategoryForm = false;
      },
      confirmDelete(id) {
        this.categoryToDelete = this.categories.find(c => c.id === id);
        this.showDeleteConfirmation = true;
      },
      confirmDeleteCategory() {
        if (this.categoryToDelete) {
          this.categories = this.categories.filter(c => c.id !== this.categoryToDelete.id);
          this.categoryToDelete = null;
          this.showDeleteConfirmation = false;
        }
      },
      cancelDelete() {
        this.categoryToDelete = null;
        this.showDeleteConfirmation = false;
      }
    }
  };
  </script>
  
  <style>
  body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f9fafb;
  }
  
  .category-management {
    max-width: 800px;
    margin: 40px auto;
    padding: 20px;
    background-color: #ffffff;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  h1 {
    margin-bottom: 20px;
  }

  .add-category-btn {
    display: block;
    width: 100%;
    padding: 10px;
    background-color: #4caf50;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
    transition: background-color 0.3s ease;
  }
  
  .add-category-btn:hover {
    background-color: #45a049;
  }

  .category-list {
    list-style: none;
    padding: 0;
    margin-top: 20px;
  }
  
  .category-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px;
    border-bottom: 1px solid #e0e0e0;
  }
  
  .category-item:last-child {
    border-bottom: none;
  }
  
  .delete-btn {
    background-color: #ff4d4d;
    color: white;
    border: none;
    padding: 5px 10px;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  
  .delete-btn:hover {
    background-color: #ff7575;
  }
  
  .add-category-form {
    margin-top: 20px;
  }
  
  .add-category-form label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
  }
  
  .add-category-form input {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  .error {
    color: red;
    font-size: 14px;
    margin-bottom: 10px;
  }
  
  .form-actions {
    display: flex;
    gap: 10px;
  }
  
  .submit-btn,
  .cancel-btn {
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
  }
  
  .submit-btn {
    background-color: #4caf50;
    color: white;
  }
  
  .submit-btn:hover {
    background-color: #45a049;
  }
  
  .cancel-btn {
    background-color: #f44336;
    color: white;
  }
  
  .cancel-btn:hover {
    background-color: #e53935;
  }

  .delete-confirmation {
    margin-top: 20px;
    padding: 20px;
    background-color: #f4f4f4;
    border-radius: 8px;
    text-align: center;
  }
  
  .confirm-delete-btn,
  .cancel-delete-btn {
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
  }
  
  .confirm-delete-btn {
    background-color: #4caf50;
    color: white;
  }
  
  .confirm-delete-btn:hover {
    background-color: #45a049;
  }
  
  .cancel-delete-btn {
    background-color: #ff4d4d;
    color: white;
  }
  
  .cancel-delete-btn:hover {
    background-color: #ff7575;
  }
  </style>