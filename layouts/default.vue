<template>
  <v-app>
    <v-navigation-drawer
      v-model="drawer"
      :clipped="clipped"
      fixed
      app
      floating
      :permanent="permanent"
        class="orange-bg"
    >
      <v-list>
        <v-list-item>
            <v-list-item-content>
                <v-list-item-title class="title">
                    {{title}}
                </v-list-item-title>
            </v-list-item-content>
        </v-list-item>
        <v-divider></v-divider>
        <v-list-item
          v-for="(item, i) in items"
          :key="i"
          :to="item.to"
          router
          exact
        >
          <v-list-item-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title v-text="item.title" />
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar
      :clipped-left="clipped"
      fixed
      app
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      
      <v-toolbar-title v-text="title" />
      <v-spacer />
    </v-app-bar>

    <v-main>
      <v-container>
        <nuxt />
      </v-container>
    </v-main>
    
    <v-footer
      :fixed="fixed"
      app
    >
        hello
    </v-footer>
  </v-app>
</template>

<script>
export default {
  data () {
    return {
      clipped: false,
      drawer: true,
      fixed: false,
      permanent: true,
      items: [
        {
          icon: 'mdi-apps',
          title: 'Welcome',
          to: '/'
        },
      ],
      title: 'SoNear',
      
    }
  },
  methods: {
      resize(e) {
          e.target.outerWidth < 960 ? this.permanent = false : this.permanent = true;
      }
  },
  mounted() {
      window.addEventListener("resize", this.resize)
  },
  beforeDestroy() {
      window.removeEventListener("resize", this.resize)
  }
}
</script>

<style lang="scss" scoped>
.orange-bg {
    background-color: $main-orange !important;
}
</style>