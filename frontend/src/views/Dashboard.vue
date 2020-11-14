<template>
  <v-main class="home">

    <span>
      <br>
      <h3 class="color-white">Invite your friends to join this room using the code <b class="color-highlight1">{{roomCode}} </b>
        <v-btn v-clipboard="roomCode" icon color="#E3E9F2" @click="snackbar = true">
          <v-icon small>mdi-content-copy</v-icon>
        </v-btn>
        <v-snackbar v-model="snackbar" :timeout="2000">
          Copied to clipboard!
          <template v-slot:action="{ attrs }">
            <v-btn color="#E3E9F2" text v-bind="attrs" @click="snackbar = false">
              Close
            </v-btn>
          </template>
        </v-snackbar>
      </h3>
      <h4 class="color-white">Make sure to <font class="color-highlight2">save the code</font> before exiting!</h4>
      <br>
      <v-btn large v-on:click="navigateRoute('/recommend')">View Recommendations</v-btn>
      <br>
      <br>
    </span>

    <v-btn v-scroll="onScroll" v-show="fab" fab dark fixed bottom right color="pink" @click="$vuetify.goTo(0)">
      <v-icon>mdi-arrow-up</v-icon>
    </v-btn>

    <v-row>
      <v-col cols="3"></v-col>
      <v-col cols="6" class="color-white">
        <h1>Here are some statistics!</h1><br>
        <h2>Total No. Of Users In Room: <b class="color-highlight2">{{userCount}}</b></h2>
      </v-col>
      <v-col cols="3"></v-col>
    </v-row>

    <v-container fluid>
      <v-row v-if="roomUsers.length != 1">
        <v-col cols="4"></v-col>
        <v-col cols="4">
          <marquee-text :repeat="1" :duration="marqueeSpeed" :paused="isPaused" @mouseenter="isPaused = !isPaused" @mouseleave="isPaused = false">
            <v-badge v-for="user in roomUsers" :key="user.name" :content="user.name" color='teal' bottom left overlap>
              <v-img v-if='user.gender == "M"' src='../images/Tanjiro.png' class="chibi-male"></v-img>
              <v-img v-else src='../images/Nezuko.png' class="chibi-female"></v-img>
            </v-badge>
          </marquee-text>
        </v-col>
        <v-col cols="4"></v-col>
      </v-row>
      <v-row v-else>
        <v-col cols="4"></v-col>
        <v-col cols="4">
          <v-badge v-for="user in roomUsers" :key="user.name" :content="user.name" color='teal' bottom left overlap>
            <RotatingImage image="Nezuko" height="150" v-if="user.gender == 'F'" class="w-150"></RotatingImage>
            <RotatingImage image="Tanjiro" height="150" v-else class="w-150"></RotatingImage>
          </v-badge>
        </v-col>
        <v-col cols="4"></v-col>
      </v-row>
    </v-container>

    <v-container class="px-10">
      <v-row>
        <v-col cols="12" sm=6 id="chart" data-aos="fade-right" data-aos-delay="100" data-aos-duration="1000">
          <!-- Put piechart for language here -->
          <h3 class="color-white">Movie Languages Selected<br></h3>
          <pie-chart :chart-data="languagePieChart.chartData" v-if="langReady">
          </pie-chart>
        </v-col>
        <v-col cols="12" sm=6 data-aos="fade-left" data-aos-delay="100" data-aos-duration="1000">
          <h3 class="color-white">Gender Population<br></h3>
          <pie-chart :chart-data="genderPieChart.chartData" v-if="genderReady">
          </pie-chart>
        </v-col>
      </v-row>
    </v-container>

    <v-row>
      <v-col cols="2"></v-col>
      <v-col cols="8" class="color-white">
        Categories or Genres ranked were assigned weights!
        <br><br>Total Weights were calculated to display the <b class="color-highlight1">TOP</b> Categories/Genres below!
      </v-col>
      <v-col cols="2"></v-col>
    </v-row>

    <v-container>
      <v-row>
        <v-col cols="12" md=6 data-aos="fade-down-right" data-aos-duration="1000" v-if="youtubeReady">
          <v-card type="chart" dark>
            <v-card-title>
              <v-icon color="red" class="media-icons" large>mdi-youtube</v-icon>
              Top Youtube Categories
            </v-card-title>
            <div class="chart-area">
              <bar-chart class="bar-chart" chart-id="youtubeStats" :chart-data="youtubeBarChart.chartData" :gradient-stops="youtubeBarChart.gradientStops" :extra-options="youtubeBarChart.extraOptions">
              </bar-chart>
            </div>
          </v-card>
        </v-col>
        <v-col cols="12" md=6 data-aos="fade-down-left" data-aos-duration="1000" data-aos-delay="500" v-if="bookReady">
          <v-card type="chart" dark>
            <v-card-title>
              <v-icon color="blue" class="media-icons" large>mdi-book</v-icon>
              Top Book Genres
            </v-card-title>
            <div class="chart-area">
              <bar-chart class="bar-chart" chart-id="bookStats" :chart-data="bookBarChart.chartData" :gradient-stops="bookBarChart.gradientStops" :extra-options="bookBarChart.extraOptions">
              </bar-chart>
            </div>
          </v-card>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12" md=6 data-aos="fade-up-right" data-aos-duration="1000" data-aos-delay="600" v-if="movieReady">
          <v-card type="chart" dark>
            <v-card-title>
              <v-icon color="rgb(255, 0, 128)" class="media-icons" large>mdi-movie-open</v-icon>
              Top Movie Genres
            </v-card-title>
            <div class="chart-area">
              <bar-chart class="bar-chart" chart-id="movieStats" :chart-data="movieBarChart.chartData" :gradient-stops="movieBarChart.gradientStops" :extra-options="movieBarChart.extraOptions">
              </bar-chart>
            </div>
          </v-card>
        </v-col>
        <v-col cols="12" md=6 data-aos="fade-up-left" data-aos-duration="1000" data-aos-delay="1000" v-if="spotifyReady">
          <v-card type="chart" dark>
            <v-card-title>
              <v-icon color="green" class="media-icons" large>mdi-spotify</v-icon>
              Top Spotify Genres
            </v-card-title>
            <div class="chart-area">
              <bar-chart class="bar-chart" chart-id="spotifyStats" :chart-data="spotifyBarChart.chartData" :gradient-stops="spotifyBarChart.gradientStops" :extra-options="spotifyBarChart.extraOptions">
              </bar-chart>
            </div>
          </v-card>
        </v-col>
      </v-row>
    </v-container>

  </v-main>
