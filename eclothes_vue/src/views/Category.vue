<template>
    <div class="page-category">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h2 class="is-size-2 has-text-centered">{{ category.name }} Products</h2>
            </div>
        </div>
        <div class="columns is-multiline ">

            <div class="column is-12">
                <h2 class="is-size-2 has-text-centered">
                    <!-- {{ category.name }} Products -->
                </h2>
            </div>

            <ProductBox v-for="product in category.products" :key="product.id"
                :product = "product"
            />


            



        </div>
    </div>
</template>

<script>
import axios from 'axios';
import { toast } from 'bulma-toast'
import ProductBox from '@/components/ProductBox.vue';
export default {
    name: "Category",
    data() {
        return {
            category: {
                products: []
            }
        };
    },
    components: {
        ProductBox
    },
    mounted() {
        this.getCategory();
    },
    methods: {
        async getCategory() {
            this.$store.commit("setIsLoading", true);
            const category_slug = this.$route.params.category_slug;
            await axios.get(`/api/v1/products/${category_slug}`)
                .then(response => {
                this.category = response.data;
                console.log(this.category);
                document.title = this.category.name + " | EClothes";
                this.$store.commit("setIsLoading", false);
            })
                .catch(error => {
                console.log(error);
                toast({
                    message: "Something Went Wrong",
                    type: "is-danger",
                    dismissible: true,
                    pauseOnHover: true,
                    duration: 2000,
                    position: "top-right",
                });
            });
        }
    },
    components: { ProductBox }
}


</script>