<template>
        <div class="page-log-in">
        <div class="columns">
            <div class="column is-4 is-offset-4 box mt-6">

                <h1 class="title">Sign Up</h1>
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
                            <button class="button is-primary">Submit</button>
                        </p>
                    </div>

                </form>
                <hr>
                <h2 class="subtitle mb-2">Don't have an account? Sign Up Here</h2>
                <button class="button is-link is-light"><router-link to="/sign-up">Sign Up</router-link></button>
            </div>
        </div>
    </div>
</template>

<script>
    export default{
        name: 'login',

    }
</script>