</template>

<script>
import BarChart from "../components/Charts/BarChart";
import * as chartConfigs from "../components/Charts/config";
import MarqueeText from "../components/MarqueeText.vue";
import PieChart from "../components/Charts/PieChart";
import RotatingImage from "../components/RotatingImage/RotatingImage.vue";
import config from "../config";
import axios from "axios";

export default {
  components: {
    BarChart,
    MarqueeText,
    "pie-chart": PieChart,
    RotatingImage,
  },
  props: {
    roomCode: {
      type: String,
      default: "",
    },
  },
  data: () => ({
    snackbar: false,
    roomUsers: [],
    userCount: 0,
    maleCount: 0,
    femaleCount: 0,
    youtubeReady: false,
    bookReady: false,
    movieReady: false,
    spotifyReady: false,
    langReady: false,
    genderReady: false,
    isPaused: false,
    fab: false,
    height: 200,
    languagePieChart: {
      // extraOptions: chartConfigs.pieChartOptions,
      chartData: {
        labels: [],
        datasets: [
          {
            data: [],
            borderColor: [
              "rgb(81, 81, 118)",
              "rgb(81, 81, 118)",
              "rgb(81, 81, 118)",
              "rgb(81, 81, 118)",
              "rgb(81, 81, 118)",
              "rgb(81, 81, 118)",
            ],
            backgroundColor: [
              "rgb(173,216,230,0.8)",
              "rgb(135,206,250,0.8)",
              "rgb(30,144,255,0.8)",
              "rgb(106,90,205,0.8)",
              "rgb(199,21,133,0.8)",
              "rgb(75,0,130, 0.8)",
              "rgb(0, 0, 139, 0.8)",
            ],
          },
        ],
      },
    },
    genderPieChart: {
      chartData: {
        labels: ["Female", "Male"],
        datasets: [
          {
            data: [],
            borderWidth: 1,
            borderColor: ["rgb(81, 81, 118)", "rgb(81, 81, 118)"],
            backgroundColor: ["#FFD6F2", "#9DD2FB"],
          },
        ],
      },
    },
    youtubeBarChart: {
      extraOptions: chartConfigs.barChartOptions,
      chartData: {
        labels: [],
        datasets: [
          {
            label: "Weight",
            fill: true,
            borderColor: "red",
            borderWidth: 2,
            borderDash: [],
            borderDashOffset: 0.0,
            data: [],
          },
        ],
      },
      gradientColors: config.colors.primaryGradient,
      gradientStops: [1, 0.4, 0],
    },
    bookBarChart: {
      extraOptions: chartConfigs.barChartOptions,
      chartData: {
        labels: [],
        datasets: [
          {
            label: "Weight",
            fill: true,
            borderColor: config.colors.info,
            borderWidth: 2,
            borderDash: [],
            borderDashOffset: 0.0,
            data: [],
          },
        ],
      },
      gradientColors: config.colors.primaryGradient,
      gradientStops: [1, 0.4, 0],
    },
    movieBarChart: {
      extraOptions: chartConfigs.barChartOptions,
      chartData: {
        labels: [],
        datasets: [
          {
            label: "Weight",
            fill: true,
            borderColor: "rgb(255, 0, 128)",
            borderWidth: 2,
            borderDash: [],
            borderDashOffset: 0.0,
            data: [],
          },
        ],
      },
      gradientColors: config.colors.primaryGradient,
      gradientStops: [1, 0.4, 0],
    },
    spotifyBarChart: {
      extraOptions: chartConfigs.barChartOptions,
      chartData: {
        labels: [],
        datasets: [
          {
            label: "Weight",
            fill: true,
            borderColor: "green",
            borderWidth: 2,
            borderDash: [],
            borderDashOffset: 0.0,
            data: [],
          },
        ],
      },
      gradientColors: config.colors.primaryGradient,
      gradientStops: [1, 0.4, 0],
    },
    rankings: [
      { rank: "1", weight: 5 },
      { rank: "2", weight: 4 },
      { rank: "3", weight: 3 },
      { rank: "4", weight: 2 },
      { rank: "5", weight: 1 },
    ],
  }),
  created() {
    this.initialise();
  },
  mounted: function () {
    window.scrollTo(0, 0);
  },
  computed: {
    marqueeSpeed: function () {
      return this.roomUsers.length * 5;
    },
  },
  methods: {
    onScroll(e) {
      if (typeof window === "undefined") return;
      const top = window.pageYOffset || e.target.scrollTop || 0;
      this.fab = top > 20;
    },
    navigateRoute(newpath) {
      this.$router.push(newpath);
    },
    processData(dict) {
      var items = Object.keys(dict).map(function (key) {
        return [key, dict[key]];
      });
      items.sort(function (first, second) {
        return second[1] - first[1];
      });
      return items.slice(0, 5);
    },
    initialise() {
      axios({
        url: "/room/" + this.roomCode,
        method: "GET",
      })
        .then((response) => {
          localStorage.clear();
          localStorage.setItem("roomName", response.data.room_name);
          localStorage.setItem("roomCode", this.roomCode);
          if (response.data.questionnaire) {
            for (var person of response.data.questionnaire) {
              this.roomUsers.push({
                name: person.name,
                gender: person.gender,
              });
            }
            localStorage.setItem("roomUsers", JSON.stringify(this.roomUsers));
            this.userCount = this.roomUsers.length;
            // Use roomUsers to get the num of female & males. (Continue...)
            for (let user of this.roomUsers) {
              if (user.gender == "M") {
                this.maleCount += 1;
              }

              if (user.gender == "F") {
                this.femaleCount += 1;
              }
            }
            this.genderPieChart.chartData.datasets[0].data.push(
              this.femaleCount
            );
            this.genderPieChart.chartData.datasets[0].data.push(this.maleCount);
            this.genderReady = true;
          } else {
            this.$bus.$emit("updated", "joined");
            this.navigateRoute("/questionnaire");
          }
          this.$bus.$emit("updated", "joined");
        })
        .catch(() => {
          this.navigateRoute("/");
        });
      axios.get("/dashboard/" + this.roomCode).then((response) => {
        for (const [key, value] of this.processData(response.data.youtube)) {
          this.youtubeBarChart.chartData.labels.push(key);
          this.youtubeBarChart.chartData.datasets[0].data.push(value);
        }
        this.youtubeReady = true;
        for (const [key, value] of this.processData(response.data.book)) {
          this.bookBarChart.chartData.labels.push(key);
          this.bookBarChart.chartData.datasets[0].data.push(value);
        }
        this.bookReady = true;
        for (const [key, value] of this.processData(response.data.movie)) {
          this.movieBarChart.chartData.labels.push(key);
          this.movieBarChart.chartData.datasets[0].data.push(value);
        }
        this.movieReady = true;

        // My Language Part
        for (const [key, value] of Object.entries(response.data.movieLang)) {
          this.languagePieChart.chartData.labels.push(key);
          this.languagePieChart.chartData.datasets[0].data.push(value);
        }
        this.langReady = true;

        for (const [key, value] of this.processData(response.data.spotify)) {
          this.spotifyBarChart.chartData.labels.push(key);
          this.spotifyBarChart.chartData.datasets[0].data.push(value);
        }
        this.spotifyReady = true;
      });
    },
  },
};
</script>
<style lang="scss">
@import "~@/styles/colors";

.home {
  background-color: $primary;
  justify-content: center;
}

.chibi {
  &-male {
    height: 160px;
    width: 125px;
  }
  &-female {
    height: 150px;
    width: 140px;
  }
}
.w {
  &-150 {
    width: 150px;
  }
}
.media-icons {
  margin-right: 5px;
}
.bar-chart {
  height: 100%;
}
</style>