<template>
  <div class="px-5 py-5">
      <div>
          <div class="blob-bg static"></div>
          <h3 class="profile-header">Check your profile</h3>
      </div>
      <v-row>
          <v-col >
              <div>
                  <span class="profile-business">hehe</span>
                    <p class="office-hours"><span>time</span> &bull; <span>Closes </span></p>
              </div>

            <div class="flex-wrap v-list-item">
                <!-- <span 
                class="d-block map-filter" 
                v-for="(tag, i) in services"
                :key="i"
                >
                    {{tag}}
                </span> -->
            </div>

          </v-col>
          <v-col>
              <div class="profile-image">
                  <img :src="image" :alt="business">
              </div>
          </v-col>
      </v-row>
      <v-row>
          <v-col cols="12" md="6">
              <span class="profile-label">Current Address</span>
              <p>hehe</p>
          </v-col>
      </v-row>
      <v-row>
          <v-col cols="12" md="6">
              <span class="profile-label">Description</span>
              <p>hehemon</p>
          </v-col>
          <v-col cols="12" md="6">
              <div class="d-flex align-center">
                  <v-icon large color="#202020">mdi-facebook</v-icon>
                  <span class="ml-2">NANIII</span>
              </div>
              <div class="d-flex align-center">
                  <v-icon large color="#202020">mdi-phone</v-icon>
                  <span class="ml-2">123</span>
              </div>
              <div class="d-flex align-center">
                  <v-icon large color="#202020">mdi-phone-classic</v-icon>
                  <span class="ml-2">123</span>
              </div>
          </v-col>
      </v-row>
  </div>
</template>

<script>
export default {

}
</script>

<style lang="scss" scoped>
.blob-bg {
    background-image: url('../assets/images/blob.png');
    width: 400px;
    height: 400px;
    position: absolute;
    top: -20px;
    right: 0;
}

.profile-header {
    color: $main-sky-blue; 
    font-family: 'ProximaBold', 'Roboto', sans-serif;
    font-size: 3.5em;
    width: 55%;
    line-height: 4.5rem;
    @media screen and (max-width: 960px) {
        display: none;
    }
}

.office-hours {
    span:first-child {
        color: $main-sky-blue
    }

    span:last-child {
        color: $main-red;
    }
}

.profile-label {
    font-family: 'ProximaBold', 'Roboto', sans-serif;
    color: $main-black;
    font-size: 1.5em;
    display: block;
}

.map-filter {
    @media screen and (max-width: 960px) {
        background-color: $main-sky-blue;
        color: $main-white;
    }
}
</style>