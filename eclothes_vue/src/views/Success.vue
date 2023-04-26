<template>
    <div class="page-success animate__animated animate__bounceInDown">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title has-text-center">Order Placed</h1>
                <h2 class="subtitle">We Shall verify the phone numbers and the orders will be processed in one working week</h2>
                <h3>Thank you for shopping with us</h3>
            </div>
        </div>

    </div>
</template>

<script>
export default {
    name: 'Success',
    mounted() {
        document.title = 'EClothes | Success!'
        
    },
    methods: {
        reloadPage() {
            window.location.reload();
        }
    }
}
</script>