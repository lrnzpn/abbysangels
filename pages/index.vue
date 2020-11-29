<template>
  <v-layout>
    <client-only v-if="lat && long">
      <l-map style="width: 100%;height: calc(100vh - 36px);" :zoom="13" :center="[lat, long]" class="map">
        <l-tile-layer
          url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"
        ></l-tile-layer>
        <l-marker :lat-lng="[lat,long]">
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
            lat: 0,
            long: 0,
            popupContent: 'Sentian HQ'
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
    },
    created() {
        this.geolocate()
    },
}
</script>

<style lang="scss" scoped>

</style>
