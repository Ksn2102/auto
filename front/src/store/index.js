import { createStore } from 'vuex'
import { authAPI, carsAPI, bookingsAPI } from '@/api/endpoints'

export default createStore({
  state: {
    user: JSON.parse(localStorage.getItem('user')) || null,
    accessToken: localStorage.getItem('access_token') || null,
    cars: [],
    bookings: [],
    isLoading: false
  },
  
  mutations: {
    SET_USER(state, user) {
      state.user = user
      localStorage.setItem('user', JSON.stringify(user))
    },
    
    SET_TOKEN(state, token) {
      state.accessToken = token
      localStorage.setItem('access_token', token)
    },
    
    SET_CARS(state, cars) {
      state.cars = cars
    },
    
    SET_BOOKINGS(state, bookings) {
      state.bookings = bookings
    },
    
    SET_LOADING(state, isLoading) {
      state.isLoading = isLoading
    },
    
    LOGOUT(state) {
      state.user = null
      state.accessToken = null
      state.cars = []
      state.bookings = []
      localStorage.clear()
    }
  },
  
  actions: {
    async login({ commit }, credentials) {
      try {
        const response = await authAPI.login(credentials)
        commit('SET_USER', response.data.user)
        commit('SET_TOKEN', response.data.access_token)
        localStorage.setItem('refresh_token', response.data.refresh_token)
        return response.data
      } catch (error) {
        throw error.response?.data?.error || 'Login failed'
      }
    },
    
    async register({ commit }, userData) {
      try {
        const response = await authAPI.register(userData)
        commit('SET_USER', response.data.user)
        commit('SET_TOKEN', response.data.access_token)
        localStorage.setItem('refresh_token', response.data.refresh_token)
        return response.data
      } catch (error) {
        throw error.response?.data?.error || 'Registration failed'
      }
    },
    
    async logout({ commit }) {
      try {
        await authAPI.logout()
      } catch (error) {
        console.error('Logout error:', error)
      } finally {
        commit('LOGOUT')
      }
    },
    
    async fetchCars({ commit }) {
      try {
        commit('SET_LOADING', true)
        const response = await carsAPI.getAll()
        commit('SET_CARS', response.data)
        return response.data
      } catch (error) {
        throw error
      } finally {
        commit('SET_LOADING', false)
      }
    },
    
    async fetchBookings({ commit }) {
      try {
        const response = await bookingsAPI.getAll()
        commit('SET_BOOKINGS', response.data)
        return response.data
      } catch (error) {
        throw error
      }
    },
    
    async createBooking({ dispatch }, bookingData) {
      try {
        const response = await bookingsAPI.create(bookingData)
        // Обновляем список бронирований
        await dispatch('fetchBookings')
        return response.data
      } catch (error) {
        throw error.response?.data?.error || 'Booking failed'
      }
    }
  },
  
  getters: {
    isAuthenticated: state => !!state.accessToken,
    user: state => state.user,
    cars: state => state.cars,
    bookings: state => state.bookings,
    activeBookings: state => state.bookings.filter(b => 
      ['pending', 'confirmed', 'active'].includes(b.status)
    ),
    pastBookings: state => state.bookings.filter(b => 
      ['completed', 'cancelled'].includes(b.status)
    )
  }
})