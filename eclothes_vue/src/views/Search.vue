<template>
    <div class="page-search animate__animated animate__bounceInDown">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Search</h1>
                <h2 class="is-size-5 has-text-grey">Search Item: "{{ query }}"</h2>
            </div>
            <ProductBox v-for="product in products" :key="product.id" :product="product">
            </ProductBox>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import ProductBox from '@/components/ProductBox.vue';
export default {
    name: 'Search',
    data() {
        return {
            products: [],
            query: ''
        }
    },
    components: {
        ProductBox
    },
    mounted() {
        document.title = 'Search | EClothes'
        console.log("modunted");

        let uri = window.location.search.substring(1)
        console.log(uri)
        let params = new URLSearchParams(uri)

        if (params.get('query')) {
            this.query = params.get('query')
            this.performSearch()
        }

    },
    methods: {
        async performSearch() {
            this.$store.commit('setIsLoading', true);
            await axios.
                post('api/v1/products/search/', { 'query': this.query })
                .then(response => {
                    this.products = response.data
                })
                .catch(error =>{
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false);

        }
    },

}



</script>