<template>
  <div class="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><strong>EClothes</strong></router-link>

        <a aria-expanded="false" aria-label="menu" data-target="navbar-menu" class="navbar-burger" @click="showMobileMenu = !showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active':showMobileMenu}">
        <div class="navbar-end">
          <a href="/summer/" class="navbar-item">Summmer</a>
          <a href="/winter/" class="navbar-item">Winter</a>  

          <div class="navbar-item">
            <div class="buttons">
              <router-link to="/login" class="button is-light">Login</router-link>
              <router-link to="/cart" class="button is-success">
                <span class="icon"><i class="fas fa-shopping-cart"></i></span>
                <span>Cart: {{ cartTotalLength }}</span>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <div class="is-loading-bar has-text-centered" :class = "{'is-loading':$store.state.isLoading}">
      <div class="lds-dual-ring">
      </div>
    </div>

    <section class="section">
      <router-view />
    </section>

    <footer class="footer">
      <p class="has-text-centered">
        Copyright 2023
      </p>
    </footer>
  </div>
</template>

<script>
export default{
  data()
  {
    return {
      showMobileMenu: false,
      cart:{
        items : [],
      },

    }
  },
  beforeCreate(){
    this.$store.commit('initialiseStore')
  },
  mounted(){
    this.cart = this.$store.state.cart
  },
  computed: {
    cartTotalLength(){
      let totalLength = 0;
      for (let i = 0; i < this.cart.items.length; i++){
        totalLength += this.cart.items[i].quantity
      }
      return totalLength  
      
    }
    // Cart Total length calculated in the base template == APP.vue
    // Cart total length is injected in the Cart Button Nav
  }
}


</script>

<style lang="scss">
@import '../node_modules/bulma';

.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}
.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}
@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
.is-loading-bar {
  height: 0;
  overflow: hidden;
  -webkit-transition: all 0.3s;
  transition: all 0.3s;
  &.is-loading {
    height: 80px;
  }
}


</style>
