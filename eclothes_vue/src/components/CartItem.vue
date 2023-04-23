<template>
    <tr v-if="item.quantity > 0">
        <!-- <td></td> Add as a feature -->
        <td><router-link :to="item.product.get_absolute_url">{{ item.product.name }}</router-link></td>
        <td>${{ item.product.price }}</td>
        <td>
            {{ item.quantity }}
            <a @click="decrementQuantity(item)" class="mr-2 ml-2">-</a>
            <a @click="incrementQuantity(item)">+</a>
        </td>
        <td>${{ getItemTotal(item).toFixed(2) }}</td>
        <td><button class="delete" @click="removeFromCart(item)"></button></td>
    </tr>
</template>

<script>

export default {
    name: 'CartItem',
    props: {
        initialItem: Object,
    },
    data() {
        return {
            item: this.initialItem,
            // props in VueJS are passed by reference, so when 
            // we update value in child component, it gets reflected in parent
        }
    },
    methods: {
        getItemTotal(item) {
            return item.quantity * item.product.price
        },
        decrementQuantity(item) {
            item.quantity = item.quantity - 1;
            if (item.quantity === 0) {
                this.$emit('removeFromCart', item)
            }
            this.updateCart()
        },
        incrementQuantity(item) {
            item.quantity = item.quantity + 1;
            this.updateCart()
            console.log(this.$store.state.cart)
        },
        updateCart() {
            localStorage.setItem('cart', JSON.stringify(this.$store.state.cart))
        },
        removeFromCart(item) {
            this.$emit('removeFromCart', item)
            this.updateCart()
        }
    }
}


</script>