<template>
    <div class="py-5 px-5">
      <div>
            <div class="picture-bg static"></div>
            <h3 class="register-header">Place your business on our map!</h3>
            <div class="progress d-flex align-center mt-2">
                <span :class="progress >= 1 ? 'current' : ''"></span>
                <span :class="progress >= 2 ? 'current' : ''"></span>
                <span :class="progress == 3 ? 'current' : ''"></span>
            </div>
      </div>
      <v-form ref="form" v-model='valid' lazy-validation>
          <!-- page 1 -->
        <div class="page--1" v-if="progress === 1">
            <v-row>
                <v-col cols="12" md="6">
                    <span class="register-label">Address</span>
                    <v-text-field outlined v-model="address" :rules='rules.textRules' required></v-text-field>
                </v-col>
            </v-row>
            <v-row>
                <v-col cols="12" md="6">
                    <div>
                        <span class="register-label">Business Name</span>
                        <v-text-field outlined v-model="business" :rules='rules.textRules' required></v-text-field>
                    </div>
                    <div>
                        <span class="register-label">Service Hours</span>
                        <!-- days of the week -->
                        <div>
                            <v-range-slider
                            :tick-labels="days"
                            min="0"
                            max="6"
                            ticks="always"
                            tick-size="4"
                            track-color="#5F5F5F"
                            color="#FF5964"
                            thumb-color="#BF3942"
                            v-model="dayRange"
                            >
                            </v-range-slider>
                        </div>

                        <!-- time picker -->
                        <div>
                            <span class="mr-1">From</span> 
                            <v-dialog v-model="dialog1" max-width="400px">
                                <template v-slot:activator="{on, attrs}">
                                    <v-btn v-bind="attrs" v-on="on" class="time time-from mr-2" @click="dialog1 = true">
                                        {{convert24(from)}}
                                    </v-btn>
                                </template>
                                <v-card justify="center" align="center" full-width>
                                    <v-system-bar>
                                        <v-spacer></v-spacer>
                                        <v-btn icon @click="dialog1 = false">
                                            <v-icon>mdi-close</v-icon>
                                        </v-btn>
                                    </v-system-bar>
                                    <v-time-picker
                                        v-model="from"
                                        ampm-in-title
                                        format="ampm"
                                        class="time-picker"
                                    >
                                    </v-time-picker>
                                </v-card>
                            </v-dialog>
                            <span class="mr-1">To</span>
                            <v-dialog v-model="dialog2" max-width="400px">
                                <template v-slot:activator="{on, attrs}">
                                    <v-btn v-bind="attrs" v-on="on" class="time time-to" @click="dialog2 = true">
                                        {{convert24(to)}}
                                    </v-btn>
                                </template>
                                <v-card justify="center" align="center" full-width>
                                    <v-system-bar>
                                        <v-spacer></v-spacer>
                                        <v-btn icon @click="dialog2 = false">
                                            <v-icon>mdi-close</v-icon>
                                        </v-btn>
                                    </v-system-bar>
                                    <v-time-picker
                                        v-model="to"
                                        ampm-in-title
                                        format="ampm"
                                        class="time-picker"
                                    >
                                    </v-time-picker>
                                </v-card>
                            </v-dialog>
                        </div>
                    </div>
                </v-col>
                <v-col cols="12" md="6">
                    <span class="register-label">Description</span>
                    <v-textarea 
                    outlined 
                    v-model="description" 
                    :counter="160"
                    >
                    </v-textarea>
                </v-col>
              </v-row>
              <v-row>
                  <v-col>
                      <span class="register-label">Type of Business/Service</span>
                      <div class="flex-wrap v-list-item">
                          <span class="d-block map-filter" 
                            v-for="(business, i) in services" 
                            :key="i" 
                            @click="filters.includes(business) ? filters.splice(filters.indexOf(business), 1) : filters.push(business)"
                            :class="filters.includes(business) ? 'active-filter' : ''"
                            >{{business}}</span>
                      </div>
                  </v-col>
              </v-row>
            </div>
                <!-- page 2 -->
            <div class="page--2" v-else-if="progress === 2">
                <v-row>
                    <v-col cols="12" md="6">
                        <span class="register-label">Company Logo</span>
                        <div class="d-flex justify-center align-center d-md-block">
                            <div v-if="!image" class="image-upload-wrap">
                                <input type="file" @change="onFileChange" accept="image/*" class="file-upload-input">
                                <div class="d-flex justify-center align-center flex-column upload">
                                    <v-icon style="font-size: 5em" color="#fefdff">mdi-plus-circle-outline</v-icon>
                                    <span>Add store logo</span>
                                </div>
                            </div>
                            <div v-else class="image-uploaded-wrap">
                                <img :src="image" :alt="business">
                                <div>
                                    <v-btn @click="removeImage">
                                        Remove {{imageName}}
                                    </v-btn>
                                </div>
                            </div>
                        </div>

                        <span class="register-label pt-5">Website/Facebook Link</span>
                    <v-text-field outlined v-model="website" :rules="rules.textRules" placeholder="https://www.facebook.com/JuanDelaCruz" required></v-text-field>
                </v-col>
                <v-col class="d-flex align-md-end" cols="12" md="6">
                    <div class="w-100">
                        <span class="register-label">Contact Number</span>
                        <v-text-field outlined v-model="mobileNumber" :rules="rules.textRules" label="Mobile Number" placeholder="0912-345-6789" required></v-text-field>
                        <v-text-field outlined v-model="teleNumber" :rules="rules.textRules" label="Telephone Number" placeholder="123-4567" required></v-text-field>
                    </div>
                </v-col>
            </v-row>
            </div>

            <div class="page--3" v-else-if="progress === 3">
                <v-row>
                    <v-col col="12" md="6">
                        <span class="register-label">Email</span>
                        <v-text-field outlined v-model="email" required placeholder="juandelacruz@email.com" :rules="[rules.textRules, rules.email]"></v-text-field>

                        <span class="register-label">Password</span>
                        <v-text-field 
                            outlined 
                            v-model="password" 
                            required 
                            :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                            :rules="[rules.textRules, rules.password]"
                            label="Password"
                            hint="At least 8 characters"
                            counter
                            :type="show1 ? 'text' : 'password'"
                            @click:append="show1 = !show1"
                            >
                        </v-text-field>

                        <span class="register-label">Confirm Password</span>
                        <v-text-field 
                            outlined 
                            v-model="rePassword" 
                            required 
                            :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
                            :rules="[rules.textRules, rules.password, passwordConfirmationRule]"
                            counter
                            label="Re-enter Password"
                            :type="show2 ? 'text' : 'password'"
                            @click:append="show2 = !show2"
                            >
                        </v-text-field>

                        <div class="d-flex justify-md-end">
                            <v-btn color="#FF5964" class="btn-submit" :disabled="!valid" medium @click="validate">
                                <span>Submit</span>
                            </v-btn>
                        </div>
                    </v-col>
                </v-row>
            </div>
        </v-form>
        <div class="d-flex jusitfy-space-between align-center button-wrapper">
            <div class="back" v-if="progress >=2">
                <v-btn @click="dec" color="#FF5964" fab medium>
                    <v-icon large color="#FEFDFF">mdi-chevron-left</v-icon>
                </v-btn>
            </div>
            <v-spacer></v-spacer>
            <div class="next" v-if="progress <=2">
                <v-btn @click="inc" color="#FF5964" fab medium>
                    <v-icon large color="#FEFDFF">mdi-chevron-right</v-icon>
                </v-btn>
            </div>
        </div>
  </div>
