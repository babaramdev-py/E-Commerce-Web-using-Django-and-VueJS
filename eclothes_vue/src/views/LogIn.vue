<template>
        <div class="page-log-in animate__animated animate__bounceInDown">
        <div class="columns">
            <div class="column is-4 is-offset-4 box mt-6">

                <h1 class="title is-2 has-text-centered mb-4">Log in</h1>
                <hr>
                <form @submit.prevent="submitForm">

                    <div class="field">
                        <label for="">Username</label>
                        <div class="control">
                            <div class="control">
                                <input type="text" class="input" v-model="username" placeholder="Username">
                            </div>
                        </div>
                    </div>

                    <div class="field">
                        <label for="">Password</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password" placeholder="Enter Password">
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <!-- <button class="delete"></button> -->
                        <p v-for="error in errors" :key="error">{{ error }}</p>
                    </div>

                    <div class="field">
                        <p class="control">
                            <button class="button is-primary">Login</button>
                        </p>
                    </div>

                </form>
                <hr>
                <h2 class="subtitle mb-2">Don't have an account? Sign Up Here</h2>
                <button class="button is-link is-light"><router-link to="/sign-up">Sign Up</router-link></button>
                <hr>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'
export default {
    name :'login',
    data(){
        return{
            username: '',
            password: '',
            errors: [],
        }
    },
    mounted() {
        document.title = 'EClothes | Login'
    },
    methods:{
        async submitForm(){
            axios.defaults.headers.common["Authorization"] = "" //reset previous token
            localStorage.removeItem("token") //remove the token from the local storage

            const formData = {
                username: this.username,
                password: this.password
            }

            await axios
                    .post('api/v1/token/login/',formData) // post the login data to back end /token/login
                    .then(response => {
                        toast({
                            message: 'Logged In!',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 4000,
                            position: 'bottom-center',
                            animate: { in: 'fadeInDownBig', out: 'fadeOutUpBig' }
                        })
                        const token = response.data.auth_token //equate JSON data's auth_token part = token
                        this.$store.commit('setToken',token)
                        axios.defaults.headers.common["Authorization"] = "Token " + token
                        localStorage.setItem("token", token)
                        const toPath = this.$route.query.to || '/cart'
                        this.$router.push(toPath)


                    })
                    .catch(error =>{
                        if(error.response){
                            for (const property in error.response.data){
                                this.errors.push(`${property}:${error.response.data[property]}`)
                            }
                        }
                        else{
                            this.errors.push('Something Went Wrong, please try again')
                            console.log(JSON.stringify(error))
                        }
                    })
        }
    }
}
</script>