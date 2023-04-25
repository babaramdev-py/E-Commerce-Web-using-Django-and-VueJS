import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Product from '../views/Product.vue'
import Category from '../views/Category.vue'
import Search from '../views/Search.vue'
import Cart from '../views/Cart.vue'
import SignUp from '../views/SignUp.vue'
import LogIn from '../views/LogIn.vue'
import MyAccount from '../views/MyAccount.vue'
import store from '../store'
const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/log-in',
    name: 'login',
    component: LogIn
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path:'/my-account',
    name: 'about',
    component: MyAccount, // append meta data to guard it via authentication
    meta : {
      requireLogin: true
    }
  },
  {
    path : '/search',
    name: 'Search',
    component: Search
  },
  {
    path : '/cart',
    name: 'Cart',
    component: Cart
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/:category_slug',
    name: 'Category',
    component: Category
  },
  {
    path: '/:category_slug/:product_slug',
    name: 'Product',
    component: Product
  },
  

  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to,from,next)=>{
  //to log out be required to login
  if(to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated){
    next({name:'login',query: {to: to.path}});
  }else{
    next() //if logged in, then do nothing, simply log out
  }
})

export default router

// Setting up myaccount page logic explained
/* 
  Add router card


*/