<template>
  <v-layout>
    <client-only v-if="lat && long">
      <l-map style="width: 100%;height: calc(100vh - 36px);z-index:200;" :zoom="13" :center="[lat, long]" class="map">
        <l-tile-layer
          url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"
        ></l-tile-layer>
        <l-marker :lat-lng="[lat,long]" @click="dialog = true">
            <l-icon>
                <v-icon large color="#202020">mdi-facebook</v-icon>
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
        class="dialog-modal"
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
export default {
    data() {
        return {
            lat: 0,
            long: 0,
            dialog: false,
            mobDialog: false
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
    },
    created() {
        this.geolocate()
    },
    mounted() {
      window.addEventListener("resize", this.resize)
      window.innerWidth < 960 ? this.mobDialog = true : this.mobDialog = false;
    },
    beforeDestroy() {
        window.removeEventListener("resize", this.resize)
    }
}
</script>

<style lang="scss" scoped>

</style>
