<template>
    <div class="page-cart animate__animated animate__bounceInDown">
        <div class="columns is-multiline">
            <div class="column is-12 has-text-centered">
                <h1 class="title">
                    Cart
                </h1>
            </div>

            <div class="column is-12 box">
                <table class="table is-fullwidth" v-if = "cartTotalLength">
                    <thead>
                        <tr>
                            <!-- <th>SNo.</th> Add as a feature later-->
                            <th>Product</th>
                            <th>Price</th>
                            <th>Quantity</th>
                            <th>Total</th>
                        </tr>
                    </thead>
                    <tbody>
                        <CartItem v-for = "item in cart.items"
                            :key = "item.product.id"
                            :initialItem = "item"
                            v-on:removeFromCart="removeFromCart"
                        />

                    </tbody>
                </table>
                <p v-else>You don't have any items in your cart</p>
            </div>
            
        </div>
        <div class="columns mt-6">
            <div class="column is-9"></div>
            <div class="column is-3 box is-dark">
                <h1 class="subtitle is-size-3">Total</h1>
                <hr class="is-dark">
                <div class="columns is-multiline">
                    <div class="column is-6">
                        <h1 class="subtitle is-size-5">Cost</h1> 
                    </div>
                    <div class="column is-6">
                        <h1 class="subtitle is-size-5">Items</h1>
                    </div>
                    <div class="column is-6">
                        <h3>{{ cartTotalPrice.toFixed(2) }}$</h3> 
                    </div>
                    <div class="column is-6">
                        <h4>{{ cartTotalLength }} items</h4>
                    </div>
                </div>
                <hr>
                <router-link to="/cart/checkout" class="button is-dark">Proceeed to Check Out</router-link>
            </div>
        </div>
    </div>


</template>


<script>

import axios from 'axios';
import CartItem from '@/components/CartItem.vue'

export default{
    name : 'Cart',
    components: {
        CartItem
    },
    data(){
        return{
            cart: {
                items : [],
            },
        }
    },
    mounted() {
        this.cart = this.$store.state.cart // both state.cart and data.cart point to
        // the same memory location.
        document.title = 'EClothes | Cart'
    },
    methods: {
        removeFromCart(item){
            this.cart.items = this.cart.items.filter(i => i.product.id !== item.product.id)
        }
    },
    computed: {
        cartTotalLength(){
            return this.cart.items.reduce((acc,curVal) => {
                return acc += curVal.quantity
            },0)
        },
        cartTotalPrice(){
            return this.cart.items.reduce((acc,curVal) => {
                return acc += curVal.product.price * curVal.quantity
            },0)
        }
    },

}




</script>

<!-- 
    Two things to keep in mind:
    1.) Objects and arrays in Vue.js and VueX are passed by reference
    so 
        this.cart = this.$store.state.cart line basically links the two
        from component to the store as we are passing down object from 
        store down to component
    2.) Even Props in VueJS and Vuex are passed by reference.
 -->