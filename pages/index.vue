<template>
  <v-layout>
    <client-only v-if="lat && long">
      <l-map style="width: 100%;height: calc(100vh - 36px);z-index:200;" :zoom="13" :center="[lat, long]" class="map">
        <l-tile-layer
          url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"
        ></l-tile-layer>
        <l-marker :lat-lng="[lat,long]" @click="dialog = true">
            <l-icon>
                <v-icon large color="#202020">mdi-home</v-icon>
            </l-icon>
        </l-marker>
        <l-marker v-for="(d,i) in data" :key="i" :lat-lng="[d.fields.latitude, d.fields.longitude]">
            <l-icon>
                <v-icon large color="#202020">{{businesses[i].icon}}</v-icon>
            </l-icon>
        </l-marker>
      </l-map>
    </client-only>


    <v-dialog
      v-model="dialog"
      max-width="290"
        :fullscreen="mobDialog"
        :hide-overlay="mobDialog"
        :transition="mobDialog && 'dialog-bottom-transition'"
        content-class="override-modal"
        style="color:red;"
    >
      <v-card>
        <v-card-title class="headline">
          Use Google's location service?
        </v-card-title>

        <v-card-text>
          Let Google help apps determine location. This means sending anonymous location data to Google, even when no apps are running.
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn
            color="green darken-1"
            text
            @click="dialog = false"
          >
            Disagree
          </v-btn>

          <v-btn
            color="green darken-1"
            text
            @click="dialog = false"
          >
            Agree
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-layout>
</template>

<script>
import data from '../app/mainapp/fixtures/data.json'

export default {
    data() {
        return {
            lat: 0,
            long: 0,
            dialog: false,
            mobDialog: false,
            // businesses: null,
            data: data,
            businesses: [
                {service:'Hospital', icon:'mdi-hospital-box'},
                {service:'Pharmacy', icon:'mdi-pill' },
                {service:'Grocery', icon:'mdi-basket' },
                {service:'Restaurant', icon:'mdi-silverware-fork-knife'},
                {service:'Supermarket', icon:'mdi-cart' },
                {service:'Gas Station', icon:'mdi-gas-station' },
                {service:'Payment Gateway', icon:'mdi-contactless-payment-circle'},
                {service:'Bank', icon: 'mdi-bank'},
                {service:'Hardware', icon: 'mdi-hammer-wrench' },
                {service:'Utility Company', icon: 'mdi-toolbox' },
                {service:'Electronics', icon: 'mdi-flash' },
                {service:'Hospital', icon:'mdi-hospital-box'},
                {service:'Pharmacy', icon:'mdi-pill' },
                {service:'Grocery', icon:'mdi-basket' },
                {service:'Restaurant', icon:'mdi-silverware-fork-knife'},
                {service:'Supermarket', icon:'mdi-cart' },
                {service:'Gas Station', icon:'mdi-gas-station' },
                {service:'Payment Gateway', icon:'mdi-contactless-payment-circle'},
                {service:'Bank', icon: 'mdi-bank'},
                {service:'Hardware', icon: 'mdi-hammer-wrench' },
                {service:'Utility Company', icon: 'mdi-toolbox' },
                {service:'Electronics', icon: 'mdi-flash' },
                {service:'Hospital', icon:'mdi-hospital-box'},
                {service:'Pharmacy', icon:'mdi-pill' },
                {service:'Grocery', icon:'mdi-basket' },
                {service:'Restaurant', icon:'mdi-silverware-fork-knife'},
                {service:'Supermarket', icon:'mdi-cart' },
                {service:'Gas Station', icon:'mdi-gas-station' },
                {service:'Payment Gateway', icon:'mdi-contactless-payment-circle'},
                {service:'Bank', icon: 'mdi-bank'},
                {service:'Hardware', icon: 'mdi-hammer-wrench' },
                {service:'Utility Company', icon: 'mdi-toolbox' },
                {service:'Electronics', icon: 'mdi-flash' },
                {service:'Hospital', icon:'mdi-hospital-box'},
                {service:'Pharmacy', icon:'mdi-pill' },
                {service:'Grocery', icon:'mdi-basket' },
                {service:'Restaurant', icon:'mdi-silverware-fork-knife'},
                {service:'Supermarket', icon:'mdi-cart' },
                {service:'Gas Station', icon:'mdi-gas-station' },
                {service:'Payment Gateway', icon:'mdi-contactless-payment-circle'},
                {service:'Bank', icon: 'mdi-bank'},
                {service:'Hardware', icon: 'mdi-hammer-wrench' },
                {service:'Utility Company', icon: 'mdi-toolbox' },
                {service:'Electronics', icon: 'mdi-flash' },
                {service:'Hospital', icon:'mdi-hospital-box'},
                {service:'Pharmacy', icon:'mdi-pill' },
                {service:'Grocery', icon:'mdi-basket' },
                {service:'Restaurant', icon:'mdi-silverware-fork-knife'},
                {service:'Supermarket', icon:'mdi-cart' },
                {service:'Gas Station', icon:'mdi-gas-station' },
                {service:'Payment Gateway', icon:'mdi-contactless-payment-circle'},
                {service:'Bank', icon: 'mdi-bank'},
                {service:'Hardware', icon: 'mdi-hammer-wrench' },
                {service:'Utility Company', icon: 'mdi-toolbox' },
                {service:'Electronics', icon: 'mdi-flash' },
            ],
        }
    },
    methods: {
        geolocate() {
            // https://nuxtjs.org/faq/window-document-undefined/
            if (process.client) { 
                if(navigator.geolocation) {
                    navigator.geolocation.getCurrentPosition(pos => {
                        localStorage.setItem('userLatitude', pos.coords.latitude) // save to localStorage
                        localStorage.setItem('userLongitude', pos.coords.longitude)
                    }, err => {
                        console.error(err)
                    })
                } else {
                    console.log('Geolocation has not been enabled.')
                }

                this.lat = localStorage.getItem('userLatitude')
                this.long = localStorage.getItem('userLongitude')
            }

        },
        
        test() {
            console.log('yay')
        },
        resize(e) {
          e.target.outerWidth < 960 ? this.mobDialog = true : this.mobDialog = false;
      }
    },
    computed: {
        services() {
            return this.$store.state.services;
        },
        filters() {
            return this.$store.state.filters
        },
        randomIcon() {
            return this.businesses[Math.floor(Math.random() * this.businesses.length)]
        }
    },
    created() {
        this.geolocate()
    },
    mounted() {
      window.addEventListener("resize", this.resize)
      window.innerWidth < 960 ? this.mobDialog = true : this.mobDialog = false;
      console.log(this.businesses[1].icon)
    },
    beforeDestroy() {
        window.removeEventListener("resize", this.resize)
    }
}
</script>

<style lang="scss" scoped>
.override-modal {
    
    @media screen and (max-width: 960px) {
        height: 60% !important;
        top: auto !important;
        bottom: 0 !important;
    }
}


</style>
