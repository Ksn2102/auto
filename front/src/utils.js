import axios from "axios";
import router from "./router/index"
 
axios.defaults.baseURL = 'http://localhost:5000'
const api = axios.create()

api.interceptors.request.use(config => {
  if(localStorage.token) {
    config.headers.authorization = `Bearer ${localStorage.token}`
  }

  return config
},error => {
  console.log(error)
})

api.interceptors.response.use(config => {
  if(localStorage.token) {
    config.headers.authorization = `Bearer ${localStorage.token}`
  }
 
  return config
}, error => {
 
  if(error.response.data.message === 'Token has expired') {
    axios.post('api/auth/refresh', {}, {
      headers: {
        'authorization': `Bearer ${localStorage.token}`
      }
    }).then(response => {
      localStorage.access_token = response.data.token
      error.config.headers.authorization = `Bearer ${response.data.token}`
 
      return api.request(error.config)
    })
  }
 
  if(error.response.status === 401) {
    router.push('/login')
  }
})
 
export default api