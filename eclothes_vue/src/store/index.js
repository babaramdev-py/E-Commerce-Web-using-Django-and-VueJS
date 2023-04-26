import { createStore } from 'vuex'

export default createStore({
  state: {
    cart: {
      items: [],
    },
    isAuthenticated: false,
    token: '',
    isLoading: false,
  },
  getters: {
  },
  mutations: {
    initialiseStore(state){
      if(localStorage.getItem('cart')){
        state.cart = JSON.parse(localStorage.getItem('cart'))
      }
      else{
        localStorage.setItem('cart',JSON.stringify(state.cart))
      }
      if(localStorage.getItem('token')){
        state.token = localStorage.getItem('token')
        state.isAuthenticated = true
      }
      else{
        state.token = ''
        state.isAuthenticated = false
      }

      //adds cart to local storage if no cart, else updates the cart in the server
    },
    addToCart(state, item){
      const exists = state.cart.items.filter(i => i.product.id === item.product.id) // Check if the item is already in cart
      console.log(exists[0])
      console.log(state.cart.items)
      if(exists.length){
        // if already in the cart, increase quantity
        exists[0].quantity = parseInt(exists[0].quantity) + parseInt(item.quantity)
      }
      else{
        // if the item doesn't exist on cart, push it to cart
        state.cart.items.push(item)
      }
      // after incrementing quantity, we're modifying local cart variable
      localStorage.setItem('cart',JSON.stringify(state.cart))
    },
    setIsLoading(state,status){
      state.isLoading = status
    },
    setToken(state, token)
    {
      //when we login, set the token
      state.token = token
      state.isAuthenticated = true
    },
    removeToken(state, token){
      // on logging out, deactivate the token
      state.token = ''
      state.isAuthenticated = false
    },
    clearCart(state) {
      state.cart = { items: [] }

      localStorage.setItem('cart', JSON.stringify(state.cart))
    },

  },
  actions: {
  },
  modules: {
  }
})

// Vuex is used for Global State, Auth, Global Cart, etc. 