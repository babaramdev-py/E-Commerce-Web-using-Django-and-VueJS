<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6 is-rounded">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">
          Welcome to EClothes
        </p>
        <p class="subtitle">
          An EClother built using Vue and Django
        </p>
      </div>
    </section>
    <div class="columns is-multiline ">

      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">
          Latest Products
        </h2>
      </div>

      <ProductBox v-for="product in latestProducts"
        :key = "product.id"
        :product = "product"
      />



    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import { labeledStatement } from '@babel/types'
import axios from 'axios'
import ProductBox from '@/components/ProductBox.vue'

export default {
  name: 'HomeView',
  data() {
    return {
      latestProducts: [],
    }
  },
  components: {
    ProductBox
  },
  // lifecyclehooks
  mounted() {
    this.getLatestProducts()
    document.title = 'Home | EClother'
  },
  methods: {
    async getLatestProducts() {
      this.$store.commit('setIsLoading',true)
      await axios
        .get('api/v1/latest-products')
        .then(response => {
          this.latestProducts = response.data
          console.log(this.latestProducts);
        })
        .catch(error =>{
          console.log("Could not make calls to backend")

        }
      )
      this.$store.commit('setIsLoading',false)
    }
  }

}
</script>



<!-- get_absolute_url in DRF is being used here to route to that link, after routing there, 
  we basically make calls using axios to the back end
  after those calls are made, we render them in the front end using a data structure like an object
 -->