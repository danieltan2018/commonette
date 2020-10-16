<template>
  <div id="app">
    <v-app>
      <v-app-bar app fixed dark clipped-left color="primary" v-on:click="navigateRoute('/')">
        <v-toolbar-title class="headline">
          <span>Commonette</span>
        </v-toolbar-title>
        <v-spacer></v-spacer>

        <v-menu offset-y v-if="roomName">
          <template v-slot:activator="{ on }">
            <v-btn text icon color="white" v-on="on">
              <v-icon dark>mdi-account-group</v-icon>
            </v-btn>
            {{ roomName }}'s Room
          </template>
          <v-list dense>
            <v-list-item>
              <v-list-item-title>
                <h3>In this room:</h3>
              </v-list-item-title>
            </v-list-item>
            <v-list-item v-for="item in roomUsers" :key="item.name">
              <v-list-item-title>
                <v-icon>mdi-account-outline</v-icon> {{item.name}}
              </v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
      </v-app-bar>

      <router-view></router-view>

      <v-footer class="justify-center" color="#292929" height="100">
        <div class="title font-weight-light grey--text text--lighten-1 text-center">
          &copy; {{ (new Date()).getFullYear() }} — Commonette — IS216 G6T5
        </div>
      </v-footer>
    </v-app>
  </div>
</template>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>

<script>
export default {
  data: () => ({
    roomName: localStorage.getItem("roomName"),
    roomUsers: JSON.parse(localStorage.getItem("roomUsers")),
  }),
  methods: {
    navigateRoute(newpath) {
      this.$router.push(newpath);
    },
  },
};
</script>