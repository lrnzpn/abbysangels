<template>
  <div class="px-5 py-5">
      <v-form ref="form" v-model="valid" lazy-validation>
            <v-layout class="d-flex justify-center align-center">
                <v-card class="login">
                    <div>
                        <v-img class="logo" :lazy-src="require('../assets/logos/SONEAR-biglogo.png')" :src="require('../assets/logos/SONEAR-biglogo.png')"></v-img>
                    </div>
                    <div>
                        <span class="register-label">Email Address</span>
                        <v-text-field outlined v-model="email" required :rules="[rules.textRules, rules.email]"></v-text-field>
                    </div>

                    <div>
                        <span class="register-label">Password</span>
                        <v-text-field 
                            outlined 
                            v-model="password" 
                            required 
                            :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                            :rules="[rules.textRules, rules.password]"
                            hint="At least 8 characters"
                            counter
                            :type="show1 ? 'text' : 'password'"
                            @click:append="show = !show"
                            >
                        </v-text-field>
                    </div>
                    <div class="d-flex justify-center align-center">
                        <v-btn color="#FF5964" class="btn-submit" :disabled="!valid" x-large>
                            <span>Submit</span>
                        </v-btn>
                    </div>
                </v-card>
            </v-layout>
      </v-form>
  </div>
</template>

<script>
export default {
    data() {
        return {
            valid: true,
            show: false,
            rules: {
                textRules: [v => !!v || 'Field is required.'],
                email: [v => {
                        const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
                        return pattern.test(v) || 'Invalid e-mail.'  
                }],
                password: [v => v.length >= 8 || 'Min 8 characters']
            },
            email: '',
            password: '',
        }
    }
}
</script>

<style lang="scss" scoped>
.register-label {
    font-family: 'ProximaBold', 'Roboto', sans-serif;
    color: $main-gray;
    font-size: 1.5em;
    display: block;
}

.btn-submit {
    border-radius: 20px;
    span {
        color: $main-white;
    }
}
.login {
    box-shadow: none !important;
    .logo {
        width:375px;
        height: 375px;
        @media screen and (max-width: 960px) {
            width:250px;
            height: 250px;
        }
    }
}
</style>