export const state = () => ({
    userLoc: null,
    status: '',
    user: {},
    services: [
        {service:'Hospital', icon:'mdi-hospital-box'},
        {service:'Pharmacy', icon:'mdi-pill' },
        {service:'Grocery', icon:'mdi-basket' },
        {service:'Restaurant', icon:'mdi-silverware-fork-knife'},
        {service:'Supermarket', icon:'mdi-cart' },
        {service:'Gas Station', icon:'mdi-gas-station' },
        {service:'Payment Gateway', icon:'mdi-contactless-payment-circle'},
        {service:'Bank', icon: 'mdi-bank'},
        {service:'Hardware', icon: 'mdi-hammer-wrench' },
        {service:'Utility Company', icon: 'mdi-toolbox' },
        {service:'Electronics', icon: 'mdi-flash' }
      //   {service:'All', icon: ''}
    ],
    filters: []
    // token: localStorage.getItem('token') || ''
  })
  
export const mutations = {
    userLocation(state, location) {
        state.userLoc = location
    },
    auth_request(state){
        state.status = 'loading'
    },
    auth_success(state, token, user){
        state.status = 'success'
        state.token = token
        state.user = user
    },
    auth_error(state){
        state.status = 'error'
    },
    logout(state){
        state.status = ''
        state.token = ''
    },
    filter(state, service) {
        state.filters.includes(service) ? state.filters.splice(state.filters.indexOf(service), 1) : state.filters.push(service)
    }
}

export const actions = {
    login({commit}, user){
        return new Promise((resolve, reject) => {
        commit('auth_request')
        this.$axios({url: process.env.SONEAR_API + 'api/login/', data: user, method: 'POST' })
        .then(resp => {
            const token = resp.data.token
            const user = resp.data.user
            localStorage.setItem('token', token)
            axios.defaults.headers.common['Authorization'] = token
            commit('auth_success', token, user)
            resolve(resp)
        })
        .catch(err => {
                commit('auth_error')
                localStorage.removeItem('token')
                reject(err)
            })
        })
      },
      register({commit}, user){
        return new Promise((resolve, reject) => {
                commit('auth_request')
                this.$axios({url: process.env.SONEAR_API + '/businesses/', data: user, method: 'POST' })
                .then(resp => {
                const token = resp.data.token
                const user = resp.data.user
                localStorage.setItem('token', token)
                axios.defaults.headers.common['Authorization'] = token
                commit('auth_success', token, user)
                resolve(resp)
            })
            .catch(err => {
                commit('auth_error', err)
                localStorage.removeItem('token')
                reject(err)
            })
        })
      },
      logout({commit}){
        return new Promise((resolve, reject) => {
            commit('logout')
            localStorage.removeItem('token')
            delete axios.defaults.headers.common[ 'Authorization' ]
            localStorage.removeItem('userId')
            resolve()
        }).then(() => location.reload())
    }
}