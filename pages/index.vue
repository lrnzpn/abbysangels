<template>
  <v-layout>
    hello
    <client-only v-if="lat && long">
      <l-map style="width: 100%;height: 50vh;" :zoom="13" :center="[lat, long]">
        <l-tile-layer
          url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"
        ></l-tile-layer>
        <l-marker :lat-lng="[lat,long]" :draggable="draggable">
          <l-popup :content="popupContent"></l-popup>
        </l-marker>
      </l-map>
    </client-only>
  </v-layout>
</template>

<script>
export default {
    data() {
        return {
            lat: null,
            long: null,
            draggable: true,
            popupContent: 'Sentian HQ'
        }
    },
    methods: {
        geolocate() {
            // https://nuxtjs.org/faq/window-document-undefined/
            if (process.client) { 
                if(navigator.geolocation) {
                    navigator.geolocation.getCurrentPosition(pos => {
                        this.$store.commit('userLocation', pos)
                    }, err => {
                        console.error(err)
                    })
                } else {
                    console.log('Geolocation has not been enabled.')
                }
            }

            if(this.$store.state.userLoc) {
                this.lat = this.$store.state.userLoc.coords.latitude
                this.long = this.$store.state.userLoc.coords.longitude
            }
        },
    },
    created() {
        this.geolocate()
    },
}
</script>

<style lang="scss" scoped>

</style>
