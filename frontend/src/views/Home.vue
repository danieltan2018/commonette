<template>
  <div class="home">
    <v-main>
      <v-dialog v-model="createRoomPopup" max-width="350">
        <v-card>
          <v-card-title class="headline justify-center">Create New Room</v-card-title>
          <v-card-text>
            <v-form @submit.prevent v-model="valid" ref="form">
              <v-text-field label="Enter a room name" v-model="roomName" :rules="inputRequiredRule" autofocus></v-text-field>
              <p v-if="errors" class="red--text">
                {{ errorMessage }}
              </p>
              <v-btn color="primary" :disabled="!valid" v-on:click="createRoom">Enter</v-btn>
            </v-form>
          </v-card-text>
        </v-card>
      </v-dialog>
      <v-dialog v-model="joinRoomPopup" max-width="350">
        <v-card>
          <v-card-title class="headline justify-center">Join Existing Room</v-card-title>
          <v-card-text>
            <v-form @submit.prevent v-model="valid" ref="form">
              <v-text-field label="Enter the room code" v-model="roomCode" :rules="inputRequiredRule" autofocus></v-text-field>
              <p v-if="errors" class="red--text">
                {{ errorMessage }}
              </p>
              <v-btn color="primary" :disabled="!valid" v-on:click="joinRoom">Enter</v-btn>
            </v-form>
          </v-card-text>
        </v-card>
      </v-dialog>

      <v-img src="https://images.unsplash.com/photo-1487017159836-4e23ece2e4cf?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1951&q=80">
        <v-theme-provider dark>
          <v-container fill-height>
            <v-row align="center" class="white--text mx-auto" justify="center">
              <v-col class="white--text text-center" cols="12" tag="h1">
                <span :class="[$vuetify.breakpoint.smAndDown ? 'display-1' : 'display-2']" class="font-weight-light">
                  WELCOME TO
                </span>
                <br>
                <span :class="[$vuetify.breakpoint.smAndDown ? 'display-3': 'display-4']" class="font-weight-black">
                  COMMONETTE
                </span>
              </v-col>

              <v-row justify="center">
                <v-btn elevation="2" large class="ma-2" v-on:click="createRoomPopup = true">
                  Create Room
                </v-btn>

                <v-btn elevation="2" large class="ma-2" @click="$vuetify.goTo('#about')">
                  About
                </v-btn>

                <v-btn elevation="2" large v-on:click="joinRoomPopup = true" class="ma-2">
                  Join Room
                </v-btn>
              </v-row>

            </v-row>
          </v-container>
        </v-theme-provider>
      </v-img>

      <section id="about">
        <div class="py-12"></div>

        <v-container class="text-center">
          <h2 class="display-2 font-weight-bold mb-3">What is commonette?</h2>

          <v-responsive class="mx-auto mb-8" width="56">
            <v-divider class="mb-1"></v-divider>
            <v-divider></v-divider>
          </v-responsive>

          <v-responsive class="mx-auto title font-weight-light mb-8" max-width="720">
            info about commonette here
          </v-responsive>

          <v-btn color="grey" v-on:click="navigateRoute('/recommend')" outlined large>
            <span class="grey--text text--darken-1 font-weight-bold">
              Recommendation Page (temporary)
            </span>
          </v-btn>
        </v-container>

        <div class="py-12"></div>
      </section>

      <section id="mediums" class="grey lighten-3">
        <div class="py-12"></div>

        <v-container class="text-center">
          <h2 class="display-2 font-weight-bold mb-3">Mediums</h2>

          <v-responsive class="mx-auto mb-12" width="56">
            <v-divider class="mb-1"></v-divider>

            <v-divider></v-divider>
          </v-responsive>

          <v-row>
            <v-col v-for="({ icon, title, text }, i) in mediums" :key="i" cols="12" md="3">
              <v-card class="py-12 px-4" color="grey lighten-5" flat>
                <v-theme-provider dark>
                  <div>
                    <v-avatar color="primary" size="88">
                      <v-icon large v-text="icon"></v-icon>
                    </v-avatar>
                  </div>
                </v-theme-provider>

                <v-card-title class="justify-center font-weight-black text-uppercase" v-text="title"></v-card-title>

                <v-card-text class="subtitle-1" v-text="text">
                </v-card-text>
              </v-card>
            </v-col>
          </v-row>
        </v-container>

        <div class="py-12"></div>
      </section>

      <section id="hero2">
        <v-parallax :height="$vuetify.breakpoint.smAndDown ? 700 : 200" src="https://images.unsplash.com/photo-1416339442236-8ceb164046f8?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1892&q=80">
          <v-container fill-height>
            <h2 class="mx-auto display-2 font-weight-bold mb-3" max-width="720">
              info about commonette here
            </h2>
            <v-row class="mx-auto" justify="center">

              <v-btn elevation="2" large class="ma-2" v-on:click="createRoomPopup = true">
                Create Room
              </v-btn>

              <v-btn elevation="2" large v-on:click="joinRoomPopup = true" class="ma-2">
                Join Room
              </v-btn>

            </v-row>
          </v-container>
        </v-parallax>
      </section>

    </v-main>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      createRoomPopup: false,
      joinRoomPopup: false,
      valid: false,
      roomCode: "",
      roomName: "",
      errors: false,
      errorMessage: "",
      inputRequiredRule: [(v) => v.length > 0 || "Required"],
      mediums: [
        {
          icon: "mdi-youtube",
          title: "YouTube",
          text: "See recommended videos for you and your friends.",
        },
        {
          icon: "mdi-spotify",
          title: "Spotify",
          text:
            "Generate Spotify recommendations from you and your friends' favourite songs.",
        },
        {
          icon: "mdi-book",
          title: "Books",
          text: "Find books ",
        },
        {
          icon: "mdi-filmstrip",
          title: "Movies",
          text: "I don't know what I'm doing",
        },
      ],
    };
  },
  methods: {
    navigateRoute(newpath) {
      this.$router.push(newpath);
    },
    createRoom() {
      if (this.$refs.form.validate()) {
        let roomName = this.roomName;
        axios({
          url: "/create-room/" + roomName,
          method: "GET",
        })
          .then((response) => {
            console.log(response.data);
            localStorage.setItem("roomCode", response.data.code);
            localStorage.setItem("roomName", response.data.name);
            this.navigateRoute('/questionnaire');
          })
          .catch((error) => {
            this.errors = true;
            this.errorMessage = "API Connection Error";
            if (error.response) {
              this.errorMessage = "Unable to create room";
            }
          });
      }
    },
    joinRoom() {
      if (this.$refs.form.validate()) {
        let roomCode = this.roomCode;
        axios({
          url: "/join-room/" + roomCode,
          method: "GET",
        })
          .then((response) => {
            console.log(response.data);
            localStorage.setItem("roomCode", response.data.code);
            localStorage.setItem("roomName", response.data.name);
            this.navigateRoute('/questionnaire');
          })
          .catch((error) => {
            this.errors = true;
            this.errorMessage = "API Connection Error";
            if (error.response) {
              this.errorMessage = "Unable to join room";
            }
          });
      }
    },
  },
};
</script>
