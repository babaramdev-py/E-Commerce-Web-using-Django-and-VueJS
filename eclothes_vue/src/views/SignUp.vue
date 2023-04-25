<template>
    <div class="page-sign-up animate__animated animate__bounceInUp">
        <div class="columns">
            <div class="column is-4 is-offset-4 box mt-6">

                <h1 class="title is-2 has-text-centered mb-4">Sign Up</h1>
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

                    <div class="field">
                        <label for="">Enter Password Again</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password2" placeholder="Re-type Password">
                        </div>
                    </div>


                    <div class="notification is-danger" v-if="errors.length">
                        <!-- <button class="delete"></button> -->
                        <p v-for="error in errors" :key="error">{{ error }}</p>
                    </div>

                    <div class="field">
                        <p class="control">
                            <button class="button is-primary" href="/log-in">Submit</button>
                        </p>
                    </div>

                </form>
                <hr>
                <h2 class="subtitle mb-2">Have an account? Login Instead</h2>
                <button class="button is-link is-light"><router-link to="/log-in">Log in </router-link></button>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import { toast } from 'bulma-toast'
export default {
    name: 'SignUp',
    data() {
        return {
            username: '',
            password: '',
            password2: '',
            errors: [],
        }
    },
    mounted() {
        document.title = 'EClothes | Sign Up'
    },
    methods: {
        submitForm() {
            this.errors = [] //set this to empty on submit because we want to be able to submit multiple times.
            if(this.username === ''){
                this.errors.push('The username is missing')
            }
            if(this.password === ''){
                this.errors.push('The password is missing')
            }
            if(this.password2 === ''){
                this.errors.push('Please repeat the password')
            }
            if(this.password != this.password2)
            {
                this.errors.push("Passwords don't match")
            }

            if(!this.errors.length){
                const formData = {
                    username: this.username,
                    password: this.password,
                }

                axios
                    .post("api/v1/users/",formData)
                    .then(response =>{
                        toast({
                            message: 'Account Created! Please log in!',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 5000,
                            position: 'top-center',
                            animate: { in: 'fadeInDownBig', out: 'fadeOutUpBig' }
                        })
                        this.$router.push('/log-in') // Had a horrible bug on this line, a spelling typo
                    })
                    .catch(error =>{
                        if(error.response){
                            for(const property in error.response.data){
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }
                            console.log("Error occured")
                        }
                        else if(error.message){
                            this.errors.push('Something went wrong. Try again!')
                            console.log(JSON.stringify(error))
                            console.log("Error occured")
                        }
                    })
            }
        },
    },


}


</script>