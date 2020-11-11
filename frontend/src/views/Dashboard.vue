<template>
  <v-main class="home">

    <span>
      <br>
      <h3 style="color:#E3E9F2">Invite your friends to join this room using the code <b style="color:#5DC0BF">{{roomCode}}</b></h3>
      <h4 style="color:#E3E9F2">Make sure to <font style="color:#F6CA83">save the code</font> before exiting!</h4>
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
      <v-col cols="6" style="color:white">
        <h1>Here are some statistics!</h1><br>
        <h2>Total No. Of Users In Room: <b style="color:#F6CA83">{{userCount}}</b></h2>
      </v-col>
      <v-col cols="3"></v-col>
    </v-row>

    <v-row v-if="roomUsers.length != 1">
      <v-col cols="4"></v-col>
      <v-col cols="4">
        <marquee-text :repeat="1" :duration="marqueeSpeed" :paused="isPaused" @mouseenter="isPaused = !isPaused" @mouseleave="isPaused = false">
          <v-badge v-for="user in roomUsers" :key="user.name" :content="user.name" color='teal' bottom left overlap>
            <v-img v-if='user.gender == "M"' src='../images/Tanjiro.png' style='height:160px; width:125px'></v-img>
            <v-img v-else src='../images/Nezuko.png' style='height:150px; width:140px'></v-img>
          </v-badge>
        </marquee-text>
      </v-col>
      <v-col cols="4"></v-col>
    </v-row>
    <v-row v-else>
      <v-col cols="5"></v-col>
      <v-col cols="2">
        <marquee-text :repeat="1" :duration="marqueeSpeed" :paused="isPaused" @mouseenter="isPaused = !isPaused" @mouseleave="isPaused = false">
          <v-badge v-for="user in roomUsers" :key="user.name" :content="user.name" color='teal' bottom left overlap>
            <v-img v-if='user.gender == "M"' src='../images/Tanjiro.png' style='height:160px; width:125px'></v-img>
            <v-img v-else src='../images/Nezuko.png' style='height:150px; width:140px'></v-img>
          </v-badge>
        </marquee-text>
      </v-col>
      <v-col cols="5"></v-col>
    </v-row>

    <v-container class="px-10">
      <v-row>
        <v-col cols="12" sm=6 id="chart" data-aos="fade-right" data-aos-delay="100" data-aos-duration="1000">
          <!-- Put piechart for language here -->
          <h3 style="color:white">Movie Languages Selected<br></h3>
          <pie-chart :chart-data="languagePieChart.chartData" v-if="langReady">
          </pie-chart>
        </v-col>
        <v-col cols="12" sm=6 data-aos="fade-left" data-aos-delay="100" data-aos-duration="1000">
          <h3 style="color:white">Gender Population<br></h3>
          <pie-chart :chart-data="genderPieChart.chartData" v-if="genderReady">
          </pie-chart>
        </v-col>
      </v-row>
    </v-container>

    <v-row>
      <v-col cols="2"></v-col>
      <v-col cols="8" style="color:white">
        Categories or Genres ranked were assigned weights!
        <br><br>Total Weights were calculated to display the <b style="color:#5DC0BF">TOP</b> Categories/Genres below!
      </v-col>
      <v-col cols="2"></v-col>
    </v-row>

    <v-container>
      <v-row>
        <v-col cols="12" md=6 data-aos="fade-down-right" data-aos-duration="1000" v-if="youtubeReady">
          <v-card type="chart" dark>
            <v-card-title>
              <v-icon color="red" style="margin-right:5px" large>mdi-youtube</v-icon>
              Top Youtube Categories
            </v-card-title>
            <div class="chart-area">
              <bar-chart style="height: 100%" chart-id="youtubeStats" :chart-data="youtubeBarChart.chartData" :gradient-stops="youtubeBarChart.gradientStops" :extra-options="youtubeBarChart.extraOptions">
              </bar-chart>
            </div>
          </v-card>
        </v-col>
        <v-col cols="12" md=6 data-aos="fade-down-left" data-aos-duration="1000" data-aos-delay="500" v-if="bookReady">
          <v-card type="chart" dark>
            <v-card-title>
              <v-icon color="blue" style="margin-right:5px" large>mdi-book</v-icon>
              Top Book Genres
            </v-card-title>
            <div class="chart-area">
              <bar-chart style="height: 100%" chart-id="bookStats" :chart-data="bookBarChart.chartData" :gradient-stops="bookBarChart.gradientStops" :extra-options="bookBarChart.extraOptions">
              </bar-chart>
            </div>
          </v-card>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12" md=6 data-aos="fade-up-right" data-aos-duration="1000" data-aos-delay="600" v-if="movieReady">
          <v-card type="chart" dark>
            <v-card-title>
              <v-icon color="rgb(255, 0, 128)" style="margin-right:5px" large>mdi-movie-open</v-icon>
              Top Movie Genres
            </v-card-title>
            <div class="chart-area">
              <bar-chart style="height: 100%" chart-id="movieStats" :chart-data="movieBarChart.chartData" :gradient-stops="movieBarChart.gradientStops" :extra-options="movieBarChart.extraOptions">
              </bar-chart>
            </div>
          </v-card>
        </v-col>
        <v-col cols="12" md=6 data-aos="fade-up-left" data-aos-duration="1000" data-aos-delay="1000" v-if="spotifyReady">
          <v-card type="chart" dark>
            <v-card-title>
              <v-icon color="green" style="margin-right:5px" large>mdi-spotify</v-icon>
              Top Spotify Genres
            </v-card-title>
            <div class="chart-area">
              <bar-chart style="height: 100%" chart-id="spotifyStats" :chart-data="spotifyBarChart.chartData" :gradient-stops="spotifyBarChart.gradientStops" :extra-options="spotifyBarChart.extraOptions">
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
import config from "../config";
import axios from "axios";
import PieChart from "../components/Charts/PieChart";

export default {
  components: {
    BarChart,
    MarqueeText,
    "pie-chart": PieChart,
  },
  props: {
    roomCode: {
      type: String,
      default: "",
    },
  },
  data: () => ({
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
    // The piechart doesn't display the data unless I click on the available data label.
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
            console.log("this.roomUsers", this.roomUsers);
            for (let user of this.roomUsers) {
              console.log("room user:", user);
              if (user.gender == "M") {
                this.maleCount += 1;
                console.log("maleCount:", this.maleCount);
              }

              if (user.gender == "F") {
                this.femaleCount += 1;
                console.log("femaleCount:", this.femaleCount);
              }
            }
            this.genderPieChart.chartData.datasets[0].data.push(
              this.femaleCount
            );
            this.genderPieChart.chartData.datasets[0].data.push(this.maleCount);
            this.genderReady = true;
            console.log(
              "genderData:",
              this.genderPieChart.chartData.datasets[0].data
            );
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
          console.log("datasets", this.languagePieChart.chartData.datasets);
          console.log("key:", key, "value:", value);
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
.home {
  background-color: rgb(81, 81, 118);
  justify-content: center;
}
</style>