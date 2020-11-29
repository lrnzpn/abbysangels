<template>
  <v-app>
    <v-navigation-drawer
      v-model="drawer"
      fixed
      app
      floating
      :permanent="permanent"
      width="350"
      color="off-white"
    >
      <v-list>
        <v-list-item router to="/" class="brand pb-5">
            <v-img :lazy-src="require('../assets/logos/SONEAR-logo.png')" :src="require('../assets/logos/SONEAR-logo.png')" width="95" height="85" max-width="95" max-height="85"></v-img>
            <v-list-item-content class="ml-3">
                <v-list-item-title class="brand-name">{{title}}</v-list-item-title>
            </v-list-item-content>
        </v-list-item>

        <v-list-item class="nav-links" style="color:#68a691 !important">
            <v-list-item-action>
                <v-icon class="nav-icon">mdi-map-marker-outline</v-icon>
            </v-list-item-action>
             <v-list-item-content>
                <v-list-item-title class="nav-title">Map Filter</v-list-item-title>
            </v-list-item-content>
        </v-list-item>

        <v-list-item class="flex-wrap pb-5">
            <span class="d-block map-filter" 
                v-for="(business, i) in services" 
                :key="i" 
                @click="filter(business.service)"
                :class="checkFilter(business.service) ? 'active-filter' : ''"
                >{{business.service}}</span>
        </v-list-item>
        
        <v-list-item 
            router
            exact
            class="nav-links py-5"
            style="color:#68a691 !important"
            to='/register'
        >
            <v-list-item-action>
                <v-icon class="nav-icon">mdi-pencil-outline</v-icon>
            </v-list-item-action>
             <v-list-item-content>
                <v-list-item-title class="nav-title">
                    Register your business
                </v-list-item-title>
            </v-list-item-content>
        </v-list-item>

        <v-list-item 
            router
            exact
            class="nav-links py-5"
            style="color:#68a691 !important"
            to='/login'
        >
            <v-list-item-action>
                <v-icon class="nav-icon">mdi-login</v-icon>
            </v-list-item-action>
             <v-list-item-content>
                <v-list-item-title class="nav-title">
                    Log In
                </v-list-item-title>
            </v-list-item-content>
        </v-list-item>

        <v-list-item 
            router
            exact
            class="nav-links py-5"
            style="color:#68a691 !important"
            to='/profile'
        >
            <v-list-item-action>
                <v-icon class="nav-icon">mdi-account-box</v-icon>
            </v-list-item-action>
             <v-list-item-content>
                <v-list-item-title class="nav-title">
                    View your profile
                </v-list-item-title>
            </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar
      fixed
      app
      :class="permanent ? 'd-none' : ''"
      class="bg-orange"
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" color="#FEFDFF" />
      
      <v-img :lazy-src="require('../assets/logos/SONEAR-white.png')" :src="require('../assets/logos/SONEAR-white.png')" width="48" height="48" max-width="48" max-height="48"></v-img>
      <v-toolbar-title class="app-title">
          {{title}}
      </v-toolbar-title>
      <v-spacer />
    </v-app-bar>

    <v-main :style="permanent ? 'paddingTop: 0px' : null">
        <nuxt />
    </v-main>

    <v-footer
        :fixed="fixed"
        app
        class="bg-green"
        >
        
    </v-footer>
  </v-app>
</template>

<script>
export default {
  data () {
    return {
      drawer: true,
      fixed: false,
      permanent: true,
      title: 'SoNear',
    }
  },
  methods: {
      resize(e) {
          e.target.outerWidth < 960 ? this.permanent = false : this.permanent = true;
      },
      filter(val) {
          this.$store.commit('filter', val)
          
      },
      checkFilter(val) {
          return this.filters.includes(val)
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
  mounted() {
      window.addEventListener("resize", this.resize)
      window.innerWidth < 960 ? this.permanent = false : this.permanent = true;
  },
  beforeDestroy() {
      window.removeEventListener("resize", this.resize)
  }
}
</script>

<style lang="scss">

.brand {
    &.v-list-item--active::before {
        opacity: 0 !important;
    }
}

.off-white {
    background: $main-white;
    box-shadow: 5px -1px 20px -6px rgba(0, 0, 0, 0.2);
    z-index: 999 !important;
}

.brand-name {
    font-family: 'ProximaBold', 'Roboto', sans-serif;
    font-size: 3.75em !important;
    color: $main-orange;
}

.nav-links {
    font-family: 'ProximaBold', 'Roboto', sans-serif;

    .nav-icon {
        color: $main-green !important;
    }

    .nav-title {
        font-size: 1.25em;
    }

    &.v-list-item--active {
        &:before {
            background-color: $main-green;
            opacity: 1 !important;
        }

        .nav-icon,.nav-title {
            color: $main-white !important;
            z-index: 9;
        }
    }
}

.map-filter {
    padding: 4px 12px;
    border-radius: 20px;
    border: 0.8px solid $main-sky-blue;
    color: $main-sky-blue;
    background-color: $main-white;
    cursor: pointer;
    text-align: center;
    margin: 5px;
    &:hover {
        background-color: $main-sky-blue;
        color: $main-white;
    }

    &.active-filter {
        background-color: $main-sky-blue;
        color: $main-white;
    }
}

.bg-green {
    background: $main-green !important;
    z-index: 999 !important;
}

.bg-orange {
    background: $main-orange !important;
}

.static {
    background-size: contain;
    background-position: center;
    background-repeat: no-repeat;
    width: 100%;
    height: 100%;
}

.app-title {
    color: $main-white;
    font-family: 'ProximaBold', 'Roboto', sans-serif;
}

.w-100 {
    width: 100%;
}
</style>