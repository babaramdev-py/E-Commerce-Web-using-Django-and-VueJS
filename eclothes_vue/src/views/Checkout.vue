<template>
    <div class="page-checkout animate__animated animate__bounceIn">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Check Out</h1>
            </div>

            <div class="column is-12 box">
                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>Product</th>
                            <th>Price</th>
                            <th>Quantity</th>
                            <th>Total</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="item in cart.items" :key="item.product.id">
                            <td>{{ item.product.name }}</td>
                            <td>{{ item.product.price }}</td>
                            <td>{{ item.quantity }}</td>
                            <td>${{ getItemTotal(item).toFixed(2) }}</td>
                        </tr>
                    </tbody>
                    <tfoot>
                        <tr>
                            <td colspan="2">Total</td>
                            <td>{{ cartTotalLength }}</td>
                            <td>${{ cartTotalPrice.toFixed(2) }}</td>
                        </tr>
                    </tfoot>
                </table>
            </div>

            <div class="column is-12 box mt-3">
                <h2 class="subtitle is-size-3">Shipping Details</h2>
                <h3 class="subtitle is-size-6">*All fields are required to be filled out</h3>

                <div class="columns is-multiline">
                    <div class="column is-6">
                        <div class="field">
                            <label for="">First Name</label>
                            <div class="control">
                                <input type="text" class="input" v-model="first_name">
                            </div>
                        </div>
                        <div class="field">
                            <label for="">Last Name</label>
                            <div class="control">
                                <input type="text" class="input" v-model="last_name">
                            </div>
                        </div>
                        <div class="field">
                            <label for="">Email</label>
                            <div class="control">
                                <input type="email" class="input" v-model="email">
                            </div>
                        </div>
                        <div class="field">
                            <label for="">Phone</label>
                            <div class="control">
                                <input type="number" class="input" v-model="phone">
                            </div>
                        </div>
                    </div>
                    <div class="column is-6">
                        <div class="field">
                            <label for="">Address</label>
                            <div class="control">
                                <input type="text" class="input" v-model="address">
                            </div>
                        </div>
                        <div class="field">
                            <label for="">Zip Code</label>
                            <div class="control">
                                <input type="number" class="input" v-model="zipcode">
                            </div>
                        </div>
                        <div class="field">
                            <label for="">Place</label>
                            <div class="control">
                                <input type="text" class="input" v-model="place">
                            </div>
                        </div>


                    </div>


                </div>
                <div class="notification is-danger mt-4 animate__animated animate__headShake" v-if="errors.length">
                    <p v-for="error in errors" :key="error">{{ error }}</p>
                </div>

                <div id="card-element" class="mb-5">

                </div>
                <template v-if="cartTotalLength">
                    <hr>
                    <button class="button is-dark" @click="submitForm">Proceed to Payment</button>
                </template>
            </div>

        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'Checkout',
    data() {
        return {
            cart: {
                items: []
            },
            stripe: {},
            card: {},
            first_name: '',
            last_name: '',
            email: '',
            phone: '',
            address: '',
            zipcode: '',
            place: '',
            errors: [],
        }
    },
    mounted() {
        document.title = 'EClothes | Checkout'
        this.cart = this.$store.state.cart
    },
    methods: {
        getItemTotal(item) {
            return item.quantity * item.product.price
        },
        submitForm(){
            this.errors = []

            if(this.first_name === '')
            {
                this.errors.push('The first name field is missing')
            }
            if(this.last_name === '')
            {
                this.errors.push('The last name field is missing')
            }
            if(this.phone === '')
            {
                this.errors.push('The phone is missing')
            }
            if(this.address === '')
            {
                this.errors.push('The address field is missing')
            }
            if(this.place === '')
            {
                this.errors.push('The place field is missing')
            }
        }
    },
    computed: {
        cartTotalPrice() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.product.price * curVal.quantity
            }, 0)
        },
        cartTotalLength() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.quantity
            }, 0)
        }
    }
}
</script>