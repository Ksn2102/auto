import api from './index'

export const authAPI = {
  login: (credentials) => api.post('/auth/login', credentials),
  register: (userData) => api.post('/auth/register', userData),
  logout: () => api.post('/auth/logout')
}

export const carsAPI = {
  getAll: () => api.get('/cars'),
  getById: (id) => api.get(`/cars/${id}`),
  create: (carData) => api.post('/cars', carData),
  update: (id, carData) => api.put(`/cars/${id}`, carData),
  delete: (id) => api.delete(`/cars/${id}`)
}

export const tariffsAPI = {
  getAll: () => api.get('/tariffs'),
  getById: (id) => api.get(`/tariffs/${id}`)
}

export const bookingsAPI = {
  getAll: () => api.get('/bookings'),
  getById: (id) => api.get(`/bookings/${id}`),
  create: (bookingData) => api.post('/bookings', bookingData),
  cancel: (id) => api.post(`/bookings/${id}/cancel`)
}

export const userAPI = {
  getProfile: () => api.get('/user/profile'),
  updateProfile: (userData) => api.put('/user/profile', userData),
  changePassword: (passwordData) => api.put('/user/password', passwordData),
  getBookings: () => api.get('/user/bookings'),
  getHistory: () => api.get('/user/history')
}