<template>
  <div class="home">
    <v-content>
      <v-dialog v-model="roompopup" max-width="350">
        <v-card>
          <v-card-title class="headline justify-center">Join existing Room</v-card-title>
          <v-card-text>
            Enter the room code to join
            <v-text-field label="Room code" v-model="room" required></v-text-field>
          </v-card-text>
          <v-card-actions class="justify-center">
            <v-btn color="primary" v-on:click="navigateRoute('/login')">Return to login page</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
      <v-dialog v-model="createroompopup" max-width="350">
        <v-card>
          <v-card-title class="headline justify-center">Let's get started</v-card-title>
          <v-card-text>
            Enter your new room name!
            <v-text-field label="Room name" v-model="room" required></v-text-field>
          </v-card-text>
          <v-card-actions class="justify-center">
            <v-btn color="primary" v-on:click="navigateRoute('/questionnaire')">Create Room</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
      <section id="hero">
        <v-row no-gutters>
          <!-- background image at the top -->
          <v-img :min-height="'calc(100vh - ' + $vuetify.application.top + 'px)'" src="https://images.unsplash.com/photo-1487017159836-4e23ece2e4cf?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1951&q=80">
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

                  

                  <!-- <v-row align='center'>
                    <v-btn class="align-self-end" fab outlined @click="$vuetify.goTo('#about')">
                      <v-icon>mdi-chevron-double-down</v-icon>
                    </v-btn>
                  </v-row> -->
                  
                  <v-row justify="center">
                    <v-btn elevation="2" large class="ma-2" v-on:click="createroompopup = true">
                      Create Room
                    </v-btn>

                    <v-btn elevation="2" large class="ma-2" @click="$vuetify.goTo('#about')">
                      About
                    </v-btn>

                    <v-btn elevation="2" large v-on:click="roompopup = true" class="ma-2">
                      Join Room
                    </v-btn>
                  </v-row>
                  

                </v-row>
              </v-container>
            </v-theme-provider>
          </v-img>
        </v-row>
      </section>

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

          <!-- <v-avatar class="elevation-12 mb-12" size="128">
            <v-img src="https://cdn.vuetifyjs.com/images/john.png"></v-img>
          </v-avatar> -->

          <div></div>

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

      <!-- <section id="stats">
        <v-parallax :height="$vuetify.breakpoint.smAndDown ? 700 : 500" src="https://images.unsplash.com/photo-1510915228340-29c85a43dcfe?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1950&q=80">
          <v-container fill-height>
            <v-row class="mx-auto">
              <v-col v-for="[value, title] of stats" :key="title" cols="12" md="3">
                <div class="text-center">
                  <div class="display-3 font-weight-black mb-4" v-text="value"></div>

                  <div class="title font-weight-regular text-uppercase" v-text="title"></div>
                </div>
              </v-col>
            </v-row>
          </v-container>
        </v-parallax>
      </section> -->

      <section id="hero2">
        <v-parallax :height="$vuetify.breakpoint.smAndDown ? 700 : 200" src="https://images.pexels.com/photos/936048/pexels-photo-936048.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260">
          <v-container fill-height>
            <h2 class="mx-auto display-2 font-weight-bold mb-3" max-width="720">
              info about commonette here
            </h2>
            <v-row class="mx-auto" justify="center">
              
              <v-btn elevation="2" large class="ma-2" v-on:click="createroompopup = true">
                Create Room
              </v-btn>

              <v-btn elevation="2" large v-on:click="roompopup = true" class="ma-2">
                Join Room
              </v-btn>

            </v-row>
          </v-container>
        </v-parallax>
      </section>


    </v-content>
  </div>
</template>

<script>
export default {
  data() {
    return {
      roompopup: false,
      createroompopup: false,
      articles: [
        {
          src:
            "https://images.unsplash.com/photo-1423784346385-c1d4dac9893a?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1950&q=80",
          title: "Mobile first & Responsive",
          text:
            "Phasellus lorem enim, luctus ut velit eget, convallis egestas eros. Sed ornare ligula eget tortor tempor, quis porta tellus dictum.",
        },
        {
          src:
            "https://images.unsplash.com/photo-1475938476802-32a7e851dad1?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1950&q=80",
          title: "Think outside the box",
          text:
            "Nam ut leo ipsum. Maecenas pretium aliquam feugiat. Aenean vel tempor est, vitae tincidunt risus. Sed sodales vestibulum nibh.",
        },
        {
          src:
            "https://images.unsplash.com/photo-1416339442236-8ceb164046f8?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1892&q=80",
          title: "Small changes, big difference",
          text:
            "Vestibulum in dictum velit, in rhoncus nibh. Maecenas neque libero, interdum a dignissim in, aliquet vitae lectus. Phasellus lorem enim, luctus ut velit eget.",
        },
      ],
      mediums: [
        {
          icon: "mdi-youtube",
          title: "YouTube",
          text:
            "See recommended videos for you and your friends.",
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
          text:
            "Find books ",
        },
        {
          icon: "mdi-filmstrip",
          title: "Movies",
          text:
            "I don't know what I'm doing"
        },
      ],
      stats: [
        ["24k", "Github Stars"],
        ["330+", "Releases"],
        ["1m", "Downloads/mo"],
        ["5m", "Total Downloads"],
      ],
    };
  },
  methods: {
    navigateRoute(newpath) {
      this.$router.push(newpath);
    },
  },
};
</script>