</template>

<script>
export default {
    data() {
        return {
            progress: 1,
            valid: true,
            address: '',
            business: '',
            description: '',
            rules: {
                textRules: [v => !!v || 'Field is required.'],
                email: [v => {
                        const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
                        return pattern.test(v) || 'Invalid e-mail.'  
                }],
                password: [v => v.length >= 8 || 'Min 8 characters']
            },
            days: [
                'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'            
            ],
            dayRange: [1,5],
            from: '08:00',
            to: '17:00',
            dialog1: false,
            dialog2: false,
            mobileNumber: '',
            teleNumber: '',
            website: '',
            image: '',
            imageName: '',
            email: '',
            password: '',
            rePassword: '',
            show1: false,
            show2: false,
            services: [
                'Hospital', 'Pharmacy', 'Grocery', 
                'Restaurant', 'Supermarket', 'Gas Station',
                'Payment Gateway', 'Bank', 'Hardware', 'Utility Company',
                'Electronics'
            ],
            filters: [],
            isSuccess: false
        }
    },
    methods: {
        validate() {
            this.$refs.form.validate()
            // console.log(this.address, this.business, this.description, this.dayRange, this.from, this.to, this.mobileNumber, this.teleNumber, this.website, this.email, this.password, this.rePassword)
            console.log(this.image)
            let data = {
                "business_days": this.dayRange,
                "linked_services": this.filters,
                "business_name": this.business,
                "address": this.address,
                "latitude": localStorage.getItem('userLatitude'),
                "longtitude": localStorage.getItem('userLongitude'),
                "representative_name": "",
                "mobile_number": this.mobileNumber,
                "telephone_number": this.teleNumber,
                "website_link": this.website,
                "email": this.email,
                "password": this.password,
                "description": this.description,
                "office_hours_start": this.from,
                "office_hours_end": this.to,
                "weekly_views": null,
                "total_views": null,

            }

            console.log(data)

            // this.$store.dispatch('register', data)
            // .then(() => this.isSuccess = true)
            // .catch(err => {
            //     console.log(err)
            //     alert("Something went wrong, please refresh and try again.");
            // })
        },
        inc(){
            this.progress++;
        },
        dec(){
            this.progress--;
        },
        convert24(time) {
            time = time.toString ().match (/^([01]\d|2[0-3])(:)([0-5]\d)(:[0-5]\d)?$/) || [time];
            if (time.length > 1) { // If time format correct
                time = time.slice (1);  // Remove full string match value
                time[5] = +time[0] < 12 ? 'AM' : 'PM'; // Set AM/PM
                time[0] = +time[0] % 12 || 12; // Adjust hours
            }
            return time.join (''); // return adjusted time or original string
        },
        onFileChange(e) {
            if(process.client) {
                let files = e.target.files || e.dataTransfer.files;
                if(!files.length) return;
                this.createImage(files[0])
                this.imageName = files[0].name
            }
        },
        createImage(file) {
            if(process.client) {
                let image = new Image()
                let reader = new FileReader()
                let vm = this;

                reader.onload = e => {
                    vm.image = e.target.result
                }

                reader.readAsDataURL(file)
            }
        },
        removeImage(e) {
            this.image = '';
        }
    },
    computed: {
        passwordConfirmationRule() {
            return () => (this.password === this.rePassword) || 'Password must match'
        }
    },
    // mounted() {
    //     console.log(this.dayRange)
    // }
}
</script>

