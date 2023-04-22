<template>
    <div class="page-cart">
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
                        />

                    </tbody>
                </table>
                <p v-else>You don't have any items in your cart</p>
            </div>
            <div class="column is-9"></div>
            <div class="column is-3 box">
                <h2 class="subtitle">Total</h2>
                <div class="columns is-multiline">
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
        this.cart = this.$store.state.cart
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