<style lang="scss" scoped>

.picture-bg {
    background-image: url('../assets/images/house.png');
    width: 400px;
    height: 400px;
    position: absolute;
    top: -5px;
    right: 0;

    @media screen and (max-width: 960px) {
        background-image: url('../assets/images/icon-house.png');
        position: relative;
        height: 300px;
        margin: 0 auto;
        top: unset;
        right: unset;
    }
}

.register-header {
    color: $main-red; 
    font-family: 'ProximaBold', 'Roboto', sans-serif;
    font-size: 3.5em;
    width: 55%;
    line-height: 4.5rem;

    @media screen and (max-width: 960px) {
        width: 100%;
        text-align: center;
        font-size: 1.5em;
    }
}

.progress {

    @media screen and (max-width: 960px) {
        justify-content: center;
    }

    span {
        display: block;
        border-radius: 18px;
        width: 4.5rem;
        height: .75rem;
        background: $alpha-sky-blue;
        margin-right: 1.5em;

        &.current {
            background: $main-sky-blue;
        }
    }
}

.register-label {
    font-family: 'ProximaBold', 'Roboto', sans-serif;
    color: $main-black;
    font-size: 1.5em;
    display: block;
}

.time {
    border: 0.8px solid #c4c4c4;
    padding: 5px 10px;
    border-radius: 5px;

    &-from {
        color: $main-sky-blue
    }
    &-to {
        color: $main-red;
    }
}

.time-picker {
    width: 100%;
}

.image-upload-wrap {
    border-radius: 50%;
    background: $main-gray;
    width: 275px;
    height: 275px;

    .file-upload-input {
        opacity: 0;
        position: absolute;
        width: inherit;
        height: inherit;
        cursor: pointer;
        outline: none;
    }

    .upload {
        height: 100%;

        span {
            color: $main-white;
        }
    }
}

.image-uploaded-wrap {
    border-radius: 50%;
    width: 275px;
    height: 275px;
    max-width: 90%;
    max-height: 90%;
    text-align: center;

    img {
        max-width: 90%;
        max-height: 90%;
        width: 275px;
        height: 275px;
        border-radius: 50%;
    }
}

.button-wrapper {
    width: 100%;
}

.btn-submit {
    border-radius: 20px;
    @media screen and (max-width: 960px) {
        width: 100%;
    }
    span {
        color: $main-white;
    }
}
</style>